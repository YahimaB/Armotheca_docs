---
id: M_Node_Spawning
type: mechanic
system: Exploration
status: Draft
---

# Node Spawning

> **System:** [_Exploration_System](_Exploration_System.md) · **Technical:** [Resource Gathering (tech)](../../../Technical_Design/Exploration/Resource_Gathering.md)

## Summary

Each realm layout has hand-made node spawn points grouped by band; which ones are active and what they hold is rolled when the door opens.

## Rules

1. Each band (Outer / Deep) rolls how many of its spawn points are active.
2. Each active point picks a node type from the band's weighted table (Outer: common veins and trees; Deep: rare veins, crystal clusters). The tables per realm are in each location doc.
3. A small chance turns a node into its rare variant.
4. **Letter guarantee:** if an active letter requires a node material that this realm can provide, at least one node of that type spawns.
5. No respawn during an expedition.

## Tunable Parameters

| Parameter | Meaning | Value |
| --- | --- | --- |
| Active spawn points per band | Share of points used | [Exploration › Nodes](../../06_Balancing/Exploration.md#nodes) |
| Rare variant chance | Per node | [Exploration › Nodes](../../06_Balancing/Exploration.md#nodes) |
| Letter guarantee | Nodes per required material | [Exploration › Nodes](../../06_Balancing/Exploration.md#nodes) |

## UI

- None.

## Dependencies

- [M_Realm_Instancing](M_Realm_Instancing.md), [M_Letter_Flow](../Orders/M_Letter_Flow.md)

## Used By

- [F03_Expeditions](../../01_Features/F03_Expeditions.md)

## Open Questions

- Should nodes have a quality grade that feeds into processing quality?
