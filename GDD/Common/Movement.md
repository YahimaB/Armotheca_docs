# Movement

> **Zone:** Common · **Technical counterpart:** [TechnicalDesign/Common/Movement](../../TechnicalDesign/Common/Movement.md)

## Design Intent

Movement is the one verb every player uses every second, in the workshop and in the realms alike. It must feel responsive and readable rather than realistic: a cluttered co-op workshop and a short, dangerous expedition both reward a character that starts, stops and turns instantly. The move set is deliberately small — **walk, sprint, jump, roll** — so that players spend their attention on teammates, orders and monsters, not on the controller.

---

## Player Experience Goals

- **Snappy Control:** The character responds within a frame or two; no long acceleration ramps or slippery stops.
- **Readable Intent:** Teammates can tell at a glance whether someone is walking, sprinting, airborne or rolling.
- **Same Rules Everywhere:** The workshop and the realms share one move set, so nothing has to be relearned when stepping through a door.
- **Carrying Has Weight:** Hauling an item through the workshop is slightly more deliberate than running empty-handed, which creates natural co-op choreography.

---

## References

- **Overcooked / PlateUp!:** Instant top-down movement with a dash, tuned for crowded co-op kitchens.
- **Moonlighter:** Roll as the single defensive tool in both town and dungeon.
- **Hades:** Short, crisp dash with brief invulnerability and a tight cooldown.
- **A Hat in Time:** Forgiving jump (coyote time, input buffering) that never feels unfair.

---

## Move Set

### Walk
- Default locomotion on the movement stick / WASD.
- Character rotates to face the movement direction quickly (no tank controls).
- Analog input scales speed between a slow step and full walk speed.

### Sprint
- Held modifier (`Shift` / left stick click or a shoulder button — final binding in input mapping).
- Higher top speed, slightly wider turning radius to sell momentum.
- **No stamina cost at this stage.** Sprint is freely available so the workshop never feels sluggish (see Open Questions).
- Allowed while carrying an item.

### Jump
- Single jump with a fixed height; no double jump.
- Limited air control so players can correct a jump but not change direction completely.
- **Coyote time** and **jump buffering** make edge jumps and early presses forgiving.
- Used for small ledges, gaps and obstacles in realms; the workshop layout should never *require* jumping to reach a station.

### Roll
- Quick directional burst on a single press, in the input direction (or facing direction with no input).
- Grants a short **invulnerability window** at the start of the roll — the main defensive tool in combat.
- Short cooldown prevents chaining rolls as a faster-than-sprint travel method.
- **Not available while carrying an item** (hands are busy — see [Object Interaction](ObjectInteraction.md)).
- Can be used to cancel the recovery of a sword swing (see [Combat](Combat.md)).

---

## Initial Tuning Targets

Starting values for the first prototype. All values are tunable data, not commitments.

| Parameter | Initial Value |
|---|---|
| Walk speed | 4.0 m/s |
| Sprint speed | 6.5 m/s |
| Carrying speed multiplier | 0.85x (walk and sprint) |
| Jump height | 1.2 m |
| Coyote time / jump buffer | 0.12 s / 0.12 s |
| Roll distance / duration | 3.5 m / 0.45 s |
| Roll invulnerability window | first 0.25 s |
| Roll cooldown | 0.6 s |

---

## State Rules

| State | Can Sprint | Can Jump | Can Roll | Can Attack | Can Interact |
|---|---|---|---|---|---|
| Grounded, empty hands | Yes | Yes | Yes | Yes | Yes |
| Grounded, carrying item | Yes | Yes | No | No | Yes (drop/place) |
| Airborne | — | No | No | Yes (orb only) | No |
| Rolling | — | No | No | No | No |
| In continuous interaction | No | No | Yes (cancels) | No | — |
| Downed | No | No | No | No | No |

---

## Open Questions

- Should sprint and roll eventually draw from a stamina pool, or stay free to keep the workshop frantic but fluid?
- Do realms need any traversal beyond a single jump (ladders, grapples, climbable ledges)?
- Should heavy items (e.g. large ore chunks) apply a stronger carrying penalty than light ones?
