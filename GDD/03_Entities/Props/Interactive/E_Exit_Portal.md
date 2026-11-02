---
id: E_Exit_Portal
type: entity
category: Props
status: Draft
---

# Exit Portal

> **Roster:** [_Prop_List](../_Prop_List.md) · **Technical:** [Door_Instances](../../../../Technical_Design/Exploration/Door_Instances.md)

## Description & Role

The way home. One stands in every realm's Entry area and is **always open**.

## Behaviour & States

- Using it (instant interaction) returns the player to the workshop in front of the door they came through ([M_Door_Lifecycle](../../../02_Systems/Exploration/M_Door_Lifecycle.md)).
- Mobs never follow players through it.

## UI

- [UI_Interaction_Prompt](../../../05_UI/World/UI_Interaction_Prompt.md)

## Appears In

- Entry area of every realm ([_World_Map](../../../04_Locations/_World_Map.md))
- [F03_Expeditions](../../../01_Features/F03_Expeditions.md)

## Open Questions

-
