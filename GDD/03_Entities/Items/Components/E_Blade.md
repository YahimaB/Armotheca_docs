---
id: E_Blade
type: entity
category: Items
status: Draft
---

# Blade

> **Roster:** [_Item_List](../_Item_List.md) · **Technical:** [Weapon Crafting (tech)](../../../../Technical_Design/Shop/Weapon_Crafting.md)

## Description & Role

Payload for swords ([M_Assembly](../../../02_Systems/Crafting/M_Assembly.md)).

## Stats

Carries Quality (from processing) + Base Damage and Element (from the ore material).

## Mechanics

- Produced by Smelting Forge → Anvil → Quenching Basin ([M_Resource_Processing](../../../02_Systems/Processing/M_Resource_Processing.md)).
- Snapped into the [E_Assembly_Bench](../../Props/Workstations/E_Assembly_Bench.md).

## UI

[UI_Assembly_Bench](../../../05_UI/World/UI_Assembly_Bench.md): socket display.

## Appears In

- [L00_Workshop](../../../04_Locations/L00_Workshop/L00_Workshop.md)
- [F02_Weapon_Crafting](../../../01_Features/F02_Weapon_Crafting.md)

## Open Questions

-
