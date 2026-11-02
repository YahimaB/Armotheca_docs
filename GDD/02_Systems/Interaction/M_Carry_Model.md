---
id: M_Carry_Model
type: mechanic
system: Interaction
status: Draft
---

# Carry Model

> **System:** [_Interaction_System](_Interaction_System.md) · **Technical:** [_Interaction_Module › Technical Specifications](../../../Technical_Design/Interaction/_Interaction_Module.md#technical-specifications)

## Summary

Each player has three places to hold things: hands, a weapon slot and a backpack.

## Rules

| Slot | Holds | Notes |
|---|---|---|
| **Hands** | One world object (raw resource, processed component, finished weapon, letter) | Visible in the character's hands. Blocks roll and attacks while occupied. |
| **Weapon Slot** | One equipped weapon (sword, wand or staff) | Drawn automatically when hands are empty and an attack is pressed. |
| **Backpack** | A small number of raw resources | Used during expeditions. Harvested resources go here first. |

1. Any weapon picked up from the world goes into the **hands** first (it may be a commission to deliver). A secondary action moves it into the weapon slot, swapping the previously equipped weapon into the hands.
2. Loose drops from nodes and mobs go into the backpack automatically when the harvester walks over them, or can be picked up into hands by anyone.
3. The backpack can be emptied into the [E_Aether_Chute](../../03_Entities/Props/Interactive/E_Aether_Chute/E_Aether_Chute.md) in a realm or into a storage crate in the workshop, one item per press or all at once with a hold.
4. When a player bleeds out, backpack and hands contents are dropped in the realm; they can be recovered while the realm is still occupied ([M_Health_And_Downed](../Combat/M_Health_And_Downed.md)).

## Player Input

`[Q] Equip` moves a weapon from hands to the weapon slot.

## Tunable Parameters

| Parameter | Meaning | Value |
| --- | --- | --- |
| Backpack slots | Raw resources carried | [Interaction › Carry Model](../../06_Balancing/Interaction.md#carry-model) |

## UI

- [UI_Interaction_Prompt](../../05_UI/World/UI_Interaction_Prompt.md). A backpack display is planned in [_UI_Flow](../../05_UI/_UI_Flow.md).

## Dependencies

- [M_Walk](../Movement/M_Walk.md), [M_Roll](../Movement/M_Roll.md): carrying slows movement and blocks roll.

## Used By

- [F02_Weapon_Crafting](../../01_Features/F02_Weapon_Crafting.md), [F03_Expeditions](../../01_Features/F03_Expeditions.md)

## Open Questions

- Backpack size: fixed, or upgradable through shop progression?
