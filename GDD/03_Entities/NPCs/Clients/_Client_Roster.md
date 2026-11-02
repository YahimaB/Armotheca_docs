---
id: _Client_Roster
type: roster
status: Draft
---

# Client Roster

> **Overview:** [Glossary](../../../00_Overview/Glossary.md) · **Balancing:** [Orders › Client Archetypes](../../../06_Balancing/Orders.md#client-archetypes) · **Technical:** [_Orders_Module › Data](../../../../Technical_Design/Orders/_Orders_Module.md#data)

## Overview

Clients never appear in person; they are factions that send commission letters ([F01_Commissions](../../../01_Features/F01_Commissions.md)). Each archetype shapes which criteria its letters use ([M_Commission_Criteria](../../../02_Systems/Orders/M_Commission_Criteria.md)), how long they last, what they pay and what failure costs.

```
+--------------------------------------------------------------------------+
|                        COMMISSION LETTER ARCHETYPES                      |
+--------------------------------------------------------------------------+
| 1. ADVENTURERS GUILD | High volume, Standard+ quality, steady gold & rep |
| 2. ARCANE ACADEMY    | Zero tolerance for defects, rare cores, blueprints|
| 3. CITY GARRISON     | Identical batch orders, bulk profits              |
| 4. SOS DISPATCH      | Extreme time pressure, high-risk windfall         |
| 5. COLLECTOR NOBLES  | Exotic material combinations, Uber catalysts      |
+--------------------------------------------------------------------------+
```

## Roster

| ID | Name | Preferred Weaponry | Key Demand | Reward Profile | Penalty for Failure | Status |
| --- | --- | --- | --- | --- | --- | --- |
| [E_Adventurers_Guild](E_Adventurers_Guild.md) | Adventurers Guild | Standard swords & wands | Standard or better quality | Moderate gold, Guild rep | Low (mild rep loss) | Draft |
| [E_Arcane_Academy](E_Arcane_Academy.md) | Arcane Academy | High-tier wands & staves | High-quality cores, zero defects | High gold, rare blueprints | High (heavy rep loss) | Draft |
| [E_City_Garrison](E_City_Garrison.md) | City Garrison | Bulk uniform swords | Exact identical batches | Bulk gold bonus | Medium | Draft |
| [E_SOS_Dispatch](E_SOS_Dispatch.md) | SOS Emergency Dispatch | Any (elemental counters) | Very tight timer | Gold multiplier, Emergency Tokens | None (order expires) | Draft |
| [E_Eccentric_Collectors](E_Eccentric_Collectors.md) | Eccentric Collectors | Exotic / hybrid combos | Rare mob parts, unusual materials | Uber-Weapon blueprints and catalysts | Rejection of weapon | Draft |

## Gaps

- Celestial clients for Prestige Endless Mode ([F06_Uber_Weapon](../../../01_Features/F06_Uber_Weapon.md)).
