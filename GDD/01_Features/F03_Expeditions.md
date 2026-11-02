---
id: F03_Expeditions
type: feature
status: Draft
priority: Must
owner:
milestone: Phase 1
pillars: [Dimensional Contract Cycle]
---

# Expeditions (Magic Doors, Realms & Gathering)

> **Hub:** [_Feature_List](_Feature_List.md) · **Technical:** [Technical Overview › Code Organization](../../Technical_Design/Technical_Overview.md#7-code-organization)

## Purpose

Magic Doors are the resource lifeline of *Armotheca*. Each door opens onto a compact, hand-crafted pocket realm with its own look, resources and monsters. Doors are **bought, not granted**, so expanding the team's reach is a deliberate investment. Once opened, a door stays open **for entering** only briefly, and there is **no time limit inside**: expeditions end when the team decides to come home, pushed by letter deadlines, a full backpack and a realm that grows more hostile the longer they stay. Resources are the reason to go through: nodes are harvested by hand, mobs drop organic ingredients, and node placement changes every opening so teams scout and split up instead of running a memorised route.

## Player Experience

- **Investing in reach:** buying a new door is a visible milestone and a real choice of where to spend gold.
- **Targeted expeditions:** teams pick a door and a band based on active letters (*"We need a Frost Core and Iron Ore — open the Frostbite Cavern!"*).
- **Instant identity:** one glance through a door tells players which realm it is and what it offers.
- **Fresh but learnable:** the layout is familiar enough to plan a route; resources and mobs move every opening.
- **Commit to the dive:** once the entry window closes, the team inside is the team that has to make it work.
- **Self-paced return:** pressure comes from the core loop (deadlines, capacity, rising danger), not a countdown.
- **Escalating danger and room for big fights:** deeper areas hold better materials and stronger mobs; Apex Guardian fights fit in a normal expedition.
- **Readable, satisfying harvesting:** distinct node silhouettes, and every strike has a crunch, a chip effect and visible damage.
- **Meaningful capacity:** backpack space is limited; the Aether Chute and teammates relieve the pressure.

## References

- **Lethal Company:** short extraction runs where greed versus safety drives leaving; small known maps with randomised loot; limited carry capacity.
- **Deep Rock Galactic:** escalating swarms while the team mines; biomes that change both resources and threats.
- **Moonlighter:** a gate between the safe shop and the dangerous dungeon, crossed many times per day; themed dungeons with distinct material pools.
- **Valheim:** readable resource nodes with satisfying per-hit feedback.

## Mechanics

- [M_Door_Purchase](../02_Systems/Exploration/M_Door_Purchase.md), [M_Door_Lifecycle](../02_Systems/Exploration/M_Door_Lifecycle.md), [M_Realm_Instancing](../02_Systems/Exploration/M_Realm_Instancing.md)
- [M_Harvesting](../02_Systems/Exploration/M_Harvesting.md), [M_Node_Spawning](../02_Systems/Exploration/M_Node_Spawning.md)
- [M_Mob_Spawning](../02_Systems/Exploration/M_Mob_Spawning.md), [M_Realm_Pressure](../02_Systems/Exploration/M_Realm_Pressure.md)
- [M_Carry_Model](../02_Systems/Interaction/M_Carry_Model.md): backpack capacity.
- Traversal: [M_Walk](../02_Systems/Movement/M_Walk.md), [M_Sprint](../02_Systems/Movement/M_Sprint.md), [M_Jump](../02_Systems/Movement/M_Jump.md).
- [M_Targeting](../02_Systems/Interaction/M_Targeting.md): harvest, door and portal prompts.
- What pushes players home: [_Exploration_System](../02_Systems/Exploration/_Exploration_System.md).

## Entities

- [E_Magic_Door](../03_Entities/Props/Interactive/E_Magic_Door.md), [E_Exit_Portal](../03_Entities/Props/Interactive/E_Exit_Portal.md), [E_Aether_Chute](../03_Entities/Props/Interactive/E_Aether_Chute.md)
- [E_Mineral_Vein](../03_Entities/Props/Resource_Nodes/E_Mineral_Vein.md), [E_Arcane_Flora](../03_Entities/Props/Resource_Nodes/E_Arcane_Flora.md)
- [_Mob_Roster](../03_Entities/Mobs/_Mob_Roster.md)

## Locations

- [_World_Map](../04_Locations/_World_Map.md): realm directory and shared band structure.
- [L01_Verdant_Corruption](../04_Locations/L01_Verdant_Corruption/L01_Verdant_Corruption.md), [L02_Pyroclastic_Trench](../04_Locations/L02_Pyroclastic_Trench/L02_Pyroclastic_Trench.md), [L03_Astral_Quarry](../04_Locations/L03_Astral_Quarry/L03_Astral_Quarry.md), [L04_Frostbite_Cavern](../04_Locations/L04_Frostbite_Cavern/L04_Frostbite_Cavern.md)

## UI

- [UI_Realm_Pressure](../05_UI/Hud/UI_Realm_Pressure.md): rising danger without a countdown.
- [UI_Interaction_Prompt](../05_UI/World/UI_Interaction_Prompt.md): harvest prompts and door plaques.

## Scope

| Item | MVP | Stretch |
| --- | --- | --- |
| First door (Verdant Corruption) | Phase 1 | |
| Entry window and Realm Pressure | Phase 2 | |
| All four realms | Phase 3 | |
| Prestige realm modifiers | | Prestige Endless Mode |

## Open Questions

-
