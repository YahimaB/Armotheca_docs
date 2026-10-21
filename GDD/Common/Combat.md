# Combat

> **Zone:** Common · **Technical counterpart:** [TechnicalDesign/Common/Combat](../../TechnicalDesign/Common/Combat.md)

## Design Intent

Combat in *Armotheca* is a means to an end: it protects the team while they harvest and it produces mob drops for magical cores. It should be **simple, readable and satisfying**, never a deep action system that competes with the shop for attention. At this stage there are only two attacks, one per weapon family:

- **Sword:** simple melee swings.
- **Wand / Staff:** a magic orb projectile.

Damage comes directly from the weapon's **Base Damage**. Weapon stats are locked to Quality and Base Damage (see [Weapon Crafting](../Shop/WeaponCrafting.md)), so combat has no hidden modifiers to learn.

---

## Player Experience Goals

- **Pick Up and Fight:** A workshop player can grab any sword or wand, run through a door and contribute immediately.
- **Clear Roles Without Classes:** Swords protect miners up close; wands and staves pick off threats from range.
- **Readable Danger:** Enemy attacks are telegraphed so that the roll is the answer, not a guess.
- **Crafting Pride:** Players can wield weapons they forged themselves — the shop and the expedition feed each other.

---

## References

- **Moonlighter:** Small set of weapon types, each with one simple attack pattern, roll as defense.
- **Hades:** Crisp hit feedback (hit-stop, flash, knockback) that makes simple attacks feel strong.
- **Deep Rock Galactic:** Combat as protection for a gathering objective, with hold-to-revive.
- **Enter the Gungeon:** Readable, slow-moving projectiles that can be avoided by rolling.

---

## Weapons in Combat

| Weapon | Handedness | Attack | Damage per Hit |
|---|---|---|---|
| **Sword** | 1-handed | Sword swing chain | Base Damage |
| **Wand** | 1-handed | Magic orb | Base Damage |
| **Staff** | 2-handed | Magic orb | Base Damage |

- **Quality does not change damage at this stage.** A Crude sword and a Flawless sword with the same blade material hit equally hard; quality matters for commissions and payouts.
- **Element has no combat effect at this stage.** It is a material identity used by orders and visuals (e.g. a fire core makes an orange orb).
- Wand and staff share the same orb attack for now; their difference is handedness and visuals (see Open Questions).

---

## Attack: Sword Swing

- **Input:** Attack button with a sword equipped and empty hands.
- **Chain:** Up to **2 swings** (right-to-left, then left-to-right). Pressing attack during the late part of a swing queues the next one; after the second swing the chain resets.
- **Hit area:** A frontal arc in front of the player. One swing can hit **several enemies**, but each enemy at most once per swing.
- **Commitment:** The player slows down heavily during a swing (cannot sprint). Rolling cancels the swing's recovery.
- **Grounded only:** Swords cannot be swung while airborne.
- **Feedback:** Short hit-stop, enemy flash, light knockback, impact sound tied to blade material.

| Parameter | Initial Value |
|---|---|
| Swing windup / active / recovery | 0.10 s / 0.12 s / 0.25 s |
| Arc angle / reach | 120° / 1.8 m |
| Chain input window | last 50% of a swing |
| Knockback | light (staggers small mobs only) |

---

## Attack: Magic Orb (Wand / Staff)

- **Input:** Attack button with a wand or staff equipped and empty hands. Holding the button repeats the cast at the cooldown rate.
- **Projectile:** A glowing orb fires straight in the facing direction (with light aim assist toward the nearest enemy in a narrow cone).
- **Hit:** The orb stops at the **first enemy or wall** it touches and deals Base Damage to that enemy only.
- **Mobility:** The player can walk (not sprint) while casting. Orbs can be cast while airborne.
- **No resource cost:** There is no mana at this stage; the cooldown is the only limiter.
- **Feedback:** Orb colour from the core's element, small burst on impact, enemy flash.

| Parameter | Initial Value |
|---|---|
| Cast time | 0.15 s |
| Cooldown between orbs | 0.6 s |
| Orb speed / max range | 14 m/s / 12 m |
| Aim assist cone | 15° |

---

## Health, Damage & Downed State

- **Players** have a health pool (initial value: 100). Mobs deal fixed damage per attack defined in mob data (see [Mobs](../Exploration/Mobs.md)).
- **Invulnerability:** Players are invulnerable during the first part of a roll and briefly after taking a hit (initial value: 0.5 s).
- **Downed:** At 0 health a player becomes *Downed*: they cannot act and a bleed-out timer starts (initial value: 20 s).
  - A teammate can **revive** them with a 3 s continuous interaction (see [Object Interaction](ObjectInteraction.md)). Revived players return at 50% health.
  - If the timer runs out (or a solo player goes down), the player is **ejected to the workshop**: their backpack and hands contents are dropped in the realm; the equipped weapon is kept. As an expedition member they can re-enter to recover the cargo while a teammate is still inside; if nobody is left, the realm and its dropped cargo are gone (see [Magic Doors](../Exploration/MagicDoors.md)).
- **Workshop safety:** No combat happens inside the workshop. Health regenerates fully on returning through a door.
- **Friendly fire:** Off.

---

## Open Questions

- Should wands and staves diverge (e.g. staff orb pierces or is larger) once the weapon stat lock is lifted?
- Should Quality or Element ever influence combat, or remain purely commercial?
- Do players get a starter sword and wand that cannot be sold, so they never enter a realm unarmed?
- Is a heavy / charged sword attack needed for larger mobs, or are swings plus orbs enough?
