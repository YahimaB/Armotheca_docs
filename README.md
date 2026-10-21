# Armotheca - Game Design Documentation

## Overview

**Armotheca** is a cooperative multiplayer (1–4 players) magical weapon shop simulator and dimensional expedition game. Players operate a workshop situated in a distinct pocket dimension, fulfilling bespoke weapon commissions (swords, wands, staves) delivered via letters. Raw ingredients are gathered through magical doors leading to otherworldly realms filled with harvestable nodes and hostile creatures. Materials undergo manual processing and modular 2-part assembly to fulfill client demands, steadily upgrading the workshop toward the ultimate goal: forging a legendary **Uber-Weapon**.

---

## Documentation Structure

Files and folders use CamelCase. Mechanics are split by **zone** and documented twice: the game-design side in `GDD/` and the implementation side in `TechnicalDesign/`, at the same relative path.

```
Armotheca_docs/
├── README.md                          # Documentation hub (this file)
├── GDD/                               # Game design: what & why
│   ├── MasterGDD.md                   # Vision, core loop, pillars, mechanics index
│   ├── Common/                        # Applies everywhere
│   │   ├── Movement.md                # Walk, sprint, jump, roll
│   │   ├── ObjectInteraction.md       # Instant & continuous interactions, carry model
│   │   └── Combat.md                  # Sword swings, wand/staff magic orb, health & downed
│   ├── Shop/                          # The workshop
│   │   ├── WeaponCrafting.md          # 2-piece assembly, Quality + Base Damage
│   │   ├── ResourceProcessing.md      # Manual workstations & mini-games
│   │   ├── OrderSystem.md             # Letters, criteria, customer archetypes
│   │   ├── ShopProgression.md         # Workshop tiers & currencies
│   │   └── UberWeapon.md              # Catalysts & the 4-phase ritual
│   └── Exploration/                   # Behind the Magic Doors
│       ├── MagicDoors.md              # Door purchase, entry window, exit portal, drop-chute
│       ├── Realms.md                  # Realm directory & structure
│       ├── ResourceGathering.md       # Node spawning & harvesting
│       └── Mobs.md                    # Creatures, spawning, drops, Apex Guardians
├── TechnicalDesign/                   # Implementation: how
│   ├── TechnicalOverview.md           # Targets, architecture principles, shared types
│   ├── Common/                        # Movement.md · ObjectInteraction.md · Combat.md
│   ├── Shop/                          # WeaponCrafting.md · ResourceProcessing.md · OrderSystem.md
│   │                                  # ShopProgression.md · UberWeapon.md
│   └── Exploration/                   # MagicDoors.md · Realms.md · ResourceGathering.md · Mobs.md
├── Guidelines/
│   ├── AssetsNaming.md                # Unity Assets folder structure, asset prefixes, UI element vocabulary
│   └── ModelingGuidelines.md          # 3D style, poly budgets, textures, export rules for artists
├── VisualDesign/
│   └── References/                    # Reference screenshots (AlchemyFactory, GoblinCleanup)
├── UIDesign/
│   ├── Mailbox/
│   │   └── LetterCommissionBoard.md   # Nexus dispatch & order ticket UI
│   └── Workstations/
│       └── AssemblyBenchUI.md         # Diegetic 2-piece assembly bench UI
└── DevelopmentPhases/
    └── DevelopmentRoadmap.md          # 4-phase production plan & milestones
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

### 📋 [Master Game Design Document](GDD/MasterGDD.md)
Game overview, design philosophy, core loop, pillars and the mechanics index.

### 🧭 Common Mechanics
| Mechanic | Design | Technical |
|---|---|---|
| Movement | [GDD](GDD/Common/Movement.md) | [Tech](TechnicalDesign/Common/Movement.md) |
| Object Interaction | [GDD](GDD/Common/ObjectInteraction.md) | [Tech](TechnicalDesign/Common/ObjectInteraction.md) |
| Combat | [GDD](GDD/Common/Combat.md) | [Tech](TechnicalDesign/Common/Combat.md) |

### 🔨 Shop Mechanics
| Mechanic | Design | Technical |
|---|---|---|
| Weapon Crafting | [GDD](GDD/Shop/WeaponCrafting.md) | [Tech](TechnicalDesign/Shop/WeaponCrafting.md) |
| Resource Processing | [GDD](GDD/Shop/ResourceProcessing.md) | [Tech](TechnicalDesign/Shop/ResourceProcessing.md) |
| Order System | [GDD](GDD/Shop/OrderSystem.md) | [Tech](TechnicalDesign/Shop/OrderSystem.md) |
| Shop Progression | [GDD](GDD/Shop/ShopProgression.md) | [Tech](TechnicalDesign/Shop/ShopProgression.md) |
| Uber-Weapon | [GDD](GDD/Shop/UberWeapon.md) | [Tech](TechnicalDesign/Shop/UberWeapon.md) |

### 🚪 Exploration Mechanics
| Mechanic | Design | Technical |
|---|---|---|
| Magic Doors | [GDD](GDD/Exploration/MagicDoors.md) | [Tech](TechnicalDesign/Exploration/MagicDoors.md) |
| Realms | [GDD](GDD/Exploration/Realms.md) | [Tech](TechnicalDesign/Exploration/Realms.md) |
| Resource Gathering | [GDD](GDD/Exploration/ResourceGathering.md) | [Tech](TechnicalDesign/Exploration/ResourceGathering.md) |
| Mobs | [GDD](GDD/Exploration/Mobs.md) | [Tech](TechnicalDesign/Exploration/Mobs.md) |

### ⚙️ [Technical Overview](TechnicalDesign/TechnicalOverview.md)
Tech stack (Unity 6.3 LTS · GameObjects, no ECS · FishNet + FishySteamworks, player-hosted · uGUI), performance targets, networking setup, architecture principles, shared types, engine upgrade plan.

### 📐 Guidelines
- **[Assets Structure & Naming](Guidelines/AssetsNaming.md)** - `Assets/` folder layout, zone tokens, asset and data-asset prefixes, code naming, UI element vocabulary (Screen, Window, Panel, Container, Card, Label, Value...) and UI layers.
- **[3D Modeling Guidelines](Guidelines/ModelingGuidelines.md)** - Target look, reference breakdown (`VisualDesign/References`), polygon budgets, LODs, textures, pivots, modular weapon sockets and delivery checklist.

### 🖥️ UI & Interaction Design
- **[Letter Commission Board UI](UIDesign/Mailbox/LetterCommissionBoard.md)** - Mailbox layout, ticket queue, archetype styling, urgency feedback.
- **[Assembly Bench Diegetic UI](UIDesign/Workstations/AssemblyBenchUI.md)** - World-space sockets, live Quality / Base Damage preview, incompatibility cues.

### 🚀 Production & Milestones
- **[Development Roadmap](DevelopmentPhases/DevelopmentRoadmap.md)** - Phased plan from Phase 1 prototype through Phase 4 polish and launch.

---

## Documentation Standards

**GDD documents** (game-design side) contain:
1. **Design Intent & Player Experience Goals**
2. **References to Shipped Titles** (*Moonlighter*, *PlateUp!*, *Potion Craft*, *Dave the Diver*, *Monster Hunter*, ...)
3. **Rules, Flows & Tuning Values** (design-facing numbers, marked as initial values where unproven)
4. **Open Questions**
5. A link to the matching technical document

**TechnicalDesign documents** contain:
1. **Technical Specifications & Performance Targets** (tick rates, memory, netcode budget)
2. **Architecture & Implementation Approaches** with trade-offs (SOLID/GRASP, MonoBehaviour vs ScriptableObject)
3. **Networking** (authority and synchronization)
4. **Unity C# Reference Code** (interfaces, managers, network-ready events)
5. A link back to the matching GDD document
