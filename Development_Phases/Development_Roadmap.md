# Armotheca - Development Roadmap & Production Phases

## Overview
This roadmap establishes the phased production plan for *Armotheca*, structured to validate the core loop as early as possible, establish robust multiplayer netcode, and scale content toward the endgame Uber-Weapon experience.

Design references: [Master GDD](../GDD/Master_GDD.md) · Technical references: [Technical Overview](../Technical_Design/Technical_Overview.md)

**Tech stack:** Unity 6.3 LTS · GameObjects (no ECS) · FishNet + FishySteamworks (player-hosted) · uGUI · Input System.

---

## Networking-First Principle

Adding networking to finished single-player code is harder and more expensive than building it networked from the start, so **every feature in every phase is developed and accepted as networked from its first version**. There is no separate "make it multiplayer" phase.

- **One code path:** Single-player is a FishNet host with no clients. No feature has a single-player-only implementation.
- **Authority from day one:** Follow the [Technical Overview §3](../Technical_Design/Technical_Overview.md): the host owns game state (items, stations, orders, doors, nodes, mobs, damage); clients send intents through `[ServerRpc]` and receive results through `SyncVar` / `SyncList` / `[ObserversRpc]`; only movement is owner-authoritative.
- **Thin network layer:** Rules (quality, assembly, verification, drops) are plain C# without `MonoBehaviour` or FishNet dependencies; `NetworkBehaviour`s only validate intents and replicate results.
- **Deterministic and tick-based:** Randomness uses a host-seeded `System.Random`; timers use FishNet `TimeManager` ticks, never local `Time`.
- **Definition of Done for every feature:**
  - Works with host + at least 1 client (Multiplayer Play Mode / ParrelSync).
  - A late-joining client sees the correct current state.
  - A client disconnecting mid-action leaves no stuck state (locks, sockets, held items).
  - Bandwidth cost is noted when it adds per-tick traffic.
- **Phases 2–4 extend and harden** the network layer (drop-in/out, scale, latency resilience) instead of retrofitting it.

---

## Phase Breakdown

```
[Phase 1: Networked Core Loop Prototype] (Months 1–3)
       |
       v
[Phase 2: Co-op Hardening & Client System] (Months 4–6)
       |
       v
[Phase 3: Multi-Realms & Full Progression] (Months 7–10)
       |
       v
[Phase 4: Uber-Weapon Ritual & Polish] (Months 11–13)
```

---

## Phase 1: Core Loop & Workshop Prototype
**Duration:** Months 1–3 (13 weeks)
**Focus:** Proving the common mechanics, physical crafting and 2-piece assembly in networked co-op (host + clients) from the first week.

**Weekly plan, required sources per week and acceptance checks:** [Phase 1 Weekly Plan](Phase_1_Core_Loop.md).

### Deliverables:
0. **Networking Foundation (Weeks 1–3):** FishNet host mode over FishySteamworks on Unity 6.3 LTS, Steam lobby join, disconnect/rejoin, networked player movement, and the networking spike (latency and bandwidth with 4 players, see [Technical Overview](../Technical_Design/Technical_Overview.md)) as a go/no-go gate before gameplay work.
1. **Common Mechanics:**
   - [Movement](../GDD/Common/Movement.md): kinematic third-person walk, sprint, jump, roll.
   - [Object Interaction](../GDD/Common/Object_Interaction.md): instant (pick up, drop, place, take, use) and continuous (hold-to-work, harvest) interactions; hands / weapon slot / backpack carry model.
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

Every deliverable above is synchronized for host and clients as it is built (see [Networking-First Principle](#networking-first-principle)).

### Success Criteria:
- A team can take a letter, step into a door, chop wood, mine ore, kill 1 mob, return to the shop, smelt a blade, carve a hilt, assemble a sword, and deliver it for gold in under 5 minutes — in a 2-player Steam session, with a 4-player session completing the same loop without desync.

---

## Phase 2: Co-op Hardening & Customer Archetypes
**Duration:** Months 4–6
**Focus:** Hardening the 2–4 player co-op built in Phase 1 and full commission mechanics. Synchronization of movement, items, stations, sockets, combat and door transitions already exists from Phase 1; this phase makes it robust at scale.

### Deliverables:
1. **Co-op Hardening (FishNet host mode over Steam):**
   - Drop-in / drop-out mid-session with full late-join state for every system (workshop, open realms, letters, treasury).
   - Polished Steam lobby flow: invites, join-in-progress, reconnect after a dropped connection.
   - Several realms open at once with players split between the workshop and different realms.
   - Latency resilience: playtests under simulated 150 ms / packet loss; decide on FishNet prediction or lag compensation for combat if needed.
   - Bandwidth and desync audit with 4 players across all Phase 1 and Phase 2 systems.
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
