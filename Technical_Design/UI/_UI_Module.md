---
id: _UI_Module
type: module
module: UI
namespace: Armotheca.UI
status: Draft
---

# UI Module

> **Design:** [_UI_Flow](../../GDD/05_UI/_UI_Flow.md) · **Map:** [_Module_Map](../_Module_Map.md) · **Overview:** [Technical Overview](../Technical_Overview.md) · **Naming:** [Assets Naming §7](../../Guidelines/Assets_Naming.md)

## Scope

Views only: every screen reads state from the module that owns it and listens to that module's events; no game rules live here.

| GDD doc | Implemented in |
| --- | --- |
| [UI_Letter_Commission_Board](../../GDD/05_UI/Screens/UI_Letter_Commission_Board.md) | [Letter Commission Board](#letter-commission-board) |
| [UI_Pinned_Letter](../../GDD/05_UI/Hud/UI_Pinned_Letter.md) | [Letter Commission Board](#letter-commission-board) |
| [UI_Assembly_Bench](../../GDD/05_UI/World/UI_Assembly_Bench.md) | [Assembly Bench](#assembly-bench) |
| [UI_Interaction_Prompt](../../GDD/05_UI/World/UI_Interaction_Prompt.md) | [Interaction Prompt](#interaction-prompt) |
| [UI_Realm_Pressure](../../GDD/05_UI/Hud/UI_Realm_Pressure.md) | [Realm Pressure](#realm-pressure) |

---

## Technical Specifications

- **Framework:** uGUI only, with TextMeshPro. Screen Space canvases for menus and HUD, World Space canvases for diegetic UI; UI Toolkit is not used ([Technical Overview §1](../Technical_Overview.md#1-technology-stack-decided)).
- **Navigation:** built-in uGUI navigation for gamepad.
- **Naming and hierarchy:** element vocabulary and layers per [Assets Naming §7](../../Guidelines/Assets_Naming.md).

---

## Networking

Views run on every client and only read replicated state; actions go through the owning module's `[ServerRpc]` intents.

---

## Letter Commission Board

- **Board:** uGUI World Space Canvas on the board (TextMeshPro text, built-in uGUI navigation for gamepad).
- **Pinned-letter HUD widget:** uGUI Screen Space Overlay canvas.
- Both views only listen to `OrderManager` events ([_Orders_Module › Events](../Orders/_Orders_Module.md#events)).

## Assembly Bench

- uGUI World Space Canvas attached to the bench, TextMeshPro for all text, Animator/tweens for socket pulses and the hologram.
- The view only listens to `AssemblyBench` events ([_Crafting_Module › Events](../Crafting/_Crafting_Module.md#events)).

## Interaction Prompt

- Reads the current `InteractionPrompt` (verb + object name + kind) and continuous progress through events from `PlayerInteractor` ([_Interaction_Module › Events](../Interaction/_Interaction_Module.md#events)).

## Realm Pressure

- Screen-edge distortion and the level-up audio cue react to `MobDirector.OnPressureLevelChanged` ([_Exploration_Module › Events](../Exploration/_Exploration_Module.md#events)).

---

## Open Technical Questions

-
