---
id: _Interaction_System
type: system
status: Draft
---

# Interaction System

> **Glossary:** [System](../../00_Overview/Glossary.md) · **Balancing:** [Interaction](../../06_Balancing/Interaction.md) · **Technical:** [_Interaction_Module](../../../Technical_Design/Interaction/_Interaction_Module.md)

## Overview

Almost everything players do beyond running and fighting is an interaction with an object: picking up ore, snapping a blade into the assembly bench, pumping bellows, chopping a tree, reading a letter, opening a door. One consistent model keeps all of these readable and lets the shop and the realms add new objects without inventing new controls. There are exactly **two kinds of interaction**: **instant** (one press, immediate result) and **continuous** (press and hold, with visible progress).

Design goals:

- **One button, clear outcome:** the interact button always does the most obvious thing for what the player is facing.
- **Always know what will happen:** a short prompt names the action before it happens.
- **Physical, tactile workshop:** items exist in the world; players carry them, set them down, hand them over and snap them into sockets.
- **Teamwork through shared objects:** some continuous interactions go faster with more than one player.

References: **Overcooked / PlateUp!** (one-button pick up / put down, hold-to-chop progress), **Ale & Tale Tavern** (carrying logs and kegs through a shared space), **Deep Rock Galactic** (hold-to-revive and hold-to-deposit), **Lethal Company** (limited carry capacity forcing prioritisation).

## Mechanics

| ID | Summary | Status |
| --- | --- | --- |
| [M_Carry_Model](M_Carry_Model.md) | Hands, weapon slot and backpack | Draft |
| [M_Instant_Interaction](M_Instant_Interaction.md) | One-press actions: pick up, place, hand over, open, dispatch | Draft |
| [M_Continuous_Interaction](M_Continuous_Interaction.md) | Hold actions with progress: harvest, work station, revive | Draft |
| [M_Targeting](M_Targeting.md) | Choosing the target and its prompt | Draft |

## Interactions

[M_Targeting](M_Targeting.md) picks one object; the object decides whether the press is instant or continuous and what it does with the player's carry slots ([M_Carry_Model](M_Carry_Model.md)). Movement limits per state are in [_Movement_System](../Movement/_Movement_System.md#interactions).

## Shared State

- **Hands** (owned by [M_Carry_Model](M_Carry_Model.md)): read by every interaction, by attacks and by roll.
- **Interaction progress** (owned by [M_Continuous_Interaction](M_Continuous_Interaction.md)): stored on the object, shared by helpers.

## UI

- [UI_Interaction_Prompt](../../05_UI/Hud/UI_Interaction_Prompt.md)

## Open Questions

- Should players be able to throw items (Overcooked-style) to speed up the workshop, or does that undermine the "physical choreography" pillar?
