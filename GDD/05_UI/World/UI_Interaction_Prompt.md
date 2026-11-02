---
id: UI_Interaction_Prompt
type: ui
category: World
status: Draft
---

# Interaction Prompt

> **Flow:** [_UI_Flow](../_UI_Flow.md) · **Technical:** [Object Interaction (tech)](../../../Technical_Design/Common/Object_Interaction.md)

## Purpose

Names the action before it happens, for whatever the player is facing ([M_Targeting](../../02_Systems/Interaction/M_Targeting.md)).

## Elements

| Element | Type | Shows | Data source |
| --- | --- | --- | --- |
| Prompt | Label | Button, verb and object name: `[E] Pick up Iron Ore`, `[Hold E] Pump Bellows` | [M_Targeting](../../02_Systems/Interaction/M_Targeting.md) |
| Progress | Bar | Fill of a continuous interaction | [M_Continuous_Interaction](../../02_Systems/Interaction/M_Continuous_Interaction.md) |

## States

- **Instant** and **hold** prompts.
- **Busy** on exclusive stations in use.
- **Invalid** with a short reason (`Wrong part for this socket`, `Hands full`).

## Input & Navigation

Only one prompt is shown at a time.

## Used By

- Every interaction; see [_Interaction_System](../../02_Systems/Interaction/_Interaction_System.md).

## Open Questions

-
