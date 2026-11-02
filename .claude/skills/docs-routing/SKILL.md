---
name: docs-routing
description: Choose where an Armotheca document belongs (DevelopmentPhases, GDD, TechnicalDesign or Guidelines) and hand off to that type's skill. Use for any request to write, update, move, split, review or index documentation in Armotheca_docs.
---

# Route Armotheca documentation

Start from the question the document answers, not from the file the user
happens to mention. Read `README.md` (the hub) and the target folder before
choosing a route.

| The document answers | Type | Folder | Skill |
| --- | --- | --- | --- |
| What the player does and why: rules, flows, tuning, screens and feedback | Game design | `GDD/` | `docs-gdd` |
| How it is built in Unity: architecture, networking, data, C# | Technical design | `TechnicalDesign/` | `docs-technical-design` |
| When and in what order work happens: phases, weeks, milestones, done criteria | Production plan | `DevelopmentPhases/` | `docs-development-phases` |
| How every contributor must produce assets or code, whatever the feature | Standard | `Guidelines/` | `docs-guidelines` |

Read the selected skill before writing. A request that touches several types is
split into one document per type; route each part and say how it was split.

## Tie-breakers

- **New mechanic:** write the GDD first, then the TechnicalDesign doc at the same
  relative path. No C# in a GDD, no design rationale in a tech doc; link instead.
- **Numbers:** a design-facing value (damage, price, lifespan) goes to GDD; a budget
  or target (ms, KB/s, tick rate, poly count) goes to TechnicalDesign or Guidelines;
  a week or deadline goes to DevelopmentPhases.
- **Feature rule vs. standard:** a rule for one feature lives in that feature's doc.
  Promote it to Guidelines only when it applies to every asset or script of a kind.
- **UI:** player-facing layout, states and feedback belong to GDD; element vocabulary
  and hierarchy naming belong to Guidelines (`AssetsNaming.md`); view bindings and
  code belong to TechnicalDesign.
- **Plans quoting specs:** a phase plan links to GDD/Tech sections; it never restates
  their rules. If a plan needs a missing spec, route the spec first.
- Still ambiguous after reading: ask the user, offering the two closest types.

## Legacy folders (pending reform)

These folders predate the four-type layout. Edit their files in place under the
owner skill's rules; do not move them until the user approves the reform. Before
creating a new document of one of these kinds, ask whether to start the reform.

| Current | Proposed target | Owner skill |
| --- | --- | --- |
| `UIDesign/<Area>/*.md` | `GDD/UI/<Area>/*.md` | `docs-gdd` |
| `VisualDesign/References/` | `Guidelines/ArtDirection/References/` | `docs-guidelines` |
| `VisualDesign/ConceptArts/` | `Guidelines/ArtDirection/ConceptArts/` | `docs-guidelines` |
| `VisualDesign/Prompts/` | `Guidelines/ArtDirection/Prompts/` | `docs-guidelines` |

## Shared rules (every route)

- File and folder names are CamelCase; documents are English Markdown.
- Links are relative Markdown links (`[Text](../GDD/Shop/OrderSystem.md)`), not
  Obsidian `[[wikilinks]]`, so they work on Git hosts and in Rider as well.
- Every document opens with an `#` title and a `>` context line linking its
  counterparts (see the type skill for the exact fields).
- `README.md` is the hub. When a document is added, moved, renamed or removed,
  update its structure tree and Quick Navigation in the same change.
- After moving or renaming anything, fix every inbound link, then run the link
  check below. A move without the link check is not finished.
- Images sit next to the document that uses them, or under the folder the type
  skill names. Do not touch `.obsidian/` or `.idea/`.
- Never delete a document or drop a section without the user's confirmation;
  moved content keeps its meaning, only its location changes.
- `Armotheca_docs` is its own git repository. Commit only when asked.

## Link check

Run from `Armotheca_docs`:

```bash
python3 .claude/skills/docs-routing/scripts/check_links.py
```

It reports relative links whose target file is missing and exits non-zero if any
exist. Anchors (`#section`) are not verified; check renamed headings by search.
