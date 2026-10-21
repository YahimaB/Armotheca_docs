# Uber-Weapon - Technical Design

> **Zone:** Shop · **Design:** [GDD/Shop/UberWeapon](../../GDD/Shop/UberWeapon.md)

## Technical Specifications

- **Catalyst tracking:** Set of acquired catalyst IDs, persisted with shop progression.
- **Ritual:** Host-run, networked multi-phase state machine (`Idle → HarmonicSmelting → ArcaneTurning → GlacialQuench → FinalBinding → Completed`).
- **Station reuse:** Phases drive the same station components and mini-games as normal processing (bellows, lathe, timing strike) in a "ritual mode" with stricter windows.
- **Player-count scaling:** Phases that run in parallel with 4 players run sequentially with fewer players.
- **Failure:** A failed phase resets only that phase; catalysts are never consumed until `Completed`.

---

## Architecture & Implementation Approaches

### Approach A: Explicit Phase State Machine with Phase Objects (Recommended)
- `RitualPhase` objects (one per phase) expose `Begin`, `Tick`, `IsSucceeded`, `IsFailed`.
- `UberRitualDirector` advances phases and broadcasts phase changes for UI, music and VFX.
- **Pros:** Each phase testable alone; easy to reorder or add phases.

### Approach B: Timeline-driven set piece
- **Cons:** Hard to combine with player-driven success/failure; better suited to the victory cinematic only.

---

## Networking

- Director runs on the host; phase index, phase progress (0–1) and per-player role assignments replicate at 10 Hz.
- Final Binding requires simultaneous mallet strikes: the host accepts strikes within a ±0.25 s window of each other.

---

## Unity C# Reference Code

```csharp
using System;
using System.Collections.Generic;
using UnityEngine;

namespace Armotheca.Progression
{
    public static class CatalystIds
    {
        public const string IgnisCore = "IgnisCore";
        public const string SylvanSpire = "SylvanSpire";
        public const string AstralPrism = "AstralPrism";
        public const string GlacialHeart = "GlacialHeart";

        public static readonly string[] All = { IgnisCore, SylvanSpire, AstralPrism, GlacialHeart };
    }

    [Serializable]
    public class UberWeaponProgress
    {
        public List<string> AcquiredCatalysts = new();

        public bool Has(string id) => AcquiredCatalysts.Contains(id);
        public int Count => AcquiredCatalysts.Count;
        public bool AllAcquired => Array.TrueForAll(CatalystIds.All, Has);

        public bool TryRegister(string id)
        {
            if (Array.IndexOf(CatalystIds.All, id) < 0 || Has(id)) return false;
            AcquiredCatalysts.Add(id);
            return true;
        }
    }

    public enum RitualPhaseId
    {
        Idle,
        HarmonicSmelting,
        ArcaneTurning,
        GlacialQuench,
        FinalBinding,
        Completed
    }

    public abstract class RitualPhase
    {
        public abstract RitualPhaseId Id { get; }
        public abstract void Begin(int playerCount);
        public abstract void Tick(float deltaTime);
        public abstract bool IsSucceeded { get; }
        public abstract bool IsFailed { get; }
        public abstract float Progress01 { get; }
    }

    public class UberRitualDirector : MonoBehaviour
    {
        [SerializeField] private ShopProgressionManager progression;

        private readonly List<RitualPhase> phases = new();
        private int phaseIndex = -1;
        private int playerCount;

        public UberWeaponProgress Progress { get; } = new();
        public RitualPhaseId CurrentPhase => phaseIndex < 0 ? RitualPhaseId.Idle
                                           : phaseIndex >= phases.Count ? RitualPhaseId.Completed
                                           : phases[phaseIndex].Id;

        public event Action<string> OnCatalystAcquired;
        public event Action<RitualPhaseId> OnPhaseStarted;
        public event Action<RitualPhaseId> OnPhaseFailed;
        public event Action OnUberWeaponForged;

        public void RegisterPhases(IEnumerable<RitualPhase> orderedPhases) => phases.AddRange(orderedPhases);

        public void RegisterCatalyst(string id)
        {
            if (Progress.TryRegister(id)) OnCatalystAcquired?.Invoke(id);
        }

        public bool CanBegin(out string reason)
        {
            if (progression.State.TierIndex < 3) { reason = "Requires the Great Crucible (Tier 3)."; return false; }
            if (!Progress.AllAcquired) { reason = $"Catalysts {Progress.Count}/4."; return false; }
            if (CurrentPhase != RitualPhaseId.Idle) { reason = "Ritual already in progress."; return false; }
            reason = null;
            return true;
        }

        public bool TryBegin(int activePlayers)
        {
            if (!CanBegin(out _)) return false;
            playerCount = activePlayers;
            StartPhase(0);
            return true;
        }

        private void Update()
        {
            if (phaseIndex < 0 || phaseIndex >= phases.Count) return;

            var phase = phases[phaseIndex];
            phase.Tick(Time.deltaTime);

            if (phase.IsFailed)
            {
                OnPhaseFailed?.Invoke(phase.Id);
                StartPhase(phaseIndex); // retry the same phase; catalysts are kept
            }
            else if (phase.IsSucceeded)
            {
                if (phaseIndex + 1 < phases.Count) StartPhase(phaseIndex + 1);
                else Complete();
            }
        }

        private void StartPhase(int index)
        {
            phaseIndex = index;
            phases[index].Begin(playerCount);
            OnPhaseStarted?.Invoke(phases[index].Id);
        }

        private void Complete()
        {
            phaseIndex = phases.Count;
            OnUberWeaponForged?.Invoke(); // victory screen, unlock Prestige mode, save
        }
    }
}
```
