---
id: M_Resource_Processing
type: mechanic
system: Processing
status: Draft
---

# Resource Processing (Station Pipelines)

> **System:** [_Processing_System](_Processing_System.md) · **Technical:** [_Processing_Module › Architecture](../../../Technical_Design/Processing/_Processing_Module.md#architecture--implementation-approaches)

## Summary

Three pipelines turn raw ore, timber and mob drops into blades, foundations and cores.

## Rules

### Blades: Smelting Forge → Anvil → Quenching Basin

1. **Heating:** raw ore is placed into the [E_Smelting_Forge](../../03_Entities/Props/Workstations/E_Smelting_Forge/E_Smelting_Forge.md) (instant). A player works the bellows (continuous) until glowing orange heat; a second player on the bellows speeds it up.
2. **Transfer:** the ingot is taken with tongs (instant) and placed on the [E_Anvil](../../03_Entities/Props/Workstations/E_Anvil/E_Anvil.md).
3. **Hammering:** rhythmic strikes set Quality ([M_Processing_Mini_Game](M_Processing_Mini_Game.md)).
4. **Quenching:** the blade is plunged into the [E_Quenching_Basin](../../03_Entities/Props/Workstations/E_Quenching_Basin/E_Quenching_Basin.md) (instant) to lock it in.

### Foundations: Woodworking Lathe → Carving Bench

1. **Rough cut:** arcane lumber is placed onto the [E_Woodworking_Lathe](../../03_Entities/Props/Workstations/E_Woodworking_Lathe/E_Woodworking_Lathe.md). The player holds the chisel (continuous) while the wood rotates.
2. **Selection:** the player chooses the output: **Hilt**, **Short Shaft** or **Long Shaft**.
3. **Sanding / polishing:** rubbed with beeswax or resin at the [E_Carving_Bench](../../03_Entities/Props/Workstations/E_Carving_Bench/E_Carving_Bench.md) (continuous).

### Cores: Arcane Extractor → Purity Distiller

1. **Maceration:** monster essence (e.g. Phoenix Feather, Void Slime Core) is loaded into the [E_Arcane_Extractor](../../03_Entities/Props/Workstations/E_Arcane_Extractor/E_Arcane_Extractor.md) mortar.
2. **Heat regulation:** the player keeps the distillation temperature in the sweet spot at the [E_Purity_Distiller](../../03_Entities/Props/Workstations/E_Purity_Distiller/E_Purity_Distiller.md) ([M_Processing_Mini_Game](M_Processing_Mini_Game.md)).
3. **Crystallisation:** the extracted fluid condenses into a socketable **Aether Core**.

## Player Input

Load and unload: [M_Instant_Interaction](../Interaction/M_Instant_Interaction.md). Work: [M_Continuous_Interaction](../Interaction/M_Continuous_Interaction.md).

## Tunable Parameters

| Parameter | Meaning | Value |
| --- | --- | --- |
| Bellows heating time | Forge to orange heat | [Processing › Stations](../../06_Balancing/Processing.md#stations) |

## UI

- [UI_Interaction_Prompt](../../05_UI/World/UI_Interaction_Prompt.md)

## Dependencies

- Inputs from [M_Harvesting](../Exploration/M_Harvesting.md) and mob drops ([_Mob_Roster](../../03_Entities/Mobs/_Mob_Roster.md)).

## Used By

- [F02_Weapon_Crafting](../../01_Features/F02_Weapon_Crafting.md)

## Open Questions

-
