---
id: M_Door_Purchase
type: mechanic
system: Exploration
status: Draft
---

# Door Purchase

> **System:** [_Exploration_System](_Exploration_System.md) · **Technical:** [Magic Doors (tech)](../../../Technical_Design/Exploration/Magic_Doors.md)

## Summary

A Magic Door is unlocked when the workshop reaches its tier **and** the team pays its gold price.

## Rules

1. When the workshop reaches a door's **required tier**, the door appears in the Threshold of Portals, sealed, with a price plaque ([E_Magic_Door](../../03_Entities/Props/Interactive/E_Magic_Door.md)).
2. The team **pays the door's gold price** from the shared treasury with a hold-to-confirm interaction on the plaque, to avoid accidental purchases.
3. The first door (Verdant Corruption) is owned at the start.
4. Tier 3 makes two doors available at once, so the team chooses which realm to invest in first.
5. Commissions only request materials obtainable through doors the team owns ([_Orders_System](../Orders/_Orders_System.md)).

## Player Input

Hold interact on the price plaque ([M_Continuous_Interaction](../Interaction/M_Continuous_Interaction.md)).

## Tunable Parameters

| Parameter | Meaning | Value |
| --- | --- | --- |
| Required tier and gold price | Per door | [Progression › Doors](../../06_Balancing/Progression.md#doors) |
| Confirm hold | Purchase hold time | [Exploration › Doors](../../06_Balancing/Exploration.md#doors) |

## UI

- [UI_Interaction_Prompt](../../05_UI/World/UI_Interaction_Prompt.md): price plaque prompt.

## Dependencies

- [M_Workshop_Tiers](../Progression/M_Workshop_Tiers.md), [M_Currencies](../Progression/M_Currencies.md)

## Used By

- [F03_Expeditions](../../01_Features/F03_Expeditions.md), [F05_Shop_Progression](../../01_Features/F05_Shop_Progression.md)

## Open Questions

- Should door prices scale in Prestige mode, or should doors stay owned permanently across prestige runs?
