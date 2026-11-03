---
id: UI_Letter_Commission_Board
type: ui
category: World
status: Draft
---

# Letter Commission Board (Mailbox Nexus)

> **Flow:** [_UI_Flow](../_UI_Flow.md) · **Technical:** [_UI_Module › Letter Commission Board](../../../Technical_Design/UI/_UI_Module.md#letter-commission-board)

## Purpose

The informational and commercial hub of the workshop. Beside the incoming pneumatic tube, this physical board / diegetic screen lets players review pending letters, inspect requirements, track deadlines, pin priority commissions and dispatch finished weapons ([M_Letter_Flow](../../02_Systems/Orders/M_Letter_Flow.md)).

## Mockup

```
+-------------------------------------------------------------------------------+
| [NEXUS DISPATCH MAILBOX]                [SHOP REPUTATION: LVL 2 (340/500)]    |
+-------------------------------------------------------------------------------+
|  PENDING LETTERS (Max 5)       |           ACTIVE COMMISSION DETAILS          |
|                                |                                              |
|  [#01] Guild: Iron Sword       | CLIENT: Arcane Academy of Oakhaven           |
|        [Time: 03:15]           | ARCHETYPE: Arcane Academy (Perfectionist)    |
|                                |                                              |
|  [#02] Academy: Frost Wand     | REQUIRED WEAPON:                             |
|        [Time: 05:40] (FOCUSED) | - Type: Wand (1-Handed)                      |
|                                | - Foundation (Shaft): Any Hardwood           |
|  [#03] SOS: Fire Sword         | - Payload (Core): Frost Core                 |
|        [Time: 00:45] [CRITICAL]| - Minimum Quality: Masterwork (75+)          |
|                                |                                              |
|  [#04] Garrison: 3x Iron Swords| REWARD:                                      |
|        [Time: 08:00]           | - Gold: 450 G                                |
|                                | - Rep: +35 Academy Standing                  |
|  [ + Empty Slot ]              | - Bonus: Blueprint "Glacial Conduit"         |
|                                |                                              |
|                                | PENALTY ON FAILURE: -50 Rep, Contract Void   |
+--------------------------------+----------------------------------------------+
| [PIN TO HUD] (Space/A)         | [DISPATCH COMPLETED WEAPON] (E/X)            |
+-------------------------------------------------------------------------------+
```

Values in the mockup are illustrative.

## Elements

| Element | Type | Shows | Data source |
| --- | --- | --- | --- |
| Letter queue | Panel | Up to the board capacity of ticket cards | [M_Letter_Flow](../../02_Systems/Orders/M_Letter_Flow.md) |
| Ticket | Widget | Faction trim colour, urgency bar, weapon silhouette and element badge, batch counter (`1/3`) | [M_Commission_Criteria](../../02_Systems/Orders/M_Commission_Criteria.md), [_Client_Roster](../../03_Entities/NPCs/Clients/_Client_Roster.md) |
| Commission dossier | Panel | Flavour text; criteria (type, foundation material, payload element/material, minimum tier with its numeric threshold); gold (with Flawless bonus), faction reputation, special unlocks; penalty | [M_Commission_Criteria](../../02_Systems/Orders/M_Commission_Criteria.md), [M_Quality](../../02_Systems/Crafting/M_Quality.md), [M_Currencies](../../02_Systems/Progression/M_Currencies.md) |
| Reputation header | Label | Shop reputation level and progress | [M_Currencies](../../02_Systems/Progression/M_Currencies.md) |
| Action bar | Panel | Pin to HUD, Dispatch | [M_Letter_Flow](../../02_Systems/Orders/M_Letter_Flow.md) |

Faction trims: Adventurers Guild brown / bronze, Arcane Academy blue / silver, City Garrison red / brass, SOS flashing crimson, Eccentric Collector gold / purple.

## States

- **Empty slot** in the queue when fewer letters than capacity.
- **Focused** ticket shows its dossier.
- **SOS critical** below the alert threshold ([Orders › UI Thresholds](../../06_Balancing/Orders.md#ui-thresholds)).

## Input & Navigation

- **Pin to HUD:** Space / controller A — pins criteria to [UI_Pinned_Letter](../Hud/UI_Pinned_Letter.md) so players at the forge or in realms can check requirements without returning.
- **Dispatch:** E / controller X — validates and delivers the weapon in the player's hands.
- Gamepad navigation across tickets.

## Feedback

- **New letter:** brass pneumatic tube hiss, then a parchment "thwack" on the table; soft ethereal spark above the inbox slot.
- **SOS critical alert:** pulsing magical beacon chime with rising pitch; flashing red parchment edges and vignette.
- **Successful dispatch:** cash register chime + arcane resonance; the letter dissolves into golden motes flying into the ceiling nexus; gold and rep counters animate upward.
- **Rejection / failure:** low dull thud / buzzer; a red rejection stamp with the reason (*"Quality Substandard: Required Masterwork, got Standard (61)"*).

## Used By

- [F01_Commissions](../../01_Features/F01_Commissions.md), [E_Mailbox_Nexus](../../03_Entities/Props/Interactive/E_Mailbox_Nexus/E_Mailbox_Nexus.md)

## Open Questions

-
