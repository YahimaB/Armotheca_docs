---
id: UI_Pinned_Letter
type: ui
category: Hud
status: Draft
---

# Pinned Letter

> **Flow:** [_UI_Flow](../_UI_Flow.md) · **Technical:** [_UI_Module › Letter Commission Board](../../../Technical_Design/UI/_UI_Module.md#letter-commission-board)

## Purpose

Shows a pinned letter's criteria in a corner of the HUD, so players at the forge or in realms can check requirements without returning to the board.

## Elements

| Element | Type | Shows | Data source |
| --- | --- | --- | --- |
| Pinned letter | Panel | Letter criteria | [M_Commission_Criteria](../../02_Systems/Orders/M_Commission_Criteria.md) |

## Input & Navigation

Pinned from [UI_Letter_Commission_Board](../Screens/UI_Letter_Commission_Board.md).

## Used By

- [F01_Commissions](../../01_Features/F01_Commissions.md)

## Open Questions

- How many letters can be pinned at once, and how is a letter unpinned?
