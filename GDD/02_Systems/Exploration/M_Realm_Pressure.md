---
id: M_Realm_Pressure
type: mechanic
system: Exploration
status: Draft
---

# Realm Pressure

> **System:** [_Exploration_System](_Exploration_System.md) · **Technical:** [Mobs (tech)](../../../Technical_Design/Exploration/Mobs.md)

## Summary

A danger level that rises while a realm is occupied — the force that replaces a door timer in ending expeditions.

## Rules

1. Pressure starts at level 0 when the realm is created and rises one level at a fixed interval while the realm is occupied.
2. It never resets during an expedition, including when members step out and back in.
3. Each level shortens the interval between wandering-mob spawns and raises the number of mobs allowed alive at once, up to a performance cap ([M_Mob_Spawning](M_Mob_Spawning.md)).
4. From a set level, Deep Grounds groups can spawn in the Outer Grounds, so even the area near the Exit Portal stops being safe.
5. There is no upper limit on danger.

## Tunable Parameters

| Parameter | Meaning | Value |
| --- | --- | --- |
| Level-up interval | Occupied time per level | [Exploration › Realm Pressure](../../06_Balancing/Exploration.md#realm-pressure) |
| Wandering spawn interval | Per level | [Exploration › Realm Pressure](../../06_Balancing/Exploration.md#realm-pressure) |
| Max simultaneous mobs | Per level and hard cap | [Exploration › Realm Pressure](../../06_Balancing/Exploration.md#realm-pressure) |
| Deep groups in Outer Grounds | Starting level | [Exploration › Realm Pressure](../../06_Balancing/Exploration.md#realm-pressure) |

## Feedback

A growing distortion around the screen edges and a realm-wide audio cue on every level-up, so players feel danger rising without a countdown.

## UI

- [UI_Realm_Pressure](../../05_UI/Hud/UI_Realm_Pressure.md)

## Dependencies

- [M_Mob_Spawning](M_Mob_Spawning.md)

## Used By

- [F03_Expeditions](../../01_Features/F03_Expeditions.md), [F04_Combat](../../01_Features/F04_Combat.md)

## Open Questions

- Should Realm Pressure also raise mob damage or health at high levels, or is more mobs enough to push teams home?
