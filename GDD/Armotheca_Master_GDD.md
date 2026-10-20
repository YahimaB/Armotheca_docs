# Armotheca - Master Game Design Document (GDD)

## 1. Executive Summary

- **Project Name:** Armotheca
- **Genre:** Cooperative Magic Weapon Shop Simulator / Dimensional Extraction Action
- **Platform:** PC (Steam), Controller & Keyboard/Mouse Support
- **Player Count:** 1–4 Players (Drop-in / Drop-out Cooperative Multiplayer)
- **Target Engine:** Unity 2022.3 LTS / Unity 6
- **Target Audience:** Fans of cooperative crafting/simulation (*PlateUp!*, *Overcooked*, *Ale & Tale Tavern*) and hybrid shop/action games (*Moonlighter*, *Dave the Diver*, *Potion Craft*).

---

## 2. High Concept & Setting

### 2.1 The Setting: The Armotheca Pocket Realm
The game takes place inside **The Armotheca** — an ancient, extradimensional emporium floating in the ethereal void. The shop does not sit on a mundane city street; instead, it is an arcane sanctuary connected to the multiverse. 

The shop features:
- **The Mailbox Nexus:** A magical pneumatic tube/portal where commission letters arrive from various factions and individuals across the planes.
- **The Workshop Hall:** Processing stations (furnaces, arcane distillation apparatus, grinding wheels, assembly benches) where materials are refined and joined.
- **The Threshold of Portals (Magic Doors):** An archway hall containing doors that open into distinct alien biomes (elemental mines, overgrown corrupted groves, spectral catacombs).

### 2.2 Core Pitch
Players run an artisanal weapon forge, taking bespoke commissions for magical swords, wands, and staves. Instead of passive queue management, players must manually process raw materials, venture into perilous pocket dimensions to harvest mineral nodes and hunt magical monsters, assemble weapons via a **2-piece modular system**, and dispatch completed orders before deadlines expire — all while working toward forging the mythic **Uber-Weapon**.

---

## 3. Core Gameplay Loop

```
+-------------------------------------------------------------+
|                     1. COMMISSION PHASE                     |
|  - Letters arrive via the Nexus Mailbox                     |
|  - Team reviews client requirements, deadlines & rewards     |
|  - Strategy discussion: select which orders to fulfill      |
+------------------------------+------------------------------+
                               |
                               v
+-------------------------------------------------------------+
|                    2. EXPEDITION PHASE                      |
|  - Step through Magic Doors into dimensional biomes         |
|  - Mine resource nodes (ore veins, arcane timber)          |
|  - Hunt & defeat monsters for organic magical ingredients   |
|  - Return to workshop through the gateway                   |
+------------------------------+------------------------------+
                               |
                               v
+-------------------------------------------------------------+
|                    3. REFINEMENT & CRAFT                    |
|  - Manual processing (no automation): Smelt, carve, refine  |
|  - 2-Piece modular assembly (Hilt+Blade or Shaft+Core)      |
|  - Optional timing mini-games for quality bonuses           |
+------------------------------+------------------------------+
                               |
                               v
+-------------------------------------------------------------+
|                    4. DISPATCH & PROGRESSION                |
|  - Package and dispatch weapons via the Mailbox Nexus       |
|  - Collect gold, client reputation, and rare catalysts     |
|  - Upgrade workshop stations, unlock new Doors              |
|  - Contribute materials to the ultimate UBER-WEAPON forge   |
+-------------------------------------------------------------+
```

---

## 4. Key Design Pillars & Constraints

### 4.1 Modularity: Exactly 2 Components per Weapon
To keep the mental model clean, snappy, and bug-resistant during early production, all weapons are strictly assembled from two components:
- **Swords:** `[Hilt]` (Ergonomics, weight, grip bonus) + `[Blade]` (Damage type, elemental affinity, sharpness).
- **Wands (1-Handed):** `[Short Shaft]` (Cast speed, cooldown) + `[Core]` (Spell payload, primary element).
- **Staves (2-Handed):** `[Long Shaft]` (Mana capacity, area radius) + `[Core]` (Spell payload, primary element).

### 4.2 Manual Labor (No Automation at Launch)
- All transformation of raw ingredients into refined components requires physical presence and player action at workstations.
- Players pick up, transport, heat, strike, extract, and combine materials.
- This creates physical chaos, communicative comedy, and rewarding tactile mastery in co-op.

### 4.3 Pacing & Anti-Downtime Design
To ensure players staying in the workshop are never stranded waiting for expedition players:
1. **Short Portal Expeditions:** Dives into Magic Doors are calibrated for **2–4 minute focused sorties**, not long 30-minute dungeon crawls.
2. **Shop Preparation & Asynchronous Work:** While combatants gather mob drops, workshop players refine previously stockpiled wood, smelt ores, or prepare standard hilts/shafts.
3. **Omni-Role Flexibility:** Any player can traverse doors or work the benches at any time.

---

## 5. Customer Archetypes (Commission System)

Commissions arrive in written letters via the Nexus Mailbox. Clients belong to 5 distinct archetypes:

| Archetype | Preferred Weaponry | Key Demand | Reward Profile | Penalty for Failure |
|---|---|---|---|---|
| **Adventurers Guild** | Standard Swords & Wands | Balanced stats, high durability | Moderate Gold, Guild Rep | Low (mild rep loss) |
| **Arcane Academy** | High-tier Wands & Staves | High purity cores, zero defect | High Gold, Rare Blueprints | High (heavy rep loss) |
| **City Garrison** | Bulk Uniform Swords | Exact identical batches (2–4 units) | Bulk Gold Bonus | Medium |
| **SOS / Emergency** | Any (Elemental counters) | Very tight timer (1–2 minutes) | 2x–3x Gold, Emergency Tokens | None (order expires) |
| **Eccentric Collectors**| Exotic / Hybrid Combos | Rare mob parts, unusual traits | Uber-Weapon Catalysts | Rejection of weapon |

---

## 6. The Endgame: The Uber-Weapon

The overarching narrative and mechanical goal of the campaign is the restoration / creation of **The Primordial Armament** (The Uber-Weapon).

1. **Catalyst Collection:** The Uber-Weapon requires 4 unique Legendary Catalysts, each locked behind the deepest tier of each dimensional door realm (requiring defeating Apex Guardians).
2. **Multi-Stage Crucible:** The Uber-Weapon cannot be forged in one click. It requires all 4 players to participate simultaneously in a synchronized multi-station forging ritual.
3. **Endgame Payoff:** Once forged, the Uber-Weapon serves as the ultimate triumph, unlocking Endless/Prestige mode with mutated portals, celestial clients, and speed-run leaderboards.

---

## 7. Technical Target Specifications

- **Target Framerate:** Solid 60 FPS on mid-tier hardware (GTX 1660 / Ryzen 5 3600).
- **Networking Model:** Client-Server / Host-Client using **Unity Netcode for GameObjects** or **Fish-Net**.
- **Physics & Interaction:** Kinematic character controller with trigger-based physical interaction (snap-to-station inventory sockets).
- **Modularity Architecture:** Pure ScriptableObject-driven data architecture with decoupled component stats calculation.
