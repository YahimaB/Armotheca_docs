---
id: L00_Workshop
type: location
unlock: Start of the game
status: Draft
---

# The Workshop (Armotheca Pocket Realm)

> **World:** [_World_Map](../_World_Map.md) · **Technical:** [_Progression_Module › Technical Specifications](../../../Technical_Design/Progression/_Progression_Module.md#technical-specifications)

## Purpose in Progression

The home base: an ancient extradimensional emporium floating in the ethereal void, connected to the multiverse. Every session starts and ends here, and it grows with each workshop tier ([M_Workshop_Tiers](../../02_Systems/Progression/M_Workshop_Tiers.md)), from a humble stone-and-timber basement to a luminous Astral Forge suspended in starlight.

## Layout

- **The Mailbox Nexus:** where commission letters arrive ([E_Mailbox_Nexus](../../03_Entities/Props/Interactive/E_Mailbox_Nexus/E_Mailbox_Nexus.md)).
- **The Workshop Hall:** processing stations (furnaces, arcane distillation apparatus, grinding wheels, assembly benches) where materials are refined and joined.
- **The Threshold of Portals:** an archway hall of Magic Doors that open into realms ([E_Magic_Door](../../03_Entities/Props/Interactive/E_Magic_Door/E_Magic_Door.md)).

Each tier upgrade adds rooms, more station slots and a larger Threshold of Portals. The layout never requires jumping to reach a station.

## Player Flow

Read letters at the board → process and assemble at stations → dispatch at the Outgoing Tube; expedition players leave and return through the doors and receive chute deliveries in the receiving basket.

## Encounters

None: no combat happens inside the workshop. Health regenerates fully on returning through a door ([M_Health_And_Downed](../../02_Systems/Combat/M_Health_And_Downed.md)).

## Props & Nodes

| Entity | Where | Notes |
| --- | --- | --- |
| [E_Mailbox_Nexus](../../03_Entities/Props/Interactive/E_Mailbox_Nexus/E_Mailbox_Nexus.md) | Mailbox Nexus | |
| [E_Magic_Door](../../03_Entities/Props/Interactive/E_Magic_Door/E_Magic_Door.md) | Threshold of Portals | One per realm, by tier |
| Workstations ([_Prop_List](../../03_Entities/Props/_Prop_List.md)) | Workshop Hall | Tier-gated |
| [E_Great_Crucible](../../03_Entities/Props/Workstations/E_Great_Crucible/E_Great_Crucible.md) | Workshop Hall | Tier 3 |
| Storage crates, receiving basket, catalyst pedestal, upgrade ledger | Workshop Hall | No docs yet ([_Prop_List › Gaps](../../03_Entities/Props/_Prop_List.md#gaps)) |

## Mood & Lighting

Cozy and daylit; references in [Modeling Guidelines](../../../Guidelines/Modeling_Guidelines.md).

## Connections

- Each owned [E_Magic_Door](../../03_Entities/Props/Interactive/E_Magic_Door/E_Magic_Door.md) leads to its realm; [E_Exit_Portal](../../03_Entities/Props/Interactive/E_Exit_Portal/E_Exit_Portal.md)s lead back.

## UI

- [UI_Letter_Commission_Board](../../05_UI/Screens/UI_Letter_Commission_Board.md), [UI_Assembly_Bench](../../05_UI/World/UI_Assembly_Bench.md)

## Open Questions

- Are station placements fixed per tier, or can players rearrange the workshop? (Tracked in [M_Workshop_Tiers](../../02_Systems/Progression/M_Workshop_Tiers.md).)
