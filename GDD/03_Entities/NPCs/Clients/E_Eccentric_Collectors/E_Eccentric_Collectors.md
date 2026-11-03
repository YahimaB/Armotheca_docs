---
id: E_Eccentric_Collectors
type: entity
category: NPCs
status: Draft
---

# Eccentric Collectors (The Milestone Givers)

> **Roster:** [_Client_Roster](../_Client_Roster.md) · **Technical:** [_Orders_Module › Data](../../../../../Technical_Design/Orders/_Orders_Module.md#data)

## Description & Role

Interdimensional oligarchs seeking bizarre vanity weapons (also called Collector Nobles). Their letters are milestones toward the Uber-Weapon.

## Behaviour & States

- **Demand pattern:** exotic material combinations (e.g. *Lightning Core inside an Ancient Bog-Wood Staff*), rare mob parts and unusual materials, using the Specific Component Material criterion ([M_Commission_Criteria](../../../../02_Systems/Orders/M_Commission_Criteria.md)).
- **Failure:** the weapon is rejected.

## Stats

Lifespan, rewards and penalty: [Orders › Client Archetypes](../../../../06_Balancing/Orders.md#client-archetypes).

## Outputs

Modest gold, but **Uber-Weapon blueprints** and **Prismatic Catalysts** ([M_Currencies](../../../../02_Systems/Progression/M_Currencies.md)).

## UI

[UI_Letter_Commission_Board](../../../../05_UI/World/UI_Letter_Commission_Board.md): gold / purple faction trim.

## Appears In

- [F01_Commissions](../../../../01_Features/F01_Commissions.md), [F06_Uber_Weapon](../../../../01_Features/F06_Uber_Weapon.md)

## Open Questions

- How do Collector "Prismatic Catalysts" relate to the four Primordial Catalysts dropped by Apex Guardians ([E_Primordial_Catalyst](../../../Items/Catalysts/E_Primordial_Catalyst/E_Primordial_Catalyst.md))?
