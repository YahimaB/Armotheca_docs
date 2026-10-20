# Armotheca - Game Design Documentation

## Overview

**Armotheca** is a cooperative multiplayer (1–4 players) magical weapon shop simulator and dimensional expedition game. Players operate a workshop situated in a distinct pocket dimension, fulfilling bespoke weapon commissions (swords, wands, staves) delivered via letters. Raw ingredients are gathered through magical doors leading to otherworldly biomes filled with harvestable nodes and hostile creatures. Materials undergo manual processing and modular 2-part assembly to fulfill client demands, steadily upgrading the workshop toward the ultimate goal: forging a legendary **Uber-Weapon**.

---

## Documentation Structure

```
Armotheca_docs/
├── README.md                                    # Documentation Hub & Architecture Overview
├── GDD/
│   └── Armotheca_Master_GDD.md                 # Master Game Design Document
├── Mechanics/
│   ├── Crafting/
│   │   └── ModularWeaponCrafting.md             # 2-Piece Modular Crafting System
│   ├── Orders/
│   │   └── CustomerOrderSystem.md               # Letters, Commission Dispatch & Customer Archetypes
│   ├── Shop/
│   │   └── ResourceProcessing.md                # Manual Workstations & Refinement (No Automation)
│   ├── Exploration/
│   │   └── MagicDoors.md                        # Dimensional Portals, Nodes & Mob Hunting
│   └── Progression/
│       └── ShopAndUberWeapon.md                 # Shop Tier Progression & Endgame Uber-Weapon
├── UI_Design/
│   ├── Mailbox/
│   │   └── LetterCommissionBoard.md             # Nexus Dispatch & Order Ticket UI
│   └── Workstations/
│       └── AssemblyBenchUI.md                   # Diegetic 2-Piece Assembly Bench UI
└── Development_Phases/
    └── DevelopmentRoadmap.md                    # 4-Phase Production Plan & Milestones
```

---

## Core Game Pillars

1. **Cooperative Synergy (Hands-On Teamwork):**
   - High communication loop between workshop artisans and expedition foragers.
   - Strictly manual crafting and processing at launch (no automation), emphasizing physical co-op coordination.
2. **Modular Craftsmanship (Depth Without Overcomplication):**
   - Exact 2-component weapon modularity (Blades + Hilts for swords; Shafts + Cores for wands and staves).
   - Combinatorial freedom allows players to tailor weapons to unique customer demands.
3. **Dimensional Contract Cycle (Risk vs. Commission):**
   - Gameplay driven by incoming letters with varying constraints (urgency, quality, rare traits).
   - Expeditions into magical doors are bite-sized, tactical resource-gathering runs tailored to active commissions.
4. **Tangible Endgame Aspiration (The Uber-Weapon):**
   - A clear, overarching win condition beyond endless wealth accumulation.

---

## Quick Navigation

### 📋 [Master Game Design Document](GDD/Armotheca_Master_GDD.md)
Comprehensive game overview, design philosophy, core loop breakdown, multiplayer architecture, and project parameters.

### 🔨 Core Systems & Mechanics

- **[2-Piece Modular Weapon Crafting](Mechanics/Crafting/ModularWeaponCrafting.md)**
  - Anatomy of swords, wands, and staves; socketing rules; stats calculation; assembly table logic; C# implementation.
- **[Customer Order & Letter System](Mechanics/Orders/CustomerOrderSystem.md)**
  - Letter mailbox mechanic; 5 distinct customer archetypes; deadlines; reputation impact; C# commission pipeline.
- **[Manual Resource Processing](Mechanics/Shop/ResourceProcessing.md)**
  - Smelting, woodworking lathe, and arcane extraction stations; optional timing/quality mini-games; physical station gameplay.
- **[Magic Doors & Dimensional Exploration](Mechanics/Exploration/MagicDoors.md)**
  - Instanced realm portals; harvesting nodes vs. slaying mobs; session pacing to prevent workshop downtime.
- **[Shop Progression & The Uber-Weapon](Mechanics/Progression/ShopAndUberWeapon.md)**
  - Workshop tier upgrades; space expansion in the pocket plane; four-phase catalyst forging of the endgame weapon.

### 🖥️ UI & Interaction Design
- **[Letter Commission Board UI](UI_Design/Mailbox/LetterCommissionBoard.md)** - Mailbox layout, ticket queue, archetype styling, urgency feedback.
- **[Assembly Bench Diegetic UI](UI_Design/Workstations/AssemblyBenchUI.md)** - World-space holographic sockets, real-time stat calculation, incompatibility cues.

### 🚀 Production & Milestones
- **[Development Roadmap](Development_Phases/DevelopmentRoadmap.md)** - Phased plan from Phase 1 prototype through Phase 4 polish and launch.

---

## Documentation Standards

Following professional studio practices, all mechanic documents contain:
1. **Design Intent & Player Experience Goals**
2. **References to Shipped Titles** (*Moonlighter*, *PlateUp!*, *Potion Craft*, *Dave the Diver*, *Monster Hunter*)
3. **Technical Specifications & Performance Targets** (60 FPS tick rates, memory, netcode budget)
4. **Architectural Approaches & Trade-offs** (SOLID/GRASP patterns, MonoBehaviour vs ScriptableObject data-driven setups)
5. **Production-Ready Unity C# Code Architecture** (interfaces, managers, network-ready events)
