# UI Composition

> How every interface is put together: the UI element vocabulary, the categories that sort UI docs and prefabs, the GameObject hierarchy and the canvas layers.
> **Naming:** [Assets Naming](Assets_Naming.md) · **Game context:** [UI Flow](../GDD/05_UI/_UI_Flow.md) · **Tech stack:** [Technical Overview](../Technical_Design/Technical_Overview.md) · **Code:** [_UI_Module](../Technical_Design/UI/_UI_Module.md)

---

## 1. General Rules

1. All interfaces are built with **uGUI** (+ TextMeshPro).
2. **Every UI GameObject is named `<Name>_<ElementType>`**, using the element types in §3–§6, so the hierarchy reads the same way in every screen: `LetterQueue_Panel`, `Dispatch_Button`, `Timer_Value`. The name part is PascalCase, as in [Assets Naming §1](Assets_Naming.md#1-general-rules).
3. **A two-digit index**, when needed, goes last: `Backpack_Slot_01`.
4. **Children whose type already says everything** (`Title`, `Label`, `Fill`, `Content`, `Header`) drop the `<Name>_` part when there is only one of them under the parent.
5. **Assets follow the same element types:**
   - UI prefabs: `PF_UI_<Name>_<ElementType>`, e.g. `PF_UI_Letter_Widget`.
   - UI sprites: `UI_<ElementType>_<Name>`, e.g. `UI_Icon_Element_Frost`, so sprites of one kind sort together.
   - View components (C#): `<Name><ElementType>`, e.g. `LetterWidget` ([Assets Naming §6](Assets_Naming.md#6-code)).

---

## 2. Categories

UI design docs (`GDD/05_UI/<Category>/`) and UI prefabs (`Assets/_Project/Prefabs/UI/<Category>/`) use the same categories. A doc or prefab goes into the category of its **root object's element type**.

| Category | Root element types | Contains |
|---|---|---|
| `Hud` | Hud, Prompt | The always-on in-game overlay and its Panels; interaction prompts |
| `Screens` | Screen | Full-screen states: main menu, lobby, settings, pause |
| `Windows` | Window | Framed, closable boxes over a Screen or the HUD |
| `Popups` | Popup | Modal boxes that need an answer |
| `Widgets` | Widget, Row, Slot, Tab | Repeatable items reused by several parents |
| `World` | WorldUI, Marker | Interfaces and indicators on 3D objects (World Space canvases) |

---

## 3. Structural Elements

From largest to smallest.

| Element type | Definition | Has visuals? | Example |
|---|---|---|---|
| **Layer** | A root Canvas that groups UI by draw order and input priority (see §7). Exists once per type in the UI root. | No | `Popup_Layer` |
| **Screen** | A full-screen state of the interface. Only **one Screen is active at a time** within its layer; switching screens replaces the content entirely. | Yes | `MainMenu_Screen`, `Settings_Screen`, `Lobby_Screen` |
| **Hud** | The always-on in-game overlay (health, pinned letters, pressure distortion). Not a Screen: it lives in its own layer and coexists with the 3D view. | Yes | `Gameplay_Hud` |
| **Window** | A framed, closable box shown **on top of a Screen or the HUD**. It has its own Title and close action and can be non-modal. | Yes | `LetterDetails_Window`, `Backpack_Window` |
| **Popup** | A small **modal** Window that blocks input behind it and needs an answer (confirm, error, purchase). | Yes | `ConfirmPurchase_Popup` |
| **Panel** | A visible region with its own background inside a Screen, Window or Hud, grouping related content. Panels do not close on their own (they may be shown/hidden by their parent). | Yes | `LetterQueue_Panel`, `Dossier_Panel` |
| **Section** | A titled part of a Panel or Window **without** its own background, separating content visually (often with a Divider). | No | `Rewards_Section` |
| **Header / Body / Footer** | The three standard parts of a Window, Panel or Widget: top (Title, close button), middle (main content), bottom (actions). | Optional | `Header`, `Body`, `Footer` |
| **Container** | An invisible object whose only job is **layout of several children** (Horizontal/Vertical/Grid Layout Group). | No | `Actions_Container`, `Rewards_Container` |
| **ScrollView** | A uGUI Scroll Rect. Its children follow Unity's names: `Viewport` → `Content`. | Optional | `Letters_ScrollView` |
| **Content** | The RectTransform that **holds dynamically spawned or scrollable children** (Widgets, Rows). Used for the Scroll Rect content and for any runtime-filled area. Only one per ScrollView. | No | `Content` (inside `Viewport`) |
| **Wrapper** | An invisible RectTransform around **exactly one child**, used only for positioning, anchoring, masking or animation (e.g. to animate scale without fighting a Layout Group). | No | `Icon_Wrapper` |

---

## 4. Repeatable Items

| Element type | Definition | Example |
|---|---|---|
| **Widget** | A self-contained, repeatable view of **one data object**, usually a prefab spawned into a Content or Container. Has its own frame and can have Header/Body/Footer. | `Letter_Widget`, `Player_Widget` (lobby), `Recipe_Widget` |
| **Row** | A one-line repeatable item in a list, without its own frame (settings entry, key binding, stat line). | `KeyBinding_Row`, `Reward_Row` |
| **Slot** | A fixed place that **can hold an item or be empty** (backpack slots, hotbar). Shows an empty state. | `Backpack_Slot_01` |
| **Tab** | A selectable header that switches the visible Panel inside a TabGroup. | `Settings_TabGroup` → `Audio_Tab` |

---

## 5. Atomic Elements

**Text**

| Element type | Definition | Example |
|---|---|---|
| **Title** | The main heading of a Screen, Window, Panel, Section or Widget. **One per parent.** | `Title` ("Nexus Dispatch Mailbox") |
| **Subtitle** | Secondary heading under a Title. | `Subtitle` ("Arcane Academy of Oakhaven") |
| **Label** | Short **static** text that names something: a caption for a value, a control or a field. Changes only with localization. | `Gold_Label` ("Gold"), `Deadline_Label` |
| **Value** | Short **dynamic** text showing data that changes at runtime: numbers, timers, names. Usually paired with a Label. | `Gold_Value` ("450"), `Timer_Value` ("03:15") |
| **Text** | Multi-line body or descriptive text (flavor text, descriptions, rejection reasons). | `Flavor_Text`, `Description_Text` |

**Graphics**

| Element type | Definition | Example |
|---|---|---|
| **Background** | The fill image behind a Panel, Window, Widget or Button. | `Background` |
| **Frame** | A decorative border/outline image, usually 9-sliced. | `Faction_Frame` |
| **Icon** | A small symbolic image representing a thing or an action (element, weapon type, currency). | `Element_Icon`, `WeaponType_Icon` |
| **Image** | A larger illustrative image that is not a symbol (portrait, preview, artwork). | `Portrait_Image` |
| **Divider** | A thin separator line between Sections or Rows. | `Divider` |
| **Badge** | A small marker attached to another element to show a **status or count** (Flawless tag, "new" dot, number of unread letters). | `Quality_Badge`, `Unread_Badge` |
| **Bar** | A progress/amount indicator; its fill child is named `Fill`. | `Urgency_Bar` → `Fill`, `Health_Bar` |

**Controls**

| Element type | Definition | Example |
|---|---|---|
| **Button** | Clickable action. Its text child is `Label`, its image child `Icon`. | `Dispatch_Button` → `Label` |
| **Toggle** | On/off control. | `Subtitles_Toggle` |
| **Slider** | Value selection along a range. | `MusicVolume_Slider` |
| **Dropdown** | Choice from a list (TMP Dropdown). | `Resolution_Dropdown` |
| **InputField** | Text input (TMP Input Field). | `LobbyName_InputField` |

---

## 6. Overlays and World-Space Elements

| Element type | Definition | Example |
|---|---|---|
| **Tooltip** | Hover/focus information next to an element; no interaction. | `Item_Tooltip` |
| **Toast** | A short, auto-dismissing notification that does not block input. | `LetterArrived_Toast` |
| **Prompt** | The interaction hint shown for the current target (`[E] Pick up Iron Ore`, see [Object Interaction](../GDD/02_Systems/Interaction/_Interaction_System.md)). | `Interact_Prompt` |
| **WorldUI** | Root of a World Space canvas that hosts a **full interface on a 3D object** (Letter Board, Assembly Bench hologram). Inside it, the normal structure applies (Header, Panels, Widgets…). | `LetterBoard_WorldUI`, `AssemblyBench_WorldUI` |
| **Marker** | A small world-space indicator above a 3D object or character: nameplate, health above mobs, door price plaque, expedition member list. | `PlayerName_Marker`, `DoorPrice_Marker` |
| **Overlay** | A full-screen non-interactive effect layer (fades, vignettes, loading curtain). | `Fade_Overlay` |

---

## 7. Layers and Sort Order

Each layer is a root Screen Space Canvas with a fixed sort order. World Space canvases (Markers, the Letter Board, the Assembly Bench hologram) live on their 3D objects and are not part of this stack.

| Layer | Sort order | Contains |
|---|---|---|
| `Hud_Layer` | 0 | Hud, Prompts |
| `Screen_Layer` | 100 | Screens (main menu, lobby, settings, pause) |
| `Window_Layer` | 200 | Windows |
| `Popup_Layer` | 300 | Popups (modal) |
| `Notification_Layer` | 400 | Toasts, Tooltips |
| `Overlay_Layer` | 500 | Overlays (fade, loading) |

---

## 8. Example Hierarchy

The Letter Commission Board (see [UI Design](../GDD/05_UI/World/UI_Letter_Commission_Board.md)):

```
LetterBoard_WorldUI                      (World Space canvas on the board)
├── Header
│   ├── Title                            "Nexus Dispatch Mailbox"
│   ├── Reputation_Label                 "Shop Reputation"
│   └── Reputation_Value                 "Lvl 2 (340/500)"
├── Body
│   ├── LetterQueue_Panel
│   │   ├── Title                        "Pending Letters"
│   │   └── Letters_ScrollView
│   │       └── Viewport
│   │           └── Content
│   │               └── Letter_Widget    (PF_UI_Letter_Widget, spawned per letter)
│   │                   ├── Faction_Frame
│   │                   ├── WeaponType_Icon
│   │                   ├── Element_Icon
│   │                   ├── Title        "Guild: Iron Sword"
│   │                   ├── Timer_Value  "03:15"
│   │                   ├── Urgency_Bar
│   │                   │   └── Fill
│   │                   └── Batch_Badge  "1/3"
│   └── Dossier_Panel
│       ├── Title                        "Active Commission"
│       ├── Flavor_Text
│       ├── Requirements_Section
│       │   ├── Title
│       │   └── Requirements_Container
│       │       └── Requirement_Row      (spawned per criterion)
│       │           ├── Label
│       │           └── Value
│       └── Rewards_Section
│           ├── Title
│           └── Rewards_Container
└── Footer
    └── Actions_Container
        ├── PinToHud_Button
        │   └── Label
        └── Dispatch_Button
            └── Label
```

---

## 9. Open Questions

- Toasts, Tooltips and Overlays have no category of their own (§2); decide where their prefabs and docs go when the first one is designed.
