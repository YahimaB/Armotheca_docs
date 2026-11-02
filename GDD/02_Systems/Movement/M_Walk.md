---
id: M_Walk
type: mechanic
system: Movement
status: Draft
---

# Walk

> **System:** [_Movement_System](_Movement_System.md) · **Technical:** [_Movement_Module › States](../../../Technical_Design/Movement/_Movement_Module.md#states)

## Summary

Default locomotion on the movement stick or WASD.

## Rules

1. The character rotates to face the movement direction quickly (no tank controls).
2. Analog input scales speed between a slow step and full walk speed.
3. Carrying an item multiplies walk speed by the carrying multiplier.

## Player Input

Movement stick / WASD.

## Tunable Parameters

| Parameter | Meaning | Value |
| --- | --- | --- |
| Walk speed | Full walk speed | [Movement › Walk](../../06_Balancing/Movement.md#walk) |
| Carrying multiplier | Speed while hands hold an item | [Movement › Walk](../../06_Balancing/Movement.md#walk) |

## UI

- None.

## Used By

- [F02_Weapon_Crafting](../../01_Features/F02_Weapon_Crafting.md), [F03_Expeditions](../../01_Features/F03_Expeditions.md); every feature with movement.

## Open Questions

-
