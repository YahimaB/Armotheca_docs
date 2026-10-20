# Armotheca - Development Roadmap & Production Phases

## Overview
This roadmap establishes the phased production plan for *Armotheca*, structured to validate the core loop as early as possible, establish robust multiplayer netcode, and scale content toward the endgame Uber-Weapon experience.

---

## Phase Breakdown

```
[Phase 1: Core Loop Prototype] (Months 1–3)
       |
       v
[Phase 2: Co-op Networking & Client System] (Months 4–6)
       |
       v
[Phase 3: Multi-Biomes & Full Progression] (Months 7–10)
       |
       v
[Phase 4: Uber-Weapon Ritual & Polish] (Months 11–13)
```

---

## Phase 1: Core Loop & Workshop Prototype
**Duration:** Months 1–3  
**Focus:** Proving the physical crafting and 2-piece assembly mechanics in single-player.

### Deliverables:
1. **Player Controller:** Kinematic third-person movement, object pickup, drop, and station snapping.
2. **2-Piece Modular Assembly:** Functional assembly bench combining 1 Foundation + 1 Payload module (Swords, Wands, Staves).
3. **Manual Processing Workstations:**
   - Smelting Forge & Anvil (with optional timing strike mini-game).
   - Woodworking Lathe & Chisel.
   - Arcane Distillation Extractor.
4. **First Dimensional Door (Verdant Corruption):**
   - 1 single test pocket biome.
   - 2 harvestable node types (Arcane Oak, Iron Vein).
   - 1 hostile creature type (Bramble Stalker).
5. **Basic Letter Mailbox:** Generates standard Adventurer Guild letters with verification of delivered items.

### Success Criteria:
- A player can take a letter, step into a door, chop wood, mine ore, kill 1 mob, return to shop, smelt a blade, carve a hilt, assemble a sword, and deliver it for gold in under 5 minutes.

---

## Phase 2: Multiplayer Netcode & Customer Archetypes
**Duration:** Months 4–6  
**Focus:** 2–4 player cooperative synchronization and full commission mechanics.

### Deliverables:
1. **Multiplayer Architecture (Host-Client):**
   - Network synchronization for carried items, station states, and workbench sockets.
   - Seamless dimensional door portal transitions between instances.
2. **Customer Archetype Engine:**
   - Implementation of all 5 archetypes (Adventurers Guild, Arcane Academy, City Garrison, SOS Emergency, Collectors).
   - Expiration timers, dynamic reputation changes, and failure penalties.
3. **Dimensional Instability Mechanic:**
   - 180-second door countdown timer with audio-visual alerts and collapse behavior.
   - Workshop Aether Chute for remote item transfer from dungeons.
4. **UI/HUD Implementation:**
   - Diegetic Assembly Bench hologram previews.
   - Letter Commission Board UI with pinned contract tracking.

### Success Criteria:
- 4 players can play in a session: 2 diving into a door while 2 remain in the workshop, communicating and delivering orders seamlessly without desync.

---

## Phase 3: Biomes, Expanded Roster & Progression
**Duration:** Months 7–10  
**Focus:** Content scaling, all 4 dimensional realms, and shop tier progression.

### Deliverables:
1. **Full Biome Suite (4 Magic Doors):**
   - *Verdant Corruption* (Wood/Beast)
   - *Pyroclastic Trench* (Fire Ore/Salamanders)
   - *Astral Quarry* (Star Metal/Void Slimes)
   - *Frostbite Caverns* (Ice Ore/Frost Wraiths)
2. **Apex Creature Encounters:**
   - Unique mini-bosses in each biome guarding the 4 Primordial Catalysts.
3. **Workshop Tier Evolution:**
   - Tier 1 (Rustic Forge) -> Tier 2 (Arcane Atelier) -> Tier 3 (Astral Armotheca).
   - Visual shop expansions, new station slots, and enhanced capacity.
4. **Economy & Reputation Balancing:**
   - Tuning gold sinks, upgrade costs, and commission pricing curves.

### Success Criteria:
- Players can progress through Tier 1 to Tier 3 over multiple game sessions, defeating biome bosses and stocking rare catalysts.

---

## Phase 4: The Uber-Weapon Ritual, Polish & Launch
**Duration:** Months 11–13  
**Focus:** Endgame climax, accessibility, audio-visual polish, and QA.

### Deliverables:
1. **The Grand Crucible (Uber-Weapon Ritual):**
   - Synchronized 4-phase forging sequence requiring full team coordination.
   - Campaign victory cinematic, stat recap, and transition to Endless Prestige Mode.
2. **Audio & Visual Polish:**
   - Soundscapes for all biomes, tactile forging SFX, and adaptive music system.
   - Particle effects for elemental weapon affinities and masterwork glow.
3. **Accessibility & Quality of Life:**
   - Full gamepad remapping, colorblind options for elemental runes, toggleable mini-game automation for accessibility.
4. **Steam Deck & Performance Optimization:**
   - Optimization targeting steady 60 FPS on mid-spec PCs and Steam Deck.

### Success Criteria:
- Complete end-to-end campaign playthrough from opening shop to forging the Uber-Weapon with zero critical blockers.
