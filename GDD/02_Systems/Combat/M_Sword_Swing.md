---
id: M_Sword_Swing
type: mechanic
system: Combat
status: Draft
---

# Sword Swing

> **System:** [_Combat_System](_Combat_System.md) · **Technical:** [_Combat_Module › Technical Specifications](../../../Technical_Design/Combat/_Combat_Module.md#technical-specifications)

## Summary

A short chain of melee swings in a frontal arc.

## Rules

1. **Chain:** swings alternate right-to-left, then left-to-right. Pressing attack during the late part of a swing queues the next one; after the last swing the chain resets.
2. **Hit area:** a frontal arc. One swing can hit **several enemies**, but each enemy at most once per swing.
3. **Damage:** Base Damage of the sword per hit.
4. **Commitment:** the player slows down heavily during a swing and cannot sprint. Rolling cancels the swing's recovery.
5. **Grounded only:** swords cannot be swung while airborne.
6. **Knockback:** light; staggers small mobs only ([_Mob_Roster](../../03_Entities/Mobs/_Mob_Roster.md)).

## Player Input

Attack button with a sword equipped and empty hands.

## Tunable Parameters

| Parameter | Meaning | Value |
| --- | --- | --- |
| Chain length | Swings before reset | [Combat › Sword Swing](../../06_Balancing/Combat.md#sword-swing) |
| Windup / active / recovery | Swing timing | [Combat › Sword Swing](../../06_Balancing/Combat.md#sword-swing) |
| Arc angle / reach | Hit area | [Combat › Sword Swing](../../06_Balancing/Combat.md#sword-swing) |
| Chain input window | Part of a swing that queues the next | [Combat › Sword Swing](../../06_Balancing/Combat.md#sword-swing) |

## Feedback

Short hit-stop, enemy flash, light knockback, impact sound tied to blade material.

## UI

- None.

## Dependencies

- [E_Sword](../../03_Entities/Items/Weapons/E_Sword/E_Sword.md), [M_Roll](../Movement/M_Roll.md)

## Used By

- [F04_Combat](../../01_Features/F04_Combat.md)

## Open Questions

- Is a heavy / charged sword attack needed for larger mobs, or are swings plus orbs enough?
