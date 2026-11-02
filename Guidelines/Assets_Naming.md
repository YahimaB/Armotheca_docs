# Assets Structure & Naming

> Single source of truth for how the Unity project's `Assets/` folder is organized and how every asset, GameObject and UI element is named.
> Related: [3D Modeling Guidelines](Modeling_Guidelines.md) · [Technical Overview](../Technical_Design/Technical_Overview.md) · [UI Design](../GDD/05_UI/Screens/UI_Letter_Commission_Board.md)

---

## 1. General Rules

1. **CamelCase words, underscores between parts.** Each part of a name is written in CamelCase (`AssemblyBench`, `StarMetal`); underscores only separate the parts.
2. **Name pattern:** `Prefix_Zone_AssetName_Variant_Suffix` — use only the parts that apply.
3. **English only, no spaces**, no special characters except `_`.
4. **No version tags** (`_final`, `_new`, `_v2`, `_old`). Git keeps the history.
5. **Variants are two-digit numbers:** `SM_Shop_Barrel_01`, `SM_Shop_Barrel_02`.
6. **Full words, no private abbreviations.** Only the prefixes and suffixes listed in this document are abbreviated.
7. **File name = asset identity.** Do not rename an asset without updating references (Unity keeps GUIDs, but docs, data IDs and search habits break).

---

## 2. Zones

The same zones are used in the docs, in folders and in asset names.

| Zone token | Meaning | Docs counterpart |
|---|---|---|
| `Common` | Used everywhere (workshop and realms) | `GDD/02_Systems` (Movement, Interaction, Combat) |
| `Shop` | The workshop pocket realm | `GDD/04_Locations/L00_Workshop` |
| `Realm` | Shared by all realms (Exit Portal, Aether Chute, shared rocks) | `GDD/04_Locations/_World_Map` |
| `Verdant` | Verdant Corruption | `GDD/04_Locations/L01_Verdant_Corruption` |
| `Pyro` | Pyroclastic Trench | `GDD/04_Locations/L02_Pyroclastic_Trench` |
| `Astral` | Astral Quarry | `GDD/04_Locations/L03_Astral_Quarry` |
| `Frost` | Frostbite Cavern | `GDD/04_Locations/L04_Frostbite_Cavern` |
| `Character` | Player characters | `GDD/03_Entities/Player` |
| `Mob` | Creatures (used together with the realm in folders) | `GDD/03_Entities/Mobs` |
| `Weapon` | Weapon components | `GDD/03_Entities/Items/Components` |
| `UI` | Interface assets | `GDD/05_UI` |

- Exploration content lives under `Realms/` in `Art`, `Prefabs`, `Audio` and `Scenes`.
- Short realm tokens (`Pyro`) are used in **file and folder names**. Full realm names (`PyroclasticTrench`) are used only for **data assets and IDs that represent the realm itself** (`Realm_PyroclasticTrench`, `Door_PyroclasticTrench`) and for realm scenes.

---

## 3. Assets Folder Structure

```
Assets/
├── _Project/                           # everything we make (underscore keeps it on top)
│   ├── Art/
│   │   ├── Characters/<Name>/
│   │   ├── Weapons/<Kind>/<Material>/          # Blade/StarMetal, Core/Frost, LongShaft/BogOak
│   │   ├── Common/
│   │   │   ├── Props/<Name>/
│   │   │   └── TrimSheets/
│   │   ├── Shop/
│   │   │   ├── Architecture/
│   │   │   ├── Props/<Name>/
│   │   │   └── Workstations/<Name>/
│   │   ├── Realms/
│   │   │   ├── Shared/                         # Exit Portal, Aether Chute, shared rocks
│   │   │   └── <Realm>/                        # Verdant, Pyro, Astral, Frost
│   │   │       ├── Environment/
│   │   │       ├── Nodes/<Name>/
│   │   │       └── Mobs/<Name>/
│   │   ├── Animations/                         # shared Humanoid clips
│   │   ├── VFX/                                # Elements, Portals, QualityGlow, Hits
│   │   ├── Shaders/
│   │   └── UI/
│   │       ├── Sprites/  Icons/  Fonts/
│   ├── Audio/
│   │   ├── Music/  Ambience/
│   │   └── SFX/<Zone>/
│   ├── Data/                                   # ScriptableObject instances (design data)
│   │   ├── Crafting/                           # CraftMaterial_, Recipe_
│   │   ├── Orders/                             # Archetype_
│   │   ├── Progression/                        # ShopTier_
│   │   ├── Realms/                             # Realm_, Door_, NodeTable_, MobTable_
│   │   ├── Nodes/                              # Node_
│   │   ├── Mobs/                               # Mob_
│   │   ├── Combat/                             # AttackProfile_
│   │   └── Settings/                           # Settings_
│   ├── Prefabs/
│   │   ├── Common/  Shop/  Characters/  Weapons/
│   │   ├── Realms/Shared/  Realms/<Realm>/
│   │   ├── UI/                                 # Screens, Windows, Popups, Cards, Hud, World
│   │   └── Network/                            # NetworkManager, bootstrap
│   ├── Scenes/
│   │   ├── Boot.unity  MainMenu.unity  Workshop.unity
│   │   ├── Realms/                             # Realm_VerdantCorruption.unity, ...
│   │   └── Sandbox/<PersonName>/               # personal test scenes, never referenced by the game
│   ├── Scripts/                                # one folder + .asmdef per namespace
│   │   ├── Core/  Networking/  Movement/  Interaction/  Combat/
│   │   ├── Crafting/  Processing/  Orders/  Progression/  Endgame/  Exploration/  UI/
│   │   └── Editor/
│   ├── Settings/                               # URP assets, Input Actions, Volume profiles, Physics
│   └── Tests/
│       ├── EditMode/  PlayMode/
├── FishNet/                            # FishNet's own install location, do not move or edit
├── Plugins/                            # Steamworks.NET (if not installed as a package), native plugins
└── ThirdParty/                         # Asset Store packs, never edited in place
```

### Folder rules
- Folder names are CamelCase. **Category folders are plural** (`Props`, `Mobs`, `Workstations`); **a folder for one asset is singular** and named after it (`AssemblyBench`, `BrambleStalker`).
- **One folder per asset** in `Art/`: mesh, textures and materials of the asset live together. Add `Textures/` and `Materials/` subfolders only when an asset has more than ~10 files.
- **Third-party content is never edited.** To modify an Asset Store asset, copy it into `_Project/` and rename it to our conventions.
- **Source files stay outside `Assets/`** (`.blend`, `.spp`, `.psd`, `.kra`, audio projects) in a separate art-source location. Only exported FBX, PNG/TGA and WAV/OGG files enter `Assets/`.
- **Script folders match namespaces** from the [Module Map](../Technical_Design/_Module_Map.md). Each has an assembly definition named after the namespace: `Scripts/Combat/Armotheca.Combat.asmdef`.
- **Git:** commit `.meta` files; binaries (fbx, png, tga, psd, wav, ogg) go through Git LFS.

---

## 4. Asset Prefixes

| Asset type | Prefix | Pattern | Example |
|---|---|---|---|
| Static mesh (FBX) | `SM_` | `SM_<Zone>_<Name>` | `SM_Shop_AssemblyBench` |
| Skeletal mesh (FBX) | `SK_` | `SK_<Zone>_<Name>` | `SK_Mob_BrambleStalker` |
| Weapon component mesh | `SM_` | `SM_Weapon_<Kind>_<Material>` | `SM_Weapon_Blade_StarMetal` |
| Texture | `T_` | `T_<AssetName>_<MapSuffix>` | `T_Shop_AssemblyBench_BC` |
| Trim sheet / tileable texture | `T_Trim_` / `T_Tile_` | `T_Trim_<Material>_<MapSuffix>` | `T_Trim_WoodPlanks_N` |
| Material | `M_` | `M_<AssetName>` | `M_Shop_AssemblyBench` |
| Shader Graph / Sub Graph | `SG_` / `SSG_` | `SG_<Name>` | `SG_PortalSurface`, `SSG_RuneGlow` |
| Prefab | `PF_` | `PF_<Zone>_<Name>` | `PF_Shop_AssemblyBench` |
| Prefab variant | `PF_` | `PF_<Zone>_<Base>_<Variant>` | `PF_Mob_BrambleStalker_Elite` |
| Animation clip | `A_` | `A_<Rig>_<Action>` | `A_Player_Roll`, `A_BrambleStalker_Lunge` |
| Animator Controller | `AC_` | `AC_<Rig>` | `AC_Player` |
| Animator Override Controller | `AOC_` | `AOC_<Rig>_<Variant>` | `AOC_Player_Staff` |
| Avatar Mask | `AM_` | `AM_<Rig>_<Part>` | `AM_Player_UpperBody` |
| VFX (particle prefab / VFX Graph) | `VFX_` | `VFX_<Category>_<Name>` | `VFX_Element_Fire_Orb`, `VFX_Portal_Swirl` |
| Sound effect | `SFX_` | `SFX_<Zone>_<Source>_<Action>_<Variant>` | `SFX_Shop_Anvil_Strike_01` |
| Music / Ambience | `MUS_` / `AMB_` | `MUS_<Context>` | `MUS_Workshop_Day`, `AMB_Frost_Cave` |
| Audio Mixer | `MIX_` | `MIX_<Name>` | `MIX_Master` |
| UI sprite | `UI_` | `UI_<ElementType>_<Name>` (§7) | `UI_Icon_Element_Frost` |
| Font asset (TextMeshPro) | `FNT_` | `FNT_<Family>_<Weight>` | `FNT_Parchment_Bold` |
| Physics material | `PM_` | `PM_<Surface>` | `PM_Ice` |
| Render texture | `RT_` | `RT_<Purpose>` | `RT_CharacterPreview` |
| Input Actions | `IA_` | `IA_<Context>` | `IA_Player`, `IA_UI` |
| Volume profile (post-processing) | `VP_` | `VP_<Context>` | `VP_Workshop`, `VP_Realm_Pyro` |
| Timeline | `TL_` | `TL_<Event>` | `TL_UberWeaponVictory` |
| Lighting settings | `LS_` | `LS_<Scene>` | `LS_Workshop` |
| Scene | *(none)* | `<Name>` / `Realm_<FullRealmName>` | `Workshop`, `Realm_VerdantCorruption` |

### Texture map suffixes

| Suffix | Map |
|---|---|
| `_BC` | Base Color (+ alpha if needed) |
| `_N` | Normal (OpenGL / Y+) |
| `_MS` | Metallic (R) + Smoothness (A) |
| `_AO` | Ambient Occlusion |
| `_E` | Emission |
| `_9S` | UI sprite set up for 9-slicing (appended after the name: `UI_Frame_Parchment_9S`) |

### Names inside models (FBX hierarchy)

| Object | Pattern | Example |
|---|---|---|
| LOD meshes | `<MeshName>_LOD0..2` | `SM_Shop_Anvil_LOD1` |
| Attachment points | `Socket_<Purpose>` | `Socket_Payload`, `Socket_Input`, `Socket_Output` |
| Interaction point | `Interact_Point` | — |
| Collision meshes | `COL_<Name>` | `COL_AnvilBase` |
| Animated moving parts | `Part_<Name>` | `Part_Bellows`, `Part_LatheChuck` |

---

## 5. Data Assets (ScriptableObjects)

Data asset names start with the short type name, followed by the identity. The identity part is also the asset's ID in code (`DoorId`, `MobId`, …).

| ScriptableObject type | Prefix | Example |
|---|---|---|
| `ComponentMaterialDefinition` | `CraftMaterial_` | `CraftMaterial_StarMetal` |
| `ProcessingRecipe` | `Recipe_<Station>_` | `Recipe_Anvil_IronBlade` |
| `ClientArchetypeDefinition` | `Archetype_` | `Archetype_ArcaneAcademy` |
| `ShopTierDefinition` | `ShopTier_` | `ShopTier_RusticForge` |
| `DoorDefinition` | `Door_` | `Door_PyroclasticTrench` |
| `RealmDefinition` | `Realm_` | `Realm_PyroclasticTrench` |
| `NodeSpawnTable` / `MobSpawnTable` | `NodeTable_` / `MobTable_` | `NodeTable_PyroclasticTrench` |
| `ResourceNodeDefinition` | `Node_` | `Node_IronVein` |
| `MobDefinition` | `Mob_` | `Mob_BrambleStalker` |
| `SwordSwingProfile` / `MagicOrbProfile` | `AttackProfile_` | `AttackProfile_SwordSwing` |
| `MovementSettings` and other settings | `Settings_` | `Settings_Movement` |

`CraftMaterial_` is used instead of `Material_` so crafting materials are never confused with Unity rendering materials (`M_`).

---

## 6. Code

- **File name = class name**, CamelCase, one public type per file: `AssemblyBench.cs`.
- **Interfaces** start with `I`: `IDamageable`, `IContinuousInteractable`.
- **ScriptableObject classes** end with `Definition`, `Settings`, `Profile`, `Table` or `Recipe` (as in the tech docs).
- **Namespaces** follow `Armotheca.<Area>` and match the `Scripts/` folder (see §3).
- **UI view components** are named `<Name><ElementType>` (§7): `MainMenuScreen`, `ConfirmPopup`, `LetterCard`, `LetterQueuePanel`, `LetterBoardWorldUI`.
- **Private fields** `camelCase`; **properties, methods, events** `CamelCase`; events start with `On`: `OnStateChanged`.

---

## 7. UI Elements: Vocabulary & Naming

All interfaces are built with **uGUI**. Every UI GameObject is named **`<ElementType>_<Name>`** using the element types below, so the hierarchy reads the same way in every screen. UI prefabs follow `PF_UI_<ElementType>_<Name>`; UI sprites follow `UI_<ElementType>_<Name>`.

### 7.1 Structural elements (from largest to smallest)

| Element type | Definition | Has visuals? | Example |
|---|---|---|---|
| **Layer** | A root Canvas that groups UI by draw order and input priority (see 7.4). Exists once per type in the UI root. | No | `Layer_Popup` |
| **Screen** | A full-screen state of the interface. Only **one Screen is active at a time** within its layer; switching screens replaces the content entirely. | Yes | `Screen_MainMenu`, `Screen_Settings`, `Screen_Lobby` |
| **Hud** | The always-on in-game overlay (health, pinned letters, pressure distortion). Not a Screen: it lives in its own layer and coexists with the 3D view. | Yes | `Hud_Gameplay` |
| **Window** | A framed, closable box shown **on top of a Screen or the HUD**. It has its own Title and close action and can be non-modal. | Yes | `Window_LetterDetails`, `Window_Backpack` |
| **Popup** | A small **modal** Window that blocks input behind it and needs an answer (confirm, error, purchase). | Yes | `Popup_ConfirmPurchase` |
| **Panel** | A visible region with its own background inside a Screen, Window or Hud, grouping related content. Panels do not close on their own (they may be shown/hidden by their parent). | Yes | `Panel_LetterQueue`, `Panel_Dossier` |
| **Section** | A titled part of a Panel or Window **without** its own background, separating content visually (often with a Divider). | No | `Section_Rewards` |
| **Header / Body / Footer** | The three standard parts of a Window, Panel or Card: top (Title, close button), middle (main content), bottom (actions). | Optional | `Header`, `Body`, `Footer` |
| **Container** | An invisible object whose only job is **layout of several children** (Horizontal/Vertical/Grid Layout Group). | No | `Container_Actions`, `Container_Rewards` |
| **ScrollView** | A uGUI Scroll Rect. Its children follow Unity's names: `Viewport` → `Content`. | Optional | `ScrollView_Letters` |
| **Content** | The RectTransform that **holds dynamically spawned or scrollable children** (Cards, Rows). Used for the Scroll Rect content and for any runtime-filled area. Only one per ScrollView. | No | `Content` (inside `Viewport`) |
| **Wrapper** | An invisible RectTransform around **exactly one child**, used only for positioning, anchoring, masking or animation (e.g. to animate scale without fighting a Layout Group). | No | `Wrapper_Icon` |

### 7.2 Repeatable items

| Element type | Definition | Example |
|---|---|---|
| **Card** | A self-contained, repeatable view of **one data object**, usually a prefab spawned into a Content or Container. Has its own frame and can have Header/Body/Footer. | `Card_Letter`, `Card_Player` (lobby), `Card_Recipe` |
| **Row** | A one-line repeatable item in a list, without its own frame (settings entry, key binding, stat line). | `Row_KeyBinding`, `Row_Reward` |
| **Slot** | A fixed place that **can hold an item or be empty** (backpack slots, hotbar). Shows an empty state. | `Slot_Backpack_01` |
| **Tab** | A selectable header that switches the visible Panel inside a TabGroup. | `TabGroup_Settings` → `Tab_Audio` |

### 7.3 Atomic elements

**Text**

| Element type | Definition | Example |
|---|---|---|
| **Title** | The main heading of a Screen, Window, Panel, Section or Card. **One per parent.** | `Title` ("Nexus Dispatch Mailbox") |
| **Subtitle** | Secondary heading under a Title. | `Subtitle` ("Arcane Academy of Oakhaven") |
| **Label** | Short **static** text that names something: a caption for a value, a control or a field. Changes only with localization. | `Label_Gold` ("Gold"), `Label_Deadline` |
| **Value** | Short **dynamic** text showing data that changes at runtime: numbers, timers, names. Usually paired with a Label. | `Value_Gold` ("450"), `Value_Timer` ("03:15") |
| **Text** | Multi-line body or descriptive text (flavor text, descriptions, rejection reasons). | `Text_Flavor`, `Text_Description` |

**Graphics**

| Element type | Definition | Example |
|---|---|---|
| **Background** | The fill image behind a Panel, Window, Card or Button. | `Background` |
| **Frame** | A decorative border/outline image, usually 9-sliced. | `Frame_Faction` |
| **Icon** | A small symbolic image representing a thing or an action (element, weapon type, currency). | `Icon_Element`, `Icon_WeaponType` |
| **Image** | A larger illustrative image that is not a symbol (portrait, preview, artwork). | `Image_Portrait` |
| **Divider** | A thin separator line between Sections or Rows. | `Divider` |
| **Badge** | A small marker attached to another element to show a **status or count** (Flawless tag, "new" dot, number of unread letters). | `Badge_Quality`, `Badge_Unread` |
| **Bar** | A progress/amount indicator; its fill child is named `Fill`. | `Bar_Urgency` → `Fill`, `Bar_Health` |

**Controls**

| Element type | Definition | Example |
|---|---|---|
| **Button** | Clickable action. Its text child is `Label`, its image child `Icon`. | `Button_Dispatch` → `Label` |
| **Toggle** | On/off control. | `Toggle_Subtitles` |
| **Slider** | Value selection along a range. | `Slider_MusicVolume` |
| **Dropdown** | Choice from a list (TMP Dropdown). | `Dropdown_Resolution` |
| **InputField** | Text input (TMP Input Field). | `InputField_LobbyName` |

### 7.4 Overlays and world-space elements

| Element type | Definition | Example |
|---|---|---|
| **Tooltip** | Hover/focus information next to an element; no interaction. | `Tooltip_Item` |
| **Toast** | A short, auto-dismissing notification that does not block input. | `Toast_LetterArrived` |
| **Prompt** | The interaction hint shown for the current target (`[E] Pick up Iron Ore`, see [Object Interaction](../GDD/02_Systems/Interaction/_Interaction_System.md)). | `Prompt_Interact` |
| **WorldUI** | Root of a World Space canvas that hosts a **full interface on a 3D object** (Letter Board, Assembly Bench hologram). Inside it, the normal structure applies (Header, Panels, Cards…). | `WorldUI_LetterBoard`, `WorldUI_AssemblyBench` |
| **Marker** | A small world-space indicator above a 3D object or character: nameplate, health above mobs, door price plaque, expedition member list. | `Marker_PlayerName`, `Marker_DoorPrice` |
| **Overlay** | A full-screen non-interactive effect layer (fades, vignettes, loading curtain). | `Overlay_Fade` |

### 7.5 UI layers and sort order

Each layer is a root Screen Space Canvas with a fixed sort order. World Space canvases (Markers, the Letter Board, the Assembly Bench hologram) live on their 3D objects and are not part of this stack.

| Layer | Sort order | Contains |
|---|---|---|
| `Layer_Hud` | 0 | Hud, Prompts |
| `Layer_Screen` | 100 | Screens (main menu, lobby, settings, pause) |
| `Layer_Window` | 200 | Windows |
| `Layer_Popup` | 300 | Popups (modal) |
| `Layer_Notification` | 400 | Toasts, Tooltips |
| `Layer_Overlay` | 500 | Overlays (fade, loading) |

### 7.6 Example hierarchy

The Letter Commission Board (see [UI Design](../GDD/05_UI/Screens/UI_Letter_Commission_Board.md)):

```
WorldUI_LetterBoard                      (World Space canvas on the board)
├── Header
│   ├── Title                            "Nexus Dispatch Mailbox"
│   ├── Label_Reputation                 "Shop Reputation"
│   └── Value_Reputation                 "Lvl 2 (340/500)"
├── Body
│   ├── Panel_LetterQueue
│   │   ├── Title                        "Pending Letters"
│   │   └── ScrollView_Letters
│   │       └── Viewport
│   │           └── Content
│   │               └── Card_Letter      (PF_UI_Card_Letter, spawned per letter)
│   │                   ├── Frame_Faction
│   │                   ├── Icon_WeaponType
│   │                   ├── Icon_Element
│   │                   ├── Title        "Guild: Iron Sword"
│   │                   ├── Value_Timer  "03:15"
│   │                   ├── Bar_Urgency
│   │                   │   └── Fill
│   │                   └── Badge_Batch  "1/3"
│   └── Panel_Dossier
│       ├── Title                        "Active Commission"
│       ├── Text_Flavor
│       ├── Section_Requirements
│       │   ├── Title
│       │   └── Container_Requirements
│       │       └── Row_Requirement      (spawned per criterion)
│       │           ├── Label
│       │           └── Value
│       └── Section_Rewards
│           ├── Title
│           └── Container_Rewards
└── Footer
    └── Container_Actions
        ├── Button_PinToHud
        │   └── Label
        └── Button_Dispatch
            └── Label
```

Children whose type already says everything (`Title`, `Label`, `Fill`, `Content`, `Header`) may drop the `_<Name>` part when there is only one of them under the parent.

---

## 8. Quick Reference

```
Mesh        SM_Shop_AssemblyBench          SK_Mob_BrambleStalker
Texture     T_Shop_AssemblyBench_BC        T_Trim_WoodPlanks_N
Material    M_Shop_AssemblyBench
Prefab      PF_Shop_AssemblyBench          PF_UI_Card_Letter
Animation   A_Player_Roll                  AC_Player
VFX         VFX_Element_Fire_Orb
Audio       SFX_Shop_Anvil_Strike_01       MUS_Workshop_Day
Data        Door_PyroclasticTrench         CraftMaterial_StarMetal
Scene       Workshop                       Realm_VerdantCorruption
UI object   Panel_LetterQueue              Button_Dispatch    Value_Timer
```
