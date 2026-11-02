---
id: M_Sprint
type: mechanic
system: Movement
status: Draft
---

# Sprint

> **System:** [_Movement_System](_Movement_System.md) · **Technical:** [Movement (tech)](../../../Technical_Design/Common/Movement.md)

## Summary

A held modifier for higher top speed.

## Rules

1. Higher top speed than walk, with a slightly wider turning radius to sell momentum.
2. **No stamina cost at this stage**, so the workshop never feels sluggish.
3. Allowed while carrying an item (the carrying multiplier applies).
4. Not available while swinging a sword or casting an orb ([M_Sword_Swing](../Combat/M_Sword_Swing.md), [M_Magic_Orb](../Combat/M_Magic_Orb.md)).

## Player Input

Held modifier: `Shift`, left stick click or a shoulder button (final binding in input mapping).

## Tunable Parameters

| Parameter | Meaning | Value |
| --- | --- | --- |
| Sprint speed | Top speed while sprinting | [Movement › Sprint](../../06_Balancing/Movement.md#sprint) |

## UI

- None.

## Used By

- [F02_Weapon_Crafting](../../01_Features/F02_Weapon_Crafting.md), [F03_Expeditions](../../01_Features/F03_Expeditions.md); every feature with movement.

## Open Questions

-
