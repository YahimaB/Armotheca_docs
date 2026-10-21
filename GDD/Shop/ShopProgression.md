# Shop Progression (Workshop Tiers)

> **Zone:** Shop · **Technical counterpart:** [TechnicalDesign/Shop/ShopProgression](../../TechnicalDesign/Shop/ShopProgression.md) · **Endgame:** [Uber-Weapon](UberWeapon.md)

## Design Intent

Progression bridges everyday shop management and the campaign's climactic objective. Many simulation and tycoon titles stagnate once wealth outpaces what there is to buy. *Armotheca* frames every commission, gold piece and reputation point as fuel toward a definitive goal — **the forging of the [Uber-Weapon](UberWeapon.md)** — and makes progress visible through workshop expansion, new stations and new Magic Doors.

---

## Player Experience Goals

- **Visual Pride:** Watching the humble stone-and-timber basement evolve into a luminous Astral Forge suspended in starlight.
- **Milestone Anticipation:** Each new door and higher-tier workstation feels like opening a new chapter.
- **Meaningful Spending:** Buying doors separately from tier upgrades turns expansion into choices (which realm first?) rather than automatic unlocks.
- **Purpose-Driven Economy:** Gold and rare materials keep their value right up to the end of the campaign.

---

## References

- **Moonlighter:** Direct shop upgrades funded by dungeon exploration.
- **PlateUp!:** Restaurant layout evolution and technology upgrades between days.
- **Factorio (Rocket Launch):** A tangible macro-objective that unifies all production toward a finale.

---

## Currencies

| Currency | Earned From | Spent On |
|---|---|---|
| **Gold** | Completed commissions | Tier upgrades, Magic Door purchases, station purchases |
| **Reputation** | Completed commissions (lost on failures) | Gate for tier upgrades (not spent) |
| **Emergency Tokens** | SOS commissions | Instant workshop buffs |
| **Blueprints / Catalysts** | Academy and Collector commissions, Apex Guardians | New recipes, the Uber-Weapon |

---

## Workshop Tier Ladder

```
+--------------------------------------------------------------------------+
|                        WORKSHOP PROGRESSION LADDER                       |
+--------------------------------------------------------------------------+
| TIER 1: RUSTIC FORGE       | 1 Door owned, 3 Workbench Stations          |
| TIER 2: ARCANE ATELIER     | +1 Door for sale, Lathe & Extractor         |
| TIER 3: ASTRAL ARMOTHECA   | +2 Doors for sale, The Great Crucible       |
+--------------------------------------------------------------------------+
```

| Workshop Tier | Upgrade Requirement | Unlocked Capabilities | Doors Made Available (price) |
|---|---|---|---|
| **Tier 1: Rustic Forge** | Starting baseline | Basic Anvil, Basic Smelter, Guild commissions. | *Verdant Corruption* (owned at start) |
| **Tier 2: Arcane Atelier** | 1,500 Gold, 200 Rep | Woodworking Lathe, Arcane Extractor, Academy commissions. | *Pyroclastic Trench* (1,000 Gold) |
| **Tier 3: Astral Armotheca** | 6,000 Gold, 800 Rep | Quenching Basins, **The Great Crucible** (Uber-Weapon), Apex Arena gates. | *Astral Quarry* (2,000 Gold), *Frostbite Cavern* (2,000 Gold) |

- Upgrading costs the listed gold; reputation is a threshold and is not consumed.
- **Doors are unlocked by tier + gold price** (see [Magic Doors](../Exploration/MagicDoors.md)): a tier makes doors available, and each door is then bought separately. Tier upgrade costs were lowered so that the full spend per tier is unchanged (Tier 2: 1,500 + 1,000 = 2,500; Tier 3: 6,000 + 2 × 2,000 = 10,000).
- Each upgrade physically expands the workshop: new rooms, more station slots, a larger Threshold of Portals.
- The game signals when an upgrade becomes affordable (HUD hint and a glow on the upgrade ledger in the workshop).

---

## Open Questions

- Tier 1 lists no lathe or extractor, yet every sword needs a hilt and every wand/staff needs a shaft and a core — should Tier 1 include a basic carving bench, or sell starter hilts? (The Phase 1 roadmap already includes the lathe and extractor.)
- Quenching Basins unlock at Tier 3, but the Tier 1 blade pipeline ends with quenching — is the Tier 3 basin an upgrade of a basic one?
- Are station placements fixed per tier, or can players rearrange the workshop (PlateUp!-style)?
