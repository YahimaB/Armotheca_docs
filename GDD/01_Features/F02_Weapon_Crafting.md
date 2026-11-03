---
id: F02_Weapon_Crafting
type: feature
status: Draft
priority: Must
owner:
milestone: Phase 1
pillars: [Modular Craftsmanship, Cooperative Synergy]
---

# Weapon Crafting (Processing & 2-Piece Assembly)

> **Hub:** [_Feature_List](_Feature_List.md) · **Technical:** [_Module_Map › Features](../../Technical_Design/_Module_Map.md#features)

## Purpose

Crafting is the tactile core of workshop life. Raw materials hauled from expeditions cannot go straight onto a weapon: they are refined by hand at workstations, with optional timing mini-games that set each component's Quality. Weapons are then built from **exactly two components**, which avoids the combinatorial explosion and UI fatigue of 5+ part forging while still letting material choice and component quality answer diverse commissions.

## Player Experience

- **Tactile satisfaction:** physically placing a blade and a hilt on the bench and hammering them together feels rewarding.
- **Physical choreography:** players move purposefully around the workshop, transferring heated ingots with tongs, operating bellows and shaving wood at the lathe.
- **Readable combinatorics:** players look at a letter and immediately deduce which two parts are needed (*Frost Core + Willow Short Shaft = Frost Willow Wand*).
- **Mastery through feel:** skilled players learn station rhythms to produce Flawless components without heavy UI gauges.
- **Quality differentiation:** careful processing raises Quality, which decides which clients accept the weapon and how much they pay.
- **Role collaboration:** one player forges blades while another works hilts; one pumps the bellows while another strikes the anvil.
- **Forgiving failure:** botched mini-games never destroy materials.

## References

- **The Legend of Zelda: Tears of the Kingdom (Fuse):** intuitive 2-part composition with predictable inheritance.
- **Potion Craft:** component properties combine without UI clutter; physical stirring, heating and grinding to precise targets.
- **PlateUp! / Overcooked:** multi-step pipelines (chop → cook → plate) and physical placement of prepared parts.
- **Kingdom Come: Deliverance (sharpening):** timing-dependent smithing that gives weight to the craft.
- **Ale & Tale Tavern:** hands-on station interactions involving carrying, stirring and cleaning.
- **Monster Hunter:** monster-derived materials visibly defining weapon identity.

## Mechanics

- [M_Resource_Processing](../02_Systems/Processing/M_Resource_Processing.md): station pipelines from raw material to component.
- [M_Processing_Mini_Game](../02_Systems/Processing/M_Processing_Mini_Game.md): optional timing that sets Quality.
- [M_Assembly](../02_Systems/Crafting/M_Assembly.md): joining foundation and payload.
- [M_Quality](../02_Systems/Crafting/M_Quality.md): the two weapon stats and Quality tiers.
- [M_Weapon_Naming](../02_Systems/Crafting/M_Weapon_Naming.md): automatic weapon names.
- [M_Continuous_Interaction](../02_Systems/Interaction/M_Continuous_Interaction.md): working stations, with helpers.
- [M_Targeting](../02_Systems/Interaction/M_Targeting.md): socket and station prompts.
- [M_Walk](../02_Systems/Movement/M_Walk.md), [M_Sprint](../02_Systems/Movement/M_Sprint.md): carrying through the workshop.

## Entities

- Workstations: [E_Smelting_Forge](../03_Entities/Props/Workstations/E_Smelting_Forge/E_Smelting_Forge.md), [E_Anvil](../03_Entities/Props/Workstations/E_Anvil/E_Anvil.md), [E_Quenching_Basin](../03_Entities/Props/Workstations/E_Quenching_Basin/E_Quenching_Basin.md), [E_Woodworking_Lathe](../03_Entities/Props/Workstations/E_Woodworking_Lathe/E_Woodworking_Lathe.md), [E_Carving_Bench](../03_Entities/Props/Workstations/E_Carving_Bench/E_Carving_Bench.md), [E_Arcane_Extractor](../03_Entities/Props/Workstations/E_Arcane_Extractor/E_Arcane_Extractor.md), [E_Purity_Distiller](../03_Entities/Props/Workstations/E_Purity_Distiller/E_Purity_Distiller.md), [E_Assembly_Bench](../03_Entities/Props/Workstations/E_Assembly_Bench/E_Assembly_Bench.md).
- Components: [E_Blade](../03_Entities/Items/Components/E_Blade/E_Blade.md), [E_Core](../03_Entities/Items/Components/E_Core/E_Core.md), [E_Hilt](../03_Entities/Items/Components/E_Hilt/E_Hilt.md), [E_Short_Shaft](../03_Entities/Items/Components/E_Short_Shaft/E_Short_Shaft.md), [E_Long_Shaft](../03_Entities/Items/Components/E_Long_Shaft/E_Long_Shaft.md).
- Weapons: [E_Sword](../03_Entities/Items/Weapons/E_Sword/E_Sword.md), [E_Wand](../03_Entities/Items/Weapons/E_Wand/E_Wand.md), [E_Staff](../03_Entities/Items/Weapons/E_Staff/E_Staff.md).

## Locations

- [L00_Workshop](../04_Locations/L00_Workshop/L00_Workshop.md): all processing and assembly happens in the Workshop Hall.

## UI

- [UI_Assembly_Bench](../05_UI/World/UI_Assembly_Bench.md): sockets, preview and incompatibility feedback.
- [UI_Interaction_Prompt](../05_UI/Hud/UI_Interaction_Prompt.md): station prompts and progress.

## Scope

| Item | MVP | Stretch |
| --- | --- | --- |
| Assembly bench with swords, wands and staves | Phase 1 | |
| Manual processing workstations | Phase 1 | |
| Further weapon stats | | After a deliberate revision of the stat lock |

## Open Questions

-
