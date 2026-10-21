# Weapon Crafting (2-Piece Modular Assembly)

> **Zone:** Shop · **Technical counterpart:** [TechnicalDesign/Shop/WeaponCrafting](../../TechnicalDesign/Shop/WeaponCrafting.md) · **UI:** [Assembly Bench UI](../../UIDesign/Workstations/AssemblyBenchUI.md)

## Design Intent

The Modular Weapon Crafting System provides an intuitive, tactile method for creating weapons in *Armotheca*. By restricting weapon construction to **strictly two modular components**, the system avoids the combinatorial explosion and UI fatigue of complex 5+ part forging, while still letting material choice and component quality answer diverse customer commissions.

At this stage weapons are deliberately simple: **two stats only — Quality and Base Damage.** All other stats from earlier drafts (speed, durability, mana, area, cast speed, cooldown, balance, damage type) have been removed. This stat set stays fixed until a deliberate design revision.

---

## Player Experience Goals

- **Tactile Satisfaction:** Physically placing a blade and a hilt onto an assembly bench and hammering them together feels physical and rewarding.
- **Readable Combinatorics:** Players can look at a client letter and immediately deduce which 2 parts are needed (e.g. *Frost Core + Willow Short Shaft = Frost Willow Wand*).
- **Quality Differentiation:** Careful processing raises component quality, which decides which clients will accept the weapon and how much they pay.
- **Role Collaboration:** One player specializes in blade forging while another works on hilts, meeting at the assembly bench to finalize the product.

---

## References

- **The Legend of Zelda: Tears of the Kingdom (Fuse):** Intuitive 2-part composition where a base is augmented by an attachment with predictable inheritance.
- **Potion Craft:** Component properties combine into distinct results without UI clutter.
- **PlateUp! / Overcooked:** Physical placement of two prepared ingredients on a counter to form a finished dish.
- **Monster Hunter:** Monster-derived materials visibly defining the identity of the resulting weapon.

---

## Weapon Categories

| Category | Foundation Component | Payload Component |
|---|---|---|
| **Sword** | Hilt | Blade |
| **Wand (1-Handed)** | Short Shaft | Magical Core |
| **Staff (2-Handed)** | Long Shaft | Magical Core |

- The **payload** (Blade or Core) defines the weapon's Base Damage and its Element.
- The **foundation** (Hilt or Shaft) defines the weapon category (sword / wand / staff) and contributes to Quality.
- Any other pairing (e.g. Short Shaft + Blade) is incompatible and rejected by the bench.

---

## Weapon Stats

| Stat | Range | Source | Notes |
|---|---|---|---|
| **Quality** | 1–100 (integer) | Average of both components' quality, rounded | Produced during manual processing. |
| **Base Damage** | Constant per payload material | Payload material data (Blade or Core) | Not modified by quality or by the foundation at this stage. |

### Quality Tiers
Quality tiers are named bands of the single Quality stat. They are used by commissions and by the UI; they do **not** add hidden stat bonuses.

| Tier | Quality Range | Typical Use |
|---|---|---|
| **Crude** | 1–39 | Accepted only by undemanding clients; rejected by the Academy. |
| **Standard** | 40–74 | Default result of processing without mini-games. |
| **Masterwork** | 75–94 | Required by demanding clients; eligible for Guild bonuses. |
| **Flawless** | 95–100 | Top payouts; emits a subtle particle glow. |

### Material Attributes (Not Stats)
Each component also carries non-numeric material identity — its **material** (e.g. Ironwood, Star Metal) and, for payloads, its **Element** (Physical, Fire, Frost, Lightning, Arcane, Holy). These are used by commission criteria, naming and visuals only; they have no numeric effect in combat at this stage.

---

## Assembly Station Gameplay Flow

1. **Placement:** Player A brings a processed *Sun-Forged Blade* and snaps it into the bench's Payload socket.
2. **Placement:** Player B brings an *Ebony Hilt* and snaps it into the Foundation socket.
3. **Locking Action:** Either player strikes the bench with the *Runed Mallet* (instant interaction), triggering a 0.5-second locking animation.
4. **Result:** The completed *Sun-Forged Ebony Sword* appears on the output riser showing its Quality and Base Damage, with a glow if Flawless. It is ready for dispatch or to be equipped.

### Naming
Weapons are auto-named from their materials: `[Payload material] [Foundation material] [Category]` — e.g. *Frost Willow Wand*, *Star-Metal Oak Sword*.

---

## Open Questions

- When the stat lock is lifted, which stat comes next (attack speed, durability, element effects)?
- Should the foundation ever contribute to Base Damage, or only to Quality?
- Can an assembled weapon be disassembled to recover one component?
