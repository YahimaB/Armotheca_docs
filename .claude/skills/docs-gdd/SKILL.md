---
name: docs-gdd
description: Write and maintain Armotheca game-design documents in GDD/, organised by type of thing (features, systems and mechanics, entities, locations, UI, balancing) with one source of truth per thing. Use for rules, player experience, feature hubs, rosters, screens, tuning values and open design questions.
---

# GDD documents

The GDD says **what the player does and why**. It is organised **by type of thing,
not by feature**: mechanics, entities and screens are reused by several features,
so each lives in exactly one file and every other doc links to it. Feature docs
are hubs that tie those pieces together.

Read `00_Overview/Vision.md` first. Its pillars and locked constraints (exactly 2
components per weapon, only Quality and Base Damage, manual labour at launch)
override any single doc. Until the layout reform is done, the vision lives in
`MasterGDD.md`; see [Migration](#migration).

## Layout

```
GDD/
├── 00_Overview/
│   ├── Vision.md                 # pitch, pillars, player fantasy, locked constraints
│   ├── CoreLoop.md               # moment-to-moment, session and meta loops
│   ├── Glossary.md               # term → definition → canonical doc
│   └── Changelog.md              # dated rule/number changes in Approved docs
├── 01_Features/
│   ├── _FeatureList.md           # ID, priority (MoSCoW), status, owner, milestone
│   └── F<NN>_<Name>.md           # hubs: F01_Commissions.md, F03_Expeditions.md
├── 02_Systems/
│   └── <System>/                 # Movement, Interaction, Combat, Crafting, Orders, ...
│       ├── _<System>System.md    # overview + how its mechanics interact
│       └── M_<Name>.md           # M_Roll.md, M_Assembly.md
├── 03_Entities/
│   ├── Player/                   # Player.md, Camera.md
│   ├── Mobs/                     # _MobRoster.md, Common/, ApexGuardians/
│   ├── NPCs/Clients/             # _ClientRoster.md, E_AdventurersGuild.md, ...
│   ├── Items/                    # _ItemList.md, Weapons/, Components/, Materials/, Catalysts/
│   └── Props/                    # _PropList.md, Interactive/, Workstations/, ResourceNodes/
├── 04_Locations/
│   ├── _WorldMap.md              # structure, unlock order, connections
│   └── L<NN>_<Name>/             # L00_Workshop/, L01_VerdantCorruption/
│       ├── L<NN>_<Name>.md
│       └── Maps/                 # layout sketches, blockout captures
├── 05_UI/
│   ├── _UIFlow.md                # screen-to-screen navigation (Mermaid flowchart)
│   ├── Hud/  Menus/  Screens/  World/  Widgets/
│   └── UI_<Name>.md              # inside the category folder; mockups next to it
└── 06_Balancing/
    └── <System>.md               # all numbers, one table per kind of thing
```

UI categories follow `Prefabs/UI/` in `Guidelines/AssetsNaming.md` §3; `World/`
holds diegetic, world-space UI. Art references, mood boards and the UI visual
style guide (fonts, colours, icons) are standards owned by `docs-guidelines`
(`Guidelines/ArtDirection/`), not GDD content. Add a new system, entity category
or UI category only when no existing one fits, and register it in the matching
hub.

## Doc types and IDs

| Type | ID / file | Folder | Template |
| --- | --- | --- | --- |
| Feature | `F<NN>_<Name>` | `01_Features/` | [Feature](templates/Feature.md) |
| System hub | `_<System>System` | `02_Systems/<System>/` | [SystemHub](templates/SystemHub.md) |
| Mechanic | `M_<Name>` | `02_Systems/<System>/` | [Mechanic](templates/Mechanic.md) |
| Entity | `E_<Name>` (`Player`, `Camera` unprefixed) | `03_Entities/<Category>/` | [Entity](templates/Entity.md) |
| Roster / list | `_<Category>Roster`, `_<Category>List` | category root | [Roster](templates/Roster.md) |
| Location | `L<NN>_<Name>` | `04_Locations/L<NN>_<Name>/` | [Location](templates/Location.md) |
| UI | `UI_<Name>` | `05_UI/<Category>/` | [UI](templates/UI.md) |
| Balancing sheet | `<System>` | `06_Balancing/` | [Balancing](templates/Balancing.md) |

- The ID is the file name without `.md`, CamelCase after the prefix. It never
  changes once other docs link to it; rename only with the user's approval and a
  full link update.
- `F` numbers are stable identifiers, not priority. `L` numbers follow unlock
  order (`L00_Workshop`, then realms by the tier that sells their door).
- Doc IDs exist only in the docs. `M_` and `UI_` are also asset prefixes
  (`AssetsNaming.md` §4); asset names always carry a zone or element token
  (`M_Shop_AssemblyBench`), doc IDs never do (`M_Assembly`).
- Every doc starts with YAML properties (`id`, `type`, `status`, plus the
  template's extra fields), then `# <Title>`, then a `>` line with its parent hub
  and technical counterpart.
- Status is one of `Draft`, `Review`, `Approved`, `Implemented`, `Cut`.

## Rules

1. **One thing, one place.** A rule, stat block or behaviour is written only in its
   owner doc: the Roll in `M_Roll`, the Bramble Stalker in `E_BrambleStalker`.
   Other docs link to it with one line of context and never paraphrase it. When
   you find the same content in two places, keep the owner's version and replace
   the other with a link.
2. **Features are hubs.** A feature doc states purpose, pillar, player experience
   and scope, then lists the mechanics, entities, locations and UI it uses. It has
   no rules of its own; a rule that appears to belong only to a feature becomes a
   mechanic.
3. **Systems group mechanics.** A system hub explains how its mechanics interact
   and share state (stamina gates roll and sprint). A mechanic is one rule set the
   player acts through.
4. **Props and mobs are entities, not location content.** A location lists which
   props, mobs and nodes appear there and how many; their behaviour lives in the
   entity doc.
5. **Every doc has a UI section.** Features, mechanics, entities and locations link
   the `UI_` docs that show them, or write `None`. A missing screen is a gap, not
   an omission: add it to `_UIFlow.md` as `Draft`.
6. **Numbers live in balancing sheets.** Docs state the rule ("damage scales with
   Quality tier") and link the sheet row or table; the sheet holds the value. The
   only numbers allowed in prose are locked constraints from the Vision (1–100
   Quality, 2 components, 1–4 players).
7. **Links:** relative Markdown links using the ID as text
   (`[M_Roll](../Movement/M_Roll.md)`), so Obsidian's graph and Git hosts both work.
   Inside a sentence: "uses [M_Parry](…), appears in [L02_PyroclasticTrench](…),
   shown in [UI_HudStamina](…)".
8. **Hubs are kept current.** Adding, renaming or cutting a doc updates its hub
   (`_FeatureList`, system hub, roster, `_WorldMap` or `_UIFlow`) in the same change,
   plus the README hub (see `docs-routing`).

## Overview files

- **Vision.md:** pitch, setting, player fantasy, pillars, locked constraints,
  USP. Links to features by ID; no mechanics.
- **CoreLoop.md:** the three loops, each step linking the feature or mechanic that
  owns it.
- **Glossary.md:** a table of `Term | Definition | Canonical doc`. Defines Feature,
  System, Mechanic, Entity, Location and every project term (Quality, Payload,
  Realm Pressure). Add a term the first time a doc uses it.
- **Changelog.md:** newest first, `YYYY-MM-DD — [ID](link) — what changed and why`.
  Required when a rule or number changes in an `Approved` or `Implemented` doc.

## Workflow

1. **Classify.** Decide which type the content is (use the Glossary definitions).
   Mixed requests split into several docs: the feature hub, its mechanics, its
   entities, its UI and its balancing rows.
2. **Find the owner.** Search by ID and by name across `GDD/`. Extend the owner doc
   if it exists; create one from the template only if none does.
3. **Write.** Fill the template; drop sections that are truly empty rather than
   leaving headings, except `UI` and `Open Questions`, which stay.
4. **Link both ways.** The new doc links its hub and dependencies; the hub, the
   features that use it and the locations where it appears link back.
5. **Propagate.** When a rule or value changes, search TechnicalDesign and
   DevelopmentPhases for the old wording or value and update or flag each hit.
   New or changed mechanics hand off to `docs-technical-design` for the
   counterpart.
6. **Resolve questions.** An answered open question becomes a rule and is
   deleted from Open Questions; log it in the Changelog if the doc is Approved.

## Checks

- Each thing has one owner doc; no paraphrased copies elsewhere.
- Every feature links at least one mechanic and its UI; every mechanic is
  listed in its system hub and in at least one feature.
- Every entity and location has a UI section and appears in its roster or the
  world map.
- No tuning value in prose outside `06_Balancing/`.
- Properties block, title and `>` line present; links resolve (run the
  `docs-routing` link check).

## Migration

The current GDD is organised by zone (`MasterGDD.md`, `Common/`, `Shop/`,
`Exploration/`) and UI lives in the legacy `UIDesign/` folder. Edit those files in
place until the user approves the reform. The planned split of each current
document is in [references/MigrationMap.md](references/MigrationMap.md). Migrate
one source document at a time, then run the link check.
