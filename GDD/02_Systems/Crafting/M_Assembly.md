---
id: M_Assembly
type: mechanic
system: Crafting
status: Draft
---

# Assembly (2-Piece Modular)

> **System:** [_Crafting_System](_Crafting_System.md) · **Technical:** [Weapon Crafting (tech)](../../../Technical_Design/Shop/Weapon_Crafting.md)

## Summary

A weapon is assembled on the bench from exactly one foundation and one payload, then locked with a mallet strike.

## Rules

| Category | Foundation Component | Payload Component |
|---|---|---|
| **Sword** | Hilt | Blade |
| **Wand (1-Handed)** | Short Shaft | Magical Core |
| **Staff (2-Handed)** | Long Shaft | Magical Core |

1. The **payload** (Blade or Core) defines the weapon's Base Damage and Element.
2. The **foundation** (Hilt or Shaft) defines the weapon category and contributes to Quality.
3. Any other pairing (e.g. Short Shaft + Blade) is incompatible and rejected by the bench; the last-inserted item returns to the player's hands, or onto the floor if hands are occupied.
4. Flow on the [E_Assembly_Bench](../../03_Entities/Props/Workstations/E_Assembly_Bench.md):
   1. A player snaps a processed payload (e.g. *Sun-Forged Blade*) into the Payload socket.
   2. A player snaps a foundation (e.g. *Ebony Hilt*) into the Foundation socket.
   3. Either player strikes the bench with the *Runed Mallet* (instant interaction), triggering a short locking animation.
   4. The finished weapon (*Sun-Forged Ebony Sword*) appears on the output riser showing Quality and Base Damage, with a glow if Flawless. It is ready for dispatch or to be equipped.

## Player Input

Place / snap and strike: [M_Instant_Interaction](../Interaction/M_Instant_Interaction.md).

## Tunable Parameters

| Parameter | Meaning | Value |
| --- | --- | --- |
| Locking animation | Duration of the lock | [Crafting › Assembly](../../06_Balancing/Crafting.md#assembly) |

## Feedback

Mallet strike, locking animation, output riser; Flawless glow ([M_Quality](M_Quality.md)).

## UI

- [UI_Assembly_Bench](../../05_UI/World/UI_Assembly_Bench.md)

## Dependencies

- [M_Quality](M_Quality.md), [M_Weapon_Naming](M_Weapon_Naming.md)
- Components: [E_Blade](../../03_Entities/Items/Components/E_Blade.md), [E_Core](../../03_Entities/Items/Components/E_Core.md), [E_Hilt](../../03_Entities/Items/Components/E_Hilt.md), [E_Short_Shaft](../../03_Entities/Items/Components/E_Short_Shaft.md), [E_Long_Shaft](../../03_Entities/Items/Components/E_Long_Shaft.md)

## Used By

- [F02_Weapon_Crafting](../../01_Features/F02_Weapon_Crafting.md)

## Open Questions

- Can an assembled weapon be disassembled to recover one component?
