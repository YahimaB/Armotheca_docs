# Weapon Crafting - Technical Design

> **Zone:** Shop · **Design:** [GDD/Shop/WeaponCrafting](../../GDD/Shop/WeaponCrafting.md) · **UI:** [Assembly Bench UI](../../UIDesign/Workstations/AssemblyBenchUI.md)

## Technical Specifications

### Weapon Stat Model (Locked)
| Field | Type | Range | Source |
|---|---|---|---|
| `Quality` | `int` | 1–100 | `round((foundation.Quality + payload.Quality) / 2)` |
| `BaseDamage` | `int` | ≥ 0 | `payload.BaseDamage` (constant from payload material data) |

- No other numeric weapon stats exist. Adding a stat requires a design revision of the GDD and of this model.
- Quality does not modify Base Damage.
- `Element` and material IDs are **non-numeric attributes** carried for order validation, naming and VFX.

### Category Resolution
| Foundation Kind | Payload Kind | Result |
|---|---|---|
| `Hilt` | `Blade` | `Sword` |
| `ShortShaft` | `Core` | `Wand` |
| `LongShaft` | `Core` | `Staff` |
| anything else | | Incompatible |

### Quality Tiers
| Tier | Range |
|---|---|
| `Crude` | 1–39 |
| `Standard` | 40–74 |
| `Masterwork` | 75–94 |
| `Flawless` | 95–100 |

---

## Architecture & Implementation Approaches

### Approach A: ScriptableObject Material Definitions + Pure Domain Assembly (Recommended)

**Patterns:** Factory, Single Responsibility, Observer.

- `ComponentMaterialDefinition` (SO): material ID, display name, element, `BaseDamage` (payload materials only), allowed component kinds.
- `WeaponComponentData` (struct): runtime component — material ID, kind, element, quality, base damage.
- `WeaponAssembler` (static): validates compatibility and builds an immutable `AssembledWeapon`.
- `AssemblyBench` (MonoBehaviour): physical workstation with two sockets and the mallet strike; uses the common [Object Interaction](../Common/ObjectInteraction.md) contracts.

**Pros:**
- Static data decoupled from runtime instances.
- Networkable as tiny payloads (two material IDs, two kinds, two quality ints).
- Assembly rules unit-testable without scenes.

### Approach B: Prefab-Per-Weapon
- Every valid combination authored as a prefab.
- **Cons:** Combinatorial explosion; rejected.

---

## Networking

- Socket contents and assembly are host-authoritative. Clients request `PlaceInSocket`, `TakeFromSocket`, `StrikeMallet`.
- An `AssembledWeapon` is replicated as `{ type, foundation, payload }`; `Quality` and `BaseDamage` are recomputed deterministically on each client.

---

## Unity C# Reference Code

```csharp
using System;
using UnityEngine;
using Armotheca.Core;

namespace Armotheca.Crafting
{
    public enum WeaponType { Sword, Wand, Staff }

    public enum ComponentKind { Hilt, Blade, ShortShaft, LongShaft, Core }

    public enum QualityTier { Crude, Standard, Masterwork, Flawless }

    public static class QualityRules
    {
        public const int Min = 1;
        public const int Max = 100;
        public const int Baseline = 60; // result when a mini-game is skipped

        public static int Clamp(int quality) => Mathf.Clamp(quality, Min, Max);

        public static QualityTier GetTier(int quality) => Clamp(quality) switch
        {
            < 40 => QualityTier.Crude,
            < 75 => QualityTier.Standard,
            < 95 => QualityTier.Masterwork,
            _ => QualityTier.Flawless
        };
    }

    [CreateAssetMenu(menuName = "Armotheca/Crafting/Component Material")]
    public class ComponentMaterialDefinition : ScriptableObject
    {
        public string MaterialId;
        public string DisplayName;
        public ElementType Element = ElementType.Physical;
        [Tooltip("Only used when this material becomes a Blade or Core.")]
        [Min(0)] public int BaseDamage;
    }

    [Serializable]
    public struct WeaponComponentData
    {
        public string MaterialId;
        public string DisplayName;
        public ComponentKind Kind;
        public ElementType Element;
        [Range(QualityRules.Min, QualityRules.Max)] public int Quality;
        public int BaseDamage; // 0 for foundations

        public bool IsPayload => Kind is ComponentKind.Blade or ComponentKind.Core;
        public bool IsFoundation => !IsPayload;
        public QualityTier Tier => QualityRules.GetTier(Quality);

        public static WeaponComponentData Create(ComponentMaterialDefinition material, ComponentKind kind, int quality)
        {
            bool payload = kind is ComponentKind.Blade or ComponentKind.Core;
            return new WeaponComponentData
            {
                MaterialId = material.MaterialId,
                DisplayName = $"{material.DisplayName} {kind}",
                Kind = kind,
                Element = payload ? material.Element : ElementType.Physical,
                Quality = QualityRules.Clamp(quality),
                BaseDamage = payload ? material.BaseDamage : 0
            };
        }
    }

    /// <summary>Immutable runtime weapon. Two stats only: Quality and BaseDamage.</summary>
    public sealed class AssembledWeapon
    {
        public WeaponType Type { get; }
        public WeaponComponentData Foundation { get; }
        public WeaponComponentData Payload { get; }

        public int Quality { get; }
        public int BaseDamage { get; }

        public QualityTier Tier => QualityRules.GetTier(Quality);
        public ElementType Element => Payload.Element;

        internal AssembledWeapon(WeaponType type, WeaponComponentData foundation, WeaponComponentData payload)
        {
            Type = type;
            Foundation = foundation;
            Payload = payload;
            Quality = QualityRules.Clamp((foundation.Quality + payload.Quality + 1) / 2); // integer average, half rounds up
            BaseDamage = payload.BaseDamage;
        }
    }

    public static class WeaponAssembler
    {
        public static bool TryResolveType(ComponentKind foundation, ComponentKind payload, out WeaponType type)
        {
            switch (foundation, payload)
            {
                case (ComponentKind.Hilt, ComponentKind.Blade): type = WeaponType.Sword; return true;
                case (ComponentKind.ShortShaft, ComponentKind.Core): type = WeaponType.Wand; return true;
                case (ComponentKind.LongShaft, ComponentKind.Core): type = WeaponType.Staff; return true;
                default: type = default; return false;
            }
        }

        public static bool TryAssemble(WeaponComponentData foundation, WeaponComponentData payload,
                                       out AssembledWeapon weapon, out string error)
        {
            weapon = null;
            if (!TryResolveType(foundation.Kind, payload.Kind, out var type))
            {
                error = $"Incompatible Modules: {foundation.Kind} cannot mount a {payload.Kind}.";
                return false;
            }

            error = null;
            weapon = new AssembledWeapon(type, foundation, payload);
            return true;
        }
    }

    /// <summary>Assembly bench with a Foundation socket, a Payload socket and a mallet strike.</summary>
    public class AssemblyBench : MonoBehaviour
    {
        [SerializeField] private Transform foundationSocket;
        [SerializeField] private Transform payloadSocket;
        [SerializeField] private Transform outputSocket;

        public WeaponComponentData? Foundation { get; private set; }
        public WeaponComponentData? Payload { get; private set; }

        public event Action<AssembledWeapon> OnPreviewChanged;   // null when not assemblable
        public event Action<string> OnIncompatible;
        public event Action<AssembledWeapon> OnWeaponAssembled;

        private bool lastInsertedWasPayload;

        /// <summary>Returns false if the socket is occupied or the part was ejected as incompatible.</summary>
        public bool TryInsert(WeaponComponentData component)
        {
            if (component.IsFoundation && !Foundation.HasValue) Foundation = component;
            else if (component.IsPayload && !Payload.HasValue) Payload = component;
            else return false;

            lastInsertedWasPayload = component.IsPayload;
            return UpdatePreview();
        }

        public bool CanStrike => Foundation.HasValue && Payload.HasValue &&
                                 WeaponAssembler.TryResolveType(Foundation.Value.Kind, Payload.Value.Kind, out _);

        /// <summary>Instant interaction: strike the runed mallet.</summary>
        public bool StrikeMallet(out AssembledWeapon result)
        {
            result = null;
            if (!Foundation.HasValue || !Payload.HasValue) return false;
            if (!WeaponAssembler.TryAssemble(Foundation.Value, Payload.Value, out result, out _)) return false;

            Foundation = null;
            Payload = null;
            OnPreviewChanged?.Invoke(null);
            OnWeaponAssembled?.Invoke(result);
            return true;
        }

        private bool UpdatePreview()
        {
            if (!Foundation.HasValue || !Payload.HasValue) { OnPreviewChanged?.Invoke(null); return true; }

            if (WeaponAssembler.TryAssemble(Foundation.Value, Payload.Value, out var preview, out var error))
            {
                OnPreviewChanged?.Invoke(preview);
                return true;
            }

            // Eject the last-inserted incompatible part back to the player (see UI doc).
            OnIncompatible?.Invoke(error);
            if (lastInsertedWasPayload) Payload = null; else Foundation = null;
            return false;
        }
    }
}
```

---

## Testing Notes

- Unit-test every `(foundation, payload)` pair for correct resolution / rejection.
- Quality averaging rounds half up and stays within 1–100 for all input pairs.
- `BaseDamage` of an assembled weapon always equals its payload's base damage, regardless of quality.
