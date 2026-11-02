---
id: E_Wand
type: entity
category: Items
status: Draft
---

# Wand

> **Roster:** [_Item_List](../_Item_List.md) · **Technical:** [_Crafting_Module › Architecture](../../../../Technical_Design/Crafting/_Crafting_Module.md#architecture--implementation-approaches)

## Description & Role

1-handed weapon assembled from a **Short Shaft** (foundation) and a **Core** (payload) ([M_Assembly](../../../02_Systems/Crafting/M_Assembly.md)). It is both a commission deliverable and a weapon players can equip.

## Stats

Quality and Base Damage only ([M_Quality](../../../02_Systems/Crafting/M_Quality.md)).

## Mechanics

- Attack: [M_Magic_Orb](../../../02_Systems/Combat/M_Magic_Orb.md), dealing Base Damage per hit.
- Named by [M_Weapon_Naming](../../../02_Systems/Crafting/M_Weapon_Naming.md).
- Carried in hands or the weapon slot ([M_Carry_Model](../../../02_Systems/Interaction/M_Carry_Model.md)).

## UI

[UI_Assembly_Bench](../../../05_UI/World/UI_Assembly_Bench.md): preview and output.

## Appears In

- [F02_Weapon_Crafting](../../../01_Features/F02_Weapon_Crafting.md), [F04_Combat](../../../01_Features/F04_Combat.md), [F01_Commissions](../../../01_Features/F01_Commissions.md)

## Open Questions

-
