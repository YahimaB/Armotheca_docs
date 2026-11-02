---
id: E_Long_Shaft
type: entity
category: Items
status: Draft
---

# Long Shaft

> **Roster:** [_Item_List](../../_Item_List.md) · **Technical:** [_Crafting_Module › Architecture](../../../../../Technical_Design/Crafting/_Crafting_Module.md#architecture--implementation-approaches)

## Description & Role

Foundation for staves ([M_Assembly](../../../../02_Systems/Crafting/M_Assembly.md)).

## Stats

Carries Quality (from processing) + material identity. No Base Damage.

## Mechanics

- Produced by Woodworking Lathe → Carving Bench ([M_Resource_Processing](../../../../02_Systems/Processing/M_Resource_Processing.md)).
- Snapped into the [E_Assembly_Bench](../../../Props/Workstations/E_Assembly_Bench/E_Assembly_Bench.md).

## UI

[UI_Assembly_Bench](../../../../05_UI/World/UI_Assembly_Bench.md): socket display.

## Appears In

- [L00_Workshop](../../../../04_Locations/L00_Workshop/L00_Workshop.md)
- [F02_Weapon_Crafting](../../../../01_Features/F02_Weapon_Crafting.md)

## Open Questions

-
