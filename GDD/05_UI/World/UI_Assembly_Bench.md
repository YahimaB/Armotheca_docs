---
id: UI_Assembly_Bench
type: ui
category: World
status: Draft
---

# Assembly Bench (2-Piece Modular Crafting)

> **Flow:** [_UI_Flow](../_UI_Flow.md) · **Technical:** [_UI_Module › Assembly Bench](../../../Technical_Design/UI/_UI_Module.md#assembly-bench)

## Purpose

The central work counter where processed components are joined into weapons ([M_Assembly](../../02_Systems/Crafting/M_Assembly.md)). In keeping with the hands-on aesthetic, the interface is **diegetic and world-space**: in-world holographic sockets and floating status projections instead of screen-blocking menus. Weapons show only Quality and Base Damage, so the UI stays minimal.

## Mockup

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

Values in the mockup are illustrative.

## Elements

| Element | Type | Shows | Data source |
| --- | --- | --- | --- |
| Socket 1 (Foundation) | World socket | Left brass indentation. Accepts Hilts or Shafts. Unfilled: pulsing soft white silhouette of a handle/shaft. Filled: snapped model with item name and Quality with tier badge. | [M_Assembly](../../02_Systems/Crafting/M_Assembly.md) |
| Socket 2 (Payload) | World socket | Right runic indentation. Accepts Blades or Cores. Unfilled: pulsing ready glow. Filled: snapped model with elemental aura (embers, frost crystals), Quality and Base Damage. | [M_Assembly](../../02_Systems/Crafting/M_Assembly.md) |
| Lock mechanism | World element | Runed vise and mini-anvil; prompt `[E] Strike Mallet` | [M_Assembly](../../02_Systems/Crafting/M_Assembly.md) |
| Preview hologram | Tooltip | Weapon name; Quality (average of both parts) with tier badge and small bar; Base Damage from the payload; element icon (identity only) | [M_Weapon_Naming](../../02_Systems/Crafting/M_Weapon_Naming.md), [M_Quality](../../02_Systems/Crafting/M_Quality.md) |

## States

- **Incomplete:** lock disabled until both sockets hold compatible parts.
- **Valid:** runic glyphs illuminate across the table connecting both sockets; the preview hologram appears.
- **Incompatible** (e.g. Short Shaft + Blade): sockets pulse red; runic lines crackle and break; hologram text *"Incompatible Modules: ShortShaft cannot mount a Blade."*; the last-inserted item pops back to the player's hands (or the floor if hands are occupied).
- **Flawless result:** glow on the output.

## Input & Navigation

Place / take with [M_Instant_Interaction](../../02_Systems/Interaction/M_Instant_Interaction.md); strike the mallet to lock.

## Feedback

Socket pulses, glyph lighting, locking animation; low magical repulsion hum on incompatibility.

## Used By

- [F02_Weapon_Crafting](../../01_Features/F02_Weapon_Crafting.md), [E_Assembly_Bench](../../03_Entities/Props/Workstations/E_Assembly_Bench/E_Assembly_Bench.md)

## Open Questions

-
