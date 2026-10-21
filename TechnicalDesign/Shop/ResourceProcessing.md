# Resource Processing - Technical Design

> **Zone:** Shop · **Design:** [GDD/Shop/ResourceProcessing](../../GDD/Shop/ResourceProcessing.md)

## Technical Specifications

- **Stations:** Smelting Forge (+ Bellows), Anvil, Quenching Basin, Woodworking Lathe, Carving Bench, Arcane Extractor, Purity Distiller.
- **Interaction model:** Loading/unloading = `IInstantInteractable`; working = `IContinuousInteractable` (see [Object Interaction](../Common/ObjectInteraction.md)).
- **Quality output:** Integer 1–100 via `QualityRules` (see [Weapon Crafting](WeaponCrafting.md)). Skipped mini-game → `QualityRules.Baseline` (60).
- **Outputs:** `WeaponComponentData` built with `WeaponComponentData.Create(material, kind, quality)`. Base Damage and Element come from the `ComponentMaterialDefinition`, never from the station.
- **Recipes:** `ProcessingRecipe` ScriptableObjects map input item ID → material definition + output kind per station.
- **Tick rate:** Station logic ticks on the host at 30 Hz; mini-game cursors run client-side and send the timing value with the strike request.

---

## Architecture & Implementation Approaches

### Approach A: Station State Machines on Shared Interaction Contracts (Recommended)
- Each station is a small state machine (`Empty → Loaded → Working → Done`).
- Stations implement the common interaction interfaces; there is no station-specific input code on the player.
- Mini-games are separate components (`TimingStrikeMiniGame`, `TemperatureHoldMiniGame`) that feed a quality delta to the station.
- **Pros:** Mini-games can be reused (e.g. the Uber-Weapon ritual), disabled for accessibility, or swapped.

### Approach B: One Generic Configurable Station
- A single `Workstation` component configured entirely by data.
- **Cons:** Stations differ enough (heat, strikes, temperature) that the configuration becomes a scripting language.

---

## Networking

- Host owns station state, inserted items and accumulated quality.
- Strike requests carry `normalizedTiming` (0–1); the host validates it was sent while a strike was allowed and applies the quality delta.
- Accessibility "auto mini-game" is a per-player setting sent with the interaction request.

---

## Unity C# Reference Code

```csharp
using System;
using System.Collections.Generic;
using UnityEngine;
using Armotheca.Crafting;
using Armotheca.Interaction;

namespace Armotheca.Shop
{
    [CreateAssetMenu(menuName = "Armotheca/Shop/Processing Recipe")]
    public class ProcessingRecipe : ScriptableObject
    {
        public string InputItemId;                      // e.g. "Ingot_Iron"
        public ComponentMaterialDefinition OutputMaterial;
        public ComponentKind OutputKind;                // Blade, Hilt, ShortShaft, LongShaft, Core
    }

    /// <summary>
    /// Anvil: an ingot is placed (instant), then struck 3 times (instant per strike, timed).
    /// Quality starts at 50: perfect +15, good +5, off-beat -5. Skipping timing yields Baseline (60).
    /// </summary>
    public class AnvilWorkstation : MonoBehaviour, IInstantInteractable
    {
        [SerializeField] private List<ProcessingRecipe> recipes;
        [SerializeField] private int requiredStrikes = 3;
        [SerializeField, Range(0f, 1f)] private float sweetSpotWindow = 0.25f;
        [SerializeField] private int startingQuality = 50;
        [SerializeField] private int perfectBonus = 15;
        [SerializeField] private int goodBonus = 5;
        [SerializeField] private int offBeatPenalty = 5;

        private ProcessingRecipe activeRecipe;
        private int strikes;
        private int quality;
        private bool autoQuality;

        public Transform Transform => transform;
        public bool HasOutput => activeRecipe != null && strikes >= requiredStrikes;
        public event Action<float> OnStrikeFeedback; // 1 perfect, 0.5 good, -1 off-beat
        public event Action<WeaponComponentData> OnOutputReady;

        public bool TryGetPrompt(PlayerCarrier player, out InteractionPrompt prompt)
        {
            if (activeRecipe == null)
                prompt = new InteractionPrompt(InteractionKind.Instant, "Place", "Ingot",
                                               player.HandsEmpty ? "Needs a hot ingot" : null);
            else if (!HasOutput)
                prompt = new InteractionPrompt(InteractionKind.Instant, "Strike", "Anvil");
            else
                prompt = new InteractionPrompt(InteractionKind.Instant, "Take", activeRecipe.OutputMaterial.DisplayName,
                                               player.HandsEmpty ? null : "Hands full");
            return true;
        }

        public bool CanInteractInstant(PlayerCarrier player) =>
            activeRecipe == null ? !player.HandsEmpty : (HasOutput ? player.HandsEmpty : true);

        public void InteractInstant(PlayerCarrier player)
        {
            // Strikes from input arrive via PerformStrike with timing; here we handle place / take.
            if (activeRecipe == null) TryLoad(player);
        }

        public bool TryLoad(PlayerCarrier player)
        {
            var item = player.HandsItem;
            var itemId = item != null ? item.name : null; // replace with ItemIdentity component
            var recipe = recipes.Find(r => r.InputItemId == itemId);
            if (recipe == null) return false;

            player.ReleaseHands();
            Destroy(item);
            activeRecipe = recipe;
            strikes = 0;
            quality = startingQuality;
            autoQuality = false;
            return true;
        }

        /// <param name="normalizedTiming">0..1 cursor position; null when the player skips the mini-game.</param>
        public void PerformStrike(float? normalizedTiming)
        {
            if (activeRecipe == null || HasOutput) return;

            if (normalizedTiming is null)
            {
                autoQuality = true;
            }
            else
            {
                float deviation = Mathf.Abs(normalizedTiming.Value - 0.5f);
                if (deviation <= sweetSpotWindow * 0.5f) { quality += perfectBonus; OnStrikeFeedback?.Invoke(1f); }
                else if (deviation <= sweetSpotWindow) { quality += goodBonus; OnStrikeFeedback?.Invoke(0.5f); }
                else { quality -= offBeatPenalty; OnStrikeFeedback?.Invoke(-1f); }
            }

            strikes++;
            if (HasOutput) OnOutputReady?.Invoke(PeekOutput());
        }

        private WeaponComponentData PeekOutput()
        {
            int finalQuality = autoQuality ? QualityRules.Baseline : QualityRules.Clamp(quality);
            return WeaponComponentData.Create(activeRecipe.OutputMaterial, activeRecipe.OutputKind, finalQuality);
        }

        public bool TryTakeOutput(out WeaponComponentData output)
        {
            output = default;
            if (!HasOutput) return false;
            output = PeekOutput();
            activeRecipe = null;
            strikes = 0;
            return true;
        }
    }

    /// <summary>Bellows on the smelting forge: cooperative continuous interaction (up to 2 players).</summary>
    public class BellowsInteractable : ContinuousInteractableBase
    {
        [SerializeField] private SmeltingForge forge;

        public override bool TryGetPrompt(PlayerCarrier player, out InteractionPrompt prompt)
        {
            prompt = new InteractionPrompt(InteractionKind.Continuous, "Pump", "Bellows",
                                           forge.HasOre ? null : "Forge is empty");
            return true;
        }

        protected override bool IsReady(PlayerCarrier player) => forge.HasOre && player.HandsEmpty;
        protected override void OnCompleted() => forge.CompleteHeating();
    }

    public class SmeltingForge : MonoBehaviour
    {
        public bool HasOre { get; private set; }
        public bool HasHotIngot { get; private set; }
        public event Action OnIngotReady;

        public void LoadOre() => HasOre = true;

        public void CompleteHeating()
        {
            HasOre = false;
            HasHotIngot = true;
            OnIngotReady?.Invoke();
        }
    }
}
```

---

## Testing Notes

- Anvil: 3 perfect strikes → 95 (Flawless); 3 off-beat → 35 (Crude); skipped → 60.
- Output Base Damage always equals the recipe material's `BaseDamage`; foundations output 0.
- Bellows with 2 helpers completes in `duration / 1.5`.
