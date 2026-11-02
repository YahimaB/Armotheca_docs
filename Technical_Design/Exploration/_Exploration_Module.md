---
id: _Exploration_Module
type: module
module: Exploration
namespace: Armotheca.Exploration
status: Draft
---

# Exploration Module

> **Design:** [_Exploration_System](../../GDD/02_Systems/Exploration/_Exploration_System.md) · **Map:** [_Module_Map](../_Module_Map.md) · **Overview:** [Technical Overview](../Technical_Overview.md)

## Scope

| GDD doc | Implemented in |
| --- | --- |
| [M_Door_Lifecycle](../../GDD/02_Systems/Exploration/M_Door_Lifecycle.md) | [Door_Instances](Door_Instances.md) |
| [M_Door_Purchase](../../GDD/02_Systems/Exploration/M_Door_Purchase.md) | [_Progression_Module](../Progression/_Progression_Module.md#technical-specifications) (purchase); [Door_Instances](Door_Instances.md) (locked state) |
| [M_Realm_Instancing](../../GDD/02_Systems/Exploration/M_Realm_Instancing.md) | [Realm_Loading](Realm_Loading.md) |
| [M_Harvesting](../../GDD/02_Systems/Exploration/M_Harvesting.md), [M_Node_Spawning](../../GDD/02_Systems/Exploration/M_Node_Spawning.md) | [Resource_Nodes](Resource_Nodes.md) |
| [M_Mob_Spawning](../../GDD/02_Systems/Exploration/M_Mob_Spawning.md), [M_Realm_Pressure](../../GDD/02_Systems/Exploration/M_Realm_Pressure.md) | [Mob_AI](Mob_AI.md) |
| [_Mob_Roster](../../GDD/03_Entities/Mobs/_Mob_Roster.md) and its mobs | [Mob_AI](Mob_AI.md) |
| [E_Magic_Door](../../GDD/03_Entities/Props/Interactive/E_Magic_Door/E_Magic_Door.md), [E_Exit_Portal](../../GDD/03_Entities/Props/Interactive/E_Exit_Portal/E_Exit_Portal.md), [E_Aether_Chute](../../GDD/03_Entities/Props/Interactive/E_Aether_Chute/E_Aether_Chute.md) | [Door_Instances](Door_Instances.md) |
| [E_Mineral_Vein](../../GDD/03_Entities/Props/Resource_Nodes/E_Mineral_Vein/E_Mineral_Vein.md), [E_Arcane_Flora](../../GDD/03_Entities/Props/Resource_Nodes/E_Arcane_Flora/E_Arcane_Flora.md) | [Resource_Nodes](Resource_Nodes.md) |
| [_World_Map](../../GDD/04_Locations/_World_Map.md) and realms L01–L04 | [Realm_Loading](Realm_Loading.md) |

Topics:

- [Door_Instances](Door_Instances.md): door state machine, membership, exit portal and drop-chute.
- [Realm_Loading](Realm_Loading.md): realm scenes, lifetime, population and isolation.
- [Resource_Nodes](Resource_Nodes.md): node definitions, spawn tables and harvesting.
- [Mob_AI](Mob_AI.md): mob definitions, archetype FSM, `MobDirector` and Realm Pressure.

---

## Shared State

- **Door membership and timestamps** (`DimensionalDoor`, host): who may enter, when entry closes, when the door is ready again.
- **Realm instance** (`RealmInstance`, owned by its door): loaded scene, `RealmSeed`, occupancy flag, populated nodes and mobs.
- **Pressure level** (`MobDirector`, host): advances only while the realm is occupied.
- **Active-letter material set** (from [_Orders_Module](../Orders/_Orders_Module.md)): read by node and mob population guarantees.

---

## Networking

- All realm logic (doors, population, nodes, mobs, pressure) runs on the host.
- Realm scenes load additively per connection through FishNet's `SceneManager`; scene observer conditions keep realm traffic away from players in the workshop ([Realm_Loading › Networking](Realm_Loading.md#networking)).
- Movement into and out of realms is a host-approved `[TargetRpc]` teleport because movement is owner-authoritative ([Door_Instances › Networking](Door_Instances.md#networking)).

---

## Events

| Event | Raised when | Consumed by |
| --- | --- | --- |
| `DimensionalDoor.OnStateChanged` | Door state changes | Door visuals, prompts |
| `DimensionalDoor.OnMembersChanged` | Expedition membership changes | Sealed-door member names |
| `ExitPortal.OnUsed` | A player leaves the realm | Door occupancy |
| `AetherDropChute.OnItemShipped` | An item is deposited | Workshop receiving basket |
| `ResourceNode.OnStruck` | A node takes a hit | Node VFX / SFX, ambusher wake-up |
| `MobBrain.OnTelegraph` | A mob starts its wind-up | Telegraph VFX / SFX |
| `MobDirector.OnPressureLevelChanged` | Pressure level rises | [UI_Realm_Pressure](../../GDD/05_UI/Hud/UI_Realm_Pressure.md), audio cue |

---

## Testing Notes

Per topic: [Door_Instances › Testing Notes](Door_Instances.md#testing-notes).

---

## Open Technical Questions

- Realm loading strategy: see [Technical Overview › Open Technical Decisions](../Technical_Overview.md#8-open-technical-decisions).
