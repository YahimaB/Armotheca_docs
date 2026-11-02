---
id: E_Bramble_Stalker
type: entity
category: Mobs
status: Draft
---

# Bramble Stalker

> **Roster:** [_Mob_Roster](../_Mob_Roster.md) · **Technical:** [Mobs (tech)](../../../../Technical_Design/Exploration/Mobs.md)

## Description & Role

Minor Fauna of [L01_Verdant_Corruption](../../../04_Locations/L01_Verdant_Corruption/L01_Verdant_Corruption.md), found mainly in the Outer Grounds. Staggered by sword hits. Shared mob rules: [_Mob_Roster](../_Mob_Roster.md).

## Behaviour & States

- **Chaser:** Closes distance and attacks with a telegraphed lunge or bite. Counter: roll through the lunge, then swing.
- **Ambusher:** Hides near nodes and wakes when a node is harvested. Counter: guard harvesters.

Can spawn as an ambusher hidden next to nodes ([M_Mob_Spawning](../../../02_Systems/Exploration/M_Mob_Spawning.md)).

## Stats

Health and attack damage: not yet defined; they will live in [Combat › Mobs](../../../06_Balancing/Combat.md#mobs).

## Outputs

Notable drop: **Thorned Pelt, Verdant Essence**. Drops are a guaranteed main drop plus chance-based extras; essences feed cores ([M_Resource_Processing](../../../02_Systems/Processing/M_Resource_Processing.md)).

## UI

None yet; mob health display is planned in [_UI_Flow](../../../05_UI/_UI_Flow.md).

## Appears In

- [L01_Verdant_Corruption](../../../04_Locations/L01_Verdant_Corruption/L01_Verdant_Corruption.md)
- [F04_Combat](../../../01_Features/F04_Combat.md)

## Open Questions

-
