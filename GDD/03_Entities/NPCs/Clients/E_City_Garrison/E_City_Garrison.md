---
id: E_City_Garrison
type: entity
category: NPCs
status: Draft
---

# City Garrison (The Mass Contractors)

> **Roster:** [_Client_Roster](../_Client_Roster.md) · **Technical:** [_Orders_Module › Data](../../../../../Technical_Design/Orders/_Orders_Module.md#data)

## Description & Role

Quartermasters supplying frontline battalions. Pushes the workshop into an assembly-line mindset where players pre-smelt and mass-forge identical components.

## Behaviour & States

- **Demand pattern:** batch orders of identical weapons (e.g. *3x Iron Swords, Fire element, Standard+*), using the Quantity criterion ([M_Commission_Criteria](../../../../02_Systems/Orders/M_Commission_Criteria.md)).

## Stats

Batch size, lifespan, rewards and penalty: [Orders › Client Archetypes](../../../../06_Balancing/Orders.md#client-archetypes).

## Outputs

Large lump-sum gold payouts (bulk gold bonus).

## UI

[UI_Letter_Commission_Board](../../../../05_UI/Screens/UI_Letter_Commission_Board.md): red / brass faction trim and a batch counter.

## Appears In

- [F01_Commissions](../../../../01_Features/F01_Commissions.md)

## Open Questions

-
