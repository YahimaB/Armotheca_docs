---
id: M_Continuous_Interaction
type: mechanic
system: Interaction
status: Draft
---

# Continuous Interaction

> **System:** [_Interaction_System](_Interaction_System.md) · **Technical:** [_Interaction_Module › Architecture](../../../Technical_Design/Interaction/_Interaction_Module.md#architecture--implementation-approaches)

## Summary

Triggered by holding the button. A progress indicator fills over time; releasing the button pauses progress.

## Rules

| Interaction | Target | Notes |
|---|---|---|
| Harvest | Resource node | Each strike is one hit on the node ([M_Harvesting](../Exploration/M_Harvesting.md)). |
| Work station | Bellows, lathe, extractor | May include an optional timing mini-game ([M_Processing_Mini_Game](../Processing/M_Processing_Mini_Game.md)). |
| Revive | Downed teammate | [M_Health_And_Downed](../Combat/M_Health_And_Downed.md) |
| Empty backpack | Chute or crate | An instant per-item alternative exists. |

1. **Interruptible:** moving away, rolling, taking a hit or releasing the button stops the interaction. Progress is **kept** on the object for a short time before decaying, so an interrupted player can resume.
2. **Cooperative stations:** objects can declare a maximum number of simultaneous helpers; each extra helper adds progress speed.
3. **Exclusive stations:** some objects (e.g. the anvil strike) accept only one player at a time; others see a "Busy" prompt.
4. **Movement lock:** the player is rooted while interacting but can always cancel with roll or by releasing the button.

## Player Input

Hold interact.

## Tunable Parameters

| Parameter | Meaning | Value |
| --- | --- | --- |
| Typical durations | Per interaction type | [Interaction › Continuous Interaction](../../06_Balancing/Interaction.md#continuous-interaction) |
| Progress hold time | Before kept progress decays | [Interaction › Continuous Interaction](../../06_Balancing/Interaction.md#continuous-interaction) |
| Helper bonus | Extra speed per extra player | [Interaction › Continuous Interaction](../../06_Balancing/Interaction.md#continuous-interaction) |

## UI

- [UI_Interaction_Prompt](../../05_UI/World/UI_Interaction_Prompt.md): hold prompt and progress fill.

## Used By

- [F02_Weapon_Crafting](../../01_Features/F02_Weapon_Crafting.md), [F03_Expeditions](../../01_Features/F03_Expeditions.md), [F07_Co_Op](../../01_Features/F07_Co_Op.md)

## Open Questions

-
