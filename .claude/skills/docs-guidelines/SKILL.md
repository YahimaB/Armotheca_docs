---
name: docs-guidelines
description: Write and maintain Armotheca production standards in Guidelines/: asset structure and naming, UI composition, 3D modeling rules, and art direction (references, concept art workflow). Use for conventions every contributor must follow, whatever the feature.
---

# Guidelines documents

A Guidelines document says **how any contributor must produce assets or code**,
independent of a specific mechanic. It is normative: write rules, budgets and
checklists, not discussion. A rule that applies to one feature belongs in that
feature's GDD or Technical_Design doc instead.

## Layout

```
Guidelines/
├── Assets_Naming.md            # Assets/ folder layout, prefixes, code naming
├── UI_Composition.md           # UI categories, element vocabulary, hierarchy, layers
├── Modeling_Guidelines.md      # 3D style, poly budgets, LODs, textures, export, delivery
└── Art_Direction/
    ├── Visual_Style.md         # Element colours, UI visual style
    ├── Concept_Art_Workflow.md # Concept image, prompt settings, skills used, common failures
    └── References/<Source>/    # Reference screenshots, prefixed per source (AF_1.jpg)
```

Concept art and modeling requirements for one entity or group (description,
palette, images, prompts, sockets, parts) are not guidelines: they live in the
entity's or group's Art doc in the GDD (`docs-gdd`, rule 9).
`Concept_Art_Workflow.md` says how such art is produced and recorded.

Add a new guideline file only for a new discipline (e.g. `Audio_Guidelines.md`,
`Code_Style.md`); otherwise extend an existing one.

## Guideline document template

```markdown
# <Title>

> <One line: who must follow this and what it guarantees.>
> **<Label>:** [<Doc>](<path>) · **<Label>:** [<Doc>](<path>)   <!-- the docs this one builds on: Naming, Modeling, Game context, Tech stack... -->

## 1. <Numbered sections: rules, budgets, conventions>
## <n>. Quick Reference or Delivery Checklist   <!-- optional: when contributors need a one-glance summary -->
## <n+1>. Open Questions
```

- The title names the subject in plain words; the context line is bold-labelled
  links. Every guideline ends with Open Questions.
- Number top-level sections so other docs can cite them (`UI_Composition.md` §2).
- Prefer tables for budgets, prefixes and per-asset rules; give one correct and,
  where useful, one incorrect example.

## Workflow

1. Read the whole guideline being changed; section numbers are referenced
   elsewhere, so append or renumber deliberately.
2. When renumbering or renaming a rule, search all docs for `§<n>` and the old term
   and update them.
3. A changed convention (prefix, folder, budget) may invalidate existing assets in
   `Armotheca_unity/Assets`; tell the user what no longer complies rather than
   renaming assets from here.
4. New guideline file: add it to the README "Guidelines" section.

## Checks

- Rules are stated as requirements with concrete values, not preferences.
- No feature-specific rules that belong in GDD/Technical_Design.
- Images referenced from docs exist; links resolve (run the `docs-routing` link
  check).
