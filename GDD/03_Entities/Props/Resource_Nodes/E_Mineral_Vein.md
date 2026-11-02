---
id: E_Mineral_Vein
type: entity
category: Props
status: Draft
---

# Mineral Vein

> **Roster:** [_Prop_List](../_Prop_List.md) · **Technical:** [Resource Gathering (tech)](../../../../Technical_Design/Exploration/Resource_Gathering.md)

## Description & Role

Ore veins and crystal clusters. Harvested with a pickaxe. Each node type has a distinct silhouette and colour, readable from across the realm. Rare variants glow.

## Behaviour & States

Intact → struck (visible damage per hit) → broken (drops yield, does not regrow this expedition). See [M_Harvesting](../../../02_Systems/Exploration/M_Harvesting.md).

## Stats

Hits per node: [Exploration › Nodes](../../../06_Balancing/Exploration.md#nodes).

## Outputs

Primary yield: Ores, Crystals, Flux. Used for: Blades (smelting).

## UI

[UI_Interaction_Prompt](../../../05_UI/World/UI_Interaction_Prompt.md)

## Appears In

- Node types: Iron Vein ([L01](../../../04_Locations/L01_Verdant_Corruption/L01_Verdant_Corruption.md)), Obsidian and Brimstone ([L02](../../../04_Locations/L02_Pyroclastic_Trench/L02_Pyroclastic_Trench.md)), Quartz and Star Metal ([L03](../../../04_Locations/L03_Astral_Quarry/L03_Astral_Quarry.md)), Glacial Ice-Ore ([L04](../../../04_Locations/L04_Frostbite_Cavern/L04_Frostbite_Cavern.md))
- [F03_Expeditions](../../../01_Features/F03_Expeditions.md)

## Open Questions

-
