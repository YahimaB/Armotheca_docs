---
id: M_Quality
type: mechanic
system: Crafting
status: Draft
---

# Weapon Stats & Quality Tiers

> **System:** [_Crafting_System](_Crafting_System.md) · **Technical:** [Weapon Crafting (tech)](../../../Technical_Design/Shop/Weapon_Crafting.md)

## Summary

Every weapon has exactly two stats, Quality and Base Damage. Quality is grouped into named tiers that commissions and UI use.

## Rules

| Stat | Range | Source | Notes |
|---|---|---|---|
| **Quality** | 1–100 (integer) | Average of both components' Quality, rounded | Produced during manual processing ([M_Processing_Mini_Game](../Processing/M_Processing_Mini_Game.md)). |
| **Base Damage** | Constant per payload material | Payload material data (Blade or Core) | Not modified by Quality or by the foundation at this stage. |

1. **Quality tiers** are named bands of the single Quality stat: **Crude**, **Standard**, **Masterwork**, **Flawless**. They are used by commissions and by the UI and add **no hidden stat bonuses**.
2. Typical use: Crude is accepted only by undemanding clients and rejected by the Academy; Standard is the default result of processing without mini-games; Masterwork is required by demanding clients and eligible for Guild bonuses; Flawless gets top payouts and emits a subtle particle glow.
3. **Material attributes are not stats.** Each component carries a material identity (e.g. Ironwood, Star Metal) and payloads carry an **Element** (Physical, Fire, Frost, Lightning, Arcane, Holy). These are used by commission criteria, naming and visuals only, with no numeric effect in combat ([_Combat_System](../Combat/_Combat_System.md)).

## Tunable Parameters

| Parameter | Meaning | Value |
| --- | --- | --- |
| Tier bands | Quality range per tier | [Crafting › Quality Tiers](../../06_Balancing/Crafting.md#quality-tiers) |
| Base Damage | Per payload material | [_Item_List › Materials](../../03_Entities/Items/_Item_List.md#materials) (values not yet defined) |

## Feedback

Flawless weapons emit a subtle particle glow.

## UI

- [UI_Assembly_Bench](../../05_UI/World/UI_Assembly_Bench.md), [UI_Letter_Commission_Board](../../05_UI/Screens/UI_Letter_Commission_Board.md): tier badges.

## Dependencies

- [M_Assembly](M_Assembly.md)

## Used By

- [F01_Commissions](../../01_Features/F01_Commissions.md), [F02_Weapon_Crafting](../../01_Features/F02_Weapon_Crafting.md), [F04_Combat](../../01_Features/F04_Combat.md)

## Open Questions

- When the stat lock is lifted, which stat comes next (attack speed, durability, element effects)?
- Should the foundation ever contribute to Base Damage, or only to Quality?
