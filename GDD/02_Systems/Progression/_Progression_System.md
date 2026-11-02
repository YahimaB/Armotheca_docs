---
id: _Progression_System
type: system
status: Draft
---

# Progression System

> **Glossary:** [System](../../00_Overview/Glossary.md) · **Balancing:** [Progression](../../06_Balancing/Progression.md) · **Technical:** [Shop Progression (tech)](../../../Technical_Design/Shop/Shop_Progression.md)

## Overview

Currencies earned from commissions buy workshop tiers, which unlock stations, clients and the right to buy Magic Doors. Purpose and experience goals are in [F05_Shop_Progression](../../01_Features/F05_Shop_Progression.md).

## Mechanics

| ID | Summary | Status |
| --- | --- | --- |
| [M_Currencies](M_Currencies.md) | Gold, reputation, Emergency Tokens, blueprints and catalysts | Draft |
| [M_Workshop_Tiers](M_Workshop_Tiers.md) | Three tiers with upgrade requirements and unlocks | Draft |

## Interactions

A tier makes doors **available**; each door is then bought separately with gold ([M_Door_Purchase](../Exploration/M_Door_Purchase.md)). Tier upgrade costs were lowered so the full spend per tier is unchanged when door prices are added (see [Progression › Workshop Tiers](../../06_Balancing/Progression.md#workshop-tiers)). The top tier gates the Uber-Weapon ([M_Forging_Ritual](../Endgame/M_Forging_Ritual.md)) and the Apex Arenas ([_World_Map](../../04_Locations/_World_Map.md)).

## Shared State

- **Treasury and reputation** (owned by [M_Currencies](M_Currencies.md)): shared by the team.
- **Current tier** (owned by [M_Workshop_Tiers](M_Workshop_Tiers.md)): read by doors, stations and letter generation.

## UI

- None yet; the "upgrade affordable" hint and the upgrade ledger are planned in [_UI_Flow](../../05_UI/_UI_Flow.md).

## Open Questions

-
