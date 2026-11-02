---
id: E_SOS_Dispatch
type: entity
category: NPCs
status: Draft
---

# SOS Emergency Dispatch (The Adrenaline Spike)

> **Roster:** [_Client_Roster](_Client_Roster.md) · **Technical:** [Order System (tech)](../../../../Technical_Design/Shop/Order_System.md)

## Description & Role

Desperate distress calls magically intercepted from ongoing battles. High-urgency letters that trigger frantic coordination.

## Behaviour & States

- **Demand pattern:** any weapon, often an elemental counter: *"A cave troll is breaking our line! Send an Acid Blade within 90 seconds!"*
- **Timing:** extreme time pressure.
- **Expiry:** no penalty — they perished or fled; only the opportunity is lost.

## Stats

Lifespan and reward multiplier: [Orders › Client Archetypes](../../../06_Balancing/Orders.md#client-archetypes).

## Outputs

A gold multiplier over standard pay and Emergency Tokens, used for instant workshop buffs ([M_Currencies](../../../02_Systems/Progression/M_Currencies.md)).

## UI

[UI_Letter_Commission_Board](../../../05_UI/Screens/UI_Letter_Commission_Board.md): flashing crimson trim and the SOS critical alert.

## Appears In

- [F01_Commissions](../../../01_Features/F01_Commissions.md)

## Open Questions

-
