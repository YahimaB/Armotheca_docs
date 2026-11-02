---
id: _Movement_System
type: system
status: Draft
---

# Movement System

> **Glossary:** [System](../../00_Overview/Glossary.md) · **Balancing:** [Movement](../../06_Balancing/Movement.md) · **Technical:** [Movement (tech)](../../../Technical_Design/Common/Movement.md)

## Overview

Movement is the one verb every player uses every second, in the workshop and in the realms alike. It must feel responsive and readable rather than realistic: a cluttered co-op workshop and a short, dangerous expedition both reward a character that starts, stops and turns instantly. The move set is deliberately small — walk, sprint, jump, roll — so players spend their attention on teammates, orders and monsters, not on the controller.

Design goals:

- **Snappy control:** the character responds within a frame or two; no long acceleration ramps or slippery stops.
- **Readable intent:** teammates can tell at a glance whether someone is walking, sprinting, airborne or rolling.
- **Same rules everywhere:** the workshop and the realms share one move set.
- **Carrying has weight:** hauling an item is slightly more deliberate than running empty-handed, which creates natural co-op choreography.

References: **Overcooked / PlateUp!** (instant movement with a dash for crowded kitchens), **Moonlighter** (roll as the single defensive tool), **Hades** (crisp dash with brief invulnerability and a tight cooldown), **A Hat in Time** (forgiving jump with coyote time and buffering).

## Mechanics

| ID | Summary | Status |
| --- | --- | --- |
| [M_Walk](M_Walk.md) | Default analog locomotion with fast facing | Draft |
| [M_Sprint](M_Sprint.md) | Held modifier for higher top speed, no stamina | Draft |
| [M_Jump](M_Jump.md) | Single fixed-height jump with forgiving timing | Draft |
| [M_Roll](M_Roll.md) | Directional burst with invulnerability and cooldown | Draft |

## Interactions

What each player state allows:

| State | Can Sprint | Can Jump | Can Roll | Can Attack | Can Interact |
|---|---|---|---|---|---|
| Grounded, empty hands | Yes | Yes | Yes | Yes | Yes |
| Grounded, carrying item | Yes | Yes | No | No | Yes (drop/place) |
| Airborne | — | No | No | Yes (orb only) | No |
| Rolling | — | No | No | No | No |
| In continuous interaction | No | No | Yes (cancels) | No | — |
| Downed | No | No | No | No | No |

## Shared State

- **Carrying** (owned by [M_Carry_Model](../Interaction/M_Carry_Model.md)): slows walk and sprint, blocks roll and attacks.
- **Continuous interaction** (owned by [M_Continuous_Interaction](../Interaction/M_Continuous_Interaction.md)): roots the player; roll cancels it.
- **Downed** (owned by [M_Health_And_Downed](../Combat/M_Health_And_Downed.md)): blocks all movement.

## UI

- None.

## Open Questions

- Should sprint and roll eventually draw from a stamina pool, or stay free to keep the workshop frantic but fluid?
- Should heavy items (e.g. large ore chunks) apply a stronger carrying penalty than light ones?
