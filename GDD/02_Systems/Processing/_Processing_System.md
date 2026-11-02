---
id: _Processing_System
type: system
status: Draft
---

# Processing System

> **Glossary:** [System](../../00_Overview/Glossary.md) · **Balancing:** [Processing](../../06_Balancing/Processing.md) · **Technical:** [_Processing_Module](../../../Technical_Design/Processing/_Processing_Module.md)

## Overview

Raw materials from expeditions cannot go straight onto a weapon; they need physical labour and careful refinement. **All processing is strictly manual, without automation.** Each station involves direct handling, multi-step procedures and optional timing mini-games that set the resulting component's Quality. Stations use the common interaction model: loading and unloading are instant interactions, working a station is a continuous interaction ([_Interaction_System](../Interaction/_Interaction_System.md)). Purpose and experience goals are in [F02_Weapon_Crafting](../../01_Features/F02_Weapon_Crafting.md).

## Mechanics

| ID | Summary | Status |
| --- | --- | --- |
| [M_Resource_Processing](M_Resource_Processing.md) | Station pipelines from raw material to component | Draft |
| [M_Processing_Mini_Game](M_Processing_Mini_Game.md) | Optional timing that sets Quality | Draft |

## Interactions

```
Raw Ores (Realms) -------> [SMELTING FORGE] -------> Hot Ingot
                                                         |
                                                         v
                                                [ANVIL SHAPING] (Timing Strike)
                                                         |
                                                         v
                                                [QUENCHING BASIN] ---> Refined BLADE

Arcane Timber (Realms) --> [WOODWORKING LATHE] ---> [CARVING BENCH] ---> Refined SHAFT / HILT

Mob Drops (Realms) ------> [ARCANE EXTRACTOR] ----> [PURITY DISTILLER] -> Refined CORE
```

What each output carries:

- **Blade:** Quality (from processing) + Base Damage and Element (from the ore material).
- **Core:** Quality (from processing) + Base Damage and Element (from the mob essence material).
- **Hilt / Short Shaft / Long Shaft:** Quality (from processing) + material identity. No Base Damage.

Outputs feed [M_Assembly](../Crafting/M_Assembly.md).

## Shared State

- **Component Quality** (set by [M_Processing_Mini_Game](M_Processing_Mini_Game.md), read by [M_Quality](../Crafting/M_Quality.md)).

## UI

- [UI_Interaction_Prompt](../../05_UI/World/UI_Interaction_Prompt.md). Mini-game displays are planned in [_UI_Flow](../../05_UI/_UI_Flow.md).

## Open Questions

- Tier 1 does not unlock the lathe or extractor, yet hilts and cores are needed for every weapon — how are Tier 1 foundations and cores obtained? (Tracked in [M_Workshop_Tiers](../Progression/M_Workshop_Tiers.md).)
