---
id: _Networking_Module
type: module
module: Networking
namespace: Armotheca.Networking
status: Draft
---

# Networking Module

> **Design:** [F07_Co_Op](../../GDD/01_Features/F07_Co_Op.md) · **Map:** [_Module_Map](../_Module_Map.md) · **Overview:** [Technical Overview](../Technical_Overview.md) · **Roadmap:** [Networking-First Principle](../../Development_Phases/Development_Roadmap.md#networking-first-principle)

## Scope

Session, lobby and transport bootstrap: hosting, joining through Steam lobbies, disconnect / rejoin and the FishNet setup every other module builds on. Each gameplay module documents its own authority and replication in its Networking section.

| GDD doc | Implemented in |
| --- | --- |
| [F07_Co_Op](../../GDD/01_Features/F07_Co_Op.md) | [Setup](#setup) |

---

## Setup

- **Topology:** Host mode. The hosting player starts both server and client (`ServerManager.StartConnection()` then `ClientManager.StartConnection()`); other players join as clients through a Steam lobby.
- **Transport:** `FishySteamworks` component on the `TransportManager`, **Peer To Peer** enabled. During development use Steam's test App ID 480 until Armotheca has its own App ID.
- **Scenes:** FishNet `SceneManager` loads the workshop globally and realm scenes additively (see [Realms](../Exploration/Realm_Loading.md)). Scene-based observer conditions limit realm objects' replication to players inside that realm.
- **Time:** Server time comes from FishNet's `TimeManager` (ticks); timestamps in door, order and pressure logic use it instead of `Time.timeAsDouble`.
- **Prediction:** Not used initially (co-op PvE, owner-authoritative movement). FishNet's prediction and lag compensation remain available if playtests show combat timing problems under latency.
- **Testing:** Multiple editor instances (e.g. ParrelSync or a second build) for local multiplayer testing; Steam relay tests with two Steam accounts.

### Phase 1 Spike (must pass before committing further)
1. Host a session on Unity 6.3 LTS with the current FishNet 4.x and FishySteamworks; join through a Steam lobby; disconnect and rejoin.
2. Confirm the FishySteamworks release works with the current FishNet version (its latest notes only mention FishNet 4.1).
3. Measure round-trip time and bandwidth with 4 players over Steam relay.

---

## Open Technical Questions

- Host migration: see [Technical Overview › Open Technical Decisions](../Technical_Overview.md#8-open-technical-decisions).
