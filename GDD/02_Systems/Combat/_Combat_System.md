---
id: _Combat_System
type: system
status: Draft
---

# Combat System

> **Glossary:** [System](../../00_Overview/Glossary.md) · **Balancing:** [Combat](../../06_Balancing/Combat.md) · **Technical:** [_Combat_Module](../../../Technical_Design/Combat/_Combat_Module.md)

## Overview

Two attacks, one per weapon family — a sword swing chain and a magic orb — plus player health and a downed state. Damage per hit is the weapon's Base Damage ([M_Quality](../Crafting/M_Quality.md)); there are no hidden modifiers. Purpose, experience goals and references are in [F04_Combat](../../01_Features/F04_Combat.md).

## Mechanics

| ID | Summary | Status |
| --- | --- | --- |
| [M_Sword_Swing](M_Sword_Swing.md) | Two-swing melee chain in a frontal arc | Draft |
| [M_Magic_Orb](M_Magic_Orb.md) | Single-target projectile for wands and staves | Draft |
| [M_Health_And_Downed](M_Health_And_Downed.md) | Player health, invulnerability, downed, revive, bleed-out | Draft |

## Interactions

- **Attacks need empty hands.** With an item in hands, attack does nothing ([M_Carry_Model](../Interaction/M_Carry_Model.md)); with empty hands the equipped weapon is drawn automatically.
- **Roll is the defence.** [M_Roll](../Movement/M_Roll.md) cancels sword recovery and its invulnerability window answers telegraphed mob attacks.
- **Quality does not change damage at this stage.** A Crude and a Flawless sword with the same blade material hit equally hard; Quality matters for commissions and payouts.
- **Element has no combat effect at this stage.** It is a material identity used by orders and visuals (a fire core makes an orange orb).
- **Wand and staff share the orb attack**; their difference is handedness and visuals ([E_Wand](../../03_Entities/Items/Weapons/E_Wand.md), [E_Staff](../../03_Entities/Items/Weapons/E_Staff.md)).
- **Friendly fire:** off.
- **Workshop safety:** no combat happens inside the workshop.
- Mob health, damage, drops and stagger rules: [_Mob_Roster](../../03_Entities/Mobs/_Mob_Roster.md).

## Shared State

- **Health and downed state** (owned by [M_Health_And_Downed](M_Health_And_Downed.md)): blocks movement and interactions while downed.

## UI

- None yet; player health and downed display are planned in [_UI_Flow](../../05_UI/_UI_Flow.md).

## Open Questions

- Should wands and staves diverge (e.g. staff orb pierces or is larger) once the weapon stat lock is lifted?
- Should Quality or Element ever influence combat, or remain purely commercial?
- Do players get a starter sword and wand that cannot be sold, so they never enter a realm unarmed?
