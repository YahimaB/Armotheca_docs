---
id: M_Forging_Ritual
type: mechanic
system: Endgame
status: Draft
---

# The Forging Ritual

> **System:** [_Endgame_System](_Endgame_System.md) · **Technical:** [_Endgame_Module › Architecture](../../../Technical_Design/Endgame/_Endgame_Module.md#architecture--implementation-approaches)

## Summary

A four-phase, synchronised co-op forging event that turns the four catalysts into the Primordial Armament.

## Rules

1. **Requirements:** Tier 3 ([E_Great_Crucible](../../03_Entities/Props/Workstations/E_Great_Crucible/E_Great_Crucible.md)) and all four catalysts ([E_Primordial_Catalyst](../../03_Entities/Items/Catalysts/E_Primordial_Catalyst/E_Primordial_Catalyst.md)). Players start the ritual from the Crucible (instant interaction).
2. **Phase 1 — Harmonic Smelting (furnace team):** the Ignis Core and Astral Prism are melted in the Great Crucible. Temperature must be held in range through synchronised bellows pumping (cooperative continuous interaction).
3. **Phase 2 — Arcane Turning (carpentry team):** the Sylvan Spire is carved into an Adamantine Shaft on the high-speed lathe.
4. **Phase 3 — The Glacial Quench (dual action):** the molten celestial blade is plunged into the Glacial Heart solution at the exact moment the temperature needle aligns.
5. **Phase 4 — Final Binding:** both components are locked into the Grand Assembly Bench, and all active players strike their mallets simultaneously to seal the weapon.
6. The ritual scales to the number of players present; with fewer than four, phases run sequentially instead of in parallel.
7. Failing a phase sets the ritual back to the start of that phase and never destroys catalysts.
8. Completion plays the campaign victory screen and unlocks Prestige Endless Mode ([F06_Uber_Weapon](../../01_Features/F06_Uber_Weapon.md)).

## Player Input

[M_Instant_Interaction](../Interaction/M_Instant_Interaction.md) to start and strike; [M_Continuous_Interaction](../Interaction/M_Continuous_Interaction.md) for bellows and lathe.

## UI

- None yet; ritual phase display and victory screen are planned in [_UI_Flow](../../05_UI/_UI_Flow.md).

## Used By

- [F06_Uber_Weapon](../../01_Features/F06_Uber_Weapon.md), [F07_Co_Op](../../01_Features/F07_Co_Op.md)

## Open Questions

- What happens if a player leaves mid-ritual?
