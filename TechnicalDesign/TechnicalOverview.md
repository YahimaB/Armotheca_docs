# Armotheca - Technical Overview

> Technical counterpart of the [Master GDD](../GDD/MasterGDD.md). Each mechanic's technical document mirrors its GDD document at the same path under `TechnicalDesign/`.

## 1. Technology Stack (Decided)

| Area | Decision | Notes |
|---|---|---|
| **Engine** | **Unity 6.3 LTS** (latest 6000.3.x patch) | Supported until December 2027. Planned single upgrade to 6.7 LTS mid-production (see §6). |
| **Architecture** | **GameObjects + MonoBehaviours, no ECS** | Data/runtime split with ScriptableObjects and plain C# domain logic (§3). Jobs + Burst allowed for isolated hot spots. |
| **Networking** | **FishNet (Fish-Networking) 4.x** | Player-hosted: one player runs server and client in the same process (FishNet host mode). |
| **Transport** | **FishySteamworks** on **Steamworks.NET** | Steam peer-to-peer through Steam's relay; host IP is never revealed. Steam lobbies for invites and joining. |
| **UI** | **uGUI only** (+ TextMeshPro) | Screen Space canvases for menus/HUD, World Space canvases for diegetic UI. UI Toolkit is not used. |
| **Input** | Unity Input System | Action maps for keyboard/mouse and gamepad; full remapping. |
| **Platforms** | PC (Steam): Windows; Steam Deck (Linux/Proton) | FishySteamworks supports Windows, macOS, Linux. |

### Why these choices (summary)
- **No ECS:** At 1–4 players, ≤20 mobs and ~40 nodes per realm there is no performance need. Unity Entities is mid-transition ("ECS for all", CoreCLR) and would force Netcode for Entities; LeoECS Proto has a very small community and no networking integration.
- **FishNet:** Free, actively maintained, mature host mode, built-in client prediction and lag compensation available if combat needs them later, and a first-class Steam transport.
- **uGUI only:** Proven world-space canvases for the game's heavily diegetic UI, Animator/particle support, built-in gamepad navigation; one UI system for the whole team.
- **Unity 6.3 LTS:** Current LTS with the longest runway; FishNet supports Unity 6 LTS. 6.0 LTS ends support in October 2026; 6.7 is still in beta.

---

## 2. Target Specifications

- **Target Framerate:** Solid 60 FPS on mid-tier hardware (GTX 1660 / Ryzen 5 3600) and on Steam Deck.
- **Session:** 1–4 players, one of them hosting. Drop-in / drop-out through Steam lobbies.
- **Network tick:** FishNet `TimeManager` tick rate 30 Hz (initial value; raise if combat feel requires it).
- **Physics & Interaction:** Kinematic character controller with overlap-based interaction and snap-to-socket placement.
- **Data Architecture:** ScriptableObject-driven definitions (materials, weapons, mobs, realms, doors, orders) with plain C# runtime models that are serializable and unit-testable.

---

## 3. Architecture Principles

- **Data / Runtime split:** ScriptableObjects (`*Definition`) hold static design data. Runtime state lives in plain C# classes or structs that can be sent over the network as IDs + small values.
- **Host authority for game state:** The host (FishNet server side) owns orders, station state, node/mob health, door state and progression. Clients send intents via `[ServerRpc]` and receive results via `SyncVar<T>` / `SyncList<T>` / `[ObserversRpc]`.
- **Owner authority for movement:** Each client simulates its own character for responsiveness (FishNet `NetworkTransform` with client authority); the host validates and relays (see [Movement](Common/Movement.md)).
- **Events over polling:** Systems expose C# events (`OnX`) consumed by UI, audio and VFX, keeping presentation decoupled.
- **Small, testable domain logic:** Rules such as weapon assembly, order validation and quality tiers are pure functions with no `MonoBehaviour` or networking dependency. Switching the network layer would not touch them.
- **Reference code convention:** Code samples in the technical docs are written as plain `MonoBehaviour`s for readability. In production, networked components derive from FishNet's `NetworkBehaviour`, server-only logic is guarded with `IsServerInitialized` / `[Server]`, and the "host RPCs" described in each doc are `[ServerRpc]` methods.

---

## 4. Networking Setup (FishNet + FishySteamworks)

- **Topology:** Host mode. The hosting player starts both server and client (`ServerManager.StartConnection()` then `ClientManager.StartConnection()`); other players join as clients through a Steam lobby.
- **Transport:** `FishySteamworks` component on the `TransportManager`, **Peer To Peer** enabled. During development use Steam's test App ID 480 until Armotheca has its own App ID.
- **Scenes:** FishNet `SceneManager` loads the workshop globally and realm scenes additively (see [Realms](Exploration/Realms.md)). Scene-based observer conditions limit realm objects' replication to players inside that realm.
- **Time:** Server time comes from FishNet's `TimeManager` (ticks); timestamps in door, order and pressure logic use it instead of `Time.timeAsDouble`.
- **Prediction:** Not used initially (co-op PvE, owner-authoritative movement). FishNet's prediction and lag compensation remain available if playtests show combat timing problems under latency.
- **Testing:** Multiple editor instances (e.g. ParrelSync or a second build) for local multiplayer testing; Steam relay tests with two Steam accounts.

### Phase 1 Spike (must pass before committing further)
1. Host a session on Unity 6.3 LTS with the current FishNet 4.x and FishySteamworks; join through a Steam lobby; disconnect and rejoin.
2. Confirm the FishySteamworks release works with the current FishNet version (its latest notes only mention FishNet 4.1).
3. Measure round-trip time and bandwidth with 4 players over Steam relay.

---

## 5. Shared Types (`Armotheca.Core`)

Types referenced by several zones are defined once:

```csharp
namespace Armotheca.Core
{
    public enum ElementType
    {
        Physical,
        Fire,
        Frost,
        Lightning,
        Arcane,
        Holy
    }

    [System.Serializable]
    public struct DropEntry
    {
        public string ItemId;
        [UnityEngine.Range(0f, 1f)] public float Chance;
        public int MinQuantity;
        public int MaxQuantity;
    }

    public static class DropRoller
    {
        public static void Roll(System.Collections.Generic.IEnumerable<DropEntry> table,
                                System.Random rng,
                                System.Collections.Generic.List<string> results)
        {
            foreach (var entry in table)
            {
                if (rng.NextDouble() > entry.Chance) continue;
                int qty = rng.Next(entry.MinQuantity, entry.MaxQuantity + 1);
                for (int i = 0; i < qty; i++) results.Add(entry.ItemId);
            }
        }
    }
}
```

- Drop rolls take an explicit `System.Random` seeded by the host so results are deterministic and reproducible in tests.

---

## 6. Engine Upgrade Plan

| When | Version | Condition |
|---|---|---|
| Start of production | Unity 6.3 LTS | — |
| After the Phase 2 multiplayer milestone | Unity 6.7 LTS | Only once 6.7 LTS is released and FishNet/FishySteamworks list it as supported. Needed because 6.3 support ends December 2027, close to launch. |
| Not before launch | Unity 6.8+ (CoreCLR) | FishNet relies on Unity's IL post-processing for code generation; wait for explicit FishNet support. |

---

## 7. Code Organization

| Namespace | Zone | Documents |
|---|---|---|
| `Armotheca.Core` | Shared | Shared types (§5) |
| `Armotheca.Networking` | Shared | Session, lobby and transport bootstrap (§4) |
| `Armotheca.Movement` | Common | [Movement](Common/Movement.md) |
| `Armotheca.Interaction` | Common | [Object Interaction](Common/ObjectInteraction.md) |
| `Armotheca.Combat` | Common | [Combat](Common/Combat.md) |
| `Armotheca.Crafting` | Shop | [Weapon Crafting](Shop/WeaponCrafting.md) |
| `Armotheca.Shop` | Shop | [Resource Processing](Shop/ResourceProcessing.md) |
| `Armotheca.Orders` | Shop | [Order System](Shop/OrderSystem.md) |
| `Armotheca.Progression` | Shop | [Shop Progression](Shop/ShopProgression.md) · [Uber-Weapon](Shop/UberWeapon.md) |
| `Armotheca.Exploration` | Exploration | [Magic Doors](Exploration/MagicDoors.md) · [Realms](Exploration/Realms.md) · [Resource Gathering](Exploration/ResourceGathering.md) · [Mobs](Exploration/Mobs.md) |
| `Armotheca.UI` | Shared | [UI Design](../UIDesign/Mailbox/LetterCommissionBoard.md) (uGUI views) |

---

## 8. Open Technical Decisions

| Decision | Options | Notes |
|---|---|---|
| Realm loading | Additive scenes at offsets vs separate physics scenes | See [Realms](Exploration/Realms.md). |
| Save format | JSON vs binary | Progression persistence, see [Shop Progression](Shop/ShopProgression.md). |
| Host migration | None (session ends if host leaves) vs custom migration | Default: session ends and players return to the main menu; progression is saved on the host's machine. |

---

## 9. Documentation Standards (Technical Docs)

Each technical document contains, where relevant:
1. **Technical Specifications & Performance Targets** (tick rates, memory, network budget).
2. **Architecture & Implementation Approaches** with trade-offs (SOLID/GRASP, MonoBehaviour vs ScriptableObject).
3. **Networking** (authority, what is synchronized, FishNet mechanisms used).
4. **Unity C# Reference Code** (interfaces, managers, network-ready events).
