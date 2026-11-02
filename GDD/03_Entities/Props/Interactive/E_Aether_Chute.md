---
id: E_Aether_Chute
type: entity
category: Props
status: Draft
---

# Aether Drop-Chute

> **Roster:** [_Prop_List](../_Prop_List.md) · **Technical:** [Magic Doors (tech)](../../../../Technical_Design/Exploration/Magic_Doors.md)

## Description & Role

A chute near the realm entry point that instantly sends deposited resources to a receiving basket in the workshop. With entry sealed after the window, it is the main way to supply the workshop mid-run without ending anyone's expedition ([_Exploration_System](../../../02_Systems/Exploration/_Exploration_System.md)).

## Behaviour & States

- Players empty their backpack into it one item per press or all at once with a hold ([M_Carry_Model](../../../02_Systems/Interaction/M_Carry_Model.md)).

## Mechanics

- [M_Instant_Interaction](../../../02_Systems/Interaction/M_Instant_Interaction.md), [M_Continuous_Interaction](../../../02_Systems/Interaction/M_Continuous_Interaction.md)

## UI

- [UI_Interaction_Prompt](../../../05_UI/World/UI_Interaction_Prompt.md)

## Appears In

- Entry area of every realm ([_World_Map](../../../04_Locations/_World_Map.md)); the receiving basket is in [L00_Workshop](../../../04_Locations/L00_Workshop/L00_Workshop.md).
- [F03_Expeditions](../../../01_Features/F03_Expeditions.md)

## Open Questions

-
