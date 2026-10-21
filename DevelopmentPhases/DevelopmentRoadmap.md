# Armotheca - Development Roadmap & Production Phases

## Overview
This roadmap establishes the phased production plan for *Armotheca*, structured to validate the core loop as early as possible, establish robust multiplayer netcode, and scale content toward the endgame Uber-Weapon experience.

Design references: [Master GDD](../GDD/MasterGDD.md) · Technical references: [Technical Overview](../TechnicalDesign/TechnicalOverview.md)

**Tech stack:** Unity 6.3 LTS · GameObjects (no ECS) · FishNet + FishySteamworks (player-hosted) · uGUI · Input System.

---

## Phase Breakdown

```
[Phase 1: Core Loop Prototype] (Months 1–3)
       |
       v
[Phase 2: Co-op Networking & Client System] (Months 4–6)
       |
       v
[Phase 3: Multi-Realms & Full Progression] (Months 7–10)
       |
       v
[Phase 4: Uber-Weapon Ritual & Polish] (Months 11–13)
```

---

## Phase 1: Core Loop & Workshop Prototype
**Duration:** Months 1–3
**Focus:** Proving the common mechanics, physical crafting and 2-piece assembly in single-player.

### Deliverables:
1. **Common Mechanics:**
   - [Movement](../GDD/Common/Movement.md): kinematic third-person walk, sprint, jump, roll.
   - [Object Interaction](../GDD/Common/ObjectInteraction.md): instant (pick up, drop, place, take, use) and continuous (hold-to-work, harvest) interactions; hands / weapon slot / backpack carry model.
   - [Combat](../GDD/Common/Combat.md): sword swing chain and wand/staff magic orb, player health and downed state.
2. **2-Piece Modular Assembly:** Functional assembly bench combining 1 Foundation + 1 Payload module (Swords, Wands, Staves). Weapons carry only **Quality (1–100)** and **Base Damage**.
3. **Manual Processing Workstations:**
   - Smelting Forge & Anvil (with optional timing strike mini-game).
   - Woodworking Lathe & Chisel.
   - Arcane Distillation Extractor.
4. **First Magic Door (Verdant Corruption):**
   - 1 single test realm (may be pre-loaded for the prototype).
   - 2 harvestable node types (Arcane Oak, Iron Vein).
   - 1 hostile creature type (Bramble Stalker).
5. **Basic Letter Mailbox:** Generates standard Adventurers Guild letters with verification of delivered items.
6. **Networking Spike:** Host a FishNet session over FishySteamworks on Unity 6.3 LTS, join via a Steam lobby, disconnect/rejoin, and measure latency and bandwidth with 4 players (see [Technical Overview](../TechnicalDesign/TechnicalOverview.md)). Gameplay code is written host-authoritative from day one even while testing single-player.

### Success Criteria:
- A player can take a letter, step into a door, chop wood, mine ore, kill 1 mob, return to the shop, smelt a blade, carve a hilt, assemble a sword, and deliver it for gold in under 5 minutes.

---

## Phase 2: Multiplayer Netcode & Customer Archetypes
**Duration:** Months 4–6
**Focus:** 2–4 player cooperative synchronization and full commission mechanics.

### Deliverables:
1. **Multiplayer Architecture (FishNet host mode over Steam):**
   - Steam lobby flow: host, invite friends, join, drop-in / drop-out.
   - Network synchronization for movement, carried items, station states, workbench sockets and combat.
   - Seamless Magic Door transitions between workshop and realm instances.
   - Cooperative continuous interactions (multiple helpers) and revive.
2. **Customer Archetype Engine:**
   - Implementation of all 5 archetypes (Adventurers Guild, Arcane Academy, City Garrison, SOS Emergency, Collectors).
   - Expiration timers, dynamic reputation changes, and failure penalties.
3. **Door Entry & Realm Pressure:**
   - Door entry window (90 s), expedition membership and member re-entry; always-open Exit Portal in realms.
   - Realm Pressure escalation (rising mob spawns) as the force that ends expeditions; no time limit inside realms.
   - Aether Drop-Chute for remote item transfer from realms.
4. **UI/HUD Implementation:**
   - Diegetic Assembly Bench hologram previews.
   - Letter Commission Board UI with pinned contract tracking.

### Success Criteria:
- 4 players can play in a session: 2 diving into a door while 2 remain in the workshop, communicating and delivering orders seamlessly without desync.

---

## Phase 3: Realms, Expanded Roster & Progression
**Duration:** Months 7–10
**Focus:** Content scaling, all 4 realms, and shop tier progression.

### Deliverables:
1. **Full Realm Suite (4 Magic Doors):**
   - *Verdant Corruption* (Wood/Beast)
   - *Pyroclastic Trench* (Fire Ore/Salamanders)
   - *Astral Quarry* (Star Metal/Void Slimes)
   - *Frostbite Cavern* (Ice Ore/Frost Wraiths)
   - Per-opening node and mob spawning with letter guarantees.
2. **Apex Creature Encounters:**
   - Unique Apex Guardians in each realm guarding the 4 Primordial Catalysts.
3. **Workshop Tier Evolution:**
   - Tier 1 (Rustic Forge) → Tier 2 (Arcane Atelier) → Tier 3 (Astral Armotheca).
   - Visual shop expansions, new station slots, and enhanced capacity.
   - Magic Door purchases (tier requirement + gold price) at the Threshold of Portals.
4. **Economy & Reputation Balancing:**
   - Tuning gold sinks, upgrade costs, and commission pricing curves.

### Success Criteria:
- Players can progress through Tier 1 to Tier 3 over multiple game sessions, defeating Apex Guardians and stocking rare catalysts.

---

## Phase 4: The Uber-Weapon Ritual, Polish & Launch
**Duration:** Months 11–13
**Focus:** Endgame climax, accessibility, audio-visual polish, and QA.

### Deliverables:
1. **The Grand Crucible (Uber-Weapon Ritual):**
   - Synchronized 4-phase forging sequence requiring full team coordination.
   - Campaign victory cinematic, stat recap, and transition to Endless Prestige Mode.
2. **Audio & Visual Polish:**
   - Soundscapes for all realms, tactile forging SFX, and adaptive music system.
   - Particle effects for elemental materials and Flawless glow.
3. **Accessibility & Quality of Life:**
   - Full gamepad remapping, colorblind options for element icons, toggleable mini-game automation for accessibility.
4. **Steam Deck & Performance Optimization:**
   - Optimization targeting steady 60 FPS on mid-spec PCs and Steam Deck.
5. **Engine:** Production runs on Unity 6.3 LTS; the planned move to 6.7 LTS happens after the Phase 2 milestone (see the Technical Overview upgrade plan), not during launch polish.

### Success Criteria:
- Complete end-to-end campaign playthrough from opening the shop to forging the Uber-Weapon with zero critical blockers.
