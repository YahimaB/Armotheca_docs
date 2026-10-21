# Realms (Dimensional Biomes)

> **Zone:** Exploration · **Technical counterpart:** [TechnicalDesign/Exploration/Realms](../../TechnicalDesign/Exploration/Realms.md) · **Entered via:** [Magic Doors](MagicDoors.md)

## Design Intent

Each Magic Door opens onto a **separate realm** — a compact, hand-crafted pocket dimension with its own look, resources and monsters. There is no time limit inside a realm (see [Magic Doors](MagicDoors.md)), but the Outer Grounds are kept small enough to cross in under a minute so that quick supply runs stay quick, while the Deep Grounds and the Apex Arena reward teams who commit to a longer dive. Variety comes from four strongly themed realms, each with a fresh resource and mob arrangement every time its door opens.

---

## Player Experience Goals

- **Instant Identity:** One glance through a door tells players which realm it is and what it offers.
- **Fresh but Learnable:** The layout is familiar enough to plan a route; the placement of resources and mobs changes per opening.
- **Purposeful Choice:** Each realm is the main source of specific materials, so active letters dictate which door to open.
- **Escalating Danger:** Deeper areas of a realm hold better materials and stronger mobs.

---

## References

- **Moonlighter:** Themed dungeons with distinct material pools.
- **Deep Rock Galactic:** Biomes that change both resources and threats.
- **Lethal Company:** Small, known maps with randomized loot and monster placement.

---

## Realm Directory

```
+--------------------------------------------------------------------------+
|                         DIMENSIONAL REALM DIRECTORY                      |
+--------------------------------------------------------------------------+
| 1. VERDANT CORRUPTION | Nodes: Bog Oak, Ironwood   | Mobs: Bramble Stalker|
| 2. PYROCLASTIC TRENCH | Nodes: Obsidian, Brimstone | Mobs: Fire Salamander|
| 3. ASTRAL QUARRY      | Nodes: Quartz, Star Metal  | Mobs: Void Slimes    |
| 4. FROSTBITE CAVERN   | Nodes: Glacial Ice-Ore     | Mobs: Frost Wraiths  |
+--------------------------------------------------------------------------+
```

| Realm | Theme | Main Materials | Main Elements | Apex Guardian / Catalyst |
|---|---|---|---|---|
| **Verdant Corruption** | Overgrown corrupted grove | Timber (Bog Oak, Ironwood), Iron Vein, beast parts | Physical, Arcane | Verdant Elder → *Sylvan Spire* |
| **Pyroclastic Trench** | Volcanic chasm | Obsidian, Brimstone, salamander essence | Fire | Pyroclastic Apex → *Ignis Core* |
| **Astral Quarry** | Floating starlit rock | Quartz, Star Metal, void essence | Arcane, Lightning | Astral Sovereign → *Astral Prism* |
| **Frostbite Cavern** | Ice caves | Glacial Ice-Ore, wraith essence | Frost | Frost Wyrm → *Glacial Heart* |

---

## Realm Structure

Every realm follows the same three-band layout:

```
 [ENTRY]  ----->  [OUTER GROUNDS]  ----->  [DEEP GROUNDS]  ----->  [APEX ARENA]
 Arrival point,   Common nodes,            Rare nodes,             Apex Guardian,
 Exit Portal,     weak mobs                stronger mobs           catalyst
 Aether Chute
 (safe zone)
```

- **Entry:** Arrival point, the always-open **Exit Portal** back to the workshop, and the Aether Drop-Chute. No mobs spawn here.
- **Outer Grounds:** Close to the entry; common nodes and minor fauna. Suited to short supply runs.
- **Deep Grounds:** Further away; rare nodes and elemental beasts that drop cores. Reaching them means staying longer under rising Realm Pressure (see [Mobs](Mobs.md)).
- **Apex Arena:** Gated area holding the realm's Apex Guardian. Since realms have no time limit, the fight fits in a normal expedition; the gate opens once the shop reaches Tier 3 (see Open Questions).

### Realm Lifetime
- A realm exists from the moment its door is opened until the **last player leaves it**.
- While at least one player is inside, expedition members can leave and re-enter; dropped cargo stays where it fell.
- When the realm empties it is discarded; the next opening generates a fresh one.

---

## Per-Opening Variation

Each time a door opens, the realm keeps its hand-made layout but re-rolls:
- Which resource nodes appear and where (see [Resource Gathering](ResourceGathering.md)).
- Which mob groups appear and where (see [Mobs](Mobs.md)).
- Optional realm modifiers in Prestige mode (e.g. denser mobs, doubled rare nodes).

---

## Open Questions

- Should the Apex Arena gate open with Tier 3 for every realm, or require a per-realm key (e.g. an Academy portal stabilizer formula)?
- One hand-made layout per realm, or a few layout variants selected at random?
- Should element-specific hazards exist (lava floors, slippery ice) and interact with movement?
