---
id: M_Targeting
type: mechanic
system: Interaction
status: Draft
---

# Targeting & Prompts

> **System:** [_Interaction_System](_Interaction_System.md) · **Technical:** [_Interaction_Module › Technical Specifications](../../../Technical_Design/Interaction/_Interaction_Module.md#technical-specifications)

## Summary

The game picks one best target in front of the player and names the action before it happens.

## Rules

1. The best target is chosen within a short reach, favouring the object closest to the facing direction.
2. Only one prompt is shown at a time: button, verb and object name (`[E] Pick up Iron Ore`, `[Hold E] Pump Bellows`).
3. Context changes the verb: facing a bench socket with a blade in hand shows `Place Blade`; with empty hands it shows `Take Blade`.
4. Invalid actions show a short reason instead of failing silently (`Wrong part for this socket`, `Hands full`).

## Tunable Parameters

| Parameter | Meaning | Value |
| --- | --- | --- |
| Reach | Maximum target distance | [Interaction › Targeting](../../06_Balancing/Interaction.md#targeting) |

## UI

- [UI_Interaction_Prompt](../../05_UI/World/UI_Interaction_Prompt.md)

## Used By

- [F02_Weapon_Crafting](../../01_Features/F02_Weapon_Crafting.md), [F03_Expeditions](../../01_Features/F03_Expeditions.md); every feature with interactions.

## Open Questions

-
