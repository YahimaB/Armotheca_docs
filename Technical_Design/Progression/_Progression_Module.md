---
id: _Progression_Module
type: module
module: Progression
namespace: Armotheca.Progression
status: Draft
---

# Progression Module

> **Design:** [_Progression_System](../../GDD/02_Systems/Progression/_Progression_System.md) · **Map:** [_Module_Map](../_Module_Map.md) · **Overview:** [Technical Overview](../Technical_Overview.md)

## Scope

| GDD doc | Implemented in |
| --- | --- |
| [M_Currencies](../../GDD/02_Systems/Progression/M_Currencies.md) | [Technical Specifications](#technical-specifications) — `ShopProgressionState` |
| [M_Workshop_Tiers](../../GDD/02_Systems/Progression/M_Workshop_Tiers.md) | [Architecture](#architecture--implementation-approaches) — `ShopTierDefinition` ladder; [Tier Assets](#tier-assets) |
| [M_Door_Purchase](../../GDD/02_Systems/Exploration/M_Door_Purchase.md) | [Technical Specifications](#technical-specifications) — `TryPurchaseDoor`; [Door Assets](#door-assets) |
| [L00_Workshop](../../GDD/04_Locations/L00_Workshop/L00_Workshop.md) | Workshop expansion per tier ([Technical Specifications](#technical-specifications)) |

---

## Technical Specifications

- **State:** Current tier, gold, reputation, emergency tokens, owned doors, unlocked blueprints.
- **Tier data:** `ShopTierDefinition` ScriptableObjects (cost, reputation threshold, unlocked stations, unlocked archetypes, workshop layout prefab/scene section).
- **Door purchases:** Doors are defined by `DoorDefinition` (required tier + gold price, see [Magic Doors](../Exploration/Door_Instances.md)). A door is purchasable when `TierIndex >= RequiredTier` and gold ≥ price; purchased door IDs are stored in `OwnedDoorIds`. Doors flagged `OwnedAtStart` are added on a new save.
- **Persistence:** Saved after every tier upgrade and every completed commission, as JSON (decision pending vs binary, see [Technical Overview](../Technical_Overview.md)). Only the host saves; clients receive state on join.
- **Workshop expansion:** Each tier enables a pre-built section of the workshop scene (rooms, station slots, door frames) rather than spawning geometry at runtime.

---

## Architecture & Implementation Approaches

### Approach A: Data-Driven Tier Ladder (Recommended)
- An ordered list of `ShopTierDefinition` assets; the manager compares requirements generically.
- **Pros:** Adding or rebalancing tiers is data-only; no hard-coded numbers in code.

### Approach B: Hard-coded tier checks
- Used in the first draft (`if tier == RusticForge && gold >= 2500`).
- **Cons:** Every balance change needs a code change; rejected.

---

## Networking

- Host-only `ShopProgressionManager`. Gold/reputation changes replicate as absolute values with change events.
- Tier upgrade is a host RPC from the upgrade ledger interaction; the host validates and broadcasts the new tier, and every client enables the matching workshop section.
- Door purchase is a host RPC from the door's price plaque (hold time: [Exploration › Doors](../../GDD/06_Balancing/Exploration.md#doors)); the host validates tier and gold and broadcasts `OnDoorPurchased`.

---

## Data

| Definition (SO) | Field | Supplied by |
| --- | --- | --- |
| `ShopTierDefinition` | gold cost, reputation threshold | [Progression › Workshop Tiers](../../GDD/06_Balancing/Progression.md#workshop-tiers) |
| `ShopTierDefinition` | unlocked stations and archetypes | [M_Workshop_Tiers](../../GDD/02_Systems/Progression/M_Workshop_Tiers.md) |
| `DoorDefinition` | required tier, gold price, owned at start | [Progression › Doors](../../GDD/06_Balancing/Progression.md#doors) |

---

## Events

| Event | Raised when | Consumed by |
| --- | --- | --- |
| `OnCurrencyChanged` | Gold or reputation changes | HUD, board header |
| `OnUpgradeAffordabilityChanged` | An upgrade becomes (un)affordable | HUD hint, ledger glow |
| `OnTierUpgraded` | A tier is bought | Workshop sections, audio |
| `OnDoorPurchased` | A door is bought | Door state, plaque |

---

## Unity C# Reference Code

```csharp
using System;
using System.Collections.Generic;
using UnityEngine;
using Armotheca.Exploration;

namespace Armotheca.Progression
{
    [CreateAssetMenu(menuName = "Armotheca/Progression/Shop Tier")]
    public class ShopTierDefinition : ScriptableObject
    {
        public int TierIndex;                  // 1, 2, 3
        public string DisplayName;             // "Rustic Forge"
        public int GoldCost;                   // spent on upgrade
        public int ReputationThreshold;        // not spent
        public List<string> UnlockedStationIds;
        public List<string> UnlockedArchetypeIds;
        public string WorkshopSectionId;
        // Doors are not listed here: each DoorDefinition declares its RequiredTier and GoldPrice.
    }

    [Serializable]
    public class ShopProgressionState
    {
        public int TierIndex = 1;
        public int Gold;
        public int Reputation;
        public int EmergencyTokens;
        public List<string> OwnedDoorIds = new();
        public List<string> Blueprints = new();
    }

    public class ShopProgressionManager : MonoBehaviour
    {
        [SerializeField] private List<ShopTierDefinition> tiers; // ordered by TierIndex
        [SerializeField] private List<DoorDefinition> doors;
        [SerializeField] private ShopProgressionState state = new();

        public event Action<string> OnDoorPurchased;

        /// <summary>Call when starting a new save.</summary>
        public void InitializeNewGame()
        {
            state = new ShopProgressionState();
            foreach (var door in doors)
                if (door.OwnedAtStart) state.OwnedDoorIds.Add(door.DoorId);
        }

        public bool IsDoorOwned(string doorId) => state.OwnedDoorIds.Contains(doorId);

        /// <summary>Door is visible with a price plaque once its tier is reached.</summary>
        public bool IsDoorAvailable(DoorDefinition door) =>
            !IsDoorOwned(door.DoorId) && state.TierIndex >= door.RequiredTier;

        public bool CanPurchaseDoor(DoorDefinition door, out string reason)
        {
            if (IsDoorOwned(door.DoorId)) { reason = "Already owned."; return false; }
            if (state.TierIndex < door.RequiredTier) { reason = $"Requires shop Tier {door.RequiredTier}."; return false; }
            if (state.Gold < door.GoldPrice) { reason = $"Needs {door.GoldPrice} gold."; return false; }
            reason = null;
            return true;
        }

        public bool TryPurchaseDoor(DoorDefinition door)
        {
            if (!CanPurchaseDoor(door, out _)) return false;

            state.Gold -= door.GoldPrice;
            state.OwnedDoorIds.Add(door.DoorId);
            OnCurrencyChanged?.Invoke(state.Gold, state.Reputation);
            OnDoorPurchased?.Invoke(door.DoorId);
            RefreshAffordability();
            return true;
        }

        public ShopProgressionState State => state;
        public ShopTierDefinition CurrentTier => tiers[state.TierIndex - 1];
        public ShopTierDefinition NextTier => state.TierIndex < tiers.Count ? tiers[state.TierIndex] : null;

        public event Action<ShopTierDefinition> OnTierUpgraded;
        public event Action<int, int> OnCurrencyChanged; // gold, rep
        public event Action<bool> OnUpgradeAffordabilityChanged;

        private bool lastAffordable;

        public void AddRewards(int gold, int reputation)
        {
            state.Gold += gold;
            state.Reputation = Mathf.Max(0, state.Reputation + reputation);
            OnCurrencyChanged?.Invoke(state.Gold, state.Reputation);
            RefreshAffordability();
        }

        public bool CanUpgrade(out string reason)
        {
            var next = NextTier;
            if (next == null) { reason = "Maximum tier reached."; return false; }
            if (state.Gold < next.GoldCost) { reason = $"Needs {next.GoldCost} gold."; return false; }
            if (state.Reputation < next.ReputationThreshold) { reason = $"Needs {next.ReputationThreshold} reputation."; return false; }
            reason = null;
            return true;
        }

        public bool TryUpgrade()
        {
            if (!CanUpgrade(out _)) return false;

            state.Gold -= NextTier.GoldCost;
            state.TierIndex++;
            OnTierUpgraded?.Invoke(CurrentTier);
            OnCurrencyChanged?.Invoke(state.Gold, state.Reputation);
            RefreshAffordability();
            return true;
        }

        private void RefreshAffordability()
        {
            bool affordable = CanUpgrade(out _);
            if (affordable == lastAffordable) return;
            lastAffordable = affordable;
            OnUpgradeAffordabilityChanged?.Invoke(affordable);
        }
    }
}
```

---

## Tier Assets

Values come from [Progression › Workshop Tiers](../../GDD/06_Balancing/Progression.md#workshop-tiers); unlocks from [M_Workshop_Tiers](../../GDD/02_Systems/Progression/M_Workshop_Tiers.md).

| Asset | Tier |
|---|---|
| `ShopTier_RusticForge` | 1 |
| `ShopTier_ArcaneAtelier` | 2 |
| `ShopTier_AstralArmotheca` | 3 |

## Door Assets

Values come from [Progression › Doors](../../GDD/06_Balancing/Progression.md#doors).

| Asset | Location |
|---|---|
| `Door_VerdantCorruption` | [L01_Verdant_Corruption](../../GDD/04_Locations/L01_Verdant_Corruption/L01_Verdant_Corruption.md) |
| `Door_PyroclasticTrench` | [L02_Pyroclastic_Trench](../../GDD/04_Locations/L02_Pyroclastic_Trench/L02_Pyroclastic_Trench.md) |
| `Door_AstralQuarry` | [L03_Astral_Quarry](../../GDD/04_Locations/L03_Astral_Quarry/L03_Astral_Quarry.md) |
| `Door_FrostbiteCavern` | [L04_Frostbite_Cavern](../../GDD/04_Locations/L04_Frostbite_Cavern/L04_Frostbite_Cavern.md) |
