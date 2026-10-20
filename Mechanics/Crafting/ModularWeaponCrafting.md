# Modular Weapon Crafting System (2-Piece Assembly)

## Design Intent

The Modular Weapon Crafting System provides an intuitive, tactile, and mathematically deep method for creating weapons in *Armotheca*. By restricting weapon construction to **strictly two modular components**, the system strikes a deliberate balance: it avoids the combinatorial explosion and UI fatigue of complex 5+ part forging, while offering rich strategic depth where material choice and component quality directly address diverse customer commission requirements.

---

## Player Experience Goals

- **Tactile Satisfaction:** Physically placing a blade and a hilt onto an assembly bench and hammering/locking them together feels physical and rewarding.
- **Readable Combinatorics:** Players can look at client letters and immediately deduce what 2 parts are needed (e.g., *Frost Core + Willow Wand Shaft = Swift Frost Wand*).
- **Quality Differentiation:** Flawless processing of components directly elevates final weapon statistics and market valuation.
- **Role Collaboration:** One player can specialize in blade forging while another works on precision hilts, meeting at the assembly bench to finalize the product.

---

## References (Specific Examples)

- **The Legend of Zelda: Tears of the Kingdom (Fuse System):** Intuitive 2-part weapon composition where an base weapon/hilt is augmented by an attachment/blade with predictable property inheritance.
- **Potion Craft:** Alchemical ingredient interaction where component properties combine into distinct potion effects without excessive UI clutter.
- **PlateUp! / Overcooked:** Physical placement of two prepared ingredients onto an assembly counter to form a completed composite dish.
- **Monster Hunter Series:** Distinct elemental and affinity properties mapped directly to monster-derived crafting parts.

---

## Technical Specifications

### Weapon Category Rules

| Category | Component 1 (Foundation) | Component 2 (Payload / Accent) | Stat Contribution Rule |
|---|---|---|---|
| **Sword** | **Hilt (`IHiltComponent`)** | **Blade (`IBladeComponent`)** | Blade dictates Base Damage, Damage Type (Slashing/Piercing), and Elemental Affinity. Hilt dictates Attack Speed, Balance (stamina cost), and Durability multiplier. |
| **Wand (1-Handed)** | **Short Shaft (`IShaftComponent`)** | **Magical Core (`ICoreComponent`)** | Core dictates Spell Payload (Fireball, Chain Lightning) and Element. Shaft dictates Cast Speed, Cooldown Reduction, and Spell Spread. |
| **Staff (2-Handed)** | **Long Shaft (`IShaftComponent`)** | **Magical Core (`ICoreComponent`)** | Core dictates Spell Payload and Base Power. Shaft dictates Mana Reservoir, Area-of-Effect (AoE) Multiplier, and Channeling Stability. |

### Quality Tiers & Multipliers

Every component has a computed Quality Level (0–100%) determined during the manual processing phase:
- **Crude (0–39%):** Value Multiplier 0.75x, -10% Base Stats (High defect risk, rejected by Academy).
- **Standard (40–74%):** Value Multiplier 1.0x, Normal Stats.
- **Masterwork (75–94%):** Value Multiplier 1.4x, +15% Stats (Eligible for Guild bonuses).
- **Flawless (95–100%):** Value Multiplier 2.0x, +30% Stats + Emits subtle particle glow (Satisfies Collector & SOS elite bonuses).

---

## Architecture & Implementation Approaches

### Approach A: ScriptableObject Definitions + Pure Domain Assembly (Recommended)

**Patterns Used:** Factory Pattern, Strategy Pattern, Observer Pattern, Single Responsibility.

- `WeaponDefinitionSO`: Defines base archetypes (Sword, Wand, Staff).
- `ComponentData`: Carries material properties, quality tier, and elemental affixes.
- `AssembledWeaponInstance`: Runtime immutable representation of the completed weapon with cached aggregate stats.
- `AssemblyTableController`: Physical world workstation where players place Component A and Component B to produce the output.

#### Pros:
- Decouples static game data (ScriptableObjects) from runtime instances.
- Fully networkable via clean data-transfer payloads (e.g. sending 2 component IDs and quality floats over RPC).
- Trivial to unit test without instantiating full 3D models or physics.

---

## Production-Ready C# Architecture

```csharp
using System;
using UnityEngine;

namespace Armotheca.Crafting
{
    public enum WeaponType
    {
        Sword,
        Wand,
        Staff
    }

    public enum ElementType
    {
        Physical,
        Fire,
        Frost,
        Lightning,
        Arcane,
        Holy
    }

    public enum QualityTier
    {
        Crude,
        Standard,
        Masterwork,
        Flawless
    }

    [System.Serializable]
    public struct WeaponComponentData
    {
        public string ComponentID;
        public string DisplayName;
        public ElementType Element;
        [Range(0f, 100f)] public float QualityScore;
        public float PowerModifier;
        public float SpeedModifier;

        public QualityTier GetQualityTier() => QualityScore switch
        {
            < 40f => QualityTier.Crude,
            < 75f => QualityTier.Standard,
            < 95f => QualityTier.Masterwork,
            _ => QualityTier.Flawless
        };
    }

    /// <summary>
    /// Runtime representation of a crafted weapon resulting from exactly 2 components.
    /// </summary>
    public class AssembledWeapon
    {
        public WeaponType Type { get; }
        public WeaponComponentData PrimaryComponent { get; }   // Blade or Core
        public WeaponComponentData SecondaryComponent { get; } // Hilt or Shaft

        public float FinalPower { get; }
        public float FinalSpeed { get; }
        public ElementType FinalElement { get; }
        public QualityTier OverallQuality { get; }
        public int BaseMarketValue { get; }

        public AssembledWeapon(WeaponType type, WeaponComponentData primary, WeaponComponentData secondary)
        {
            Type = type;
            PrimaryComponent = primary;
            SecondaryComponent = secondary;

            // Element inherited primarily from the offensive/magical component
            FinalElement = primary.Element != ElementType.Physical ? primary.Element : secondary.Element;

            // Stats aggregation
            float averageQuality = (primary.QualityScore + secondary.QualityScore) * 0.5f;
            OverallQuality = averageQuality switch
            {
                < 40f => QualityTier.Crude,
                < 75f => QualityTier.Standard,
                < 95f => QualityTier.Masterwork,
                _ => QualityTier.Flawless
            };

            float qualityMultiplier = OverallQuality switch
            {
                QualityTier.Crude => 0.8f,
                QualityTier.Standard => 1.0f,
                QualityTier.Masterwork => 1.25f,
                QualityTier.Flawless => 1.5f,
                _ => 1.0f
            };

            FinalPower = (primary.PowerModifier * 1.5f + secondary.PowerModifier * 0.5f) * qualityMultiplier;
            FinalSpeed = (secondary.SpeedModifier * 1.5f + primary.SpeedModifier * 0.5f) * qualityMultiplier;

            int rawBaseCost = 50;
            BaseMarketValue = Mathf.RoundToInt(rawBaseCost * (FinalPower + FinalSpeed) * qualityMultiplier);
        }
    }

    /// <summary>
    /// Assembly bench workstation requiring 2 valid components to produce a weapon.
    /// </summary>
    public class AssemblyTable : MonoBehaviour
    {
        [Header("Sockets")]
        [SerializeField] private Transform primarySocket;
        [SerializeField] private Transform secondarySocket;
        [SerializeField] private Transform outputSocket;

        public WeaponComponentData? CurrentPrimary { get; private set; }
        public WeaponComponentData? CurrentSecondary { get; private set; }

        public event Action<AssembledWeapon> OnWeaponAssembled;
        public event Action OnTableReset;

        public bool TryInsertPrimary(WeaponComponentData component)
        {
            if (CurrentPrimary.HasValue) return false;
            CurrentPrimary = component;
            CheckAssembleReadiness();
            return true;
        }

        public bool TryInsertSecondary(WeaponComponentData component)
        {
            if (CurrentSecondary.HasValue) return false;
            CurrentSecondary = component;
            CheckAssembleReadiness();
            return true;
        }

        private void CheckAssembleReadiness()
        {
            if (CurrentPrimary.HasValue && CurrentSecondary.HasValue)
            {
                // Both slots filled; ready for manual assembly action (e.g. hammer strike)
            }
        }

        /// <summary>
        /// Triggered when player performs the assembly interaction (e.g. hammer strike / binding spell).
        /// </summary>
        public bool PerformAssembly(WeaponType targetType, out AssembledWeapon result)
        {
            result = null;
            if (!CurrentPrimary.HasValue || !CurrentSecondary.HasValue)
                return false;

            result = new AssembledWeapon(targetType, CurrentPrimary.Value, CurrentSecondary.Value);

            // Clear input sockets
            CurrentPrimary = null;
            CurrentSecondary = null;

            OnWeaponAssembled?.Invoke(result);
            return true;
        }

        public void ClearTable()
        {
            CurrentPrimary = null;
            CurrentSecondary = null;
            OnTableReset?.Invoke();
        }
    }
}
```

---

## Assembly Station Gameplay Flow

1. **Placement:** Player A brings a processed *Sun-Forged Blade* and snaps it to the table's Primary Socket.
2. **Placement:** Player B brings an *Ebony Dragon Hilt* and snaps it to the Secondary Socket.
3. **Locking Action:** Either player picks up the *Runed Mallet* and strikes the bench central anvil, initiating a 0.5-second locking animation.
4. **Result:** The completed *Sun-Forged Dragon Longsword* spawns on the output riser, complete with visual particle effects indicating its *Masterwork* tier. The weapon is now ready for inspection or packaging.
