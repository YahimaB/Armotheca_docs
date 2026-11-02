---
id: L03_Astral_Quarry
type: location
unlock: Tier 3 + gold (Door 3)
status: Draft
---

# Astral Quarry

> **World:** [_World_Map](../_World_Map.md) · **Technical:** [Realm_Loading](../../../Technical_Design/Exploration/Realm_Loading.md)

## Purpose in Progression

Quartz, Star Metal and void essence — the main source of arcane and lightning materials. Unlock: Tier 3 + gold (Door 3) ([M_Door_Purchase](../../02_Systems/Exploration/M_Door_Purchase.md)). Main elements: Arcane, Lightning.

## Layout

Follows the shared band layout (Entry → Outer Grounds → Deep Grounds → Apex Arena) in [_World_Map › Realm Bands](../_World_Map.md#realm-bands). No layout sketch yet; add it under `Maps/`.

## Encounters

| Mob | Where | Notes |
| --- | --- | --- |
| [E_Void_Slime](../../03_Entities/Mobs/Minor_Fauna/E_Void_Slime/E_Void_Slime.md) | Outer Grounds, in swarms | |
| [E_Astral_Sovereign](../../03_Entities/Mobs/Apex_Guardians/E_Astral_Sovereign/E_Astral_Sovereign.md) | Apex Arena | Guards the *Astral Prism* |

## Props & Nodes

| Entity | Where | Notes |
| --- | --- | --- |
| [E_Mineral_Vein](../../03_Entities/Props/Resource_Nodes/E_Mineral_Vein/E_Mineral_Vein.md) | Outer / Deep Grounds | Quartz, Star Metal |
| [E_Exit_Portal](../../03_Entities/Props/Interactive/E_Exit_Portal/E_Exit_Portal.md) | Entry | |
| [E_Aether_Chute](../../03_Entities/Props/Interactive/E_Aether_Chute/E_Aether_Chute.md) | Entry | |

Node types per band are rolled per opening ([M_Node_Spawning](../../02_Systems/Exploration/M_Node_Spawning.md)).

## Mood & Lighting

Floating starlit rock. Realms are darker and moodier than the workshop, lit by strong coloured accents ([Modeling Guidelines](../../../Guidelines/Modeling_Guidelines.md)).

## Connections

- Entered through its [E_Magic_Door](../../03_Entities/Props/Interactive/E_Magic_Door/E_Magic_Door.md) in [L00_Workshop](../L00_Workshop/L00_Workshop.md); left through the [E_Exit_Portal](../../03_Entities/Props/Interactive/E_Exit_Portal/E_Exit_Portal.md).

## UI

- [UI_Realm_Pressure](../../05_UI/Hud/UI_Realm_Pressure.md)

## Open Questions

-
