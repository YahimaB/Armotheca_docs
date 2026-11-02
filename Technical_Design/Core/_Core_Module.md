---
id: _Core_Module
type: module
module: Core
namespace: Armotheca.Core
status: Draft
---

# Core Module

> **Design:** technical-only (no GDD system) · **Map:** [_Module_Map](../_Module_Map.md) · **Overview:** [Technical Overview](../Technical_Overview.md)

## Scope

Types and helpers referenced by several modules, defined once. Every other module may depend on Core; Core depends on nothing.

| Used by | For |
| --- | --- |
| [_Crafting_Module](../Crafting/_Crafting_Module.md), [_Orders_Module](../Orders/_Orders_Module.md) | `ElementType` |
| [Resource_Nodes](../Exploration/Resource_Nodes.md), [Mob_AI](../Exploration/Mob_AI.md) | `DropEntry`, `DropRoller` |

---

## Architecture

The data / runtime split and the other architecture principles are in [Technical Overview §3](../Technical_Overview.md#3-architecture-principles); Core holds the shared types that follow them.

---

## Shared Types

Types referenced by several modules are defined once:

```csharp
namespace Armotheca.Core
{
    public enum ElementType
    {
        Physical,
        Fire,
        Frost,
        Lightning,
        Arcane,
        Holy
    }

    [System.Serializable]
    public struct DropEntry
    {
        public string ItemId;
        [UnityEngine.Range(0f, 1f)] public float Chance;
        public int MinQuantity;
        public int MaxQuantity;
    }

    public static class DropRoller
    {
        public static void Roll(System.Collections.Generic.IEnumerable<DropEntry> table,
                                System.Random rng,
                                System.Collections.Generic.List<string> results)
        {
            foreach (var entry in table)
            {
                if (rng.NextDouble() > entry.Chance) continue;
                int qty = rng.Next(entry.MinQuantity, entry.MaxQuantity + 1);
                for (int i = 0; i < qty; i++) results.Add(entry.ItemId);
            }
        }
    }
}
```

- Drop rolls take an explicit `System.Random` seeded by the host so results are deterministic and reproducible in tests.
