# UI Design: Assembly Bench (2-Piece Modular Crafting)

## Screen & Diegetic Interaction Overview
The Assembly Bench is the central work counter where processed components are joined into finished weapons. In keeping with the physical, hands-on aesthetic of *Armotheca*, this interface is primarily **diegetic and world-space**, minimizing screen-blocking 2D menus in favor of intuitive in-world holographic sockets and floating status projections.

---

## World-Space Layout & Sockets

```
                           [FLOATING PREVIEW HOLOGRAM]
                      "Flame-Forged Longsword (Masterwork)"
                            Est. Power: 48 | Speed: 1.2
                                      [===|===]
                                          |
        +---------------------------------+---------------------------------+
        |                                                                   |
        v                                                                   v
+-----------------------+                                 +-----------------------+
|   SOCKET 1 (FOUNDATION) |                                 |    SOCKET 2 (PAYLOAD)  |
|   [ Ebony Wood Hilt ]  |                                 |   [ Sun-Forged Blade] |
|   Quality: 82% (Master)|                                 |   Quality: 88% (Master|
|   Element: Physical    |                                 |   Element: Fire       |
+-----------------------+                                 +-----------------------+
        \                                                                   /
         \                                                                 /
          +-----------------------[ LOCK ANVIL ]--------------------------+
                               [HOLD 'E' / STRIKE MALLET]
```

---

## Component Sockets

### 1. Socket 1 (Foundation Module)
- **Physical Position:** Left brass indentation on the bench.
- **Accepted Items:** Hilts (Swords) or Shafts (Wands / Staves).
- **Diegetic Indicator:** 
  - Unfilled: Pulsing soft white silhouette of a handle/shaft.
  - Filled: Snapped 3D model with floating text showing Item Name and Quality Tier badge.

### 2. Socket 2 (Payload / Accent Module)
- **Physical Position:** Right runic indentation on the bench.
- **Accepted Items:** Blades (Swords) or Arcane Cores (Wands / Staves).
- **Diegetic Indicator:**
  - Unfilled: Pulsing elemental glow indicating ready state.
  - Filled: Snapped 3D model with elemental particle aura (e.g. fire embers, frost crystals).

### 3. Center Lock Mechanism (Assembly Trigger)
- **Visual State:** Runed vise and mini-anvil.
- **Activation:** 
  - Disabled until both Socket 1 and Socket 2 are populated with compatible parts (e.g. Sword Hilt + Sword Blade).
  - When valid, runic glyphs illuminate across the table connecting both sockets.
  - Interaction: Single prompt appears: **`[E] Strike Runed Mallet to Forge`** (or physical swing with tool).

---

## Floating Real-Time Stat Preview

When both sockets contain valid parts, a floating magical tooltip appears above the bench showing the calculated composite stats:
- **Weapon Title:** Auto-generated name (e.g. *Frost-Bite Oak Staff*).
- **Composite Quality Badge:** Calculated average quality level (`Crude`, `Standard`, `Masterwork`, `Flawless`).
- **Calculated Stats:**
  - **Power Bar:** Green/Orange gauge based on Blade/Core rating.
  - **Speed Bar:** Blue gauge based on Hilt/Shaft balance rating.
  - **Elemental Affinity Icon:** Displaying primary elemental effect.
- **Estimated Base Value:** Projected coin value before client bonuses.

---

## Error & Incompatibility States

If a player attempts to assemble mismatched modules (e.g., trying to socket a Wand Shaft with a Sword Blade):
- **Visual Feedback:** Sockets pulse red. Runic lines between sockets crackle and break.
- **Hologram Text:** *“Incompatible Modules: Wand Shaft cannot mount a Sword Blade.”*
- **Audio Feedback:** Low magical repulsion hum.
- **Ejection:** The incompatible second item pops off the bench onto the floor or back into the player's hands.
