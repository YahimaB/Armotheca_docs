# Mobs (Realm Creatures)

> **Zone:** Exploration · **Technical counterpart:** [TechnicalDesign/Exploration/Mobs](../../TechnicalDesign/Exploration/Mobs.md) · **Combat rules:** [Combat](../Common/Combat.md)

## Design Intent

Mobs are the danger and the second resource source of every realm. They threaten players who are busy harvesting, and they drop the organic ingredients — essences, cores, claws — that wand and staff cores require. Mobs are simple, readable enemies built around a few behaviour archetypes, so they work with the deliberately simple sword-and-orb combat.

---

## Player Experience Goals

- **Protect the Gatherers:** Mobs pressure players who are locked into harvesting, making bodyguarding a real role.
- **Readable Threats:** Every attack is telegraphed long enough to roll away.
- **Hunt with Purpose:** Players hunt specific mobs because a letter needs their essence.
- **Rising Pressure:** With no time limit in realms, mobs are what make staying longer a gamble: the realm keeps getting more dangerous for as long as players remain.

---

## References

- **Moonlighter:** Small set of readable dungeon enemies, each dropping themed crafting materials.
- **Monster Hunter:** Monster parts directly defining crafted weapon identity.
- **Deep Rock Galactic:** Swarms escalating while the team works an objective.

---

## Mob Categories

| Category | Role | Typical Drops | Where |
|---|---|---|---|
| **Minor Fauna** | Weak, often in groups | Pelts, Claws, Fangs | Outer Grounds |
| **Elemental Beasts** | Tougher, elemental attacks | Cores, Essences, Ichor | Deep Grounds |
| **Apex Guardian** | Boss, one per realm | Primordial Catalyst | Apex Arena |

### Behaviour Archetypes
Every mob uses one of a small set of behaviours:

| Archetype | Behaviour | Counter |
|---|---|---|
| **Chaser** | Closes distance, telegraphed lunge/bite | Roll through the lunge, swing |
| **Ranged** | Keeps distance, fires slow projectiles | Close in with a sword or trade orbs |
| **Swarm** | Weak, many, surrounds players | Sword arcs hit several at once |
| **Ambusher** | Hides near nodes, wakes when a node is harvested | Guard harvesters |

---

## Realm Roster

| Realm | Mob | Category | Archetype | Notable Drop |
|---|---|---|---|---|
| Verdant Corruption | Bramble Stalker | Minor Fauna | Chaser / Ambusher | Thorned Pelt, Verdant Essence |
| Pyroclastic Trench | Fire Salamander | Elemental Beast | Ranged | Salamander Ichor (Fire) |
| Astral Quarry | Void Slime | Minor Fauna | Swarm | Void Slime Core (Arcane) |
| Frostbite Cavern | Frost Wraith | Elemental Beast | Chaser | Wraith Essence (Frost) |

Additional mobs per realm are expected; this roster is the minimum for each realm.

---

## Spawning Rules

- Each realm layout has hand-placed **mob spawn zones** by band (Outer / Deep). No mobs spawn in the Entry area.
- **On door open:** Each zone rolls whether it is active and which mob group (from the band's weighted table) it spawns.
- **Ambushers** spawn hidden next to some nodes and wake when harvesting starts.
- **Letter guarantee:** If an active letter needs a mob drop available in this realm, at least one group containing that mob spawns.
- Mobs do not leave the realm and never follow players through the Exit Portal or the door.

### Realm Pressure (Escalation)
Realm Pressure replaces the old door timer as the force that ends expeditions. It starts at level 0 when the realm is created and rises by one level every 60 seconds while the realm is occupied. It never resets during an expedition, including when members step out and back in.

Each level:
- Shortens the interval between wandering-mob spawns.
- Raises the number of mobs allowed alive at once (up to a performance cap).
- From level 3, Deep Grounds groups can spawn in the Outer Grounds, so even the area near the Exit Portal stops being safe.

The HUD shows the current pressure level as a growing distortion around the screen edges and a realm-wide audio cue on every level-up, so players feel the danger rising without a countdown.

| Rule | Initial Value |
|---|---|
| Active spawn zones per band (on creation) | 50–70% |
| Pressure level-up | every 60 s occupied |
| Wandering spawn interval | 30 s at level 0, −5 s per level, minimum 8 s |
| Max simultaneous mobs | 12 at level 0, +2 per level, hard cap 20 |
| Deep groups spawning in Outer Grounds | from level 3 |

---

## Health, Damage & Drops

- Each mob type has fixed **health** and fixed **attack damage** defined in data. Player weapons deal their Base Damage per hit (see [Combat](../Common/Combat.md)).
- On death a mob drops items from its drop table (guaranteed main drop plus chance-based extras). Drops behave like node yields: walk over to collect into the backpack, or pick up into hands.
- Small mobs are staggered by sword hits; Elemental Beasts and Apex Guardians are not.

---

## Apex Guardians

- One per realm, in the Apex Arena, guarding that realm's Primordial Catalyst (see [Uber-Weapon](../Shop/UberWeapon.md)).
- Multi-phase fights with telegraphed area attacks designed for 1–4 players; health scales with player count.
- Defeating a Guardian drops its catalyst; Guardians do not respawn once their catalyst is taken (except in Prestige mode).

---

## Open Questions

- Should mob health scale with player count, or should more mobs spawn instead?
- Should Realm Pressure also raise mob damage or health at high levels, or is more mobs enough to push teams home?
- Do mobs attack workshop-bound items (e.g. destroy dropped cargo), or only players?
- Should elemental beasts resist or be weak to elements once element effects exist?
