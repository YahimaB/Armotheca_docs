# Resource Spawning & Gathering

> **Zone:** Exploration · **Technical counterpart:** [TechnicalDesign/Exploration/ResourceGathering](../../TechnicalDesign/Exploration/ResourceGathering.md)

## Design Intent

Resources are the reason to go through a door. Static **resource nodes** (ore veins, arcane trees, crystal clusters) are harvested with a simple continuous interaction, while **mob drops** come from combat (see [Mobs](Mobs.md)). Node placement changes every time a door opens, so teams scout and split up instead of running the same memorized route, and the backpack limit forces choices about what to bring home.

---

## Player Experience Goals

- **Targeted Harvesting:** Players know which realm and which band of it to visit for the material a letter needs.
- **Readable Nodes:** Each node type has a distinct silhouette and colour, readable from across the realm.
- **Satisfying Strikes:** Every tool strike has a crunch, a chip effect and visible damage on the node.
- **Meaningful Capacity:** Backpack space is limited; the Aether Chute and teammates relieve the pressure.

---

## References

- **Deep Rock Galactic:** Mining veins while teammates hold off attackers.
- **Valheim:** Readable resource nodes with satisfying per-hit feedback.
- **Lethal Company:** Limited carry capacity driving prioritization during extraction.

---

## Resource Sources

| Source Type | Gathering Method | Primary Yield | Used For |
|---|---|---|---|
| **Mineral Vein (Node)** | Harvest (hold) — 3–5 strikes | Ores, Crystals, Flux | Blades (smelting) |
| **Arcane Flora (Node)** | Harvest (hold) — 3–4 strikes | Heartwood, Ancient Bark | Hilts, Wand/Staff Shafts |
| **Minor Fauna (Mob)** | Combat | Pelts, Claws, Fangs | Hilt grips, Collector requests |
| **Elemental Beasts (Mob)** | Combat | Cores, Essences, Ichor | Wand & Staff Magical Cores |

---

## Gathering Nodes

- Harvesting is a **continuous interaction** (see [Object Interaction](../Common/ObjectInteraction.md)): the player holds interact and the character performs repeated strikes with a contextual tool (pickaxe for veins, axe for flora). Each strike is one hit.
- When a node's hits are exhausted, it breaks and drops its yield on the ground around it. Items go to the backpack automatically when the harvester walks over them, or can be picked up into hands by anyone.
- Up to **2 players** can harvest the same node together; each adds strikes.
- Releasing the button or getting hit interrupts harvesting; hits already dealt are kept.
- Harvested nodes **do not regrow** during the same expedition. Since realms have no time limit, depletion is one of the forces that ends a run: the longer a team stays, the further they must travel for the next node while Realm Pressure rises (see [Mobs](Mobs.md)).

### Yields
- Each node type has a drop table: guaranteed main material plus chance-based extras (e.g. an Iron Vein always yields Iron Ore, sometimes Flux).
- Rare node variants (glowing) give the same material in larger quantity or a rare extra.

---

## Spawning Rules

Each realm layout is hand-made with **node spawn points** grouped by band (Outer / Deep). When a door opens:

1. Each band rolls how many of its spawn points are active (e.g. 60–80% of points).
2. Each active point picks a node type from the band's weighted table (Outer: common veins/trees; Deep: rare veins, crystal clusters).
3. A small chance turns a node into its rare variant.
4. **Letter guarantee:** If an active letter requires a node material that this realm can provide, at least one node of that type is guaranteed to spawn.

| Rule | Initial Value |
|---|---|
| Active spawn points per band | 60–80% |
| Rare variant chance | 10% |
| Respawn during an expedition | None |
| Guaranteed node for active letters | At least 1 per required material |

---

## Open Questions

- Should nodes have a quality grade that feeds into processing quality?
- Is the contextual tool enough, or should tools be physical items players must bring (and can forget)?
- Should yields scale with player count to keep 4-player sessions supplied?
