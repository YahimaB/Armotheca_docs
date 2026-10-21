# Armotheca - Master Game Design Document (GDD)

> Game-design overview. Mechanic details live in the zone folders below; implementation lives in [TechnicalDesign](../TechnicalDesign/TechnicalOverview.md).

## 1. Executive Summary

- **Project Name:** Armotheca
- **Genre:** Cooperative Magic Weapon Shop Simulator / Dimensional Extraction Action
- **Platform:** PC (Steam), Controller & Keyboard/Mouse Support
- **Player Count:** 1–4 Players (Drop-in / Drop-out Cooperative Multiplayer)
- **Target Engine:** Unity 6.3 LTS (full stack: [Technical Overview](../TechnicalDesign/TechnicalOverview.md))
- **Multiplayer:** Player-hosted sessions over Steam (one player is both server and client)
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
Players run an artisanal weapon forge, taking bespoke commissions for magical swords, wands, and staves. Instead of passive queue management, players must manually process raw materials, venture into perilous pocket dimensions to harvest resource nodes and hunt magical monsters, assemble weapons via a **2-piece modular system**, and dispatch completed orders before deadlines expire — all while working toward forging the mythic **Uber-Weapon**.

---

## 3. Core Gameplay Loop

```
+-------------------------------------------------------------+
|                     1. COMMISSION PHASE                     |
|  - Letters arrive via the Nexus Mailbox                     |
|  - Team reviews client requirements, deadlines & rewards    |
|  - Strategy discussion: select which orders to fulfill      |
+------------------------------+------------------------------+
                               |
                               v
+-------------------------------------------------------------+
|                    2. EXPEDITION PHASE                      |
|  - Step through Magic Doors into dimensional realms         |
|  - Harvest resource nodes (ore veins, arcane timber)        |
|  - Hunt & defeat monsters for organic magical ingredients   |
|  - Return to workshop through the gateway                   |
+------------------------------+------------------------------+
                               |
                               v
+-------------------------------------------------------------+
|                    3. REFINEMENT & CRAFT                    |
|  - Manual processing (no automation): smelt, carve, refine  |
|  - 2-piece modular assembly (Hilt+Blade or Shaft+Core)      |
|  - Optional timing mini-games for quality bonuses           |
+------------------------------+------------------------------+
                               |
                               v
+-------------------------------------------------------------+
|                    4. DISPATCH & PROGRESSION                |
|  - Package and dispatch weapons via the Mailbox Nexus       |
|  - Collect gold, client reputation, and rare catalysts      |
|  - Upgrade workshop tiers, buy new Magic Doors              |
|  - Contribute materials to the ultimate UBER-WEAPON forge   |
+-------------------------------------------------------------+
```

---

## 4. Key Design Pillars & Constraints

### 4.1 Modularity: Exactly 2 Components per Weapon
To keep the mental model clean, snappy, and bug-resistant during early production, all weapons are strictly assembled from two components:
- **Swords:** `[Hilt]` (foundation) + `[Blade]` (payload).
- **Wands (1-Handed):** `[Short Shaft]` (foundation) + `[Core]` (payload).
- **Staves (2-Handed):** `[Long Shaft]` (foundation) + `[Core]` (payload).

### 4.2 Weapon Stats Are Locked to Two Values
For now every weapon carries exactly two stats, and this stat set stays fixed until a deliberate design revision:
- **Quality (1–100)** — produced by manual processing, averaged from both components.
- **Base Damage** — a constant defined by the payload material (Blade or Core).

No speed, durability, mana, area or other numeric stats exist at this stage. See [Weapon Crafting](Shop/WeaponCrafting.md).

### 4.3 Manual Labor (No Automation at Launch)
- All transformation of raw ingredients into refined components requires physical presence and player action at workstations.
- Players pick up, transport, heat, strike, extract, and combine materials.
- This creates physical chaos, communicative comedy, and rewarding tactile mastery in co-op.

### 4.4 Pacing & Anti-Downtime Design
To ensure players staying in the workshop are never stranded waiting for expedition players:
1. **Self-Paced but Pressured Expeditions:** There is no time limit inside realms. Instead, letter deadlines, backpack capacity and steadily rising Realm Pressure push teams home, so most runs stay short (2–4 minutes) while deep dives remain possible. See [Magic Doors](Exploration/MagicDoors.md).
2. **Entry Window:** A door accepts new entrants only for a short window after opening; afterwards only that expedition's members can pass. Teams decide together who goes in.
3. **Shop Preparation & Asynchronous Work:** While combatants gather mob drops, workshop players refine previously stockpiled wood, smelt ores, or prepare standard hilts/shafts. The Aether Drop-Chute keeps raw materials flowing mid-run.
4. **Omni-Role Flexibility:** Any player can work the benches at any time, or open another owned door if they missed an entry window.

---

## 5. Mechanics Index (by Zone)

Mechanics are grouped by the zone of the game where they apply.

| Zone | Scope | Documents |
|---|---|---|
| **Common** | Applies everywhere (workshop and realms) | [Movement](Common/Movement.md) · [Object Interaction](Common/ObjectInteraction.md) · [Combat](Common/Combat.md) |
| **Shop** | The workshop pocket realm | [Weapon Crafting](Shop/WeaponCrafting.md) · [Resource Processing](Shop/ResourceProcessing.md) · [Order System](Shop/OrderSystem.md) · [Shop Progression](Shop/ShopProgression.md) · [Uber-Weapon](Shop/UberWeapon.md) |
| **Exploration** | Behind the Magic Doors | [Magic Doors](Exploration/MagicDoors.md) · [Realms](Exploration/Realms.md) · [Resource Gathering](Exploration/ResourceGathering.md) · [Mobs](Exploration/Mobs.md) |

---

## 6. Customer Archetypes (Summary)

Commissions arrive in written letters via the Nexus Mailbox. Full rules: [Order System](Shop/OrderSystem.md).

| Archetype | Preferred Weaponry | Key Demand | Reward Profile | Penalty for Failure |
|---|---|---|---|---|
| **Adventurers Guild** | Standard Swords & Wands | Standard or better quality | Moderate Gold, Guild Rep | Low (mild rep loss) |
| **Arcane Academy** | High-tier Wands & Staves | High quality cores, zero defect | High Gold, Rare Blueprints | High (heavy rep loss) |
| **City Garrison** | Bulk Uniform Swords | Exact identical batches (2–4 units) | Bulk Gold Bonus | Medium |
| **SOS / Emergency** | Any (elemental counters) | Very tight timer (1–2 minutes) | 2x–3x Gold, Emergency Tokens | None (order expires) |
| **Eccentric Collectors** | Exotic / Hybrid Combos | Rare mob parts, unusual materials | Uber-Weapon Catalysts | Rejection of weapon |

---

## 7. The Endgame: The Uber-Weapon (Summary)

The overarching narrative and mechanical goal of the campaign is the creation of **The Primordial Armament** (the Uber-Weapon). Full rules: [Uber-Weapon](Shop/UberWeapon.md).

1. **Catalyst Collection:** 4 unique Primordial Catalysts, each guarded by an Apex Guardian in the deepest part of a realm.
2. **Multi-Stage Crucible:** A synchronized multi-station forging ritual that needs the whole team.
3. **Endgame Payoff:** Campaign victory, then Endless/Prestige mode with mutated portals, celestial clients, and speed-run leaderboards.

---

## 8. Technical Targets

Performance, networking and architecture targets are owned by [TechnicalDesign/TechnicalOverview](../TechnicalDesign/TechnicalOverview.md).
