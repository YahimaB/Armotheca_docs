# Assets Structure & Naming

> Single source of truth for how the Unity project's `Assets/` folder is organized and how every asset and GameObject is named. UI elements and their hierarchy follow [UI Composition](UI_Composition.md).
> Related: [3D Modeling Guidelines](Modeling_Guidelines.md) · [UI Composition](UI_Composition.md) · [Technical Overview](../Technical_Design/Technical_Overview.md)

---

## 1. General Rules

1. **PascalCase words, underscores between parts.** Each part of a name is written in PascalCase (`AssemblyBench`, `StarMetal`); underscores only separate the parts.
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
│   │   ├── UI/                                 # one folder per UI category (UI Composition §2)
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
- Folder names are PascalCase. **Category folders are plural** (`Props`, `Mobs`, `Workstations`); **a folder for one asset is singular** and named after it (`AssemblyBench`, `BrambleStalker`).
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
| UI prefab | `PF_UI_` | `PF_UI_<Name>_<ElementType>` ([UI Composition §1](UI_Composition.md#1-general-rules)) | `PF_UI_Letter_Widget` |
| UI sprite | `UI_` | `UI_<ElementType>_<Name>` ([UI Composition §1](UI_Composition.md#1-general-rules)) | `UI_Icon_Element_Frost` |
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
| `_N` | Normal |
| `_MS` | Metallic + Smoothness |
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

- **File name = class name**, PascalCase, one public type per file: `AssemblyBench.cs`.
- **Interfaces** start with `I`: `IDamageable`, `IContinuousInteractable`.
- **ScriptableObject classes** end with `Definition`, `Settings`, `Profile`, `Table` or `Recipe` (as in the tech docs).
- **Namespaces** follow `Armotheca.<Area>` and match the `Scripts/` folder (see §3).
- **UI view components** are named `<Name><ElementType>` ([UI Composition](UI_Composition.md)): `MainMenuScreen`, `ConfirmPopup`, `LetterWidget`, `LetterQueuePanel`, `LetterBoardWorldUI`.
- **Private fields** `camelCase`; **properties, methods, events** `PascalCase`; events start with `On`: `OnStateChanged`.

---

## 7. Quick Reference

```
Mesh        SM_Shop_AssemblyBench          SK_Mob_BrambleStalker
Texture     T_Shop_AssemblyBench_BC        T_Trim_WoodPlanks_N
Material    M_Shop_AssemblyBench
Prefab      PF_Shop_AssemblyBench          PF_UI_Letter_Widget
Animation   A_Player_Roll                  AC_Player
VFX         VFX_Element_Fire_Orb
Audio       SFX_Shop_Anvil_Strike_01       MUS_Workshop_Day
Data        Door_PyroclasticTrench         CraftMaterial_StarMetal
Scene       Workshop                       Realm_VerdantCorruption
UI object   LetterQueue_Panel              Dispatch_Button    Timer_Value
```
