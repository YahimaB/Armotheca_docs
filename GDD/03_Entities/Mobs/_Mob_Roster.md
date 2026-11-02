---
id: _Mob_Roster
type: roster
status: Draft
---

# Mob Roster

> **Overview:** [Glossary](../../00_Overview/Glossary.md) · **Balancing:** [Combat › Mobs](../../06_Balancing/Combat.md#mobs) · **Technical:** [Mob_AI](../../../Technical_Design/Exploration/Mob_AI.md)

## Overview

Mobs are the danger and the second resource source of every realm. They threaten players busy harvesting and drop the organic ingredients — essences, cores, claws — that wand and staff cores need. They are simple, readable enemies built on a few behaviour archetypes, so they work with the deliberately simple sword-and-orb combat ([F04_Combat](../../01_Features/F04_Combat.md)).

### Categories

| Category | Role | Typical Drops | Where | Folder |
|---|---|---|---|---|
| **Minor Fauna** | Weak, often in groups | Pelts, Claws, Fangs | Outer Grounds | `Minor_Fauna/` |
| **Elemental Beasts** | Tougher, elemental attacks | Cores, Essences, Ichor | Deep Grounds | `Elemental_Beasts/` |
| **Apex Guardian** | Boss, one per realm | Primordial Catalyst | Apex Arena | `Apex_Guardians/` |

### Behaviour Archetypes

| Archetype | Behaviour | Counter |
|---|---|---|
| **Chaser** | Closes distance, telegraphed lunge/bite | Roll through the lunge, swing |
| **Ranged** | Keeps distance, fires slow projectiles | Close in with a sword or trade orbs |
| **Swarm** | Weak, many, surrounds players | Sword arcs hit several at once |
| **Ambusher** | Hides near nodes, wakes when a node is harvested | Guard harvesters |

### Shared Rules

1. Each mob type has fixed **health** and fixed **attack damage** defined in data. Player weapons deal their Base Damage per hit ([_Combat_System](../../02_Systems/Combat/_Combat_System.md)).
2. Every attack is telegraphed long enough to roll away.
3. On death a mob drops items from its drop table (guaranteed main drop plus chance-based extras). Drops are collected like node yields ([M_Carry_Model](../../02_Systems/Interaction/M_Carry_Model.md)).
4. Minor Fauna are staggered by sword hits; Elemental Beasts and Apex Guardians are not.
5. Placement and escalation: [M_Mob_Spawning](../../02_Systems/Exploration/M_Mob_Spawning.md), [M_Realm_Pressure](../../02_Systems/Exploration/M_Realm_Pressure.md).

### Apex Guardians

1. One per realm, in the Apex Arena, guarding that realm's Primordial Catalyst ([E_Primordial_Catalyst](../Items/Catalysts/E_Primordial_Catalyst/E_Primordial_Catalyst.md)).
2. Multi-phase fights with telegraphed area attacks designed for 1–4 players; health scales with player count.
3. Defeating a Guardian drops its catalyst; Guardians do not respawn once their catalyst is taken (except in Prestige mode).

## Roster

| ID | Name | Group | Archetype | Notable Drop | Appears In | Status |
| --- | --- | --- | --- | --- | --- | --- |
| [E_Bramble_Stalker](Minor_Fauna/E_Bramble_Stalker/E_Bramble_Stalker.md) | Bramble Stalker | Minor Fauna | Chaser / Ambusher | Thorned Pelt, Verdant Essence | [L01](../../04_Locations/L01_Verdant_Corruption/L01_Verdant_Corruption.md) | Draft |
| [E_Void_Slime](Minor_Fauna/E_Void_Slime/E_Void_Slime.md) | Void Slime | Minor Fauna | Swarm | Void Slime Core (Arcane) | [L03](../../04_Locations/L03_Astral_Quarry/L03_Astral_Quarry.md) | Draft |
| [E_Fire_Salamander](Elemental_Beasts/E_Fire_Salamander/E_Fire_Salamander.md) | Fire Salamander | Elemental Beast | Ranged | Salamander Ichor (Fire) | [L02](../../04_Locations/L02_Pyroclastic_Trench/L02_Pyroclastic_Trench.md) | Draft |
| [E_Frost_Wraith](Elemental_Beasts/E_Frost_Wraith/E_Frost_Wraith.md) | Frost Wraith | Elemental Beast | Chaser | Wraith Essence (Frost) | [L04](../../04_Locations/L04_Frostbite_Cavern/L04_Frostbite_Cavern.md) | Draft |
| [E_Verdant_Elder](Apex_Guardians/E_Verdant_Elder/E_Verdant_Elder.md) | Verdant Elder | Apex Guardian | — | Sylvan Spire | [L01](../../04_Locations/L01_Verdant_Corruption/L01_Verdant_Corruption.md) | Draft |
| [E_Pyroclastic_Apex](Apex_Guardians/E_Pyroclastic_Apex/E_Pyroclastic_Apex.md) | Pyroclastic Apex | Apex Guardian | — | Ignis Core | [L02](../../04_Locations/L02_Pyroclastic_Trench/L02_Pyroclastic_Trench.md) | Draft |
| [E_Astral_Sovereign](Apex_Guardians/E_Astral_Sovereign/E_Astral_Sovereign.md) | Astral Sovereign | Apex Guardian | — | Astral Prism | [L03](../../04_Locations/L03_Astral_Quarry/L03_Astral_Quarry.md) | Draft |
| [E_Frost_Wyrm](Apex_Guardians/E_Frost_Wyrm/E_Frost_Wyrm.md) | Frost Wyrm | Apex Guardian | — | Glacial Heart | [L04](../../04_Locations/L04_Frostbite_Cavern/L04_Frostbite_Cavern.md) | Draft |

## Gaps

- This roster is the minimum per realm; additional mobs per realm are expected.
- No mob stats, drop tables or Apex Guardian phases yet.

## Open Questions

- Do mobs attack workshop-bound items (e.g. destroy dropped cargo), or only players?
- Should elemental beasts resist or be weak to elements once element effects exist?
