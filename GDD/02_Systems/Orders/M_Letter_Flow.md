---
id: M_Letter_Flow
type: mechanic
system: Orders
status: Draft
---

# Letter Flow

> **System:** [_Orders_System](_Orders_System.md) · **Technical:** [_Orders_Module › Architecture](../../../Technical_Design/Orders/_Orders_Module.md#architecture--implementation-approaches)

## Summary

How a letter arrives, is worked on, dispatched and verified.

## Rules

1. **Arrival:** a letter drops out of the Mailbox Nexus tube onto the board ([E_Mailbox_Nexus](../../03_Entities/Props/Interactive/E_Mailbox_Nexus/E_Mailbox_Nexus.md)). The board holds a limited number of letters at once.
2. **Review and pin:** players read the letter (instant interaction) and may pin it to the HUD.
3. **Fulfilment:** the team gathers, processes and assembles the requested weapon.
4. **Dispatch:** a player holding the finished weapon uses the Outgoing Tube (instant interaction) and chooses the target letter.
5. **Verification:** the weapon is checked against the letter's criteria ([M_Commission_Criteria](M_Commission_Criteria.md)) instantly. Success pays out; failure shows the rejection reason and, depending on the archetype, applies a penalty.
6. **Rejection** returns the weapon to the player's hands.
7. **Flawless delivery** pays a gold bonus.
8. **Expiry:** each letter has a lifespan set by its archetype; letter deadlines keep ticking while teams are on expeditions.

## Player Input

Read, pin, dispatch: [M_Instant_Interaction](../Interaction/M_Instant_Interaction.md).

## Tunable Parameters

| Parameter | Meaning | Value |
| --- | --- | --- |
| Max simultaneous letters | Board capacity | [Orders › Letter Rules](../../06_Balancing/Orders.md#letter-rules) |
| Flawless bonus | Extra gold | [Orders › Letter Rules](../../06_Balancing/Orders.md#letter-rules) |
| Lifespan, rewards, penalty | Per archetype | [Orders › Client Archetypes](../../06_Balancing/Orders.md#client-archetypes) |

## Feedback

Arrival, success and rejection cues: [UI_Letter_Commission_Board](../../05_UI/Screens/UI_Letter_Commission_Board.md#feedback).

## UI

- [UI_Letter_Commission_Board](../../05_UI/Screens/UI_Letter_Commission_Board.md), [UI_Pinned_Letter](../../05_UI/Hud/UI_Pinned_Letter.md)

## Dependencies

- [M_Commission_Criteria](M_Commission_Criteria.md), [M_Currencies](../Progression/M_Currencies.md)

## Used By

- [F01_Commissions](../../01_Features/F01_Commissions.md)

## Open Questions

- Should letters require explicit acceptance (committing reputation), or is every letter on the board implicitly accepted?
- How are batch orders dispatched — one weapon at a time, or all units together?
