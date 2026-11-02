---
id: _Orders_System
type: system
status: Draft
---

# Orders System

> **Glossary:** [System](../../00_Overview/Glossary.md) · **Balancing:** [Orders](../../06_Balancing/Orders.md) · **Technical:** [Order System (tech)](../../../Technical_Design/Shop/Order_System.md)

## Overview

Commission letters arrive through the Mailbox Nexus, state what the client wants and by when, and pay out or penalise on delivery. Purpose and experience goals are in [F01_Commissions](../../01_Features/F01_Commissions.md); the clients themselves are entities in [_Client_Roster](../../03_Entities/NPCs/Clients/_Client_Roster.md).

## Mechanics

| ID | Summary | Status |
| --- | --- | --- |
| [M_Commission_Criteria](M_Commission_Criteria.md) | What a letter can require | Draft |
| [M_Letter_Flow](M_Letter_Flow.md) | Arrival, review, pin, dispatch, verification | Draft |

## Interactions

The client archetype decides which criteria a letter uses, its lifespan, rewards and penalty ([_Client_Roster](../../03_Entities/NPCs/Clients/_Client_Roster.md)). [M_Letter_Flow](M_Letter_Flow.md) checks a dispatched weapon against [M_Commission_Criteria](M_Commission_Criteria.md) and pays in [M_Currencies](../Progression/M_Currencies.md). Letters only request materials obtainable through doors the team owns ([M_Door_Purchase](../Exploration/M_Door_Purchase.md)), and active letters guarantee matching nodes and mobs in realms ([M_Node_Spawning](../Exploration/M_Node_Spawning.md), [M_Mob_Spawning](../Exploration/M_Mob_Spawning.md)).

## Shared State

- **Active letters** (owned by [M_Letter_Flow](M_Letter_Flow.md)): read by realm spawning guarantees and by the HUD.

## UI

- [UI_Letter_Commission_Board](../../05_UI/Screens/UI_Letter_Commission_Board.md), [UI_Pinned_Letter](../../05_UI/Hud/UI_Pinned_Letter.md)

## Open Questions

-
