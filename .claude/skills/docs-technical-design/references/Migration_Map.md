# Technical_Design migration map (zone layout → module layout)

Planned destination of every current tech doc. Paths are relative to
`Technical_Design/`. Module names equal the GDD system names in the `docs-gdd`
migration map; confirm both together with the user.

## Order

1. Migrate the GDD docs a module implements first (`docs-gdd`), including their
   `06_Balancing/` tables.
2. Create `_Module_Map.md`, then migrate one module at a time.
3. For each module: replace the `> **Zone:**` header with properties and a
   `> **Design:**` line, add the Scope table, replace restated design values with
   balancing links (keeping technical budgets), add the Data and Events sections,
   set the GDD docs' `Technical:` links, fix inbound links and run the link check.
4. Delete a source file only with the user's confirmation.

## Modules

| Module | Namespace | GDD system | Built from |
| --- | --- | --- | --- |
| Core | `Armotheca.Core` | — | `Technical_Overview.md` §3 data/runtime split, §5 Shared Types |
| Networking | `Armotheca.Networking` | — (serves `F07_Co_Op`) | `Technical_Overview.md` §4 Networking Setup and spike |
| Movement | `Armotheca.Movement` | Movement | `Common/Movement.md` (keep Input Mapping as a section) |
| Interaction | `Armotheca.Interaction` | Interaction | `Common/Object_Interaction.md` |
| Combat | `Armotheca.Combat` | Combat | `Common/Combat.md` |
| Crafting | `Armotheca.Crafting` | Crafting | `Shop/Weapon_Crafting.md` |
| Processing | `Armotheca.Processing` (was `Armotheca.Shop`) | Processing | `Shop/Resource_Processing.md` |
| Orders | `Armotheca.Orders` | Orders | `Shop/Order_System.md` |
| Progression | `Armotheca.Progression` | Progression | `Shop/Shop_Progression.md` |
| Endgame | `Armotheca.Endgame` (split from `Armotheca.Progression`) | Endgame | `Shop/Uber_Weapon.md` |
| Exploration | `Armotheca.Exploration` | Exploration | hub from the shared parts of the four `Exploration/` docs; topics below |
| UI | `Armotheca.UI` | — (serves `05_UI/`) | view notes from `UI_Design/` docs and the "view" parts of each tech doc |

### Exploration topics

| Topic | Built from |
| --- | --- |
| `Exploration/Door_Instances.md` | `Exploration/Magic_Doors.md` |
| `Exploration/Realm_Loading.md` | `Exploration/Realms.md` |
| `Exploration/Resource_Nodes.md` | `Exploration/Resource_Gathering.md` |
| `Exploration/Mob_AI.md` | `Exploration/Mobs.md` (FSM, director, Realm Pressure runtime) |

## Technical_Overview.md after migration

Keeps §1 stack, §2 targets, §3 principles (minus the data split, now in Core),
§4 a one-paragraph networking summary linking Networking, §6 upgrade plan, §8 open
decisions and §9 standards (shortened to a link to this skill's rules). §5 moves to
Core; §7 Code Organization is replaced by `_Module_Map.md`.

## Design values to move out

Known restated values that belong in GDD `06_Balancing/` (the tech doc keeps a
link): letter lifespans and queue size (`Shop/Order_System.md`), Realm Pressure
step, interval and caps (`Exploration/Mobs.md`), and every value marked as a
tuning target in the module's Technical Specifications. Tick rates, bandwidth
and frame budgets stay.

## Inbound references to update

- `README.md`: structure tree, Quick Navigation tables, Documentation Standards.
- GDD docs: `Technical counterpart` / `Technical:` links (done during GDD migration
  or right after the module moves).
- `Development_Phases/**`: "Required sources" links.
- `Guidelines/Assets_Naming.md` §3 `Scripts/` folder list: `Shop/` → `Processing/`,
  add `Endgame/`.
