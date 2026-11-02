---
name: docs-guidelines
description: Write and maintain Armotheca production standards in Guidelines/: asset structure and naming, 3D modeling rules, and art direction (references, style). Use for conventions every contributor must follow, whatever the feature.
---

# Guidelines documents

A Guidelines document says **how any contributor must produce assets or code**,
independent of a specific mechanic. It is normative: write rules, budgets and
checklists, not discussion. A rule that applies to one feature belongs in that
feature's GDD or Technical_Design doc instead.

## Layout

```
Guidelines/
├── Assets_Naming.md            # Assets/ folder layout, prefixes, code naming, UI vocabulary
├── Modeling_Guidelines.md      # 3D style, poly budgets, LODs, textures, export, delivery
└── Art_Direction/              # Target of legacy Visual_Design/References/
    └── References/<Source>/    # Reference screenshots, prefixed per source (AF_1.jpg)
```

Concept art for a specific entity (description, palette, images, prompts) is not a
guideline: it lives in the entity's Art doc in the GDD (`docs-gdd`, rule 9).

Add a new guideline file only for a new discipline (e.g. `Audio_Guidelines.md`,
`Code_Style.md`); otherwise extend an existing one.

## Guideline document template

```markdown
# <Discipline> Guidelines

> <One line: who must follow this and what it guarantees.>
> **Naming:** [Assets Naming](Assets_Naming.md) · **Game context:** [Vision](../GDD/00_Overview/Vision.md) · **Tech stack:** [Technical Overview](../Technical_Design/Technical_Overview.md)

## 1. <Numbered sections: rules, budgets, conventions>
## <n>. Quick Reference or Delivery Checklist
## <n+1>. Open Questions
```

- Number top-level sections so other docs can cite them (`Assets_Naming.md` §7).
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
