---
id: Orders
type: balancing
system: Orders
status: Draft
---

# Orders Balancing

> **System:** [_Orders_System](../02_Systems/Orders/_Orders_System.md)

Values marked `*` are initial values not yet validated by playtest. Docs link here by table anchor and never repeat the value.

## Letter Rules

Owner: [M_Letter_Flow](../02_Systems/Orders/M_Letter_Flow.md)

| Parameter | Value | Notes |
| --- | --- | --- |
| Max simultaneous letters | 5 |  |
| Flawless delivery bonus | +50% gold |  |
| Letter lifespan range | 90 s (SOS) to 360 s (Guild) | Conflicts with per-archetype timings below |

## Client Archetypes

Owner: [_Client_Roster](../03_Entities/NPCs/Clients/_Client_Roster.md)

| ID | Lifespan | Batch size | Reward | Failure penalty |
| --- | --- | --- | --- | --- |
| [E_Adventurers_Guild](../03_Entities/NPCs/Clients/E_Adventurers_Guild.md) | 4–6 min | 1 | Moderate gold, Guild rep | Low (mild / negligible rep loss) |
| [E_Arcane_Academy](../03_Entities/NPCs/Clients/E_Arcane_Academy.md) | — | 1 | High gold, rare blueprints | High (severe rep loss) |
| [E_City_Garrison](../03_Entities/NPCs/Clients/E_City_Garrison.md) | — | 2–4 | Bulk gold bonus | Medium |
| [E_SOS_Dispatch](../03_Entities/NPCs/Clients/E_SOS_Dispatch.md) | 60–120 s | 1 | 2.5x standard gold (2x–3x in the old Master GDD), Emergency Tokens | None (expires) |
| [E_Eccentric_Collectors](../03_Entities/NPCs/Clients/E_Eccentric_Collectors.md) | — | 1 | Modest gold, Uber-Weapon blueprints, Prismatic Catalysts | Weapon rejected |

Source conflicts to resolve: SOS lifespan (60–120 s here vs 90 s in Letter Rules), Guild lifespan (4–6 min vs 360 s), SOS gold (2.5x vs 2x–3x). The example reward on the board mockup (450 G, +35 rep, −50 rep) is illustrative.

## UI Thresholds

Owner: [UI_Letter_Commission_Board](../05_UI/Screens/UI_Letter_Commission_Board.md)

| Parameter | Value | Notes |
| --- | --- | --- |
| SOS critical alert | < 60 s remaining |  |
