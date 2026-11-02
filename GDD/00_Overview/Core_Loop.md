---
id: Core_Loop
type: overview
status: Draft
---

# Core Loop

> **Vision:** [Vision](Vision.md) · **Features:** [_Feature_List](../01_Features/_Feature_List.md)

## Session Loop

```
+-------------------------------------------------------------+
|                     1. COMMISSION PHASE                     |
|  - Letters arrive via the Nexus Mailbox                     |
|  - Team reviews client requirements, deadlines & rewards    |
|  - Strategy discussion: select which orders to fulfill      |
+------------------------------+------------------------------+
                               |
                               v
+-------------------------------------------------------------+
|                    2. EXPEDITION PHASE                      |
|  - Step through Magic Doors into dimensional realms         |
|  - Harvest resource nodes (ore veins, arcane timber)        |
|  - Hunt & defeat monsters for organic magical ingredients   |
|  - Return to workshop through the gateway                   |
+------------------------------+------------------------------+
                               |
                               v
+-------------------------------------------------------------+
|                    3. REFINEMENT & CRAFT                    |
|  - Manual processing (no automation): smelt, carve, refine  |
|  - 2-piece modular assembly (Hilt+Blade or Shaft+Core)      |
|  - Optional timing mini-games for quality bonuses           |
+------------------------------+------------------------------+
                               |
                               v
+-------------------------------------------------------------+
|                    4. DISPATCH & PROGRESSION                |
|  - Package and dispatch weapons via the Mailbox Nexus       |
|  - Collect gold, client reputation, and rare catalysts      |
|  - Upgrade workshop tiers, buy new Magic Doors              |
|  - Contribute materials to the ultimate UBER-WEAPON forge   |
+-------------------------------------------------------------+
```

| Step | Owner |
| --- | --- |
| 1. Commission | [F01_Commissions](../01_Features/F01_Commissions.md) · [M_Letter_Flow](../02_Systems/Orders/M_Letter_Flow.md) |
| 2. Expedition | [F03_Expeditions](../01_Features/F03_Expeditions.md) · [F04_Combat](../01_Features/F04_Combat.md) |
| 3. Refinement & Craft | [F02_Weapon_Crafting](../01_Features/F02_Weapon_Crafting.md) |
| 4. Dispatch & Progression | [M_Letter_Flow](../02_Systems/Orders/M_Letter_Flow.md) · [F05_Shop_Progression](../01_Features/F05_Shop_Progression.md) · [F06_Uber_Weapon](../01_Features/F06_Uber_Weapon.md) |

## Moment-to-Moment Loop

Move ([_Movement_System](../02_Systems/Movement/_Movement_System.md)), pick up, carry and place objects ([_Interaction_System](../02_Systems/Interaction/_Interaction_System.md)), work stations and nodes with hold interactions ([M_Continuous_Interaction](../02_Systems/Interaction/M_Continuous_Interaction.md)), and fight with one simple attack per weapon family ([_Combat_System](../02_Systems/Combat/_Combat_System.md)).

## Meta Loop

Gold and reputation from commissions buy workshop tiers and Magic Doors ([F05_Shop_Progression](../01_Features/F05_Shop_Progression.md)); Apex Guardians yield the four Primordial Catalysts; the Uber-Weapon ritual ends the campaign and unlocks Prestige Endless Mode ([F06_Uber_Weapon](../01_Features/F06_Uber_Weapon.md)).

## Pacing & Anti-Downtime

Players who stay in the workshop are never stranded waiting for expedition players:

1. **Self-paced but pressured expeditions:** no time limit inside realms; letter deadlines, backpack capacity and rising Realm Pressure push teams home, so most runs stay short while deep dives remain possible. → [_Exploration_System](../02_Systems/Exploration/_Exploration_System.md)
2. **Entry window:** a door accepts new entrants only for a short window after opening; teams decide together who goes in. → [M_Door_Lifecycle](../02_Systems/Exploration/M_Door_Lifecycle.md)
3. **Shop preparation and asynchronous work:** while combatants gather mob drops, workshop players refine stockpiled wood, smelt ores or prepare standard hilts and shafts. The [E_Aether_Chute](../03_Entities/Props/Interactive/E_Aether_Chute.md) keeps raw materials flowing mid-run.
4. **Omni-role flexibility:** any player can work any bench at any time, or open another owned door after missing an entry window.

## Open Questions

-
