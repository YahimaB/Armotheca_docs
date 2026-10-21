# Magic Doors

> **Zone:** Exploration · **Technical counterpart:** [TechnicalDesign/Exploration/MagicDoors](../../TechnicalDesign/Exploration/MagicDoors.md) · **Destinations:** [Realms](Realms.md)

## Design Intent

The Magic Doors are the resource lifeline of *Armotheca*. The shop does not rest on ordinary geography; its Threshold of Portals opens onto tears in reality. Each door leads to a bite-sized, dangerous pocket realm.

Doors are **bought, not granted**: each door becomes available at a shop tier and is then purchased with gold, so expanding the team's reach is a deliberate investment. Once opened, a door only stays open **for entering** for a short window; there is **no time limit inside the realm**. Expeditions end when the team decides to come home — pushed by letter deadlines, a full backpack and a realm that grows more hostile the longer they stay.

---

## Player Experience Goals

- **Investing in Reach:** Buying a new door is a visible milestone and a real choice of where to spend gold.
- **Targeted Expeditions:** Teams pick a door based on active letters (*"We need a Frost Core and Iron Ore — open the Frostbite Cavern!"*).
- **Commit to the Dive:** Once the entry window closes, the team inside is the team that has to make it work; late arrivals cannot pile in.
- **Self-Paced Return:** Players choose when to leave. The pressure comes from the core loop (deadlines, capacity, rising danger), not an arbitrary countdown.
- **Room for Big Fights:** Without a timer, deep areas and Apex Guardian fights fit inside a normal expedition.

---

## References

- **Lethal Company:** Short extraction runs where greed versus safety drives the decision to leave.
- **Deep Rock Galactic:** Escalating swarms that make staying longer increasingly dangerous.
- **Moonlighter:** A gate between the safe shop and the dangerous dungeon, crossed many times per day.

---

## Door Unlocks (Shop Tier + Gold Price)

A door is unlocked when **both** conditions are met:
1. The workshop has reached the door's **required tier** (the door appears in the Threshold of Portals, sealed, with a price plaque).
2. The team **pays the door's gold price** from the shared treasury (hold-to-confirm interaction on the plaque, 1 s, to avoid accidental purchases).

| Door | Realm | Required Tier | Gold Price |
|---|---|---|---|
| Door 1 | Verdant Corruption | Tier 1 | Free (owned at start) |
| Door 2 | Pyroclastic Trench | Tier 2 | 1,000 |
| Door 3 | Astral Quarry | Tier 3 | 2,000 |
| Door 4 | Frostbite Cavern | Tier 3 | 2,000 |

- Tier upgrade gold costs were reduced so the **total spend per tier stays the same as before** (see [Shop Progression](../Shop/ShopProgression.md)); gold is now split between the upgrade and the doors it makes available.
- Tier 3 makes two doors available at once, so the team chooses which realm to invest in first.
- Commissions only request materials obtainable through doors the team owns (see [Order System](../Shop/OrderSystem.md)).

---

## Door Lifecycle

```
 [LOCKED] --(tier reached + gold paid)--> [READY] --(open)--> [ENTRY OPEN] --(90 s)--> [IN PROGRESS] --(realm empty)--> [COOLDOWN] --(20 s)--> [READY]
                                                                                 \___(nobody inside when window closes)___/
```

1. **Ready:** The door is owned and closed. Any player can open it (instant interaction). A fresh realm is generated (see [Realms](Realms.md)).
2. **Entry Open (90 s):** Anyone can step through, and players may come and go freely. Every player who enters becomes an **expedition member** for this run.
3. **In Progress:** The door seals **for entry**. Only expedition members can pass back in (for example after dropping cargo in the workshop or being ejected). Other players see a shimmering sealed surface and the names of the members inside. If nobody is inside when the window closes, the expedition ends at once.
4. **Realm empty:** When the last player leaves the realm (by any route) after the entry window has closed, the expedition ends and the realm is discarded.
5. **Cooldown (20 s):** The door rests, then returns to Ready and can be opened into a newly generated realm.

### Leaving a Realm
- An **Exit Portal** stands in every realm's Entry area and is **always open**. Using it (instant interaction) returns the player to the workshop in front of the door.
- Being **downed and bleeding out** also returns the player to the workshop, dropping their backpack and hands contents in the realm (see [Combat](../Common/Combat.md)). As an expedition member they may re-enter to recover the dropped cargo — as long as at least one teammate is still inside.
- If a solo player (or the last member inside) steps out, the realm empties and the expedition ends.

---

## What Pushes Players Home

There is no expedition timer. Instead:
1. **Letter deadlines** keep ticking in the workshop (90–360 s per letter).
2. **Backpack capacity** fills up (see [Object Interaction](../Common/ObjectInteraction.md)).
3. **Realm Pressure** rises the longer the realm is occupied: more frequent and stronger mob spawns with no upper limit on danger (see [Mobs](Mobs.md)).
4. **Depletion:** Harvested nodes do not regrow, so a realm gradually runs out of easy resources (see [Resource Gathering](ResourceGathering.md)).

---

## Anti-Downtime Features

1. **Aether Drop-Chute:** Near the realm entry point, a chute instantly sends deposited resources to a receiving basket in the workshop. With entry sealed after 90 s, the chute is the main way to supply the workshop mid-run without ending anyone's expedition.
2. **Member Re-entry:** Expedition members can still step out and back in while a teammate holds the realm, so carrying cargo home or grabbing a better weapon does not end the run.
3. **Multiple Owned Doors:** Each owned door runs its own expedition. A workshop player who missed one entry window can open a different owned door instead.
4. **Self-Paced Length:** Teams can make quick 2-minute supply runs or long deep dives; letter deadlines naturally keep most runs short.

---

## Open Questions

- Is 90 s the right entry window, or should it scale with the number of players still in the workshop?
- Should non-members ever be able to join after the window closes (e.g. a paid "breach" using Emergency Tokens) to keep emergency reinforcement possible?
- Should door prices scale in Prestige mode, or should doors stay owned permanently across prestige runs?
