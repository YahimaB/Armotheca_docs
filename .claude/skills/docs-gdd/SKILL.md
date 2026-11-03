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
override any single doc.

## Layout

```
GDD/
├── 00_Overview/
│   ├── Vision.md               # pitch, pillars, player fantasy, locked constraints
│   ├── Core_Loop.md            # moment-to-moment, session and meta loops
│   ├── Glossary.md             # term → definition → canonical doc
│   └── Changelog.md            # dated rule/number changes in Approved docs
├── 01_Features/
│   ├── _Feature_List.md        # ID, priority (MoSCoW), status, owner, milestone
│   └── F<NN>_<Name>.md         # hubs: F01_Commissions.md, F03_Expeditions.md
├── 02_Systems/
│   └── <System>/               # Movement, Interaction, Combat, Crafting, Processing, ...
│       ├── _<System>_System.md # overview + how its mechanics interact
│       └── M_<Name>.md         # M_Roll.md, M_Assembly.md
├── 03_Entities/
│   ├── Player/                 # Player.md (the only entity in its category: this is its folder)
│   ├── Mobs/                   # _Mob_Roster.md, Minor_Fauna/, Elemental_Beasts/, Apex_Guardians/
│   ├── NPCs/Clients/           # _Client_Roster.md, E_Adventurers_Guild/, ...
│   ├── Items/                  # _Item_List.md, Weapons/, Components/, Catalysts/
│   └── Props/                  # _Prop_List.md, Interactive/, Workstations/, Resource_Nodes/
│       └── <Group>/E_<Name>/   # one folder per entity
│           ├── E_<Name>.md
│           ├── E_<Name>_Art.md # optional: concept art description and history
│           └── Art/            # E_<Name>_Art_<NN>_<Short_Name>.png
├── 04_Locations/
│   ├── _World_Map.md           # structure, unlock order, connections
│   └── L<NN>_<Name>/           # L00_Workshop/, L01_Verdant_Corruption/
│       ├── L<NN>_<Name>.md
│       └── Maps/               # layout sketches, blockout captures
├── 05_UI/
│   ├── _UI_Flow.md             # screen-to-screen navigation (Mermaid flowchart)
│   ├── Hud/  Screens/  Windows/  Popups/  Widgets/  World/
│   └── UI_<Name>.md            # inside the category folder; mockups next to it
└── 06_Balancing/
    └── <System>.md             # all numbers, one table per kind of thing
```

UI categories, and which one a UI doc goes in, are defined in
`Guidelines/UI_Composition.md` §2; `Prefabs/UI/` uses the same folders. An
entity's own concept art belongs to the entity (its Art doc); art references,
mood boards and the UI visual style guide (fonts, colours, icons) are standards
owned by `docs-guidelines` (`Guidelines/Art_Direction/`), not GDD content. Add a
new system, entity category or UI category only when no existing one fits, and
register it in the matching hub (a UI category in `UI_Composition.md` §2).

System names equal code module names: `02_Systems/Combat/` is implemented by
`Technical_Design/Combat/` in `Armotheca.Combat`. A new or renamed system is
agreed with `docs-technical-design` in the same change. Every `Technical:` link
points to a module doc section, or to `_Module_Map.md` for features.

## Doc types and IDs

| Type | ID / file | Folder | Template |
| --- | --- | --- | --- |
| Feature | `F<NN>_<Name>` | `01_Features/` | [Feature](templates/Feature.md) |
| System hub | `_<System>_System` | `02_Systems/<System>/` | [System_Hub](templates/System_Hub.md) |
| Mechanic | `M_<Name>` | `02_Systems/<System>/` | [Mechanic](templates/Mechanic.md) |
| Entity | `E_<Name>` (`Player`, `Camera` unprefixed) | `03_Entities/<Category>/<Group>/E_<Name>/` | [Entity](templates/Entity.md) |
| Entity art | `E_<Name>_Art` | the entity's folder | [Entity_Art](templates/Entity_Art.md) |
| Roster / list | `_<Category>_Roster`, `_<Category>_List` | category root | [Roster](templates/Roster.md) |
| Location | `L<NN>_<Name>` | `04_Locations/L<NN>_<Name>/` | [Location](templates/Location.md) |
| UI | `UI_<Name>` | `05_UI/<Category>/` | [UI](templates/UI.md) |
| Balancing sheet | `<System>` | `06_Balancing/` | [Balancing](templates/Balancing.md) |

- The ID is the file name without `.md`, in the docs naming rule from
  `docs-routing` (`M_Sword_Swing`, `E_Bramble_Stalker`, `_Combat_System`). It
  never changes once other docs link to it; rename only with the user's approval
  and a full link update.
- `F` numbers are stable identifiers, not priority. `L` numbers follow unlock
  order (`L00_Workshop`, then realms by the tier that sells their door).
- Doc IDs exist only in the docs and are never used as asset names. `M_` and `UI_`
  are also asset prefixes (`Assets_Naming.md` §4), but assets join CamelCase words
  after a zone token (`M_Shop_AssemblyBench`) while doc IDs separate every word and
  carry no zone (`M_Assembly`, `UI_Assembly_Bench`).
- Every doc starts with YAML properties (`id`, `type`, `status`, plus the
  template's extra fields), then `# <Title>`, then a `>` line with its parent hub
  and technical counterpart.
- Status is one of `Draft`, `Review`, `Approved`, `Implemented`, `Cut`.

## Rules

1. **One thing, one place.** A rule, stat block or behaviour is written only in its
   owner doc: the Roll in `M_Roll`, the Bramble Stalker in `E_Bramble_Stalker`.
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
   an omission: add it to `_UI_Flow.md` as `Draft`.
6. **Numbers live in balancing sheets.** Docs state the rule ("damage scales with
   Quality tier") and link the sheet row or table; the sheet holds the value. The
   only numbers allowed in prose are locked constraints from the Vision (1–100
   Quality, 2 components, 1–4 players).
7. **Links:** relative Markdown links using the ID as text
   (`[M_Roll](../Movement/M_Roll.md)`), so Obsidian's graph and Git hosts both work.
   Inside a sentence: "uses [M_Parry](…), appears in [L02_Pyroclastic_Trench](…),
   shown in [UI_Hud_Stamina](…)".
8. **Hubs are kept current.** Adding, renaming or cutting a doc updates its hub
   (`_Feature_List`, system hub, roster, `_World_Map` or `_UI_Flow`) in the same change,
   plus the README hub (see `docs-routing`).
9. **Entity art lives with the entity.** Every entity has its own folder. Its
   concept art goes in an optional `E_<Name>_Art.md` beside the entity doc, which
   links it from Art & Audio References. The Art doc holds:
   - **Description:** the look in a few sentences plus a list of key visual
     elements; behaviour and role stay in the entity doc.
   - **Palette:** key colours, each a swatch followed by its hex value:
     ``<span style="color:#3A4A61;">■</span> `#3A4A61` ``.
   - **Selected:** a table of the chosen History versions in version order; the
     first row links each heading, the second shows its image.
   - **History:** one `### <NN> <Short Name>` entry per kept image, newest first,
     with the image, the AI model and the prompt folded in a quoted
     `<details><summary>Prompt</summary>` block (see the template). A version
     is one image that was kept; rejected variants are not recorded. Numbers are
     two digits and never reused. A generated image records its full prompt; an
     edited one records the prompt that changed the version it was made from.
   - **Images** live in the entity's `Art/` folder, named
     `E_<Name>_Art_<NN>_<Short_Name>.png` so the file matches its History heading
     (`### 02 Glowing Core` → `E_Void_Slime_Art_02_Glowing_Core.png`).
   - **Image size:** every image, in Selected and History, is an HTML `<img>`
     capped at 400×400, whatever its aspect:
     `<img src="Art/E_Void_Slime_Art_02_Glowing_Core.png" alt="02 Glowing Core" style="max-width:400px; max-height:400px;">`.

## Overview files

- **Vision.md:** pitch, setting, player fantasy, pillars, locked constraints,
  USP. Links to features by ID; no mechanics.
- **Core_Loop.md:** the three loops, each step linking the feature or mechanic that
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
5. **Propagate.** When a rule or value changes, search Technical_Design and
   Development_Phases for the old wording or value and update or flag each hit.
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
- Every entity sits in its own folder; every Art doc's Selected links and images
  match History headings, and every History image exists in `Art/` under the matching
  name.
- No tuning value in prose outside `06_Balancing/`.
- Properties block, title and `>` line present; links resolve (run the
  `docs-routing` link check).

## Migration

The GDD was migrated from its zone layout on 2026-11-02 (see `00_Overview/Changelog.md`).
[references/Migration_Map.md](references/Migration_Map.md) records where each old
section went; use it to answer "where did X go" questions.
