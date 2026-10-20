# Shop Progression & The Uber-Weapon Endgame

## Design Intent

Progression in *Armotheca* bridges the gap between everyday shop management and an epic climactic objective. Many simulation and tycoon titles suffer from endgame stagnation once financial wealth outpaces available expenditures. *Armotheca* solves this by framing every commission, gold piece, and reputation point as fuel toward a definitive zenith: **The Forging of the Uber-Weapon (The Primordial Armament)**. Progress is visually manifested through workshop expansion, station upgrades, portal stabilization, and crucible milestone rituals.

---

## Player Experience Goals

- **Visual Pride:** Watching the humble, stone-and-timber basement evolve into a magnificent, luminescent Astral Forge suspended in starlight.
- **Milestone Anticipation:** Unlocking each new dimensional door and higher-tier workstation feels like opening a new chapter of possibilities.
- **Climactic Climax:** Forging the Uber-Weapon is not a silent button click in a menu, but an intense, synchronized cooperative event requiring all players to execute their roles under pressure.
- **Purpose-Driven Economy:** Gold and rare monster materials retain value right up to the final seconds of the campaign.

---

## References (Specific Examples)

- **Factorio (Rocket Launch):** Clear, tangible macro-objective that unifies all manufacturing branches toward a triumphant finale.
- **Moonlighter:** Direct shop upgrades (cash register speed, display cases, bed storage) funded by dungeon exploration.
- **PlateUp!:** Day-by-day restaurant layout evolution and technology upgrades.
- **Subnautica (Neptune Escape Rocket):** Multi-phase colossal construction project requiring rare ingredients gathered across the most perilous corners of the world.

---

## Shop Tier Milestones

```
+--------------------------------------------------------------------------+
|                        WORKSHOP PROGRESSION LADDER                       |
+--------------------------------------------------------------------------+
| TIER 1: RUSTIC FORGE       | 1 Active Door, 3 Workbench Stations         |
| TIER 2: ARCANE ATELIER     | 2 Active Doors, Lathe & Distiller Unlocked  |
| TIER 3: ASTRAL ARMORTHECA  | 4 Active Doors, The Great Crucible Unlocked |
+--------------------------------------------------------------------------+
```

### Tier Unlocks

| Workshop Tier | Requirement | Unlocked Capabilities |
|---|---|---|
| **Tier 1: Rustic Forge** | Starting Baseline | Basic Anvil, Basic Smelter, 1 Door (*Verdant Corruption*), Guild Commissions. |
| **Tier 2: Arcane Atelier** | 2,500 Gold, 200 Rep | 2nd Door (*Pyroclastic Trench*), Woodworking Lathe, Arcane Extractor, Academy Commissions. |
| **Tier 3: Astral Armotheca**| 10,000 Gold, 800 Rep | 3rd & 4th Doors (*Astral Quarry*, *Frostbite Caverns*), Quenching Basins, **The Uber-Weapon Crucible**. |

---

## The Uber-Weapon: The Primordial Armament

The Uber-Weapon is the legendary magnum opus of the Armotheca lineage. It demands four **Primordial Catalysts**, each guarded by an Apex Entity deep inside the dimensional doorways:

```
                  [THE PRIMORDIAL ARMAMENT]
                             |
         +-------------------+-------------------+
         |                   |                   |
         v                   v                   v
   [Ignis Core]       [Sylvan Spire]     [Astral Prism]     [Glacial Heart]
 (Pyroclastic Apex)  (Verdant Elder)     (Astral Sovereign) (Frost Wyrm)
```

### The 4-Phase Forging Ritual

When all 4 catalysts are gathered, players initiate the final contract:

1. **Phase 1: Harmonic Smelting (Furnace Team):**
   - Ignis Core and Astral Prism melted in the Great Crucible. Requires constant temperature maintenance via synchronized bellows pumping.
2. **Phase 2: Arcane Turning (Carpentry Team):**
   - Sylvan Spire carved into an Adamantine Shaft using the high-speed lathe.
3. **Phase 3: The Glacial Quench (Dual Action):**
   - The molten celestial blade is plunged into the Glacial Heart solution at the exact moment the temperature needle aligns.
4. **Phase 4: Final Binding:**
   - Both components are locked into the Grand Assembly Bench, and all active players strike their mallets simultaneously to seal the weapon.

Upon completion, the campaign victory screen triggers, celebrating player stats, and unlocking **Prestige Endless Mode** (chaos modifiers, unstable multi-door breaches, and global high-score ladders).

---

## Technical Specifications

- **Crucible Event State Machine:** Driven by a synchronized networked multi-phase manager.
- **Persistent Data:** Workshop level, unlocked doors, and catalyst acquisition state saved via JSON/Binary serialization.

---

## Production-Ready C# Architecture

```csharp
using System;
using System.Collections.Generic;
using UnityEngine;
using Armotheca.Crafting;

namespace Armotheca.Progression
{
    public enum ShopTier
    {
        RusticForge = 1,
        ArcaneAtelier = 2,
        AstralArmotheca = 3
    }

    [System.Serializable]
    public class UberWeaponProgress
    {
        public bool HasIgnisCore;
        public bool HasSylvanSpire;
        public bool HasAstralPrism;
        public bool HasGlacialHeart;

        public bool AllCatalystsAcquired => 
            HasIgnisCore && HasSylvanSpire && HasAstralPrism && HasGlacialHeart;

        public int CatalystsCount => 
            (HasIgnisCore ? 1 : 0) + (HasSylvanSpire ? 1 : 0) + 
            (HasAstralPrism ? 1 : 0) + (HasGlacialHeart ? 1 : 0);
    }

    /// <summary>
    /// Coordinates shop level upgrades, economic treasury, and endgame Uber-Weapon creation.
    /// </summary>
    public class ShopProgressionManager : MonoBehaviour
    {
        [Header("State")]
        [SerializeField] private ShopTier currentTier = ShopTier.RusticForge;
        [SerializeField] private int currentGold = 0;
        [SerializeField] private int currentReputation = 0;
        [SerializeField] private UberWeaponProgress uberProgress = new();

        public ShopTier CurrentTier => currentTier;
        public int CurrentGold => currentGold;
        public int CurrentReputation => currentReputation;
        public UberWeaponProgress UberProgress => uberProgress;

        public event Action<ShopTier> OnShopTierUpgraded;
        public event Action<int, int> OnCurrencyUpdated; // gold, rep
        public event Action<string> OnCatalystAcquired;
        public event Action OnUberWeaponForged;

        public void AddRewards(int gold, int reputation)
        {
            currentGold += gold;
            currentReputation += reputation;
            OnCurrencyUpdated?.Invoke(currentGold, currentReputation);
            CheckForTierUpgradeEligibility();
        }

        public bool TryUpgradeShopTier()
        {
            if (currentTier == ShopTier.RusticForge && currentGold >= 2500 && currentReputation >= 200)
            {
                currentGold -= 2500;
                currentTier = ShopTier.ArcaneAtelier;
                OnShopTierUpgraded?.Invoke(currentTier);
                OnCurrencyUpdated?.Invoke(currentGold, currentReputation);
                return true;
            }

            if (currentTier == ShopTier.ArcaneAtelier && currentGold >= 10000 && currentReputation >= 800)
            {
                currentGold -= 10000;
                currentTier = ShopTier.AstralArmotheca;
                OnShopTierUpgraded?.Invoke(currentTier);
                OnCurrencyUpdated?.Invoke(currentGold, currentReputation);
                return true;
            }

            return false;
        }

        public void RegisterCatalyst(string catalystID)
        {
            switch (catalystID)
            {
                case "IgnisCore": uberProgress.HasIgnisCore = true; break;
                case "SylvanSpire": uberProgress.HasSylvanSpire = true; break;
                case "AstralPrism": uberProgress.HasAstralPrism = true; break;
                case "GlacialHeart": uberProgress.HasGlacialHeart = true; break;
            }

            OnCatalystAcquired?.Invoke(catalystID);
        }

        public bool CanBeginUberRitual()
        {
            return currentTier == ShopTier.AstralArmotheca && uberProgress.AllCatalystsAcquired;
        }

        public void CompleteUberRitual()
        {
            if (!CanBeginUberRitual()) return;
            OnUberWeaponForged?.Invoke();
        }

        private void CheckForTierUpgradeEligibility()
        {
            // Trigger visual HUD indicator when upgrade is affordable
        }
    }
}
```
