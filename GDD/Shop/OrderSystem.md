# Order System (Customer Letters & Commissions)

> **Zone:** Shop · **Technical counterpart:** [TechnicalDesign/Shop/OrderSystem](../../TechnicalDesign/Shop/OrderSystem.md) · **UI:** [Letter Commission Board](../../UIDesign/Mailbox/LetterCommissionBoard.md)

## Design Intent

The Order System governs the commercial pulse and narrative context of *Armotheca*. Instead of faceless customers lining up at a counter, orders arrive as **commission letters** through the shop's Mailbox Nexus. Each letter embodies a client faction, explicit requirements (weapon type, element, minimum quality tier), a deadline, and stakes. This turns shop operations from inventory stockpiling into focused, tactical problem-solving for the team.

---

## Player Experience Goals

- **Analytical Prioritization:** Players gather around the mailbox to evaluate incoming contracts, debate feasibility, and coordinate material requirements.
- **Narrative Personality:** Flavor text and specific client demands make the extradimensional world feel alive and reactive.
- **Dramatic Pacing (SOS Moments):** High-urgency emergency orders trigger frantic coordination, contrasting with relaxed, perfectionist Academy commissions.
- **Consequential Choices:** Accepting an order stakes reputation; failing it or delivering subpar work affects the workshop's standing.

---

## References

- **Papers, Please:** Verifying several criteria against a strict set of rules.
- **Overcooked / PlateUp!:** Order tickets with expiration bars, rewarding fast execution.
- **Potion Craft:** Customers requesting specific effects, with bonus reputation for exceeding expectations.
- **Dave the Diver:** VIP events requiring specific dishes by a deadline, unlocking progression on success.

---

## Commission Criteria

Every letter specifies a combination of:

| Criterion | Example | Required? |
|---|---|---|
| Weapon type | Sword / Wand / Staff | Always |
| Minimum quality tier | Masterwork (Quality 75+) | Always |
| Element | Frost | Optional |
| Quantity | 3 identical units | Optional (default 1) |
| Specific component material | Ancient Bog-Wood Long Shaft | Optional |

Weapon stats are limited to Quality and Base Damage (see [Weapon Crafting](WeaponCrafting.md)); letters do not request any other stat.

---

## Customer Archetypes

```
+--------------------------------------------------------------------------+
|                        COMMISSION LETTER ARCHETYPES                      |
+--------------------------------------------------------------------------+
| 1. ADVENTURERS GUILD | High volume, Standard+ quality, steady gold & rep |
| 2. ARCANE ACADEMY    | Zero tolerance for defects, rare cores, blueprints|
| 3. CITY GARRISON     | Identical batch orders (2-4 units), bulk profits  |
| 4. SOS DISPATCH      | Extreme time pressure (<120s), high-risk windfall |
| 5. COLLECTOR NOBLES  | Exotic material combinations, Uber catalysts      |
+--------------------------------------------------------------------------+
```

### 1. Adventurers Guild (The Bread & Butter)
- **Profile:** Pragmatic monster hunters needing dependable gear.
- **Demand Pattern:** 1 Sword or 1 Wand; accepts `Standard` or `Masterwork`; general elements.
- **Timing:** Relaxed (4–6 minutes).
- **Consequence:** Steady cash flow; failure incurs negligible reputation loss.

### 2. Arcane Academy (The Perfectionists)
- **Profile:** Elitist scholars and archmages researching planar anomalies.
- **Demand Pattern:** Staves and Wands only; strict demand for `Masterwork` or `Flawless` and specific arcane cores.
- **Tolerance:** **Zero tolerance for `Crude` components.** Delivering anything below the requested tier results in immediate contract rejection and a severe reputation penalty.
- **Rewards:** Unlocks rare research blueprints and portal stabilizer formulas.

### 3. City Garrison (The Mass Contractors)
- **Profile:** Quartermasters supplying frontline battalions.
- **Demand Pattern:** Batch orders (e.g. *3x Iron Swords, Fire element, Standard+*).
- **Gameplay Impact:** Pushes the workshop into an assembly-line mindset where players pre-smelt and mass-forge identical components.
- **Rewards:** Large lump-sum gold payouts.

### 4. SOS Emergency Dispatch (The Adrenaline Spike)
- **Profile:** Desperate distress calls magically intercepted from ongoing battles.
- **Demand Pattern:** *"A cave troll is breaking our line! Send an Acid Blade within 90 seconds!"*
- **Timing:** 60 to 120 seconds maximum.
- **Rewards:** 2.5x standard gold, Emergency Tokens (used for instant workshop buffs).
- **Penalty:** None on expiration (they perished or fled); only lost opportunity.

### 5. Eccentric Collectors (The Milestone Givers)
- **Profile:** Interdimensional oligarchs seeking bizarre vanity weapons.
- **Demand Pattern:** Exotic material combos (e.g. *Lightning Core inside an Ancient Bog-Wood Staff*).
- **Rewards:** Modest gold, but **Uber-Weapon Blueprints** and **Prismatic Catalysts**.

---

## Letter Flow & Rules

1. **Arrival:** A letter drops out of the Mailbox Nexus tube onto the board.
2. **Review & Pin:** Players read the letter (instant interaction) and may pin it to the HUD.
3. **Fulfilment:** The team gathers, processes and assembles the requested weapon.
4. **Dispatch:** A player holding the finished weapon uses the Outgoing Tube (instant interaction) and chooses the target letter.
5. **Verification:** The weapon is checked against the letter instantly. Success pays out; failure shows the rejection reason and, depending on the archetype, applies a penalty.

| Rule | Value |
|---|---|
| Max simultaneous letters on the board | 5 |
| Letter lifespan | 90 s (SOS) to 360 s (Standard Guild) |
| Flawless delivery bonus | +50% gold |
| Rejection | Weapon is returned to the player's hands |

---

## Open Questions

- Should letters require explicit acceptance (committing reputation), or is every letter on the board implicitly accepted?
- How are batch orders dispatched — one weapon at a time, or all units together?
- Should orders ever request a minimum Base Damage, or keep criteria purely material/quality based?
