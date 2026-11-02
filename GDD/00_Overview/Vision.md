---
id: Vision
type: overview
status: Draft
---

# Armotheca — Vision

> **Loops:** [Core_Loop](Core_Loop.md) · **Features:** [_Feature_List](../01_Features/_Feature_List.md) · **Glossary:** [Glossary](Glossary.md) · **Changes:** [Changelog](Changelog.md) · **Technical:** [Technical Overview](../../Technical_Design/Technical_Overview.md)

## Executive Summary

- **Genre:** Cooperative magic weapon shop simulator / dimensional extraction action.
- **Platform:** PC (Steam), controller and keyboard/mouse.
- **Players:** 1–4, drop-in / drop-out cooperative multiplayer in player-hosted sessions over Steam (one player is both server and client).
- **Engine:** Unity 6.3 LTS; full stack in the [Technical Overview](../../Technical_Design/Technical_Overview.md).
- **Audience:** Fans of cooperative crafting and simulation (*PlateUp!*, *Overcooked*, *Ale & Tale Tavern*) and hybrid shop/action games (*Moonlighter*, *Dave the Diver*, *Potion Craft*).

## Setting

The game takes place inside **the Armotheca**, an ancient extradimensional emporium floating in the ethereal void. It is not on a city street but an arcane sanctuary connected to the multiverse: letters arrive from factions across the planes, and Magic Doors open onto alien pocket realms. The workshop itself is described in [L00_Workshop](../04_Locations/L00_Workshop/L00_Workshop.md); the realms in [_World_Map](../04_Locations/_World_Map.md).

## Pitch

Players run an artisanal weapon forge, taking bespoke commissions for magical swords, wands and staves. Instead of passive queue management, they manually process raw materials, venture into perilous pocket dimensions to harvest resource nodes and hunt magical monsters, assemble weapons from **two modular components**, and dispatch completed orders before deadlines expire — all while working toward forging the mythic **Uber-Weapon**.

## Pillars

1. **Cooperative Synergy (Hands-On Teamwork):** a high-communication loop between workshop artisans and expedition foragers. Crafting and processing are strictly manual at launch, so co-op coordination is physical. → [F07_Co_Op](../01_Features/F07_Co_Op.md), [F02_Weapon_Crafting](../01_Features/F02_Weapon_Crafting.md)
2. **Modular Craftsmanship (Depth Without Overcomplication):** exactly two components per weapon and only two weapon stats. → [F02_Weapon_Crafting](../01_Features/F02_Weapon_Crafting.md)
3. **Dimensional Contract Cycle (Risk vs. Commission):** letters with varying constraints drive play; Magic Doors are bought with gold once the shop reaches the right tier, and expeditions are self-paced resource runs with rising danger instead of a timer. → [F01_Commissions](../01_Features/F01_Commissions.md), [F03_Expeditions](../01_Features/F03_Expeditions.md)
4. **Tangible Endgame Aspiration (The Uber-Weapon):** a clear win condition beyond endless wealth. → [F06_Uber_Weapon](../01_Features/F06_Uber_Weapon.md)

## Locked Constraints

These hold until a deliberate design revision and override any single doc.

1. **Exactly two components per weapon.** Swords: Hilt (foundation) + Blade (payload). Wands (1-handed): Short Shaft + Core. Staves (2-handed): Long Shaft + Core. → [M_Assembly](../02_Systems/Crafting/M_Assembly.md)
2. **Exactly two weapon stats:** **Quality (1–100)**, produced by manual processing and averaged from both components, and **Base Damage**, a constant of the payload material. No speed, durability, mana, area or other numeric stats. → [M_Quality](../02_Systems/Crafting/M_Quality.md)
3. **Manual labour, no automation at launch.** Every transformation of raw ingredients into components needs a player at a workstation: picking up, transporting, heating, striking, extracting and combining. This creates physical chaos, communicative comedy and tactile mastery in co-op. → [_Processing_System](../02_Systems/Processing/_Processing_System.md)
4. **1–4 players**, one shared code path for solo and co-op. → [F07_Co_Op](../01_Features/F07_Co_Op.md)

## Open Questions

-
