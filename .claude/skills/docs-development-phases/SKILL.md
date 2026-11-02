---
name: docs-development-phases
description: Write and maintain Armotheca production plans in Development_Phases/: the Development Roadmap and per-phase weekly plans with required sources, networking work and done criteria. Use for scheduling, milestones, scope cuts, progress tracking and phase acceptance.
---

# Development Phases documents

A Development_Phases document says **when and in what order** work happens and how
each step is accepted. It schedules GDD and Technical_Design content; it does not
specify it. If a week needs a rule or class that no spec describes, route that
spec through `docs-routing` first and link it from the plan.

## Layout

```
Development_Phases/
├── Development_Roadmap.md    # All phases, Networking-First Principle, milestones
└── Phase_<N>_<Short_Name>.md # Weekly plan for one phase (e.g. Phase_1_Core_Loop.md)
```

One roadmap; one weekly-plan file per phase, created when that phase is planned
in detail. The roadmap keeps each phase's duration, focus and deliverables and
links to its weekly plan.

## Phase plan template

```markdown
# Phase <N>: <Name> — Weekly Plan

> Part of the [Development Roadmap](Development_Roadmap.md) · Design: [Master GDD](../GDD/Master_GDD.md) · Tech: [Technical Overview](../Technical_Design/Technical_Overview.md) · Naming: [Assets Naming](../Guidelines/Assets_Naming.md) · Art specs: [Modeling Guidelines](../Guidelines/Modeling_Guidelines.md)

**Duration:** <weeks> (Months <a–b>)
**Focus:** <one sentence>

## Phase Goal              <!-- one observable, testable end-of-phase scenario -->
## How to Read This Plan
### Global Definition of Done (every week)
### Overview              <!-- week → theme table -->
## Week <n> — <Theme>
### Required sources      <!-- links to GDD/Tech sections this week implements -->
### Work this week
### Networking
### Done when             <!-- checkable statements, not activities -->
```

## Rules

- Every feature is accepted as networked (host + at least one client, late join,
  disconnect mid-action) per the roadmap's Networking-First Principle. Do not
  schedule a separate "make it multiplayer" step.
- "Done when" items are verifiable outcomes ("a client sees the same letter queue
  after rejoining"), never tasks ("implement OrderManager").
- Mark go/no-go gates explicitly and say what happens on no-go.
- Link specs by section; never copy rules or numbers from GDD/Tech into a plan.
- Scope changes: update the roadmap and the phase plan together, and note what
  moved to which phase.

## Workflow

1. Read the roadmap, the phase plan and every spec the change touches.
2. Edit the plan; keep week numbering contiguous and the Overview table in sync.
3. When a phase deliverable changes, update the roadmap's deliverables list.
4. New phase plan: link it from the roadmap and the README "Production &
   Milestones" section.

## Checks

- Each week has Required sources, Work, Networking and Done when.
- Every Required source link resolves (run the `docs-routing` link check).
- Roadmap and phase plan agree on duration, focus and deliverables.
