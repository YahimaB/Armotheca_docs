# Shop Progression - Technical Design

> **Zone:** Shop · **Design:** [GDD/Shop/ShopProgression](../../GDD/Shop/ShopProgression.md)

## Technical Specifications

- **State:** Current tier, gold, reputation, emergency tokens, owned doors, unlocked blueprints.
- **Tier data:** `ShopTierDefinition` ScriptableObjects (cost, reputation threshold, unlocked stations, unlocked archetypes, workshop layout prefab/scene section).
- **Door purchases:** Doors are defined by `DoorDefinition` (required tier + gold price, see [Magic Doors](../Exploration/MagicDoors.md)). A door is purchasable when `TierIndex >= RequiredTier` and gold ≥ price; purchased door IDs are stored in `OwnedDoorIds`. Doors flagged `OwnedAtStart` are added on a new save.
- **Persistence:** Saved after every tier upgrade and every completed commission, as JSON (decision pending vs binary, see [Technical Overview](../TechnicalOverview.md)). Only the host saves; clients receive state on join.
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
- Door purchase is a host RPC from the door's price plaque (1 s hold); the host validates tier and gold and broadcasts `OnDoorPurchased`.

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

## Tier Data (Current Values)

| Asset | Tier | Gold Cost | Rep Threshold | Stations |
|---|---|---|---|---|
| `ShopTier_RusticForge` | 1 | 0 | 0 | Anvil, Smelter |
| `ShopTier_ArcaneAtelier` | 2 | 1,500 | 200 | Lathe, ArcaneExtractor |
| `ShopTier_AstralArmotheca` | 3 | 6,000 | 800 | QuenchingBasin, GreatCrucible |

## Door Data (Current Values)

| Asset | Realm | Required Tier | Gold Price | Owned at Start |
|---|---|---|---|---|
| `Door_VerdantCorruption` | Verdant Corruption | 1 | 0 | Yes |
| `Door_PyroclasticTrench` | Pyroclastic Trench | 2 | 1,000 | No |
| `Door_AstralQuarry` | Astral Quarry | 3 | 2,000 | No |
| `Door_FrostbiteCavern` | Frostbite Cavern | 3 | 2,000 | No |

Total gold per tier is unchanged from the previous design (Tier 2: 2,500; Tier 3: 10,000), now split between upgrade and doors.
