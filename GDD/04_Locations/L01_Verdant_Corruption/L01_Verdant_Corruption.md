---
id: L01_Verdant_Corruption
type: location
unlock: Owned at start (Door 1)
status: Draft
---

# Verdant Corruption

> **World:** [_World_Map](../_World_Map.md) · **Technical:** [Realm_Loading](../../../Technical_Design/Exploration/Realm_Loading.md)

## Purpose in Progression

Timber (Bog Oak, Ironwood), Iron Vein and beast parts — the first source of foundations and basic ore. Unlock: Owned at start (Door 1) ([M_Door_Purchase](../../02_Systems/Exploration/M_Door_Purchase.md)). Main elements: Physical, Arcane.

## Layout

Follows the shared band layout (Entry → Outer Grounds → Deep Grounds → Apex Arena) in [_World_Map › Realm Bands](../_World_Map.md#realm-bands). No layout sketch yet; add it under `Maps/`.

## Encounters

| Mob | Where | Notes |
| --- | --- | --- |
| [E_Bramble_Stalker](../../03_Entities/Mobs/Minor_Fauna/E_Bramble_Stalker.md) | Outer Grounds; also hidden next to nodes as ambushers | |
| [E_Verdant_Elder](../../03_Entities/Mobs/Apex_Guardians/E_Verdant_Elder.md) | Apex Arena | Guards the *Sylvan Spire* |

## Props & Nodes

| Entity | Where | Notes |
| --- | --- | --- |
| [E_Arcane_Flora](../../03_Entities/Props/Resource_Nodes/E_Arcane_Flora.md) | Outer / Deep Grounds | Bog Oak, Ironwood |
| [E_Mineral_Vein](../../03_Entities/Props/Resource_Nodes/E_Mineral_Vein.md) | Outer / Deep Grounds | Iron Vein |
| [E_Exit_Portal](../../03_Entities/Props/Interactive/E_Exit_Portal.md) | Entry | |
| [E_Aether_Chute](../../03_Entities/Props/Interactive/E_Aether_Chute.md) | Entry | |

Node types per band are rolled per opening ([M_Node_Spawning](../../02_Systems/Exploration/M_Node_Spawning.md)).

## Mood & Lighting

Overgrown corrupted grove. Realms are darker and moodier than the workshop, lit by strong coloured accents ([Modeling Guidelines](../../../Guidelines/Modeling_Guidelines.md)).

## Connections

- Entered through its [E_Magic_Door](../../03_Entities/Props/Interactive/E_Magic_Door.md) in [L00_Workshop](../L00_Workshop/L00_Workshop.md); left through the [E_Exit_Portal](../../03_Entities/Props/Interactive/E_Exit_Portal.md).

## UI

- [UI_Realm_Pressure](../../05_UI/Hud/UI_Realm_Pressure.md)

## Open Questions

-
