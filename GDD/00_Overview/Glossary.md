---
id: Glossary
type: overview
status: Draft
---

# Glossary

> **Vision:** [Vision](Vision.md)

## Document Types

| Term | Definition | Canonical doc |
| --- | --- | --- |
| Feature | A player-facing capability that serves a pillar and is prioritised and scheduled. A hub that links mechanics, entities, locations and UI; it has no rules of its own. | [_Feature_List](../01_Features/_Feature_List.md) |
| System | A group of mechanics that share state; same name as its code module. | [02_Systems](../02_Systems) |
| Mechanic | One rule set the player acts through. | `M_` docs |
| Entity | A thing that exists in the world or inventory: player, mob, client, item, prop. | `E_` docs |
| Location | A place: the workshop or a realm. | [_World_Map](../04_Locations/_World_Map.md) |
| UI | A screen, HUD element, world-space display or shared widget. | [_UI_Flow](../05_UI/_UI_Flow.md) |
| Balancing sheet | The only place tunable numbers live. | [06_Balancing](../06_Balancing) |

## Game Terms

| Term | Definition | Canonical doc |
| --- | --- | --- |
| Quality | Weapon and component stat, 1–100, produced by manual processing. | [M_Quality](../02_Systems/Crafting/M_Quality.md) |
| Quality Tier | Named band of Quality: Crude, Standard, Masterwork, Flawless. | [M_Quality](../02_Systems/Crafting/M_Quality.md) |
| Base Damage | Weapon stat; a constant of the payload material. | [M_Quality](../02_Systems/Crafting/M_Quality.md) |
| Element | Non-numeric material identity of a payload (Physical, Fire, Frost, Lightning, Arcane, Holy). | [_Item_List](../03_Entities/Items/_Item_List.md) |
| Foundation | The component that defines the weapon category: Hilt, Short Shaft or Long Shaft. | [M_Assembly](../02_Systems/Crafting/M_Assembly.md) |
| Payload | The component that defines Base Damage and Element: Blade or Core. | [M_Assembly](../02_Systems/Crafting/M_Assembly.md) |
| Commission / Letter | An order from a client, with criteria, deadline, reward and penalty. | [M_Letter_Flow](../02_Systems/Orders/M_Letter_Flow.md) |
| Client Archetype | The faction behind a letter, which shapes its demands and stakes. | [_Client_Roster](../03_Entities/NPCs/Clients/_Client_Roster.md) |
| Workshop Tier | Shop progression level that unlocks stations, clients and doors. | [M_Workshop_Tiers](../02_Systems/Progression/M_Workshop_Tiers.md) |
| Magic Door | A purchasable door in the workshop that opens onto one realm. | [E_Magic_Door](../03_Entities/Props/Interactive/E_Magic_Door/E_Magic_Door.md) |
| Expedition | One run through an opened door, from opening until the realm empties. | [M_Door_Lifecycle](../02_Systems/Exploration/M_Door_Lifecycle.md) |
| Expedition Member | A player who entered during the entry window; only members may re-enter afterwards. | [M_Door_Lifecycle](../02_Systems/Exploration/M_Door_Lifecycle.md) |
| Entry Window | The short period after opening during which anyone may enter a door. | [M_Door_Lifecycle](../02_Systems/Exploration/M_Door_Lifecycle.md) |
| Band | One of a realm's areas: Entry, Outer Grounds, Deep Grounds, Apex Arena. | [_World_Map](../04_Locations/_World_Map.md) |
| Realm Pressure | Danger level that rises while a realm is occupied. | [M_Realm_Pressure](../02_Systems/Exploration/M_Realm_Pressure.md) |
| Downed | Player state at 0 health; can be revived until bleed-out. | [M_Health_And_Downed](../02_Systems/Combat/M_Health_And_Downed.md) |
| Primordial Catalyst | Unique Uber-Weapon ingredient dropped by an Apex Guardian. | [E_Primordial_Catalyst](../03_Entities/Items/Catalysts/E_Primordial_Catalyst/E_Primordial_Catalyst.md) |
| Uber-Weapon | The Primordial Armament; forging it wins the campaign. | [F06_Uber_Weapon](../01_Features/F06_Uber_Weapon.md) |
