# Armotheca - Game Design Documentation

## Overview

**Armotheca** is a cooperative multiplayer (1–4 players) magical weapon shop simulator and dimensional expedition game. Players operate a workshop situated in a distinct pocket dimension, fulfilling bespoke weapon commissions (swords, wands, staves) delivered via letters. Raw ingredients are gathered through magical doors leading to otherworldly realms filled with harvestable nodes and hostile creatures. Materials undergo manual processing and modular 2-part assembly to fulfill client demands, steadily upgrading the workshop toward the ultimate goal: forging a legendary **Uber-Weapon**.

---

## Documentation Structure

Files and folders use `Capitalized_Words` separated by underscores, with an underscore after any prefix (`Order_System.md`, `Technical_Design/`, `Phase_1_Core_Loop.md`); acronyms stay uppercase (`Master_GDD.md`). The docs have four types; Claude's `docs-routing` skill (`.claude/skills/`) decides which type a document belongs to.

- **GDD** — what the player does and why, organised **by type of thing**: features are hubs that link the mechanics, entities, locations and UI they use, and every thing is described in exactly one place. Numbers live only in balancing sheets.
- **Technical_Design** — how it is built in Unity, organised **by code module**: one module = one `Armotheca.<Module>` namespace = one folder, named like its GDD system, with every section traced back to the GDD IDs it implements.
- **Guidelines** — standards every contributor follows.
- **Development_Phases** — when and in what order work happens.

```
Armotheca_docs/
├── README.md                     # Documentation hub (this file)
├── GDD/                          # Game design: what & why
│   ├── 00_Overview/              # Vision, Core_Loop, Glossary, Changelog
│   ├── 01_Features/              # _Feature_List + F01–F07 feature hubs
│   ├── 02_Systems/               # One folder per system: _<System>_System hub + M_ mechanics
│   ├── 03_Entities/              # Player, Mobs, NPCs/Clients, Items, Props (a folder per entity + rosters)
│   ├── 04_Locations/             # _World_Map, L00_Workshop, L01–L04 realms
│   ├── 05_UI/                    # _UI_Flow + Hud/, Screens/, World/ (UI_ docs)
│   └── 06_Balancing/             # All tuning values, one sheet per system
├── Technical_Design/             # Implementation: how
│   ├── Technical_Overview.md     # Stack, targets, architecture principles, upgrade plan, open decisions
│   ├── _Module_Map.md            # Module ↔ namespace ↔ GDD system, entities, UI and features
│   ├── <Module>/                 # Core, Networking, Movement, Interaction, Combat, Crafting, Processing,
│   │                             # Orders, Progression, Endgame, Exploration, UI — _<Module>_Module.md each
│   └── Exploration/              # + topics: Door_Instances, Realm_Loading, Resource_Nodes, Mob_AI
├── Guidelines/
│   ├── Assets_Naming.md          # Unity Assets folder structure, asset prefixes, code naming
│   ├── UI_Composition.md         # UI categories, element vocabulary, GameObject hierarchy, layers
│   ├── Modeling_Guidelines.md    # 3D style, poly budgets, textures, export rules for artists
│   └── Art_Direction/            # Visual_Style, Concept_Art_Workflow + References/ (AF_, GC_ screenshots)
└── Development_Phases/
    ├── Development_Roadmap.md    # 4-phase production plan & milestones
    └── Phase_1_Core_Loop.md      # Phase 1 weekly plan
```

---

## Quick Navigation

### 📋 Game Design
- **[Vision](GDD/00_Overview/Vision.md)** — pitch, setting, pillars and locked constraints.
- **[Core Loop](GDD/00_Overview/Core_Loop.md)** — session, moment-to-moment and meta loops; pacing.
- **[Glossary](GDD/00_Overview/Glossary.md)** — document types and game terms.
- **[Changelog](GDD/00_Overview/Changelog.md)** — dated changes to approved rules and values.

### 🎯 Features
| ID | Feature | Milestone |
|---|---|---|
| [F01_Commissions](GDD/01_Features/F01_Commissions.md) | Commission letters, verification and rewards | Phase 1 |
| [F02_Weapon_Crafting](GDD/01_Features/F02_Weapon_Crafting.md) | Manual processing and 2-piece assembly | Phase 1 |
| [F03_Expeditions](GDD/01_Features/F03_Expeditions.md) | Magic Doors, realms and resource gathering | Phase 1 |
| [F04_Combat](GDD/01_Features/F04_Combat.md) | Sword and orb combat against realm mobs | Phase 1 |
| [F05_Shop_Progression](GDD/01_Features/F05_Shop_Progression.md) | Currencies, workshop tiers and door purchases | Phase 3 |
| [F06_Uber_Weapon](GDD/01_Features/F06_Uber_Weapon.md) | Catalysts, the forging ritual and the endgame | Phase 4 |
| [F07_Co_Op](GDD/01_Features/F07_Co_Op.md) | 1–4 player drop-in / drop-out co-op | Phase 1 |

Full list with priorities: [_Feature_List](GDD/01_Features/_Feature_List.md).

### ⚙️ Systems
| System | Design | Technical | Balancing |
|---|---|---|---|
| Movement | [_Movement_System](GDD/02_Systems/Movement/_Movement_System.md) | [Tech](Technical_Design/Movement/_Movement_Module.md) | [Movement](GDD/06_Balancing/Movement.md) |
| Interaction | [_Interaction_System](GDD/02_Systems/Interaction/_Interaction_System.md) | [Tech](Technical_Design/Interaction/_Interaction_Module.md) | [Interaction](GDD/06_Balancing/Interaction.md) |
| Combat | [_Combat_System](GDD/02_Systems/Combat/_Combat_System.md) | [Tech](Technical_Design/Combat/_Combat_Module.md) | [Combat](GDD/06_Balancing/Combat.md) |
| Crafting | [_Crafting_System](GDD/02_Systems/Crafting/_Crafting_System.md) | [Tech](Technical_Design/Crafting/_Crafting_Module.md) | [Crafting](GDD/06_Balancing/Crafting.md) |
| Processing | [_Processing_System](GDD/02_Systems/Processing/_Processing_System.md) | [Tech](Technical_Design/Processing/_Processing_Module.md) | [Processing](GDD/06_Balancing/Processing.md) |
| Orders | [_Orders_System](GDD/02_Systems/Orders/_Orders_System.md) | [Tech](Technical_Design/Orders/_Orders_Module.md) | [Orders](GDD/06_Balancing/Orders.md) |
| Progression | [_Progression_System](GDD/02_Systems/Progression/_Progression_System.md) | [Tech](Technical_Design/Progression/_Progression_Module.md) | [Progression](GDD/06_Balancing/Progression.md) |
| Endgame | [_Endgame_System](GDD/02_Systems/Endgame/_Endgame_System.md) | [Tech](Technical_Design/Endgame/_Endgame_Module.md) | — |
| Exploration | [_Exploration_System](GDD/02_Systems/Exploration/_Exploration_System.md) | [Tech](Technical_Design/Exploration/_Exploration_Module.md) | [Exploration](GDD/06_Balancing/Exploration.md) |

### 🧩 Entities, Locations & UI
- **Entities:** [E_Player](GDD/03_Entities/Player/E_Player/E_Player.md) · [_Mob_Roster](GDD/03_Entities/Mobs/_Mob_Roster.md) · [_Client_Roster](GDD/03_Entities/NPCs/Clients/_Client_Roster.md) · [_Item_List](GDD/03_Entities/Items/_Item_List.md) · [_Prop_List](GDD/03_Entities/Props/_Prop_List.md)
- **Locations:** [_World_Map](GDD/04_Locations/_World_Map.md) · [L00_Workshop](GDD/04_Locations/L00_Workshop/L00_Workshop.md)
- **UI:** [_UI_Flow](GDD/05_UI/_UI_Flow.md) · [UI_Letter_Commission_Board](GDD/05_UI/World/UI_Letter_Commission_Board.md) · [UI_Assembly_Bench](GDD/05_UI/World/UI_Assembly_Bench.md)

### 🛠️ [Technical Overview](Technical_Design/Technical_Overview.md)
Tech stack (Unity 6.3 LTS · GameObjects, no ECS · FishNet + FishySteamworks, player-hosted · uGUI), performance targets, architecture principles, engine upgrade plan. Modules: [_Module_Map](Technical_Design/_Module_Map.md) · technical-only modules: [Core](Technical_Design/Core/_Core_Module.md), [Networking](Technical_Design/Networking/_Networking_Module.md), [UI](Technical_Design/UI/_UI_Module.md).

### 📐 Guidelines
- **[Assets Structure & Naming](Guidelines/Assets_Naming.md)** - `Assets/` folder layout, zone tokens, asset and data-asset prefixes, code naming.
- **[UI Composition](Guidelines/UI_Composition.md)** - UI categories shared by `GDD/05_UI` and `Prefabs/UI`, element vocabulary (Screen, Window, Panel, Container, Widget, Label, Value...), `<Name>_<ElementType>` GameObject names, UI layers and an example hierarchy.
- **[3D Modeling Guidelines](Guidelines/Modeling_Guidelines.md)** - Target look, reference breakdown (`Guidelines/Art_Direction/References`), polygon budgets, LODs, textures, pivots, modular weapon sockets and delivery checklist.
- **[Visual Style](Guidelines/Art_Direction/Visual_Style.md)** - Element colours shared by models, VFX and UI; home of the UI visual style (fonts, frames, icons).
- **[Concept Art Workflow](Guidelines/Art_Direction/Concept_Art_Workflow.md)** - Concept → T-pose → views stages, prompt settings and templates, common failures; results go to each entity's Art doc ([E_Player_Art](GDD/03_Entities/Player/E_Player/E_Player_Art.md)).

### 🚀 Production & Milestones
- **[Development Roadmap](Development_Phases/Development_Roadmap.md)** - Phased plan from Phase 1 prototype through Phase 4 polish and launch.
- **[Phase 1 Weekly Plan](Development_Phases/Phase_1_Core_Loop.md)** - Weeks, required sources and done criteria for Phase 1.

---

## Documentation Standards

Each document type has a skill with its rules and templates in `.claude/skills/`: `docs-gdd` (GDD templates for features, systems, mechanics, entities, rosters, locations, UI and balancing), `docs-technical-design`, `docs-guidelines` and `docs-development-phases`.
