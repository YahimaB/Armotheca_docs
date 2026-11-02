---
id: M_Processing_Mini_Game
type: mechanic
system: Processing
status: Draft
---

# Processing Mini-Games

> **System:** [_Processing_System](_Processing_System.md) · **Technical:** [_Processing_Module › Architecture](../../../Technical_Design/Processing/_Processing_Module.md#architecture--implementation-approaches)

## Summary

Optional, lightweight timing interactions at stations that set a component's Quality.

## Rules

1. Mini-games are **rhythmic micro-interactions**, not full-screen pausing puzzles.
2. **Anvil strike:** a sweeping cursor crosses a target zone for a series of strikes. Each strike is Perfect, Good or Off-beat and adjusts Quality from a base value.
3. **Heat regulation (distiller):** the player keeps the temperature inside the sweet-spot zone with flame valves for a set time.
4. **Accessibility guarantee:** a player who skips the timing (or has accessibility aids enabled) still completes the station and receives a baseline **Standard** component.
5. Engaging with the mini-game lets players reach **Masterwork** and **Flawless**, which top-paying Collector and Academy commissions require.
6. **Forgiving failure:** botched mini-games never destroy materials; they yield Crude or Standard items.
7. Final Quality is always clamped to **1–100**.

## Player Input

Timed presses during the station's continuous interaction.

## Tunable Parameters

| Parameter | Meaning | Value |
| --- | --- | --- |
| Anvil strikes, base Quality, strike modifiers | Hammering | [Processing › Anvil Strike](../../06_Balancing/Processing.md#anvil-strike) |
| Heat regulation duration | Distiller | [Processing › Heat Regulation](../../06_Balancing/Processing.md#heat-regulation) |
| Skip baseline Quality | Accessibility guarantee | [Processing › Accessibility](../../06_Balancing/Processing.md#accessibility) |

## UI

- None yet; mini-game displays are planned in [_UI_Flow](../../05_UI/_UI_Flow.md).

## Dependencies

- [M_Quality](../Crafting/M_Quality.md): tiers.

## Used By

- [F02_Weapon_Crafting](../../01_Features/F02_Weapon_Crafting.md)

## Open Questions

- Should raw materials have their own quality that caps the result, or is quality purely a product of player skill?
- Does the lathe have a mini-game, or is it a pure hold interaction with fixed quality?
