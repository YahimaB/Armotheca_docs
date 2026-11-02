# Armotheca - Game Design Documentation

## Overview

**Armotheca** is a cooperative multiplayer (1–4 players) magical weapon shop simulator and dimensional expedition game. Players operate a workshop situated in a distinct pocket dimension, fulfilling bespoke weapon commissions (swords, wands, staves) delivered via letters. Raw ingredients are gathered through magical doors leading to otherworldly realms filled with harvestable nodes and hostile creatures. Materials undergo manual processing and modular 2-part assembly to fulfill client demands, steadily upgrading the workshop toward the ultimate goal: forging a legendary **Uber-Weapon**.

---

## Documentation Structure

Files and folders use `Capitalized_Words` separated by underscores, with an underscore after any prefix (`Order_System.md`, `Technical_Design/`, `Phase_1_Core_Loop.md`); acronyms stay uppercase (`Master_GDD.md`). Mechanics are split by **zone** and documented twice: the game-design side in `GDD/` and the implementation side in `Technical_Design/`, at the same relative path.

```
Armotheca_docs/
├── README.md                          # Documentation hub (this file)
├── GDD/                               # Game design: what & why
│   ├── Master_GDD.md                  # Vision, core loop, pillars, mechanics index
│   ├── Common/                        # Applies everywhere
│   │   ├── Movement.md                # Walk, sprint, jump, roll
│   │   ├── Object_Interaction.md      # Instant & continuous interactions, carry model
│   │   └── Combat.md                  # Sword swings, wand/staff magic orb, health & downed
│   ├── Shop/                          # The workshop
│   │   ├── Weapon_Crafting.md         # 2-piece assembly, Quality + Base Damage
│   │   ├── Resource_Processing.md     # Manual workstations & mini-games
│   │   ├── Order_System.md            # Letters, criteria, customer archetypes
│   │   ├── Shop_Progression.md        # Workshop tiers & currencies
│   │   └── Uber_Weapon.md             # Catalysts & the 4-phase ritual
│   └── Exploration/                   # Behind the Magic Doors
│       ├── Magic_Doors.md             # Door purchase, entry window, exit portal, drop-chute
│       ├── Realms.md                  # Realm directory & structure
│       ├── Resource_Gathering.md      # Node spawning & harvesting
│       └── Mobs.md                    # Creatures, spawning, drops, Apex Guardians
├── Technical_Design/                  # Implementation: how
│   ├── Technical_Overview.md          # Targets, architecture principles, shared types
│   ├── Common/                        # Movement.md · Object_Interaction.md · Combat.md
│   ├── Shop/                          # Weapon_Crafting.md · Resource_Processing.md · Order_System.md
│   │                                  # Shop_Progression.md · Uber_Weapon.md
│   └── Exploration/                   # Magic_Doors.md · Realms.md · Resource_Gathering.md · Mobs.md
├── Guidelines/
│   ├── Assets_Naming.md               # Unity Assets folder structure, asset prefixes, UI element vocabulary
│   └── Modeling_Guidelines.md         # 3D style, poly budgets, textures, export rules for artists
├── Visual_Design/
│   └── References/                    # Reference screenshots (Alchemy_Factory, Goblin_Cleanup)
├── UI_Design/
│   ├── Mailbox/
│   │   └── Letter_Commission_Board.md # Nexus dispatch & order ticket UI
│   └── Workstations/
│       └── Assembly_Bench_UI.md       # Diegetic 2-piece assembly bench UI
└── Development_Phases/
    └── Development_Roadmap.md         # 4-phase production plan & milestones
```

---

## Core Game Pillars

1. **Cooperative Synergy (Hands-On Teamwork):**
   - High communication loop between workshop artisans and expedition foragers.
   - Strictly manual crafting and processing at launch (no automation), emphasizing physical co-op coordination.
2. **Modular Craftsmanship (Depth Without Overcomplication):**
   - Exact 2-component weapon modularity (Blades + Hilts for swords; Shafts + Cores for wands and staves).
   - Weapons carry only two stats for now: **Quality (1–100)** and **Base Damage**.
3. **Dimensional Contract Cycle (Risk vs. Commission):**
   - Gameplay driven by incoming letters with varying constraints (urgency, quality, materials).
   - Magic Doors are bought with gold once the shop reaches the right tier; expeditions through them are self-paced, tactical resource-gathering runs tailored to active commissions, with rising danger instead of a timer.
4. **Tangible Endgame Aspiration (The Uber-Weapon):**
   - A clear, overarching win condition beyond endless wealth accumulation.

---

## Quick Navigation

### 📋 [Master Game Design Document](GDD/Master_GDD.md)
Game overview, design philosophy, core loop, pillars and the mechanics index.

### 🧭 Common Mechanics
| Mechanic | Design | Technical |
|---|---|---|
| Movement | [GDD](GDD/Common/Movement.md) | [Tech](Technical_Design/Common/Movement.md) |
| Object Interaction | [GDD](GDD/Common/Object_Interaction.md) | [Tech](Technical_Design/Common/Object_Interaction.md) |
| Combat | [GDD](GDD/Common/Combat.md) | [Tech](Technical_Design/Common/Combat.md) |

### 🔨 Shop Mechanics
| Mechanic | Design | Technical |
|---|---|---|
| Weapon Crafting | [GDD](GDD/Shop/Weapon_Crafting.md) | [Tech](Technical_Design/Shop/Weapon_Crafting.md) |
| Resource Processing | [GDD](GDD/Shop/Resource_Processing.md) | [Tech](Technical_Design/Shop/Resource_Processing.md) |
| Order System | [GDD](GDD/Shop/Order_System.md) | [Tech](Technical_Design/Shop/Order_System.md) |
| Shop Progression | [GDD](GDD/Shop/Shop_Progression.md) | [Tech](Technical_Design/Shop/Shop_Progression.md) |
| Uber-Weapon | [GDD](GDD/Shop/Uber_Weapon.md) | [Tech](Technical_Design/Shop/Uber_Weapon.md) |

### 🚪 Exploration Mechanics
| Mechanic | Design | Technical |
|---|---|---|
| Magic Doors | [GDD](GDD/Exploration/Magic_Doors.md) | [Tech](Technical_Design/Exploration/Magic_Doors.md) |
| Realms | [GDD](GDD/Exploration/Realms.md) | [Tech](Technical_Design/Exploration/Realms.md) |
| Resource Gathering | [GDD](GDD/Exploration/Resource_Gathering.md) | [Tech](Technical_Design/Exploration/Resource_Gathering.md) |
| Mobs | [GDD](GDD/Exploration/Mobs.md) | [Tech](Technical_Design/Exploration/Mobs.md) |

### ⚙️ [Technical Overview](Technical_Design/Technical_Overview.md)
Tech stack (Unity 6.3 LTS · GameObjects, no ECS · FishNet + FishySteamworks, player-hosted · uGUI), performance targets, networking setup, architecture principles, shared types, engine upgrade plan.

### 📐 Guidelines
- **[Assets Structure & Naming](Guidelines/Assets_Naming.md)** - `Assets/` folder layout, zone tokens, asset and data-asset prefixes, code naming, UI element vocabulary (Screen, Window, Panel, Container, Card, Label, Value...) and UI layers.
- **[3D Modeling Guidelines](Guidelines/Modeling_Guidelines.md)** - Target look, reference breakdown (`Visual_Design/References`), polygon budgets, LODs, textures, pivots, modular weapon sockets and delivery checklist.

### 🖥️ UI & Interaction Design
- **[Letter Commission Board UI](UI_Design/Mailbox/Letter_Commission_Board.md)** - Mailbox layout, ticket queue, archetype styling, urgency feedback.
- **[Assembly Bench Diegetic UI](UI_Design/Workstations/Assembly_Bench_UI.md)** - World-space sockets, live Quality / Base Damage preview, incompatibility cues.

### 🚀 Production & Milestones
- **[Development Roadmap](Development_Phases/Development_Roadmap.md)** - Phased plan from Phase 1 prototype through Phase 4 polish and launch.

---

## Documentation Standards

**GDD documents** (game-design side) contain:
1. **Design Intent & Player Experience Goals**
2. **References to Shipped Titles** (*Moonlighter*, *PlateUp!*, *Potion Craft*, *Dave the Diver*, *Monster Hunter*, ...)
3. **Rules, Flows & Tuning Values** (design-facing numbers, marked as initial values where unproven)
4. **Open Questions**
5. A link to the matching technical document

**Technical_Design documents** (implementation side) contain:
1. **Technical Specifications & Performance Targets** (tick rates, memory, netcode budget)
2. **Architecture & Implementation Approaches** with trade-offs (SOLID/GRASP, MonoBehaviour vs ScriptableObject)
3. **Networking** (authority and synchronization)
4. **Unity C# Reference Code** (interfaces, managers, network-ready events)
5. A link back to the matching GDD document
