---
id: M_Commission_Criteria
type: mechanic
system: Orders
status: Draft
---

# Commission Criteria

> **System:** [_Orders_System](_Orders_System.md) · **Technical:** [_Orders_Module › Technical Specifications](../../../Technical_Design/Orders/_Orders_Module.md#technical-specifications)

## Summary

Every letter specifies a combination of criteria the delivered weapon must meet.

## Rules

| Criterion | Example | Required? |
|---|---|---|
| Weapon type | Sword / Wand / Staff | Always |
| Minimum quality tier | Masterwork | Always |
| Element | Frost | Optional |
| Quantity | 3 identical units | Optional (default 1) |
| Specific component material | Ancient Bog-Wood Long Shaft | Optional |

1. Weapon stats are limited to Quality and Base Damage ([M_Quality](../Crafting/M_Quality.md)); letters do not request any other stat.
2. Which criteria a letter uses depends on its client archetype ([_Client_Roster](../../03_Entities/NPCs/Clients/_Client_Roster.md)).

## UI

- [UI_Letter_Commission_Board](../../05_UI/World/UI_Letter_Commission_Board.md): criteria breakdown.
- [UI_Pinned_Letter](../../05_UI/Hud/UI_Pinned_Letter.md)

## Used By

- [F01_Commissions](../../01_Features/F01_Commissions.md)

## Open Questions

- Should orders ever request a minimum Base Damage, or keep criteria purely material/quality based?
