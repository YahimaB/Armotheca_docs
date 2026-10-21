# Resource Processing (Manual Workstations)

> **Zone:** Shop · **Technical counterpart:** [TechnicalDesign/Shop/ResourceProcessing](../../TechnicalDesign/Shop/ResourceProcessing.md)

## Design Intent

The Resource Processing System is the tactile core of workshop life in *Armotheca*. Raw materials hauled from dimensional expeditions cannot be slapped directly onto a weapon; they require physical labor and careful refinement. **All processing is strictly manual, without automation.** Each station involves direct physical handling, multi-step procedures, and optional timing mini-games that set the resulting component's **Quality (1–100)**.

Workstations are built on the common [Object Interaction](../Common/ObjectInteraction.md) model: loading and unloading are instant interactions, working the station is a continuous interaction.

---

## Player Experience Goals

- **Physical Choreography:** Players move purposefully around the workshop: transferring heated ingots with tongs, operating bellows, and shaving wood at the lathe.
- **Mastery Through Feel:** Skilled players learn the rhythm of stations to produce *Flawless* components consistently without relying on heavy UI gauges.
- **Emergent Cooperative Assistance:** One player can pump the bellows while another strikes the anvil, speeding up the pipeline and building camaraderie.
- **Forgiving Failure:** Botched mini-games never destroy materials; they yield *Crude* or *Standard* items rather than zero-gain losses.

---

## References

- **PlateUp! & Overcooked:** Multi-step transformation pipelines (chop → cook → plate) with risk.
- **Kingdom Come: Deliverance (Sharpening):** Angle- and timing-dependent smithing that gives physical weight to the craft.
- **Potion Craft:** Physical stirring, heating with bellows, and grinding to reach precise targets.
- **Ale & Tale Tavern:** Hands-on station interactions involving carrying, stirring and cleaning up.

---

## Workshop Stations & Transformation Pipelines

```
Raw Ores (Realms) -------> [SMELTING FORGE] -------> Hot Ingot
                                                         |
                                                         v
                                                [ANVIL SHAPING] (Timing Strike)
                                                         |
                                                         v
                                                [QUENCHING BASIN] ---> Refined BLADE

Arcane Timber (Realms) --> [WOODWORKING LATHE] ---> [CARVING BENCH] ---> Refined SHAFT / HILT

Mob Drops (Realms) ------> [ARCANE EXTRACTOR] ----> [PURITY DISTILLER] -> Refined CORE
```

### What Each Output Carries
- **Blade:** Quality (from processing) + Base Damage and Element (from the ore material).
- **Core:** Quality (from processing) + Base Damage and Element (from the mob essence material).
- **Hilt / Short Shaft / Long Shaft:** Quality (from processing) + material identity. No Base Damage.

### 1. Smelting Forge & Anvil (Blades)
1. **Heating:** Raw ore is placed into the forge (instant). A player works the bellows (continuous) to reach glowing orange heat (3–6 s). A second player on the bellows speeds it up.
2. **Transfer:** The ingot is taken with tongs (instant) and placed on the anvil.
3. **Hammering (Mini-Game):** 3 rhythmic strikes. A sweeping cursor crosses a target zone.
   - *Perfect strike:* +15 Quality.
   - *Good strike:* +5 Quality.
   - *Off-beat strike:* −5 Quality.
   - Strikes start from a base of 50 Quality.
4. **Quenching:** The blade is plunged into the basin (instant) to lock it in.

### 2. Woodworking Lathe & Carving Bench (Hilts & Shafts)
1. **Rough Cut:** Arcane lumber is placed onto the lathe. The player holds the chisel (continuous) while the wood rotates.
2. **Selection:** The player chooses the output: **Hilt**, **Short Shaft** or **Long Shaft**.
3. **Sanding / Polishing:** Rubbed with beeswax or resin at the carving bench (continuous).

### 3. Arcane Extractor & Distiller (Cores)
1. **Maceration:** Monster essence (e.g. Phoenix Feather, Void Slime Core) is loaded into the extraction mortar.
2. **Heat Regulation (Mini-Game):** The player keeps the distillation temperature inside the sweet-spot zone using flame valves for 4 seconds.
3. **Crystallization:** The extracted fluid condenses into a socketable **Aether Core**.

---

## Optional Mini-Game Philosophy

- Mini-games are **lightweight, rhythmic micro-interactions**, not full-screen pausing puzzles.
- **Accessibility Guarantee:** A player who skips the mini-game timing (or has accessibility aids enabled) still completes the station and receives a baseline **Quality 60 (Standard)** component.
- Engaging with the mini-game lets players reach **Masterwork (75+)** and **Flawless (95+)**, which top-paying Collector and Academy commissions require.
- Final quality is always clamped to **1–100**.

---

## Open Questions

- Should raw materials have their own quality that caps the result, or is quality purely a product of player skill?
- Does the lathe have a mini-game, or is it a pure hold interaction with fixed quality?
- Tier 1 shop (see [Shop Progression](ShopProgression.md)) does not unlock the lathe or extractor, yet hilts and cores are needed for every weapon — how are Tier 1 foundations and cores obtained?
