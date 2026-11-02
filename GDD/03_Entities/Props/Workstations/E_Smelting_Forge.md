---
id: E_Smelting_Forge
type: entity
category: Props
status: Draft
---

# Smelting Forge

> **Roster:** [_Prop_List](../_Prop_List.md) · **Technical:** [Resource Processing (tech)](../../../../Technical_Design/Shop/Resource_Processing.md)

## Description & Role

Heats raw ore into a hot ingot. Ore is loaded (instant); a player works the bellows (continuous), and a second player on the bellows speeds it up.

## Behaviour & States

- **Input → output:** Raw ore → hot ingot
- **Unlocked at:** Tier 1 (Basic Smelter)

## Mechanics

- [M_Resource_Processing](../../../02_Systems/Processing/M_Resource_Processing.md), [M_Instant_Interaction](../../../02_Systems/Interaction/M_Instant_Interaction.md), [M_Continuous_Interaction](../../../02_Systems/Interaction/M_Continuous_Interaction.md)

## UI

[UI_Interaction_Prompt](../../../05_UI/World/UI_Interaction_Prompt.md)

## Appears In

- [L00_Workshop](../../../04_Locations/L00_Workshop/L00_Workshop.md)
- [F02_Weapon_Crafting](../../../01_Features/F02_Weapon_Crafting.md)

## Open Questions

-
