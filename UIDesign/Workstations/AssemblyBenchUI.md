# UI Design: Assembly Bench (2-Piece Modular Crafting)

> **Mechanic:** [GDD/Shop/WeaponCrafting](../../GDD/Shop/WeaponCrafting.md) · **Technical:** [TechnicalDesign/Shop/WeaponCrafting](../../TechnicalDesign/Shop/WeaponCrafting.md)

## Screen & Diegetic Interaction Overview
The Assembly Bench is the central work counter where processed components are joined into finished weapons. In keeping with the physical, hands-on aesthetic of *Armotheca*, this interface is primarily **diegetic and world-space**, minimizing screen-blocking 2D menus in favor of in-world holographic sockets and floating status projections.

Weapons show exactly two stats — **Quality (1–100)** and **Base Damage** — so the bench UI stays minimal.

**Implementation:** uGUI World Space Canvas attached to the bench, TextMeshPro for all text, Animator/tweens for socket pulses and the hologram. The view only listens to `AssemblyBench` events (see the technical doc).

---

## World-Space Layout & Sockets

```
                           [FLOATING PREVIEW HOLOGRAM]
                       "Sun-Forged Ebony Sword (Masterwork)"
                          Quality: 85  |  Base Damage: 12
                                      [===|===]
                                          |
        +---------------------------------+---------------------------------+
        |                                                                   |
        v                                                                   v
+-------------------------+                               +-------------------------+
|  SOCKET 1 (FOUNDATION)  |                               |   SOCKET 2 (PAYLOAD)    |
|  [ Ebony Wood Hilt ]    |                               |  [ Sun-Forged Blade ]   |
|  Quality: 82 (Master)   |                               |  Quality: 88 (Master)   |
|                         |                               |  Base Damage: 12 · Fire |
+-------------------------+                               +-------------------------+
        \                                                                   /
         \                                                                 /
          +-----------------------[ LOCK ANVIL ]--------------------------+
                                 [E] STRIKE MALLET
```

---

## Component Sockets

### 1. Socket 1 (Foundation Module)
- **Physical Position:** Left brass indentation on the bench.
- **Accepted Items:** Hilts (Swords) or Shafts (Wands / Staves).
- **Diegetic Indicator:**
  - Unfilled: Pulsing soft white silhouette of a handle/shaft.
  - Filled: Snapped 3D model with floating text showing item name and Quality with its tier badge.

### 2. Socket 2 (Payload Module)
- **Physical Position:** Right runic indentation on the bench.
- **Accepted Items:** Blades (Swords) or Arcane Cores (Wands / Staves).
- **Diegetic Indicator:**
  - Unfilled: Pulsing glow indicating ready state.
  - Filled: Snapped 3D model with an elemental particle aura (e.g. fire embers, frost crystals), floating text with Quality and Base Damage.

### 3. Center Lock Mechanism (Assembly Trigger)
- **Visual State:** Runed vise and mini-anvil.
- **Activation:**
  - Disabled until both sockets hold compatible parts (e.g. Hilt + Blade).
  - When valid, runic glyphs illuminate across the table connecting both sockets.
  - Interaction (instant): single prompt **`[E] Strike Mallet`**.

---

## Floating Real-Time Preview

When both sockets contain compatible parts, a floating tooltip appears above the bench:
- **Weapon Title:** Auto-generated name (e.g. *Frost Willow Wand*).
- **Quality:** Final value (average of both parts, 1–100) with tier badge (`Crude`, `Standard`, `Masterwork`, `Flawless`) and a small bar.
- **Base Damage:** Number taken from the payload part.
- **Element Icon:** Material element shown as an icon (identity only, no numeric effect).

---

## Error & Incompatibility States

If a player attempts to assemble mismatched modules (e.g. a Short Shaft with a Blade):
- **Visual Feedback:** Sockets pulse red. Runic lines between sockets crackle and break.
- **Hologram Text:** *"Incompatible Modules: ShortShaft cannot mount a Blade."*
- **Audio Feedback:** Low magical repulsion hum.
- **Ejection:** The last-inserted item pops back into the player's hands (or onto the floor if hands are occupied).
