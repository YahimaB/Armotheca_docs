---
id: M_Currencies
type: mechanic
system: Progression
status: Draft
---

# Currencies

> **System:** [_Progression_System](_Progression_System.md) · **Technical:** [_Progression_Module › Technical Specifications](../../../Technical_Design/Progression/_Progression_Module.md#technical-specifications)

## Summary

What the team earns and spends.

## Rules

| Currency | Earned From | Spent On |
|---|---|---|
| **Gold** | Completed commissions | Tier upgrades, Magic Door purchases, station purchases |
| **Reputation** | Completed commissions (lost on failures) | Gate for tier upgrades (not spent) |
| **Emergency Tokens** | SOS commissions | Instant workshop buffs |
| **Blueprints / Catalysts** | Academy and Collector commissions, Apex Guardians | New recipes, the Uber-Weapon |

1. Gold is held in a shared team treasury.
2. Reputation is a threshold and is never consumed.

## UI

- [UI_Letter_Commission_Board](../../05_UI/World/UI_Letter_Commission_Board.md): reputation display and payout animation.

## Used By

- [F01_Commissions](../../01_Features/F01_Commissions.md), [F05_Shop_Progression](../../01_Features/F05_Shop_Progression.md)

## Open Questions

-
