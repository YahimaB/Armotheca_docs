---
id: M_Magic_Orb
type: mechanic
system: Combat
status: Draft
---

# Magic Orb

> **System:** [_Combat_System](_Combat_System.md) · **Technical:** [_Combat_Module › Technical Specifications](../../../Technical_Design/Combat/_Combat_Module.md#technical-specifications)

## Summary

Wands and staves fire a glowing orb that hits the first enemy in its path.

## Rules

1. **Projectile:** the orb fires straight in the facing direction, with light aim assist toward the nearest enemy in a narrow cone.
2. **Hit:** the orb stops at the **first enemy or wall** it touches and deals Base Damage to that enemy only.
3. **Mobility:** the player can walk (not sprint) while casting. Orbs can be cast while airborne.
4. **No resource cost:** there is no mana at this stage; the cooldown is the only limiter.
5. Holding the button repeats the cast at the cooldown rate.

## Player Input

Attack button with a wand or staff equipped and empty hands; hold to repeat.

## Tunable Parameters

| Parameter | Meaning | Value |
| --- | --- | --- |
| Cast time / cooldown | Fire rate | [Combat › Magic Orb](../../06_Balancing/Combat.md#magic-orb) |
| Orb speed / max range | Projectile | [Combat › Magic Orb](../../06_Balancing/Combat.md#magic-orb) |
| Aim assist cone | Assist angle | [Combat › Magic Orb](../../06_Balancing/Combat.md#magic-orb) |

## Feedback

Orb colour from the core's element, small burst on impact, enemy flash.

## UI

- None.

## Dependencies

- [E_Wand](../../03_Entities/Items/Weapons/E_Wand.md), [E_Staff](../../03_Entities/Items/Weapons/E_Staff.md)

## Used By

- [F04_Combat](../../01_Features/F04_Combat.md)

## Open Questions

-
