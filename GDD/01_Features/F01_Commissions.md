---
id: F01_Commissions
type: feature
status: Draft
priority: Must
owner:
milestone: Phase 1
pillars: [Dimensional Contract Cycle]
---

# Commissions (Customer Letters)

> **Hub:** [_Feature_List](_Feature_List.md) · **Technical:** [Technical Overview › Code Organization](../../Technical_Design/Technical_Overview.md#7-code-organization)

## Purpose

Commissions are the commercial pulse and narrative context of *Armotheca*. Instead of faceless customers at a counter, orders arrive as **commission letters** through the Mailbox Nexus. Each letter embodies a client faction, explicit requirements, a deadline and stakes, which turns shop operations from inventory stockpiling into focused, tactical problem-solving for the team.

## Player Experience

- **Analytical prioritisation:** players gather around the mailbox to evaluate incoming contracts, debate feasibility and coordinate material requirements.
- **Narrative personality:** flavour text and specific client demands make the extradimensional world feel alive and reactive.
- **Dramatic pacing:** high-urgency SOS orders trigger frantic coordination, contrasting with relaxed, perfectionist Academy commissions.
- **Consequential choices:** accepting an order stakes reputation; failing it or delivering subpar work affects the workshop's standing.

## References

- **Papers, Please:** verifying several criteria against a strict set of rules.
- **Overcooked / PlateUp!:** order tickets with expiration bars, rewarding fast execution.
- **Potion Craft:** customers requesting specific effects, with bonus reputation for exceeding expectations.
- **Dave the Diver:** VIP events requiring specific dishes by a deadline, unlocking progression on success.

## Mechanics

- [M_Commission_Criteria](../02_Systems/Orders/M_Commission_Criteria.md): what a letter can ask for.
- [M_Letter_Flow](../02_Systems/Orders/M_Letter_Flow.md): arrival, review, dispatch and verification.
- [M_Quality](../02_Systems/Crafting/M_Quality.md): tiers that letters require.
- [M_Currencies](../02_Systems/Progression/M_Currencies.md): what letters pay out.

## Entities

- [_Client_Roster](../03_Entities/NPCs/Clients/_Client_Roster.md): the five client archetypes.
- [E_Mailbox_Nexus](../03_Entities/Props/Interactive/E_Mailbox_Nexus.md): incoming tube, board and outgoing tube.

## Locations

- [L00_Workshop](../04_Locations/L00_Workshop/L00_Workshop.md): the board stands in the workshop.

## UI

- [UI_Letter_Commission_Board](../05_UI/Screens/UI_Letter_Commission_Board.md): reviewing, pinning and dispatching.
- [UI_Pinned_Letter](../05_UI/Hud/UI_Pinned_Letter.md): pinned criteria visible at the forge and in realms.

## Scope

| Item | MVP | Stretch |
| --- | --- | --- |
| Adventurers Guild letters with verification | Phase 1 | |
| All five client archetypes | Phase 2 | |
| Celestial clients | | Prestige Endless Mode ([F06_Uber_Weapon](F06_Uber_Weapon.md)) |

## Open Questions

-
