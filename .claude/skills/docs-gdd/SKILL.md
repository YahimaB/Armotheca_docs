---
name: docs-gdd
description: Write and maintain Armotheca game-design documents in GDD/: the Master GDD, per-mechanic design docs by zone, and player-facing UI screens. Use for rules, flows, tuning values, player experience goals and open design questions.
---

# GDD documents

A GDD document says **what the player does and why**. It is the source of truth
for rules and design-facing numbers; TechnicalDesign implements it, and
DevelopmentPhases schedules it. Read `GDD/MasterGDD.md` first: pillars and locked
constraints (exactly 2 components per weapon, only Quality and Base Damage, manual
labour at launch) override any single mechanic doc.

## Layout

```
GDD/
├── MasterGDD.md            # Vision, core loop, pillars, mechanics index
├── Common/<Mechanic>.md    # Applies in every zone (Movement, Combat, ...)
├── Shop/<Mechanic>.md      # The workshop
├── Exploration/<Mechanic>.md  # Behind the Magic Doors
└── UI/<Area>/<Screen>.md   # Player-facing screens (target of legacy UIDesign/)
```

Zones match `Guidelines/AssetsNaming.md`. A new zone needs the user's approval
and a matching folder in TechnicalDesign.

## Mechanic document template

```markdown
# <Mechanic> (<short subtitle>)

> **Zone:** <Zone> · **Technical counterpart:** [TechnicalDesign/<Zone>/<Mechanic>](../../TechnicalDesign/<Zone>/<Mechanic>.md) · **UI:** [<Screen>](../UI/<Area>/<Screen>.md)

## Design Intent
## Player Experience Goals
## References          <!-- shipped titles: what we take, what we avoid -->
## <Rules, flows and tuning sections specific to the mechanic>
## Open Questions
```

- Mark unproven numbers as initial values (`**Initial value:** 90 s`) so tuning
  passes can find them.
- Use tables for tuning data and per-archetype or per-tier variants.
- Omit the `UI` field when the mechanic has no screen of its own.

## UI screen document template

```markdown
# UI Design: <Screen> (<context>)

> **Mechanic:** [GDD/<Zone>/<Mechanic>](../../<Zone>/<Mechanic>.md) · **Technical:** [TechnicalDesign/<Zone>/<Mechanic>](../../../TechnicalDesign/<Zone>/<Mechanic>.md)

## Screen Overview        <!-- diegetic or overlay, when it opens, who sees it -->
## Layout Structure
## Panel Breakdown        <!-- per panel: content, states, actions -->
## Feedback & States      <!-- hover, disabled, empty, error, success; audio cues -->
```

Use the element vocabulary from `Guidelines/AssetsNaming.md` §7 (Screen, Window,
Panel, Card, ...). Describe behaviour and player-visible data only; bindings and
classes go to the technical counterpart.

## Workflow

1. Check the Master GDD index and the zone folder; extend an existing doc before
   creating a new one.
2. Write or edit the doc. Keep implementation detail out; if it is needed, add a
   note to the technical counterpart instead.
3. When a rule or number changes, search TechnicalDesign, DevelopmentPhases and
   other GDD docs for the old value and update or flag each occurrence.
4. New mechanic: add it to the Master GDD mechanics index and the README tables,
   then hand off to `docs-technical-design` for the counterpart (a stub is fine).
5. Resolved open questions move into the rules; delete the question.

## Checks

- Header line present and links resolve (run the `docs-routing` link check).
- No contradiction with Master GDD pillars and locked constraints.
- Every mechanic doc has a technical counterpart at the same relative path.
