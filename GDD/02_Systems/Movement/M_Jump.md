---
id: M_Jump
type: mechanic
system: Movement
status: Draft
---

# Jump

> **System:** [_Movement_System](_Movement_System.md) · **Technical:** [_Movement_Module › States](../../../Technical_Design/Movement/_Movement_Module.md#states)

## Summary

A single jump with a fixed height and forgiving timing.

## Rules

1. Single jump with a fixed height; no double jump.
2. Limited air control: players can correct a jump but not change direction completely.
3. **Coyote time** and **jump buffering** make edge jumps and early presses forgiving.
4. Used for small ledges, gaps and obstacles in realms. The workshop layout never *requires* jumping to reach a station.

## Tunable Parameters

| Parameter | Meaning | Value |
| --- | --- | --- |
| Jump height | Fixed apex height | [Movement › Jump](../../06_Balancing/Movement.md#jump) |
| Coyote time / jump buffer | Grace windows | [Movement › Jump](../../06_Balancing/Movement.md#jump) |

## UI

- None.

## Used By

- [F03_Expeditions](../../01_Features/F03_Expeditions.md)

## Open Questions

- Do realms need any traversal beyond a single jump (ladders, grapples, climbable ledges)?
