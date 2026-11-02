---
id: F07_Co_Op
type: feature
status: Draft
priority: Must
owner:
milestone: Phase 1
pillars: [Cooperative Synergy]
---

# Co-op (1–4 Players)

> **Hub:** [_Feature_List](_Feature_List.md) · **Technical:** [_Networking_Module](../../Technical_Design/Networking/_Networking_Module.md)

## Purpose

*Armotheca* is built around a high-communication loop between workshop artisans and expedition foragers. 1–4 players share one workshop in player-hosted Steam sessions with drop-in / drop-out, and solo play is the same game with one player. Co-op is not a mode but a property of every mechanic: shared objects, cooperative stations, revives and expedition membership all assume more than one pair of hands.

## Player Experience

- **Teamwork through shared objects:** some stations and nodes go faster with helpers, rewarding coordination.
- **Hand-offs:** items move between players by hand, by the drop-chute and through the workshop.
- **Nobody waits:** any player can work any bench or open another door, so roles stay flexible (see [Core_Loop › Pacing](../00_Overview/Core_Loop.md#pacing--anti-downtime)).

## Mechanics

- [M_Continuous_Interaction](../02_Systems/Interaction/M_Continuous_Interaction.md): cooperative and exclusive stations.
- [M_Instant_Interaction](../02_Systems/Interaction/M_Instant_Interaction.md): hand-over between players.
- [M_Health_And_Downed](../02_Systems/Combat/M_Health_And_Downed.md): revives.
- [M_Door_Lifecycle](../02_Systems/Exploration/M_Door_Lifecycle.md): expedition membership and re-entry.
- [M_Forging_Ritual](../02_Systems/Endgame/M_Forging_Ritual.md): scales to the number of players.

## Entities

- [Player](../03_Entities/Player/Player.md)

## Locations

- All locations.

## UI

- None yet. Lobby, join and drop-in screens are planned in [_UI_Flow](../05_UI/_UI_Flow.md).

## Scope

| Item | MVP | Stretch |
| --- | --- | --- |
| Networked host + clients from the first week, Steam lobby join, disconnect / rejoin | Phase 1 | |
| Co-op hardening for 2–4 players | Phase 2 | |
| Host migration | | Open decision in the [Technical Overview](../../Technical_Design/Technical_Overview.md#8-open-technical-decisions) |

## Open Questions

-
