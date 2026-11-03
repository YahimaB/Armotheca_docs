# Phase 1: Core Loop & Workshop Prototype — Weekly Plan

> Part of the [Development Roadmap](Development_Roadmap.md) · Design: [Vision](../GDD/00_Overview/Vision.md) · Tech: [Technical Overview](../Technical_Design/Technical_Overview.md) · Naming: [Assets Naming](../Guidelines/Assets_Naming.md) · Art specs: [Modeling Guidelines](../Guidelines/Modeling_Guidelines.md)

**Duration:** 13 weeks (Months 1–3)
**Focus:** Prove the common mechanics, physical crafting and 2-piece assembly — **networked from the first week** (host + clients over FishNet / FishySteamworks), following the [Networking-First Principle](Development_Roadmap.md#networking-first-principle).

---

## Phase Goal

A team (1–2 players for the milestone, tested up to 4) can take a letter, step into a door, chop wood, mine ore, kill 1 mob, return to the shop, smelt a blade, carve a hilt, assemble a sword, and deliver it for gold in **under 5 minutes** — with the host and every client seeing the same world state at every step.

## How to Read This Plan

Each week lists:
1. **Required sources** — what must be delivered to the implementer **before the week starts** (models, textures, animations, audio, data values, decisions, accounts). Items marked *placeholder OK* can be replaced by greybox primitives, Unity built-in shapes or free stand-ins; the final asset can be swapped in later without code changes, as long as it keeps the names, pivots and sockets defined in the [Modeling Guidelines](../Guidelines/Modeling_Guidelines.md).
2. **Work this week** — what gets built.
3. **Networking** — what is synchronized and who owns it. Every feature is accepted only when it works for the host **and** a connected client.
4. **Done when** — the acceptance check at the end of the week.

All assets follow the naming in [Assets Naming](../Guidelines/Assets_Naming.md) and are delivered into `Assets/_Project/...`. Source files (`.blend`, `.spp`, `.psd`) stay outside `Assets/`.

### Global Definition of Done (every week)
- Works in a session with **host + at least 1 client** (Multiplayer Play Mode / ParrelSync locally); single-player is simply a host with no clients.
- A client that joins **after** the action sees the correct current state (late-join).
- A client disconnecting mid-action leaves no stuck state on the host (locks, occupied sockets, held items released).
- Domain rules (quality, assembly, verification, drops) are plain C# with EditMode tests; randomness uses a host-seeded `System.Random`; times use FishNet `TimeManager` ticks.

### Overview

| Week | Theme | Main Output |
|---|---|---|
| 1 | Project & network foundation | Unity project, folder/asmdef structure, host/join locally |
| 2 | Networked player & movement | Walk, sprint, jump, roll for every connected player |
| 3 | Steam lobby & networking spike | Join through Steam, RTT/bandwidth measured — **go/no-go gate** |
| 4 | Interaction & carry model | Pick up, drop, place, take, hand over; hands / weapon slot / backpack |
| 5 | Continuous interactions & workshop greybox | Hold-to-work with helpers, station framework, workshop layout |
| 6 | Blade pipeline | Smelting Forge, Anvil mini-game, Quenching Basin |
| 7 | Foundation & core pipelines | Lathe + Carving Bench, Arcane Extractor + Distiller |
| 8 | Assembly bench & weapons | 2-piece assembly, weapon naming, equip |
| 9 | Mailbox & letters | Guild letters, board, dispatch, verification, gold |
| 10 | Combat (player side) | Sword chain, magic orb, health, downed, revive |
| 11 | Magic Door & Verdant realm | Door lifecycle, realm loading, Exit Portal, node spawning & harvesting |
| 12 | Bramble Stalker | Networked mob AI, damage, drops, letter guarantee |
| 13 | Integration, playtest & performance | Full 5-minute loop, 4-player test, budget check, buffer |

---

## Week 1 — Project & Network Foundation

**Goal:** A clean Unity project where two instances can host and join a FishNet session on the same machine.

### Required sources
| Source | Type | Notes |
|---|---|---|
| Git repository with **Git LFS** enabled | Infrastructure | LFS tracking for fbx, png, tga, psd, wav, ogg (see naming guide §3). |
| Confirmed versions: Unity 6.3 LTS patch, FishNet 4.x, FishySteamworks, Steamworks.NET | Decision | Exact versions to pin in the manifest. |
| Render pipeline confirmation (**URP** assumed) | Decision | Decided: URP ([Technical Overview §1](../Technical_Design/Technical_Overview.md#1-technology-stack-decided)). |
| Steam client installed + Steam test **App ID 480** | Account | Used until Armotheca has its own App ID. |

### Work this week
- Create the project on Unity 6.3 LTS with URP; set up `Assets/_Project/` folder structure, one `.asmdef` per namespace (`Armotheca.Core`, `Armotheca.Networking`, …) and `Tests/EditMode` + `Tests/PlayMode`.
- Install FishNet, FishySteamworks and Steamworks.NET; create `PF_Network_NetworkManager` (in `Prefabs/Network/`) with `TimeManager` at 30 Hz.
- Scenes: `Boot` (initializes services) → `MainMenu` (Host / Join buttons, placeholder uGUI) → `Workshop` (empty plane).
- Use FishNet's **Tugboat** transport for local tests and FishySteamworks for Steam; switchable from a `Settings_Network` asset.
- Set up local multiplayer testing (Unity Multiplayer Play Mode or ParrelSync).
- `Armotheca.Core` shared types (`ElementType`, `DropEntry`, `DropRoller`) with tests.

### Networking
- Host mode bootstrap (`ServerManager.StartConnection()` + `ClientManager.StartConnection()`), client join, clean shutdown; on host leave, clients return to `MainMenu`.
- FishNet `SceneManager` loads `Workshop` globally for all connections.

### Done when
- Two editor instances: one hosts, the other joins, both load `Workshop`; closing the host returns the client to `MainMenu`.

---

## Week 2 — Networked Player & Movement

**Goal:** Every connected player has a character with the full move set (walk, sprint, jump, roll), seen correctly by everyone.

### Required sources
| Source | Type | Notes |
|---|---|---|
| `SK_Character_<Name>` player mesh, Humanoid rig | Skeletal mesh | *Placeholder OK* (capsule or a free Humanoid such as Unity's starter character). 20–30k tris, ≤75 bones when final. |
| Locomotion clips: `A_Player_Idle`, `A_Player_Walk`, `A_Player_Sprint`, `A_Player_JumpStart`, `A_Player_JumpLoop`, `A_Player_Land`, `A_Player_Roll` | Animations | *Placeholder OK* (free Humanoid clips, e.g. Mixamo). |
| 4 distinct player tint colors | Decision | So players are distinguishable before final characters exist. |
| Camera reference: distance, height, angle, follow behaviour | Decision | Third person; affects art budgets (Modeling Guidelines §11). A short video or screenshot from a reference game is enough. |
| Gamepad (Xbox or PlayStation) | Hardware | For input testing. |

### Work this week
- `IA_Player` Input Actions (keyboard/mouse + gamepad): move, sprint, jump, roll, interact, secondary, attack.
- Kinematic character controller per [Technical_Design/Movement](../Technical_Design/Movement/_Movement_Module.md): walk/sprint, jump with coyote time and buffer, roll with cooldown and invulnerability window flag, values from `Settings_Movement`.
- Character state machine matching the GDD state table (grounded, airborne, rolling, carrying, interacting, downed — the last three as stubs).
- `AC_Player` with a locomotion blend tree; third-person camera following the local player only.

### Networking
- Player prefab is a `NetworkObject` spawned per connection by the host.
- Movement is **owner-authoritative** (`NetworkTransform` client authority); the host validates speed limits.
- Animation parameters synchronized (`NetworkAnimator` or synced state enum); roll and invulnerability state replicated so later combat can trust it.
- Input and camera are enabled only for the owning client.

### Done when
- 2–4 local instances move, sprint, jump and roll; each sees the others' animations correctly, without jitter at 30 Hz tick.

---

## Week 3 — Steam Lobby & Networking Spike (Go / No-Go Gate)

**Goal:** Play over the internet through Steam, and verify the networking stack before building gameplay on it.

### Required sources
| Source | Type | Notes |
|---|---|---|
| 2–4 Steam accounts on separate machines (at least 2 locations / networks) | Test setup | For relay and latency tests. |
| Testers available for one 30-minute session | People | 4 players ideally, 2 minimum. |
| Main menu / lobby layout sketch | Design | *Placeholder OK* — functional uGUI is enough; final style comes later. |

### Work this week
- `Armotheca.Networking`: Steam lobby create, invite friends (Steam overlay), join by invite, lobby member list (`Lobby_Screen`, `Player_Widget`), host starts the game.
- Disconnect and rejoin flow; host leaving ends the session for everyone (decided default).
- Lag/packet-loss simulation settings for local tests.
- Network stats overlay (debug only): RTT, bytes in/out per second, tick.
- Spike report: RTT and bandwidth with 2 and 4 players over Steam relay; confirm FishySteamworks works with the installed FishNet version.

### Networking
- Transport: FishySteamworks peer-to-peer over Steam relay; host IP never exposed.

### Done when
- Spike checklist in the [Technical Overview §4](../Technical_Design/Technical_Overview.md) passes and results are written into it.
- **Gate:** if FishySteamworks or FishNet fails on Unity 6.3, stop and decide on a fallback before Week 4.

---

## Week 4 — Interaction & Carry Model

**Goal:** Players physically pick up, carry, drop, place and hand over items, and every player sees who holds what.

### Required sources
| Source | Type | Notes |
|---|---|---|
| Carried test items: `SM_Common_IronOre`, `SM_Common_ArcaneOakLog`, `SM_Common_Crate` | Static meshes | *Placeholder OK.* Pivot at grip point; small prop budget 200–1,200 tris. |
| Carry clips: `A_Player_CarryIdle`, `A_Player_CarryWalk`, `A_Player_PickUp`, `A_Player_Place`; Avatar Mask `AM_Player_UpperBody` | Animations | *Placeholder OK* (arms-forward pose). |
| Prompt font and frame: `FNT_<Family>_Regular`, `UI_Frame_Prompt_9S`, gamepad/keyboard button glyph sprites | UI | *Placeholder OK* (TMP default font). |
| Item list for Phase 1 with display names (raw → processed → weapon) | Data | See the material table in Week 6–8; can be finalized then. |

### Work this week
- `Armotheca.Interaction` per [Technical_Design/Object_Interaction](../Technical_Design/Interaction/_Interaction_Module.md): best-target selection (1.8 m reach, facing bias), single `Interact_Prompt` with verb + object name, invalid-action reasons (`Hands full`, `Wrong part for this socket`).
- `ItemDefinition` ScriptableObjects and networked world item prefab.
- Carry model: **Hands** (1 item), **Weapon Slot** (1 weapon), **Backpack** (6 raw resources).
- Instant interactions: pick up, drop, place/snap into socket, take, hand over to teammate, generic open/use.
- Generic `ItemSocket` component (accepts item types) for counters, crates and later stations.
- Carrying blocks roll/attack and applies the 0.85x speed multiplier.

### Networking
- Clients send interaction **intents** (`[ServerRpc]`); the host validates distance, state and target, then applies the result.
- Item ownership (world / player hands / socket) is host-owned state (`SyncVar`); held items are parented visually on every client.
- Conflict rule: two players grabbing the same item — the first request the host processes wins, the other gets a reason.
- Disconnect: a disconnected player's hands contents drop at their last position.

### Done when
- Two players can pass an item back and forth, place it in a crate socket, take it out, and a client joining afterwards sees the item in the correct place.

---

## Week 5 — Continuous Interactions, Station Framework & Workshop Greybox

**Goal:** Hold-to-work interactions with cooperative helpers, a reusable workstation base, and a workshop layout to place stations in.

### Required sources
| Source | Type | Notes |
|---|---|---|
| Workshop layout plan (top-down sketch): door wall (Threshold of Portals), mailbox, forge corner, wood corner, extractor, assembly bench, storage crates | Design | Required — even a hand drawing with rough sizes. Doorways ≥1.4 m × 2.4 m. |
| Modular architecture kit: walls 2 m / 4 m, floor tile, beam, doorway | Static meshes | *Placeholder OK* (ProBuilder greybox). |
| Storage crate `SM_Shop_StorageCrate` | Static mesh | *Placeholder OK.* |
| Progress bar sprites `UI_Bar_Progress`, `Fill` | UI | *Placeholder OK.* |
| Work loop clip `A_Player_WorkGeneric` | Animation | *Placeholder OK.* |

### Work this week
- Continuous interactions: hold to progress, release pauses, progress kept 5 s then decays; interrupted by moving away, roll, hit.
- Cooperative helpers (max helpers per object, +50% speed per extra helper) and exclusive objects (`Busy` prompt).
- `Workstation` base: input socket(s), output socket, processing state machine, recipe lookup (`ProcessingRecipe` assets), world-space progress `Marker`.
- Storage crate holding raw resources (backpack unload per item / hold to unload all).
- `Workshop` greybox scene built from the layout plan, with lighting placeholder.

### Networking
- Continuous interaction progress is **host-simulated** from helpers' held-input state; clients receive progress via `SyncVar` (no per-frame RPCs).
- Station state (`Idle / Loaded / Working / Done`) and sockets are host-owned and late-join safe.
- A helper disconnecting is removed from the helper list; progress continues per the decay rule.

### Done when
- Two players hold-work a test station together and finish it faster than one; the workshop greybox is walkable with all station spots marked.

---

## Week 6 — Blade Pipeline: Smelting Forge, Anvil, Quenching Basin

**Goal:** Iron Ore becomes an Iron Blade with a Quality value produced by player skill.

### Required sources
| Source | Type | Notes |
|---|---|---|
| `SM_Shop_SmeltingForge` with `Part_Bellows`, `Socket_Input`, `Interact_Point` | Workstation mesh | *Placeholder OK* for week; final 6–15k tris, sockets as named empties. |
| `SM_Shop_Anvil` with `Socket_Input`, `Interact_Point` | Workstation mesh | *Placeholder OK.* |
| `SM_Shop_QuenchingBasin` with `Socket_Input`, `Socket_Output` | Workstation mesh | *Placeholder OK.* |
| Tongs `SM_Shop_Tongs`, items `SM_Common_HotIngot_Iron`, `SM_Weapon_Blade_Iron` (pivot at connection point) | Static meshes | *Placeholder OK*, but the blade must follow the standard connector rule ([_Components_Art](../GDD/03_Entities/Items/Components/_Components_Art.md)). |
| Clips: `A_Player_PumpBellows`, `A_Player_HammerStrike` | Animations | *Placeholder OK.* |
| Heat glow `VFX_Forge_Heat`, sparks `VFX_Anvil_Sparks`, steam `VFX_Quench_Steam` | VFX | *Placeholder OK.* |
| SFX: `SFX_Shop_Bellows_Pump_01`, `SFX_Shop_Anvil_Strike_01..03`, `SFX_Shop_Quench_Hiss_01` | Audio | *Placeholder OK* (free library sounds). |
| **Iron material data:** Base Damage of Iron Blade; heating time (3–6 s); anvil cursor speed and target zone sizes (Perfect / Good) | Data / Design | Required decision; GDD gives strike values (+15 / +5 / −5 from base 50). |

### Work this week
- Forge: load ore (instant) → pump bellows (continuous, cooperative) → Hot Ingot.
- Tongs transfer of the hot ingot to the anvil.
- Anvil timing mini-game (3 strikes, sweeping cursor, world-space UI), exclusive to one player; skip / accessibility path gives Quality 60.
- Quenching Basin locks the blade; output `Blade` item carries Quality, Base Damage, Element (Physical) and material.
- Pure `QualityCalculator` with tests (clamp 1–100, tiers Crude / Standard / Masterwork / Flawless).

### Networking
- Mini-game is played **locally by the owning client** (timing feel); the client sends strike results (tick + offset) via `[ServerRpc]`; the host validates against the tick window and computes Quality.
- Other players see the cursor and strikes through `[ObserversRpc]` (cosmetic), and bellows animation from station state.
- Component Quality / material live on the item's host-owned data and replicate to all.

### Done when
- Player A pumps bellows while Player B strikes; the resulting blade shows the same Quality on both screens.

---

## Week 7 — Foundation & Core Pipelines: Lathe, Carving Bench, Extractor, Distiller

**Goal:** Arcane Oak becomes a Hilt / Short Shaft / Long Shaft, and mob essence becomes an Aether Core — reusing the Week 5 framework.

### Required sources
| Source | Type | Notes |
|---|---|---|
| `SM_Shop_Lathe` with `Part_LatheChuck`, `SM_Shop_CarvingBench` | Workstation meshes | *Placeholder OK.* |
| `SM_Shop_ArcaneExtractor` (mortar), `SM_Shop_PurityDistiller` with `Part_Valve` | Workstation meshes | *Placeholder OK.* |
| Items: `SM_Weapon_Hilt_ArcaneOak`, `SM_Weapon_ShortShaft_ArcaneOak`, `SM_Weapon_LongShaft_ArcaneOak` (each with `Socket_Payload`), `SM_Common_VerdantEssence`, `SM_Weapon_Core_Verdant` | Static meshes | *Placeholder OK*, connector sizes must match across materials. |
| Clips: `A_Player_Chisel`, `A_Player_Polish`, `A_Player_TurnValve` | Animations | *Placeholder OK.* |
| SFX/VFX: wood shavings, lathe hum, bubbling distiller, core crystallize glow | Audio / VFX | *Placeholder OK.* |
| **Decisions:** (1) does the lathe have a mini-game or a fixed-quality hold? (2) element and Base Damage of the Verdant Core (Bramble Stalker essence) (3) distiller temperature zone size and drift speed | Design | Required. Open questions in [Resource Processing](../GDD/02_Systems/Processing/_Processing_System.md). |

### Work this week
- Lathe: load log → hold chisel (continuous) → choose output (Hilt / Short Shaft / Long Shaft) → Carving Bench polish (continuous).
- Extractor: load essence → maceration (continuous) → Distiller heat-regulation mini-game (keep in zone 4 s with valves) → Aether Core.
- `ProcessingRecipe` assets: `Recipe_Lathe_ArcaneOakHilt`, `…ShortShaft`, `…LongShaft`, `Recipe_Distiller_VerdantCore`.
- Debug spawner (dev only) to drop any raw item into the workshop for testing without realms.

### Networking
- Output selection is a `[ServerRpc]` choice validated by the host.
- Distiller mini-game: owner client sends valve input; temperature is **host-simulated** and replicated so all players see the gauge and anyone can take over.

### Done when
- A hilt, a short shaft, a long shaft and a core can be produced by any player, with consistent Quality on host and client.

---

## Week 8 — Assembly Bench & Weapons

**Goal:** Two components become a finished, named weapon that can be equipped.

### Required sources
| Source | Type | Notes |
|---|---|---|
| `SM_Shop_AssemblyBench` with `Socket_Foundation`, `Socket_Payload`, `Socket_Output` (riser), `Interact_Point` | Workstation mesh | *Placeholder OK.* |
| `SM_Shop_RunedMallet` | Static mesh | *Placeholder OK.* |
| Lock animation of the bench (0.5 s), `A_Player_MalletStrike` | Animation | *Placeholder OK.* |
| Flawless glow `VFX_QualityGlow_Flawless` | VFX | *Placeholder OK.* |
| Hologram preview style per [Assembly Bench UI](../GDD/05_UI/World/UI_Assembly_Bench.md) | UI | *Placeholder OK* — data must be correct, styling can come later. |
| Equipped weapon attachment points on the character: `Socket_HandRight`, `Socket_Back` | Rig | Required on the final character; placeholder bones OK. |

### Work this week
- Pure assembly domain logic per [Technical_Design/Weapon_Crafting](../Technical_Design/Crafting/_Crafting_Module.md): valid pairs (Hilt+Blade, Short Shaft+Core, Long Shaft+Core), Quality = rounded average, Base Damage from payload, auto-naming `[Payload] [Foundation] [Category]`; EditMode tests for every pair and rejection.
- Bench sockets accept only their part type; mallet strike (instant) assembles; weapon appears on the output riser.
- World-space hologram preview showing predicted name, Quality tier and Base Damage before locking.
- Weapons go to hands on pickup; `[Q] Equip` swaps with the weapon slot; equipped weapon visible on the character.

### Networking
- Assembly executed only on the host; the new weapon is a host-spawned `NetworkObject`; component items despawn.
- Equipped weapon id is a `SyncVar` on the player so every client renders it.

### Done when
- Player A places a blade, Player B places a hilt, either strikes the mallet; both see the same named sword with the same stats, and either can equip it.

---

## Week 9 — Mailbox, Letters & Gold

**Goal:** Adventurers Guild letters arrive, can be read and pinned, and weapons are delivered for gold.

### Required sources
| Source | Type | Notes |
|---|---|---|
| `SM_Shop_MailboxNexus` (arrival tube + board) and `SM_Shop_OutgoingTube` | Static meshes | *Placeholder OK.* |
| `SM_Common_Letter` | Static mesh | *Placeholder OK.* |
| Letter Board UI per [Letter Commission Board](../GDD/05_UI/World/UI_Letter_Commission_Board.md): `PF_UI_Letter_Widget`, frames, `UI_Icon_WeaponType_*`, `UI_Icon_Element_*` | UI sprites / prefabs | *Placeholder OK* (functional layout first). |
| **Guild letter data:** 5–10 flavor texts, gold reward per weapon type, lifespan (240–360 s), arrival interval | Data / Writing | Required. |
| SFX: `SFX_Shop_Mailbox_Arrive_01`, `SFX_Shop_Dispatch_Success_01`, `SFX_Shop_Dispatch_Reject_01` | Audio | *Placeholder OK.* |
| Gold counter placement on the HUD | Design | *Placeholder OK.* |

### Work this week
- `Archetype_AdventurersGuild` data and letter generator (only weapons buildable from Phase 1 materials).
- `LetterBoard_WorldUI` with letter queue, dossier, timers; pin to `Gameplay_Hud`.
- Outgoing Tube dispatch: choose a target letter, verify (type, minimum quality tier, element, material) as a pure function with tests; reject returns the weapon to hands with a reason.
- Shared gold treasury and Flawless +50% bonus.

### Networking
- Letters, timers (server ticks), treasury and pinned state are host-owned (`SyncList` / `SyncVar`); pinning is per player (local) or shared — **decide**, default: per player.
- Dispatch is a `[ServerRpc]` with item + letter id; the host verifies and broadcasts the result.

### Done when
- A letter appears for everyone, a matching weapon delivered by a client pays gold visible to all; a wrong weapon is rejected with the correct reason.

---

## Week 10 — Combat (Player Side), Health, Downed & Revive

**Goal:** Players can fight with swords and wands/staves, take damage, go down and be revived.

### Required sources
| Source | Type | Notes |
|---|---|---|
| Clips: `A_Player_SwordSwing_01`, `A_Player_SwordSwing_02`, `A_Player_CastOrb`, `A_Player_HitReact`, `A_Player_Downed`, `A_Player_Revive`; `AOC_Player_Staff` (two-handed) | Animations | *Placeholder OK.* |
| Orb VFX per element used in Phase 1: `VFX_Element_Physical_Orb`, `VFX_Element_Arcane_Orb` (or the Verdant core element), impact `VFX_Hit_Orb`, `VFX_Hit_Sword` | VFX | *Placeholder OK.* |
| SFX: swing whoosh, sword impact (iron), orb cast, orb impact, player hurt, downed | Audio | *Placeholder OK.* |
| Training dummy `SM_Common_TrainingDummy` | Static mesh | *Placeholder OK.* |
| Health bar `Health_Bar` and downed/revive markers | UI | *Placeholder OK.* |
| **Decision:** starter weapons — do players start with a sword/wand so they are never unarmed? | Design | Required: the Phase 1 loop kills a mob before any weapon is crafted. Open question in [Combat](../GDD/02_Systems/Combat/_Combat_System.md). |

### Work this week
- `Armotheca.Combat` per [Technical_Design/Combat](../Technical_Design/Combat/_Combat_Module.md): sword 2-swing chain (frontal arc, multi-hit once per swing), magic orb (cooldown, aim assist, stops on first hit), values from `AttackProfile_SwordSwing` / `AttackProfile_MagicOrb`.
- `IDamageable`, player health 100, invulnerability (roll start, 0.5 s after hit), hit-stop and flash feedback.
- Downed state with 20 s bleed-out, 3 s cooperative revive (continuous interaction), ejection hook (wired to realms in Week 11).
- Training dummy in the workshop sandbox.

### Networking
- Attack input from the owner client; the **host** performs hit detection and applies damage (host-authoritative damage, no client-side hit claims).
- Orbs are host-spawned projectiles replicated to observers (or host-simulated with cosmetic client copies — choose by bandwidth from the Week 3 spike).
- Health, downed and bleed-out timers are `SyncVar`s; hit feedback via `[ObserversRpc]`.

### Done when
- Two players hit the dummy with sword and wand and see the same results; a player downed by a debug damage command is revived by a teammate.

---

## Week 11 — Magic Door, Verdant Realm & Resource Nodes

**Goal:** Players open the first door, enter the Verdant Corruption, harvest nodes and come back.

### Required sources
| Source | Type | Notes |
|---|---|---|
| `SM_Shop_MagicDoor` frame with rune emission mask (`T_Shop_MagicDoor_E`), portal surface `SG_PortalSurface` / `VFX_Portal_Swirl` | Mesh / Shader / VFX | *Placeholder OK* (AF_4 is the reference). |
| `SM_Realm_ExitPortal` | Static mesh | *Placeholder OK.* |
| Verdant realm layout plan: Entry (Exit Portal), Outer Grounds, node spawn points, mob spawn zones (Deep Grounds and Apex Arena can be blocked off) | Design | Required — top-down sketch with rough sizes. Outer Grounds crossable in under a minute. |
| Verdant environment kit (ground, rocks, trees, bramble walls) | Static meshes | *Placeholder OK* (greybox). |
| `SM_Verdant_Node_ArcaneOak` and `SM_Verdant_Node_IronVein`, each in states intact / damaged / broken (same pivot) | Static meshes | *Placeholder OK.* 2–6k tris each when final. |
| Tool props `SM_Common_Pickaxe`, `SM_Common_Axe`; clips `A_Player_Mine`, `A_Player_Chop` | Mesh / Animation | *Placeholder OK.* |
| Node strike VFX/SFX (chips, crunch) | VFX / Audio | *Placeholder OK.* |
| **Decision:** node names — roadmap says *Arcane Oak*, Realms GDD says *Bog Oak / Ironwood* | Design | Required, to fix item ids. |
| Node yields: hits per node, drop table (Iron Ore + Flux chance; log count) | Data | Required. |

### Work this week
- `Door_VerdantCorruption` + `Realm_VerdantCorruption` data; door lifecycle for Phase 1: Ready → Entry Open (90 s) → In Progress → Cooldown, expedition membership, member re-entry.
- `Realm_VerdantCorruption` scene loaded **additively** through FishNet `SceneManager` (decide offset vs separate physics scene — Technical Overview §8); teleport through the door and back through the Exit Portal.
- Realm discarded when empty; health refills on return to the workshop.
- Node spawning on door open with host-seeded rolls (active points, weighted table, rare variant 10%), letter guarantee for node materials.
- Harvesting as continuous interaction (up to 2 players), node states, drops auto-collected into the backpack on walk-over.

### Networking
- Door state machine and entry window are host-owned with tick timestamps.
- Scene-based observer conditions: realm objects replicate only to players inside the realm.
- Node seed and spawn results decided by the host; node hit counts and states are `SyncVar`s; drops are host-spawned items.

### Done when
- One player opens the door, both players enter within the window, each harvests a different node, one returns through the Exit Portal and the other stays; the realm is discarded when the second leaves.

---

## Week 12 — Bramble Stalker

**Goal:** The realm is dangerous: Bramble Stalkers chase, lunge, ambush harvesters and drop the essence needed for cores.

### Required sources
| Source | Type | Notes |
|---|---|---|
| `SK_Mob_BrambleStalker` with generic rig | Skeletal mesh | *Placeholder OK* (5–10k tris final, clear wind-up parts for the telegraph). |
| Clips: `A_BrambleStalker_Idle`, `_Walk`, `_Run`, `_LungeWindUp`, `_Lunge`, `_HitReact`, `_Death`, `_AmbushWake` | Animations | *Placeholder OK.* |
| SFX: growl, lunge, hurt, death; VFX: telegraph flash, death burst | Audio / VFX | *Placeholder OK.* |
| Drop item meshes: `SM_Common_ThornedPelt`, `SM_Common_VerdantEssence` (from Week 7) | Static meshes | *Placeholder OK.* |
| **`Mob_BrambleStalker` data:** health, lunge damage, telegraph time, speeds, aggro range, drop table, group sizes | Data | Required (initial values). |

### Work this week
- `Armotheca.Exploration` mobs per [Technical_Design/Mobs](../Technical_Design/Exploration/Mob_AI.md): Chaser behaviour (approach, telegraphed lunge), Ambusher variant hidden next to nodes, waking on harvest.
- NavMesh for the Verdant realm (AI Navigation package).
- Spawn zones rolled on door open with the letter guarantee for mob drops; sword stagger; death drops.
- Downed bleed-out in a realm ejects the player to the workshop and drops their backpack/hands contents in the realm.
- Realm Pressure is **not** in Phase 1 (Phase 2) — keep a hook for it.

### Networking
- Mob AI, pathing, target selection and damage run **only on the host**; clients receive transform + animation state.
- Mobs belong to the realm scene and use the same observer conditions.

### Done when
- Two players fight a group of Bramble Stalkers in the realm; telegraphs and hits match on both screens; a killed stalker drops Verdant Essence that can be carried home and processed into a core.

---

## Week 13 — Integration, Playtest & Performance

**Goal:** The complete Phase 1 loop runs end-to-end in co-op, and the art budgets are validated.

### Required sources
| Source | Type | Notes |
|---|---|---|
| Playtesters: one 2-player and one 4-player session over Steam | People | Required. |
| Any final assets that are ready (characters, stations, nodes, mob) | Art | Optional — swapped in to test the budgets of the Modeling Guidelines §4. |
| Target test hardware: GTX 1660-class PC and (if available) Steam Deck | Hardware | For the performance check. |
| Feedback form / questions for testers | Design | *Placeholder OK.* |

### Work this week
- Full loop pass: letter → door → chop → mine → kill mob → return → smelt blade → carve hilt → assemble → deliver, timed (< 5 minutes target).
- Fix integration bugs and desyncs found in playtests; tune timings in data assets.
- Performance capture: FPS, draw calls, triangles in workshop and realm vs scene budgets; network bandwidth with 4 players vs the Week 3 baseline.
- Update GDD open questions answered during Phase 1 and the Phase 2 backlog.
- Buffer for any slipped week.

### Networking
- 4-player session with simulated latency (100–150 ms) and 1–2% packet loss; late join into a running workshop; host quitting ends the session cleanly.

### Done when
- Phase 1 success criterion met in a **2-player Steam session**, and a 4-player session completes the loop without desync or blocking bugs.

---

## Phase 1 Materials Summary

| Raw (source) | Station chain | Component | Used in |
|---|---|---|---|
| Iron Ore (Iron Vein node) | Smelting Forge → Anvil → Quenching Basin | Iron Blade (Physical) | Sword |
| Arcane Oak log (Arcane Oak node) | Lathe → Carving Bench | Hilt / Short Shaft / Long Shaft | Sword / Wand / Staff |
| Verdant Essence (Bramble Stalker) | Arcane Extractor → Purity Distiller | Verdant Core (element to be decided) | Wand / Staff |

## Consolidated Decisions Needed Before Starting

| Decision | Needed by |
|---|---|
| Pinned versions (Unity patch, FishNet, FishySteamworks, Steamworks.NET) | Week 1 |
| Camera distance / angle | Week 2 |
| Iron Blade Base Damage, anvil timing values | Week 6 |
| Lathe mini-game or not; Verdant Core element and Base Damage; distiller values | Week 7 |
| Guild letter texts, rewards, lifespan; per-player or shared pinning | Week 9 |
| Starter weapons | Week 10 |
| Node names (Arcane Oak vs Bog Oak / Ironwood); node yields; realm loading approach | Week 11 |
| Bramble Stalker stats and drops | Week 12 |
