---
id: Player
type: entity
category: Player
status: Draft
---

# Player

> **Overview:** [Vision](../../00_Overview/Vision.md) · **Technical:** [_Movement_Module › Controller](../../../Technical_Design/Movement/_Movement_Module.md#controller-context)

## Description & Role

An artisan of the Armotheca. Every player has the same abilities: there are no classes, and any player can work any bench, enter any owned door or fight with any weapon. 1–4 players share the workshop ([F07_Co_Op](../../01_Features/F07_Co_Op.md)).

## Behaviour & States

What each state allows is in [_Movement_System › Interactions](../../02_Systems/Movement/_Movement_System.md#interactions): grounded (empty hands or carrying), airborne, rolling, in continuous interaction, downed.

## Stats

- Health: [Combat › Health and Downed](../../06_Balancing/Combat.md#health-and-downed).
- Carry slots: hands, weapon slot, backpack ([M_Carry_Model](../../02_Systems/Interaction/M_Carry_Model.md)).

## Mechanics

- Movement: [M_Walk](../../02_Systems/Movement/M_Walk.md), [M_Sprint](../../02_Systems/Movement/M_Sprint.md), [M_Jump](../../02_Systems/Movement/M_Jump.md), [M_Roll](../../02_Systems/Movement/M_Roll.md)
- Interaction: [M_Targeting](../../02_Systems/Interaction/M_Targeting.md), [M_Instant_Interaction](../../02_Systems/Interaction/M_Instant_Interaction.md), [M_Continuous_Interaction](../../02_Systems/Interaction/M_Continuous_Interaction.md)
- Combat: [M_Sword_Swing](../../02_Systems/Combat/M_Sword_Swing.md), [M_Magic_Orb](../../02_Systems/Combat/M_Magic_Orb.md), [M_Health_And_Downed](../../02_Systems/Combat/M_Health_And_Downed.md)

## UI

- [UI_Interaction_Prompt](../../05_UI/World/UI_Interaction_Prompt.md), [UI_Pinned_Letter](../../05_UI/Hud/UI_Pinned_Letter.md), [UI_Realm_Pressure](../../05_UI/Hud/UI_Realm_Pressure.md). Health, downed and backpack displays are planned in [_UI_Flow](../../05_UI/_UI_Flow.md).

## Art & Audio References

- Concept art: [Main Character](../../../Visual_Design/Prompts/Main_Character.md).

## Appears In

- All locations and features.

## Open Questions

-
