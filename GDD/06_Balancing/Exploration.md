---
id: Exploration
type: balancing
system: Exploration
status: Draft
---

# Exploration Balancing

> **System:** [_Exploration_System](../02_Systems/Exploration/_Exploration_System.md)

Values marked `*` are initial values not yet validated by playtest. Docs link here by table anchor and never repeat the value.

## Doors

Owner: [M_Door_Lifecycle](../02_Systems/Exploration/M_Door_Lifecycle.md)

| Parameter | Value | Notes |
| --- | --- | --- |
| Entry window | 90 s |  |
| Cooldown | 20 s |  |
| Purchase confirm hold | 1 s | [M_Door_Purchase](../02_Systems/Exploration/M_Door_Purchase.md) |

## Nodes

Owner: [M_Node_Spawning](../02_Systems/Exploration/M_Node_Spawning.md), [M_Harvesting](../02_Systems/Exploration/M_Harvesting.md)

| Parameter | Value | Notes |
| --- | --- | --- |
| Active spawn points per band | 60–80%* |  |
| Rare variant chance | 10%* |  |
| Respawn during an expedition | None |  |
| Letter guarantee | ≥ 1 node per required material |  |
| Hits per Mineral Vein | 3–5 |  |
| Strike interval | 0.6 s* | One hit per helper per interval |
| Hits per Arcane Flora | 3–4 |  |
| Max harvesters per node | 2 |  |

## Mobs

Owner: [M_Mob_Spawning](../02_Systems/Exploration/M_Mob_Spawning.md)

| Parameter | Value | Notes |
| --- | --- | --- |
| Active spawn zones per band (on creation) | 50–70%* |  |

## Realm Pressure

Owner: [M_Realm_Pressure](../02_Systems/Exploration/M_Realm_Pressure.md)

| Parameter | Value | Notes |
| --- | --- | --- |
| Level-up interval | every 60 s occupied* |  |
| Wandering spawn interval | 30 s at level 0, −5 s per level, minimum 8 s* |  |
| Max simultaneous mobs | 12 at level 0, +2 per level, hard cap 20* |  |
| Deep groups spawning in Outer Grounds | from level 3* |  |

## Targets

Owner: [_Exploration_System](../02_Systems/Exploration/_Exploration_System.md)

| Parameter | Value | Notes |
| --- | --- | --- |
| Typical run length | 2–4 min | Design target, not a limit |
| Quick supply run | ~2 min |  |
| Outer Grounds crossing time | < 1 min | Layout target |
