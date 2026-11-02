# GDD migration map (zone layout → type layout)

Planned destination of every section in the current GDD. Paths are relative to
`GDD/`. Names are proposals: confirm new IDs with the user before the first
migration, then treat them as fixed.

## Order

1. Create `00_Overview/` (Vision, CoreLoop, Glossary with the type definitions,
   empty Changelog) and empty hubs (`_FeatureList`, system hubs, rosters,
   `_WorldMap`, `_UIFlow`).
2. Migrate one source document at a time, systems and entities before features,
   so feature hubs can link to docs that exist.
3. After each source document: move its numbers to `06_Balancing/`, fix inbound
   links (TechnicalDesign, DevelopmentPhases, Guidelines, README), run the link
   check, and delete the source file only with the user's confirmation.

## Feature hubs

| ID | Built from |
| --- | --- |
| `F01_Commissions` | `Shop/OrderSystem.md`: intent, experience goals |
| `F02_WeaponCrafting` | `Shop/WeaponCrafting.md`, `Shop/ResourceProcessing.md`: intent, experience goals |
| `F03_Expeditions` | `Exploration/MagicDoors.md`, `Exploration/Realms.md`, `Exploration/ResourceGathering.md`: intent, experience goals |
| `F04_Combat` | `Common/Combat.md`, `Exploration/Mobs.md`: intent, experience goals |
| `F05_ShopProgression` | `Shop/ShopProgression.md`: intent, experience goals |
| `F06_UberWeapon` | `Shop/UberWeapon.md`, `MasterGDD.md` §7 |
| `F07_CoOp` | `MasterGDD.md` pillar 1 (cooperative synergy); networking-first rules stay in TechnicalDesign |

## Source documents

| Source | Destination |
| --- | --- |
| `MasterGDD.md` §1–2, §4 | `00_Overview/Vision.md` |
| `MasterGDD.md` §3 | `00_Overview/CoreLoop.md` |
| `MasterGDD.md` §5 | `01_Features/_FeatureList.md` (replaces the zone index) |
| `MasterGDD.md` §6 | `03_Entities/NPCs/Clients/_ClientRoster.md` |
| `MasterGDD.md` §8 | Link from `Vision.md` to the Technical Overview |
| `Common/Movement.md` | `02_Systems/Movement/`: `_MovementSystem` (State Rules), `M_Walk`, `M_Sprint`, `M_Jump`, `M_Roll`; Initial Tuning Targets → `06_Balancing/Movement.md` |
| `Common/ObjectInteraction.md` | `02_Systems/Interaction/`: `_InteractionSystem`, `M_CarryModel`, `M_InstantInteraction`, `M_ContinuousInteraction`, `M_Targeting`; prompts → `05_UI/World/UI_InteractionPrompt.md` |
| `Common/Combat.md` | `02_Systems/Combat/`: `_CombatSystem`, `M_SwordSwing`, `M_MagicOrb`, `M_HealthAndDowned`; Weapons in Combat → weapon entities; values → `06_Balancing/Combat.md` |
| `Shop/WeaponCrafting.md` | `02_Systems/Crafting/`: `M_Assembly`, `M_Quality`, `M_WeaponNaming`; Weapon Categories → `03_Entities/Items/Weapons/` (`E_Sword`, `E_Wand`, `E_Staff`) and `Items/Components/`; Material Attributes → `Items/Materials/`; bench → `Props/Workstations/E_AssemblyBench` |
| `Shop/ResourceProcessing.md` | `02_Systems/Crafting/`: `_CraftingSystem`, `M_ResourceProcessing`, `M_ProcessingMiniGame`; stations → `03_Entities/Props/Workstations/` (`E_SmeltingForge`, `E_Anvil`, `E_WoodworkingLathe`, `E_CarvingBench`, `E_ArcaneExtractor`, `E_Distiller`) |
| `Shop/OrderSystem.md` | `02_Systems/Orders/`: `_OrdersSystem`, `M_CommissionCriteria`, `M_LetterFlow`; archetypes → `03_Entities/NPCs/Clients/` (`E_AdventurersGuild`, `E_ArcaneAcademy`, `E_CityGarrison`, `E_SosDispatch`, `E_EccentricCollectors`); mailbox → `Props/Interactive/E_MailboxNexus`; rewards and lifespans → `06_Balancing/Orders.md` |
| `Shop/ShopProgression.md` | `02_Systems/Progression/`: `_ProgressionSystem`, `M_Currencies`, `M_WorkshopTiers`; tier table → `06_Balancing/Progression.md`; workshop space → `04_Locations/L00_Workshop/` |
| `Shop/UberWeapon.md` | `02_Systems/Endgame/`: `_EndgameSystem`, `M_ForgingRitual`; catalysts → `03_Entities/Items/Catalysts/`; crucible → `Props/Workstations/E_GreatCrucible`; payoff → `F06_UberWeapon` |
| `Exploration/MagicDoors.md` | `02_Systems/Expedition/`: `M_DoorPurchase`, `M_DoorLifecycle`, `M_ReturnPressure`; anti-downtime rules → `_ExpeditionSystem`; `Props/Interactive/` (`E_MagicDoor`, `E_ExitPortal`, `E_AetherChute`) |
| `Exploration/Realms.md` | `04_Locations/_WorldMap.md` (directory, unlock order); `L01_VerdantCorruption`, `L02_PyroclasticTrench`, `L03_AstralQuarry`, `L04_FrostbiteCavern`; Realm Structure, Lifetime and Per-Opening Variation → `02_Systems/Expedition/M_RealmInstancing` |
| `Exploration/ResourceGathering.md` | `02_Systems/Expedition/`: `M_Harvesting`, `M_NodeSpawning`; nodes → `03_Entities/Props/ResourceNodes/`; yields → `06_Balancing/Expedition.md` |
| `Exploration/Mobs.md` | `03_Entities/Mobs/_MobRoster` (categories, archetypes, roster); `Mobs/Common/` (`E_BrambleStalker`, `E_FireSalamander`, `E_VoidSlime`, `E_FrostWraith`); `Mobs/ApexGuardians/` (`E_VerdantElder`, `E_PyroclasticApex`, `E_AstralSovereign`, `E_FrostWyrm`); Spawning and Realm Pressure → `02_Systems/Expedition/M_MobSpawning`, `M_RealmPressure`; health, damage, drops → `06_Balancing/Mobs.md` |
| `../UIDesign/Mailbox/LetterCommissionBoard.md` | `05_UI/Screens/UI_LetterCommissionBoard.md` |
| `../UIDesign/Workstations/AssemblyBenchUI.md` | `05_UI/World/UI_AssemblyBench.md` |

## Inbound references to update

- `README.md`: structure tree, Quick Navigation tables, Documentation Standards.
- `TechnicalDesign/**`: `> **Design:**` header lines (the technical side's own
  layout is decided by `docs-technical-design`).
- `DevelopmentPhases/**`: "Required sources" links.
- `Guidelines/AssetsNaming.md` §2: the "Docs counterpart" column.
- `Guidelines/ModelingGuidelines.md`: Game context link.
