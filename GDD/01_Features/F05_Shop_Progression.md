---
id: F05_Shop_Progression
type: feature
status: Draft
priority: Must
owner:
milestone: Phase 3
pillars: [Tangible Endgame Aspiration]
---

# Shop Progression (Workshop Tiers)

> **Hub:** [_Feature_List](_Feature_List.md) · **Technical:** [Technical Overview › Code Organization](../../Technical_Design/Technical_Overview.md#7-code-organization)

## Purpose

Progression bridges everyday shop management and the campaign's climactic objective. Many simulation and tycoon games stagnate once wealth outpaces what there is to buy. *Armotheca* frames every commission, gold piece and reputation point as fuel toward a definitive goal — the forging of the [Uber-Weapon](F06_Uber_Weapon.md) — and makes progress visible through workshop expansion, new stations and new Magic Doors.

## Player Experience

- **Visual pride:** the humble stone-and-timber basement evolves into a luminous Astral Forge suspended in starlight.
- **Milestone anticipation:** each new door and higher-tier station feels like a new chapter.
- **Meaningful spending:** buying doors separately from tier upgrades turns expansion into choices (which realm first?) rather than automatic unlocks.
- **Purpose-driven economy:** gold and rare materials keep their value up to the end of the campaign.

## References

- **Moonlighter:** direct shop upgrades funded by dungeon exploration.
- **PlateUp!:** layout evolution and technology upgrades between days.
- **Factorio (rocket launch):** a tangible macro-objective that unifies all production toward a finale.

## Mechanics

- [M_Currencies](../02_Systems/Progression/M_Currencies.md)
- [M_Workshop_Tiers](../02_Systems/Progression/M_Workshop_Tiers.md)
- [M_Door_Purchase](../02_Systems/Exploration/M_Door_Purchase.md)

## Entities

- [E_Magic_Door](../03_Entities/Props/Interactive/E_Magic_Door.md): doors become available by tier.
- Tier-gated workstations: [E_Woodworking_Lathe](../03_Entities/Props/Workstations/E_Woodworking_Lathe.md), [E_Arcane_Extractor](../03_Entities/Props/Workstations/E_Arcane_Extractor.md), [E_Quenching_Basin](../03_Entities/Props/Workstations/E_Quenching_Basin.md), [E_Great_Crucible](../03_Entities/Props/Workstations/E_Great_Crucible.md).

## Locations

- [L00_Workshop](../04_Locations/L00_Workshop/L00_Workshop.md): each tier physically expands the workshop.

## UI

- None yet. The "upgrade affordable" HUD hint and the upgrade ledger are planned in [_UI_Flow](../05_UI/_UI_Flow.md).

## Scope

| Item | MVP | Stretch |
| --- | --- | --- |
| Three workshop tiers and door purchases | Phase 3 | |
| Economy and reputation balancing | Phase 3 | |
| Player-arranged workshop layout | | Open question in [M_Workshop_Tiers](../02_Systems/Progression/M_Workshop_Tiers.md) |

## Open Questions

-
