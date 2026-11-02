---
id: F06_Uber_Weapon
type: feature
status: Draft
priority: Must
owner:
milestone: Phase 4
pillars: [Tangible Endgame Aspiration]
---

# The Uber-Weapon (Endgame)

> **Hub:** [_Feature_List](_Feature_List.md) · **Technical:** [_Module_Map › Features](../../Technical_Design/_Module_Map.md#features)

## Purpose

The Uber-Weapon — **The Primordial Armament** — is the legendary magnum opus of the Armotheca lineage and the campaign's win condition. It gives every commission and expedition a long-term purpose, and its forging is not a silent menu click but an intense, synchronised co-op event that uses every station the team has mastered.

## Player Experience

- **Climactic finale:** the final forge is a set-piece where every player has a role under pressure.
- **Long-term anticipation:** each catalyst brought home is a visible, celebrated step toward the end.
- **Mastery showcase:** the ritual reuses the workshop's manual stations at higher intensity, rewarding skills built over the campaign.

## References

- **Factorio (rocket launch):** a clear macro-objective that ends the campaign.
- **Subnautica (Neptune rocket):** a multi-phase construction project needing rare ingredients from the most dangerous places.
- **Overcooked (final level):** a frantic finale combining every mechanic learned.

## Mechanics

- [M_Forging_Ritual](../02_Systems/Endgame/M_Forging_Ritual.md)
- [M_Workshop_Tiers](../02_Systems/Progression/M_Workshop_Tiers.md): the ritual needs the top tier.

## Entities

- [E_Primordial_Catalyst](../03_Entities/Items/Catalysts/E_Primordial_Catalyst/E_Primordial_Catalyst.md): the four ingredients.
- Apex Guardians that guard them: see [_Mob_Roster](../03_Entities/Mobs/_Mob_Roster.md).
- [E_Great_Crucible](../03_Entities/Props/Workstations/E_Great_Crucible/E_Great_Crucible.md) and the catalyst display pedestal (planned in [_Prop_List](../03_Entities/Props/_Prop_List.md)).

## Locations

- [L00_Workshop](../04_Locations/L00_Workshop/L00_Workshop.md): the ritual.
- Apex Arenas of every realm: see [_World_Map](../04_Locations/_World_Map.md).

## UI

- None yet. The ritual phase display and the campaign victory screen are planned in [_UI_Flow](../05_UI/_UI_Flow.md).

## Scope

| Item | MVP | Stretch |
| --- | --- | --- |
| Catalysts, the 4-phase ritual and the victory screen | Phase 4 | |
| Prestige Endless Mode: chaos modifiers, unstable multi-door breaches, celestial clients, global high-score ladders | Unlocked on completion | Content depth |

## Open Questions

- Does the Uber-Weapon obey the two-stat lock (Quality + Base Damage), or is it outside the normal weapon model?
- Can players wield the Uber-Weapon in Endless Mode?
