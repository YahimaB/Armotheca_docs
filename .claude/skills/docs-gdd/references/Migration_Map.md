# GDD migration map (zone layout → type layout)

Planned destination of every section in the current GDD. Paths are relative to
`GDD/`. Names are proposals: confirm new IDs with the user before the first
migration, then treat them as fixed. System names equal the code module names in
the `docs-technical-design` migration map (Movement, Interaction, Combat,
Crafting, Processing, Orders, Progression, Endgame, Exploration).

## Order

1. Create `00_Overview/` (Vision, Core_Loop, Glossary with the type definitions,
   empty Changelog) and empty hubs (`_Feature_List`, system hubs, rosters,
   `_World_Map`, `_UI_Flow`).
2. Migrate one source document at a time, systems and entities before features,
   so feature hubs can link to docs that exist.
3. After each source document: move its numbers to `06_Balancing/`, fix inbound
   links (Technical_Design, Development_Phases, Guidelines, README), run the link
   check, and delete the source file only with the user's confirmation.

## Feature hubs

| ID | Built from |
| --- | --- |
| `F01_Commissions` | `Shop/Order_System.md`: intent, experience goals |
| `F02_Weapon_Crafting` | `Shop/Weapon_Crafting.md`, `Shop/Resource_Processing.md`: intent, experience goals |
| `F03_Expeditions` | `Exploration/Magic_Doors.md`, `Exploration/Realms.md`, `Exploration/Resource_Gathering.md`: intent, experience goals |
| `F04_Combat` | `Common/Combat.md`, `Exploration/Mobs.md`: intent, experience goals |
| `F05_Shop_Progression` | `Shop/Shop_Progression.md`: intent, experience goals |
| `F06_Uber_Weapon` | `Shop/Uber_Weapon.md`, `Master_GDD.md` §7 |
| `F07_Co_Op` | `Master_GDD.md` pillar 1 (cooperative synergy); networking-first rules stay in Technical_Design |

## Source documents

| Source | Destination |
| --- | --- |
| `Master_GDD.md` §1–2, §4 | `00_Overview/Vision.md` |
| `Master_GDD.md` §3 | `00_Overview/Core_Loop.md` |
| `Master_GDD.md` §5 | `01_Features/_Feature_List.md` (replaces the zone index) |
| `Master_GDD.md` §6 | `03_Entities/NPCs/Clients/_Client_Roster.md` |
| `Master_GDD.md` §8 | Link from `Vision.md` to the Technical Overview |
| `Common/Movement.md` | `02_Systems/Movement/`: `_Movement_System` (State Rules), `M_Walk`, `M_Sprint`, `M_Jump`, `M_Roll`; Initial Tuning Targets → `06_Balancing/Movement.md` |
| `Common/Object_Interaction.md` | `02_Systems/Interaction/`: `_Interaction_System`, `M_Carry_Model`, `M_Instant_Interaction`, `M_Continuous_Interaction`, `M_Targeting`; prompts → `05_UI/Hud/UI_Interaction_Prompt.md` |
| `Common/Combat.md` | `02_Systems/Combat/`: `_Combat_System`, `M_Sword_Swing`, `M_Magic_Orb`, `M_Health_And_Downed`; Weapons in Combat → weapon entities; values → `06_Balancing/Combat.md` |
| `Shop/Weapon_Crafting.md` | `02_Systems/Crafting/`: `_Crafting_System`, `M_Assembly`, `M_Quality`, `M_Weapon_Naming`; Weapon Categories → `03_Entities/Items/Weapons/` (`E_Sword`, `E_Wand`, `E_Staff`) and `Items/Components/`; Material Attributes → `Items/Materials/`; bench → `Props/Workstations/E_Assembly_Bench` |
| `Shop/Resource_Processing.md` | `02_Systems/Processing/`: `_Processing_System`, `M_Resource_Processing`, `M_Processing_Mini_Game`; stations → `03_Entities/Props/Workstations/` (`E_Smelting_Forge`, `E_Anvil`, `E_Woodworking_Lathe`, `E_Carving_Bench`, `E_Arcane_Extractor`, `E_Distiller`) |
| `Shop/Order_System.md` | `02_Systems/Orders/`: `_Orders_System`, `M_Commission_Criteria`, `M_Letter_Flow`; archetypes → `03_Entities/NPCs/Clients/` (`E_Adventurers_Guild`, `E_Arcane_Academy`, `E_City_Garrison`, `E_SOS_Dispatch`, `E_Eccentric_Collectors`); mailbox → `Props/Interactive/E_Mailbox_Nexus`; rewards and lifespans → `06_Balancing/Orders.md` |
| `Shop/Shop_Progression.md` | `02_Systems/Progression/`: `_Progression_System`, `M_Currencies`, `M_Workshop_Tiers`; tier table → `06_Balancing/Progression.md`; workshop space → `04_Locations/L00_Workshop/` |
| `Shop/Uber_Weapon.md` | `02_Systems/Endgame/`: `_Endgame_System`, `M_Forging_Ritual`; catalysts → `03_Entities/Items/Catalysts/`; crucible → `Props/Workstations/E_Great_Crucible`; payoff → `F06_Uber_Weapon` |
| `Exploration/Magic_Doors.md` | `02_Systems/Exploration/`: `M_Door_Purchase`, `M_Door_Lifecycle`, `M_Return_Pressure`; anti-downtime rules → `_Exploration_System`; `Props/Interactive/` (`E_Magic_Door`, `E_Exit_Portal`, `E_Aether_Chute`) |
| `Exploration/Realms.md` | `04_Locations/_World_Map.md` (directory, unlock order); `L01_Verdant_Corruption`, `L02_Pyroclastic_Trench`, `L03_Astral_Quarry`, `L04_Frostbite_Cavern`; Realm Structure, Lifetime and Per-Opening Variation → `02_Systems/Exploration/M_Realm_Instancing` |
| `Exploration/Resource_Gathering.md` | `02_Systems/Exploration/`: `M_Harvesting`, `M_Node_Spawning`; nodes → `03_Entities/Props/Resource_Nodes/`; yields → `06_Balancing/Exploration.md` |
| `Exploration/Mobs.md` | `03_Entities/Mobs/_Mob_Roster` (categories, archetypes, roster); `Mobs/Common/` (`E_Bramble_Stalker`, `E_Fire_Salamander`, `E_Void_Slime`, `E_Frost_Wraith`); `Mobs/Apex_Guardians/` (`E_Verdant_Elder`, `E_Pyroclastic_Apex`, `E_Astral_Sovereign`, `E_Frost_Wyrm`); Spawning and Realm Pressure → `02_Systems/Exploration/M_Mob_Spawning`, `M_Realm_Pressure`; health, damage, drops → `06_Balancing/Mobs.md` |
| `../UI_Design/Mailbox/Letter_Commission_Board.md` | `05_UI/World/UI_Letter_Commission_Board.md` |
| `../UI_Design/Workstations/Assembly_Bench_UI.md` | `05_UI/World/UI_Assembly_Bench.md` |

## Inbound references to update

- `README.md`: structure tree, Quick Navigation tables, Documentation Standards.
- `Technical_Design/**`: `> **Design:**` header lines (the technical side's own
  layout is decided by `docs-technical-design`).
- `Development_Phases/**`: "Required sources" links.
- `Guidelines/Assets_Naming.md` §2: the "Docs counterpart" column.
- `Guidelines/Modeling_Guidelines.md`: Game context link.
