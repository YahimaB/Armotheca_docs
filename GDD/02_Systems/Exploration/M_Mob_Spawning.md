---
id: M_Mob_Spawning
type: mechanic
system: Exploration
status: Draft
---

# Mob Spawning

> **System:** [_Exploration_System](_Exploration_System.md) · **Technical:** [Mobs (tech)](../../../Technical_Design/Exploration/Mobs.md)

## Summary

Mobs are placed in hand-made spawn zones when the realm is created, then keep arriving as wandering spawns driven by Realm Pressure.

## Rules

1. Each realm layout has hand-placed **mob spawn zones** by band (Outer / Deep). No mobs spawn in the Entry area.
2. **On door open:** each zone rolls whether it is active and which mob group (from the band's weighted table) it spawns.
3. **Ambushers** spawn hidden next to some nodes and wake when harvesting starts ([M_Harvesting](M_Harvesting.md)).
4. **Letter guarantee:** if an active letter needs a mob drop available in this realm, at least one group containing that mob spawns.
5. **Wandering spawns** arrive at an interval and up to an alive cap, both set by the pressure level ([M_Realm_Pressure](M_Realm_Pressure.md)).
6. Mobs do not leave the realm and never follow players through the Exit Portal or the door.

## Tunable Parameters

| Parameter | Meaning | Value |
| --- | --- | --- |
| Active spawn zones per band | Share of zones used on creation | [Exploration › Mobs](../../06_Balancing/Exploration.md#mobs) |
| Mob groups per band | Weighted tables | Not yet defined |

## UI

- None.

## Dependencies

- [_Mob_Roster](../../03_Entities/Mobs/_Mob_Roster.md), [M_Realm_Instancing](M_Realm_Instancing.md), [M_Letter_Flow](../Orders/M_Letter_Flow.md)

## Used By

- [F03_Expeditions](../../01_Features/F03_Expeditions.md), [F04_Combat](../../01_Features/F04_Combat.md)

## Open Questions

- Should mob health scale with player count, or should more mobs spawn instead?
