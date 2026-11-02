---
id: _Module_Map
type: map
status: Draft
---

# Module Map

> **Overview:** [Technical Overview](Technical_Overview.md) · **Naming:** [Assets Naming §3](../Guidelines/Assets_Naming.md)

Each module is one `Armotheca.<Module>` namespace, one assembly (`Scripts/<Module>/Armotheca.<Module>.asmdef`) and one folder here, named like its GDD system.

## Modules

| Module | Namespace | GDD system | Doc | Depends on |
| --- | --- | --- | --- | --- |
| Core | `Armotheca.Core` | — | [_Core_Module](Core/_Core_Module.md) | — |
| Networking | `Armotheca.Networking` | — (serves [F07_Co_Op](../GDD/01_Features/F07_Co_Op.md)) | [_Networking_Module](Networking/_Networking_Module.md) | — |
| Movement | `Armotheca.Movement` | [Movement](../GDD/02_Systems/Movement/_Movement_System.md) | [_Movement_Module](Movement/_Movement_Module.md) | — |
| Interaction | `Armotheca.Interaction` | [Interaction](../GDD/02_Systems/Interaction/_Interaction_System.md) | [_Interaction_Module](Interaction/_Interaction_Module.md) | Movement |
| Combat | `Armotheca.Combat` | [Combat](../GDD/02_Systems/Combat/_Combat_System.md) | [_Combat_Module](Combat/_Combat_Module.md) | Movement |
| Crafting | `Armotheca.Crafting` | [Crafting](../GDD/02_Systems/Crafting/_Crafting_System.md) | [_Crafting_Module](Crafting/_Crafting_Module.md) | Core |
| Processing | `Armotheca.Processing` | [Processing](../GDD/02_Systems/Processing/_Processing_System.md) | [_Processing_Module](Processing/_Processing_Module.md) | Crafting, Interaction |
| Orders | `Armotheca.Orders` | [Orders](../GDD/02_Systems/Orders/_Orders_System.md) | [_Orders_Module](Orders/_Orders_Module.md) | Core, Crafting |
| Progression | `Armotheca.Progression` | [Progression](../GDD/02_Systems/Progression/_Progression_System.md) | [_Progression_Module](Progression/_Progression_Module.md) | Exploration |
| Endgame | `Armotheca.Endgame` | [Endgame](../GDD/02_Systems/Endgame/_Endgame_System.md) | [_Endgame_Module](Endgame/_Endgame_Module.md) | Progression |
| Exploration | `Armotheca.Exploration` | [Exploration](../GDD/02_Systems/Exploration/_Exploration_System.md) | [_Exploration_Module](Exploration/_Exploration_Module.md) | Core, Combat, Interaction, Progression |
| UI | `Armotheca.UI` | — (serves [_UI_Flow](../GDD/05_UI/_UI_Flow.md)) | [_UI_Module](UI/_UI_Module.md) | every module it displays |

`Depends on` reflects the `using` directives and cross-module calls in each doc's reference code and prose. Progression ↔ Exploration is a two-way reference (door definitions and ownership); resolve it with an interface in Core before the assemblies are created.

## Entities and UI

Where each GDD entity, location and screen is implemented.

| GDD doc | Module | Section |
| --- | --- | --- |
| [Player](../GDD/03_Entities/Player/Player.md) | Movement, Interaction, Combat | [_Movement_Module](Movement/_Movement_Module.md#controller-context) |
| Mobs ([_Mob_Roster](../GDD/03_Entities/Mobs/_Mob_Roster.md)) | Exploration | [Mob_AI](Exploration/Mob_AI.md) |
| Clients ([_Client_Roster](../GDD/03_Entities/NPCs/Clients/_Client_Roster.md)) | Orders | [_Orders_Module › Data](Orders/_Orders_Module.md#data) |
| Weapons and components ([_Item_List](../GDD/03_Entities/Items/_Item_List.md)) | Crafting | [_Crafting_Module](Crafting/_Crafting_Module.md#architecture--implementation-approaches) |
| [E_Primordial_Catalyst](../GDD/03_Entities/Items/Catalysts/E_Primordial_Catalyst.md) | Endgame | [_Endgame_Module](Endgame/_Endgame_Module.md#technical-specifications) |
| Workstations ([_Prop_List](../GDD/03_Entities/Props/_Prop_List.md)) | Processing; Crafting (bench); Endgame (crucible) | [_Processing_Module](Processing/_Processing_Module.md#technical-specifications) |
| Doors, Exit Portal, Aether Chute | Exploration | [Door_Instances](Exploration/Door_Instances.md) |
| Resource nodes | Exploration | [Resource_Nodes](Exploration/Resource_Nodes.md) |
| [E_Mailbox_Nexus](../GDD/03_Entities/Props/Interactive/E_Mailbox_Nexus.md) | Orders | [_Orders_Module › Networking](Orders/_Orders_Module.md#networking) |
| [L00_Workshop](../GDD/04_Locations/L00_Workshop/L00_Workshop.md) | Progression | [_Progression_Module](Progression/_Progression_Module.md#technical-specifications) |
| Realms ([_World_Map](../GDD/04_Locations/_World_Map.md)) | Exploration | [Realm_Loading](Exploration/Realm_Loading.md) |
| All `UI_` screens ([_UI_Flow](../GDD/05_UI/_UI_Flow.md)) | UI | [_UI_Module](UI/_UI_Module.md) |

## Features

| Feature | Modules |
| --- | --- |
| [F01_Commissions](../GDD/01_Features/F01_Commissions.md) | Orders, Progression, UI |
| [F02_Weapon_Crafting](../GDD/01_Features/F02_Weapon_Crafting.md) | Processing, Crafting, Interaction, UI |
| [F03_Expeditions](../GDD/01_Features/F03_Expeditions.md) | Exploration, Interaction, Movement |
| [F04_Combat](../GDD/01_Features/F04_Combat.md) | Combat, Movement, Exploration (mobs) |
| [F05_Shop_Progression](../GDD/01_Features/F05_Shop_Progression.md) | Progression |
| [F06_Uber_Weapon](../GDD/01_Features/F06_Uber_Weapon.md) | Endgame, Processing |
| [F07_Co_Op](../GDD/01_Features/F07_Co_Op.md) | Networking (every module's Networking section) |
