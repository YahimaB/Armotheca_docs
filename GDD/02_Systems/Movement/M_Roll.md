---
id: M_Roll
type: mechanic
system: Movement
status: Draft
---

# Roll

> **System:** [_Movement_System](_Movement_System.md) · **Technical:** [_Movement_Module › States](../../../Technical_Design/Movement/_Movement_Module.md#states)

## Summary

A quick directional burst with a short invulnerability window — the main defensive tool in combat.

## Rules

1. Triggered on a single press, in the input direction (or the facing direction with no input).
2. Grants an **invulnerability window** at the start of the roll.
3. A short cooldown prevents chaining rolls as a faster-than-sprint travel method.
4. **Not available while carrying an item** (hands are busy, see [M_Carry_Model](../Interaction/M_Carry_Model.md)).
5. Cancels the recovery of a sword swing ([M_Sword_Swing](../Combat/M_Sword_Swing.md)) and cancels a continuous interaction ([M_Continuous_Interaction](../Interaction/M_Continuous_Interaction.md)).

## Tunable Parameters

| Parameter | Meaning | Value |
| --- | --- | --- |
| Roll distance / duration | Burst size | [Movement › Roll](../../06_Balancing/Movement.md#roll) |
| Invulnerability window | From roll start | [Movement › Roll](../../06_Balancing/Movement.md#roll) |
| Cooldown | Between rolls | [Movement › Roll](../../06_Balancing/Movement.md#roll) |

## Feedback

Readable at a glance by teammates (see [_Movement_System](_Movement_System.md) design goals).

## UI

- None.

## Used By

- [F04_Combat](../../01_Features/F04_Combat.md)

## Open Questions

-
