---
id: M_Harvesting
type: mechanic
system: Exploration
status: Draft
---

# Harvesting

> **System:** [_Exploration_System](_Exploration_System.md) · **Technical:** [Resource_Nodes](../../../Technical_Design/Exploration/Resource_Nodes.md)

## Summary

Players hold interact on a resource node to strike it with a contextual tool until it breaks and drops its yield.

## Rules

1. Harvesting is a **continuous interaction** ([M_Continuous_Interaction](../Interaction/M_Continuous_Interaction.md)): the player holds interact and the character performs repeated strikes with a contextual tool (pickaxe for veins, axe for flora). Each strike is one hit.
2. When a node's hits are exhausted, it breaks and drops its yield on the ground around it. Drops are collected as described in [M_Carry_Model](../Interaction/M_Carry_Model.md).
3. A limited number of players can harvest the same node together; each adds strikes.
4. Releasing the button or getting hit interrupts harvesting; hits already dealt are kept.
5. Harvested nodes **do not regrow** during the same expedition, so the longer a team stays, the further they must travel for the next node while Realm Pressure rises.
6. **Yields:** each node type has a drop table — a guaranteed main material plus chance-based extras (e.g. an Iron Vein always yields Iron Ore, sometimes Flux). Rare node variants (glowing) give the same material in larger quantity or a rare extra.
7. Starting to harvest a node wakes ambushers hidden next to it ([M_Mob_Spawning](M_Mob_Spawning.md)).

## Player Input

Hold interact on a node.

## Tunable Parameters

| Parameter | Meaning | Value |
| --- | --- | --- |
| Hits per node | Per node kind | [Exploration › Nodes](../../06_Balancing/Exploration.md#nodes) |
| Max harvesters per node | Co-op limit | [Exploration › Nodes](../../06_Balancing/Exploration.md#nodes) |
| Drop tables | Per node kind | Not yet defined |

## Feedback

Every strike has a crunch, a chip effect and visible damage on the node.

## UI

- [UI_Interaction_Prompt](../../05_UI/World/UI_Interaction_Prompt.md)

## Dependencies

- Nodes: [E_Mineral_Vein](../../03_Entities/Props/Resource_Nodes/E_Mineral_Vein/E_Mineral_Vein.md), [E_Arcane_Flora](../../03_Entities/Props/Resource_Nodes/E_Arcane_Flora/E_Arcane_Flora.md)

## Used By

- [F03_Expeditions](../../01_Features/F03_Expeditions.md)

## Open Questions

- Is the contextual tool enough, or should tools be physical items players must bring (and can forget)?
- Should the same weapon used for fighting also act as the harvesting tool, or should harvesting stay purely contextual?
- Should yields scale with player count to keep 4-player sessions supplied?
