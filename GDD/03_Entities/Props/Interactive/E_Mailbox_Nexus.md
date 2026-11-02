---
id: E_Mailbox_Nexus
type: entity
category: Props
status: Draft
---

# Mailbox Nexus

> **Roster:** [_Prop_List](../_Prop_List.md) · **Technical:** [Order System (tech)](../../../../Technical_Design/Shop/Order_System.md)

## Description & Role

A magical pneumatic tube / portal where commission letters arrive from factions across the planes, with the letter board beside it and the Outgoing Tube for dispatching weapons. The commercial hub of the workshop.

## Behaviour & States

- **Incoming tube:** letters drop out onto the board ([M_Letter_Flow](../../../02_Systems/Orders/M_Letter_Flow.md)).
- **Board:** players read and pin letters.
- **Outgoing Tube:** a player holding a finished weapon dispatches it to a chosen letter (instant interaction).

## Mechanics

- [M_Letter_Flow](../../../02_Systems/Orders/M_Letter_Flow.md), [M_Instant_Interaction](../../../02_Systems/Interaction/M_Instant_Interaction.md)

## UI

- [UI_Letter_Commission_Board](../../../05_UI/Screens/UI_Letter_Commission_Board.md)

## Appears In

- [L00_Workshop](../../../04_Locations/L00_Workshop/L00_Workshop.md)
- [F01_Commissions](../../../01_Features/F01_Commissions.md)

## Open Questions

-
