---
id: _Exploration_System
type: system
status: Draft
---

# Exploration System

> **Glossary:** [System](../../00_Overview/Glossary.md) · **Balancing:** [Exploration](../../06_Balancing/Exploration.md) · **Technical:** [_Exploration_Module](../../../Technical_Design/Exploration/_Exploration_Module.md)

## Overview

Doors are bought, opened into a freshly rolled realm, and kept open for entering only briefly; inside there is no time limit. Nodes and mobs are placed per opening, harvesting depletes the realm, and Realm Pressure keeps rising. Purpose and experience goals are in [F03_Expeditions](../../01_Features/F03_Expeditions.md); the realms are in [_World_Map](../../04_Locations/_World_Map.md).

## Mechanics

| ID | Summary | Status |
| --- | --- | --- |
| [M_Door_Purchase](M_Door_Purchase.md) | Doors unlock by tier and are bought with gold | Draft |
| [M_Door_Lifecycle](M_Door_Lifecycle.md) | Ready → entry window → in progress → cooldown; leaving a realm | Draft |
| [M_Realm_Instancing](M_Realm_Instancing.md) | Realm lifetime and per-opening variation | Draft |
| [M_Harvesting](M_Harvesting.md) | Striking nodes, yields and depletion | Draft |
| [M_Node_Spawning](M_Node_Spawning.md) | Node placement per opening | Draft |
| [M_Mob_Spawning](M_Mob_Spawning.md) | Mob placement per opening, ambushers, wandering spawns | Draft |
| [M_Realm_Pressure](M_Realm_Pressure.md) | Danger that rises while a realm is occupied | Draft |

## Interactions

### What pushes players home

There is no expedition timer. Instead:

1. **Letter deadlines** keep ticking in the workshop ([M_Letter_Flow](../Orders/M_Letter_Flow.md)).
2. **Backpack capacity** fills up ([M_Carry_Model](../Interaction/M_Carry_Model.md)).
3. **Realm Pressure** rises the longer the realm is occupied, with no upper limit on danger ([M_Realm_Pressure](M_Realm_Pressure.md)).
4. **Depletion:** harvested nodes do not regrow, so a realm gradually runs out of easy resources ([M_Harvesting](M_Harvesting.md)).

### Anti-downtime

1. **Aether Drop-Chute:** near the entry point, a chute instantly sends deposited resources to the workshop. With entry sealed after the window, the chute is the main way to supply the workshop mid-run without ending anyone's expedition ([E_Aether_Chute](../../03_Entities/Props/Interactive/E_Aether_Chute/E_Aether_Chute.md)).
2. **Member re-entry:** expedition members can step out and back in while a teammate holds the realm, so carrying cargo home or grabbing a better weapon does not end the run.
3. **Multiple owned doors:** each owned door runs its own expedition; a workshop player who missed one entry window can open a different owned door.
4. **Self-paced length:** teams can make quick supply runs or long deep dives; letter deadlines naturally keep most runs short.

## Shared State

- **Expedition membership** (owned by [M_Door_Lifecycle](M_Door_Lifecycle.md)).
- **Realm instance** with its nodes, mobs and dropped cargo (owned by [M_Realm_Instancing](M_Realm_Instancing.md)).
- **Pressure level** (owned by [M_Realm_Pressure](M_Realm_Pressure.md)), read by mob spawning.
- **Active letters** (owned by [M_Letter_Flow](../Orders/M_Letter_Flow.md)), read by node and mob spawning guarantees.

## UI

- [UI_Realm_Pressure](../../05_UI/Hud/UI_Realm_Pressure.md)

## Open Questions

-
