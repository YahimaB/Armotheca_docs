# Object Interaction

> **Zone:** Common · **Technical counterpart:** [TechnicalDesign/Common/ObjectInteraction](../../TechnicalDesign/Common/ObjectInteraction.md)

## Design Intent

Almost everything players do in *Armotheca* beyond running and fighting is an interaction with an object: picking up ore, snapping a blade into the assembly bench, pumping bellows, chopping a tree, reading a letter, opening a door. A single, consistent interaction model keeps all of these readable and lets the shop and the realms add new objects without inventing new controls.

There are exactly **two kinds of interaction**:

- **Instant** — one press, immediate result (pick up, drop, place, open, read, dispatch).
- **Continuous** — press and hold over time, with visible progress (harvest a node, work a station, revive a teammate).

---

## Player Experience Goals

- **One Button, Clear Outcome:** The interact button always does the most obvious thing for what the player is facing.
- **Always Know What Will Happen:** A short prompt names the action before it happens (`[E] Pick up Iron Ore`, `[Hold E] Pump Bellows`).
- **Physical, Tactile Workshop:** Items exist in the world; players carry them in their hands, set them down, hand them over, and snap them into sockets.
- **Teamwork Through Shared Objects:** Some continuous interactions go faster when more than one player helps, rewarding coordination.

---

## References

- **Overcooked / PlateUp!:** One-button pick up / put down on counters, hold-to-chop progress bars.
- **Ale & Tale Tavern:** Carrying logs and kegs physically through a shared space.
- **Deep Rock Galactic:** Hold-to-revive and hold-to-deposit interactions in co-op.
- **Lethal Company:** Limited carry capacity forcing prioritization during extraction.

---

## Carry Model

Each player has three places to hold things:

| Slot | Holds | Notes |
|---|---|---|
| **Hands** | One world object (raw resource, processed component, finished weapon, letter) | Visible in the character's hands. Blocks roll and attacks while occupied. |
| **Weapon Slot** | One equipped weapon (sword, wand or staff) | Drawn automatically when hands are empty and an attack is pressed. |
| **Backpack** | A small number of raw resources (initial value: 6 slots) | Used during expeditions. Harvested resources go here first; contents are dropped in the realm if the player bleeds out (recoverable while the realm is still occupied). |

- Any weapon picked up from the world goes into the **hands** first (it may be a commission to deliver). A secondary action (`[Q] Equip`) moves it into the weapon slot, swapping the previously equipped weapon into the hands.
- The backpack can be emptied into the Aether Drop-Chute in a realm or into a storage crate in the workshop, one item per press or all at once with a hold.

---

## Instant Interactions

Triggered on button press. Resolve immediately.

| Interaction | Target | Result |
|---|---|---|
| Pick up | Loose item in the world | Item moves to hands |
| Drop | Empty floor (hands full) | Item placed in front of the player |
| Place / Snap | Station socket, counter, crate | Item moves from hands into the socket |
| Take | Filled socket / output tray | Item moves into empty hands |
| Hand over | Teammate with empty hands | Item moves directly between players |
| Open / Use | Door, letter, mailbox, lever | Object-specific action |
| Dispatch | Outgoing mail tube (hands hold a weapon) | Submits the weapon to an order |

---

## Continuous Interactions

Triggered by holding the button. A progress indicator fills over time; releasing the button pauses progress.

| Interaction | Target | Typical Duration | Notes |
|---|---|---|---|
| Harvest | Resource node | 3–5 tool strikes | Each strike is one hit on the node. See [Resource Gathering](../Exploration/ResourceGathering.md). |
| Work station | Bellows, lathe, extractor | 3–6 s | May include an optional timing mini-game. See [Resource Processing](../Shop/ResourceProcessing.md). |
| Revive | Downed teammate | 3 s | See [Combat](Combat.md). |
| Empty backpack | Chute or crate | 1 s | Instant per-item alternative exists. |

### Rules
- **Interruptible:** Moving away, rolling, taking a hit, or releasing the button stops the interaction. Progress is **kept** on the object for a short time (initial value: 5 s) before decaying, so an interrupted player can resume.
- **Cooperative stations:** Objects can declare a maximum number of simultaneous helpers. Each extra helper adds progress speed (initial value: +50% per extra player).
- **Exclusive stations:** Some objects (e.g. the anvil strike) accept only one player at a time; others see a "Busy" prompt.
- **Movement lock:** The player is rooted while interacting but can always cancel with roll or by releasing the button.

---

## Targeting & Prompts

- The game picks the **best target in front of the player** within a short reach (initial value: 1.8 m), favouring the object closest to the facing direction.
- Only one prompt is shown at a time. The prompt shows the button, the verb and the object name.
- Context changes the verb: facing a bench socket with a blade in hand shows `Place Blade`; with empty hands it shows `Take Blade`.
- Invalid actions show a short reason instead of failing silently (`Wrong part for this socket`, `Hands full`).

---

## Open Questions

- Should players be able to throw items (Overcooked-style) to speed up the workshop, or does that undermine the "physical choreography" pillar?
- Backpack size: fixed, or upgradable through shop progression?
- Should the same weapon used for fighting also act as the harvesting tool, or should harvesting stay purely contextual?
