---
id: _Crafting_System
type: system
status: Draft
---

# Crafting System

> **Glossary:** [System](../../00_Overview/Glossary.md) · **Balancing:** [Crafting](../../06_Balancing/Crafting.md) · **Technical:** [Weapon Crafting (tech)](../../../Technical_Design/Shop/Weapon_Crafting.md)

## Overview

Turns two processed components into a finished weapon with exactly two stats. Weapons are deliberately simple: **Quality and Base Damage only**; every stat from earlier drafts (speed, durability, mana, area, cast speed, cooldown, balance, damage type) has been removed, and the set stays fixed until a deliberate design revision ([Vision › Locked Constraints](../../00_Overview/Vision.md#locked-constraints)). Purpose and experience goals are in [F02_Weapon_Crafting](../../01_Features/F02_Weapon_Crafting.md).

## Mechanics

| ID | Summary | Status |
| --- | --- | --- |
| [M_Assembly](M_Assembly.md) | Foundation + payload on the bench, locked with a mallet | Draft |
| [M_Quality](M_Quality.md) | Quality, Base Damage, tiers and material attributes | Draft |
| [M_Weapon_Naming](M_Weapon_Naming.md) | Names generated from materials | Draft |

## Interactions

Components arrive from the [_Processing_System](../Processing/_Processing_System.md) carrying their Quality and material. [M_Assembly](M_Assembly.md) checks compatibility, [M_Quality](M_Quality.md) computes the weapon's stats, and [M_Weapon_Naming](M_Weapon_Naming.md) names it. Orders read the result ([M_Commission_Criteria](../Orders/M_Commission_Criteria.md)).

## Shared State

- **Component Quality and material** (set by processing, read here and by orders).

## UI

- [UI_Assembly_Bench](../../05_UI/World/UI_Assembly_Bench.md)

## Open Questions

-
