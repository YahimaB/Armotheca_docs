---
id: _Prop_List
type: roster
status: Draft
---

# Prop List

> **Overview:** [Glossary](../../00_Overview/Glossary.md) · **Balancing:** [Exploration › Nodes](../../06_Balancing/Exploration.md#nodes)

## Overview

World objects players interact with. Props are reused across locations, so behaviour lives here and each location lists which props it contains.

- `Interactive/`: doors, portals, chutes, the mailbox.
- `Workstations/`: processing and assembly stations in the workshop. Modeling requirements: [_Workstations_Art](Workstations/_Workstations_Art.md).
- `Resource_Nodes/`: harvestable nodes in realms. Modeling requirements: [_Resource_Nodes_Art](Resource_Nodes/_Resource_Nodes_Art.md).

## Roster

| ID | Name | Group | Appears In | Status |
| --- | --- | --- | --- | --- |
| [E_Magic_Door](Interactive/E_Magic_Door/E_Magic_Door.md) | Magic Door | Interactive | Workshop | Draft |
| [E_Exit_Portal](Interactive/E_Exit_Portal/E_Exit_Portal.md) | Exit Portal | Interactive | Every realm (Entry) | Draft |
| [E_Aether_Chute](Interactive/E_Aether_Chute/E_Aether_Chute.md) | Aether Drop-Chute | Interactive | Every realm (Entry) → workshop basket | Draft |
| [E_Mailbox_Nexus](Interactive/E_Mailbox_Nexus/E_Mailbox_Nexus.md) | Mailbox Nexus | Interactive | Workshop | Draft |
| [E_Smelting_Forge](Workstations/E_Smelting_Forge/E_Smelting_Forge.md) | Smelting Forge | Workstations | Workshop | Draft |
| [E_Anvil](Workstations/E_Anvil/E_Anvil.md) | Anvil | Workstations | Workshop | Draft |
| [E_Quenching_Basin](Workstations/E_Quenching_Basin/E_Quenching_Basin.md) | Quenching Basin | Workstations | Workshop | Draft |
| [E_Woodworking_Lathe](Workstations/E_Woodworking_Lathe/E_Woodworking_Lathe.md) | Woodworking Lathe | Workstations | Workshop | Draft |
| [E_Carving_Bench](Workstations/E_Carving_Bench/E_Carving_Bench.md) | Carving Bench | Workstations | Workshop | Draft |
| [E_Arcane_Extractor](Workstations/E_Arcane_Extractor/E_Arcane_Extractor.md) | Arcane Extractor | Workstations | Workshop | Draft |
| [E_Purity_Distiller](Workstations/E_Purity_Distiller/E_Purity_Distiller.md) | Purity Distiller | Workstations | Workshop | Draft |
| [E_Assembly_Bench](Workstations/E_Assembly_Bench/E_Assembly_Bench.md) | Assembly Bench | Workstations | Workshop | Draft |
| [E_Great_Crucible](Workstations/E_Great_Crucible/E_Great_Crucible.md) | The Great Crucible | Workstations | Workshop (Tier 3) | Draft |
| [E_Mineral_Vein](Resource_Nodes/E_Mineral_Vein/E_Mineral_Vein.md) | Mineral Vein | Resource Nodes | Realms | Draft |
| [E_Arcane_Flora](Resource_Nodes/E_Arcane_Flora/E_Arcane_Flora.md) | Arcane Flora | Resource Nodes | Realms | Draft |

## Gaps

Mentioned in the design but without a doc yet:

- Storage crate (workshop backpack drop-off, [M_Carry_Model](../../02_Systems/Interaction/M_Carry_Model.md)).
- Receiving basket for the Aether Chute.
- Catalyst display pedestal ([E_Primordial_Catalyst](../Items/Catalysts/E_Primordial_Catalyst/E_Primordial_Catalyst.md)).
- Upgrade ledger ([M_Workshop_Tiers](../../02_Systems/Progression/M_Workshop_Tiers.md)).
- Grand Assembly Bench and high-speed lathe used by the ritual ([M_Forging_Ritual](../../02_Systems/Endgame/M_Forging_Ritual.md)).
- Runed Mallet and tongs (tools used at stations).
