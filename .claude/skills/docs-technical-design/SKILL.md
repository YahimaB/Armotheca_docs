---
name: docs-technical-design
description: Write and maintain Armotheca technical-design documents in Technical_Design/: the Technical Overview and per-mechanic implementation docs mirroring the GDD. Use for architecture, networking authority, performance targets, data models and Unity C# reference code.
---

# Technical Design documents

A Technical_Design document says **how a GDD mechanic is built** in Unity. It
implements the matching GDD doc and never redefines its rules; when they differ,
the GDD wins and the tech doc is updated (or the conflict is raised to the user).
Read `Technical_Design/Technical_Overview.md` first: its stack, architecture
principles, networking model and shared types apply to every doc here.

## Layout

```
Technical_Design/
├── Technical_Overview.md # Stack, targets, architecture, shared types, upgrades
├── Common/<Mechanic>.md
├── Shop/<Mechanic>.md
└── Exploration/<Mechanic>.md
```

The path mirrors `GDD/` exactly: `GDD/Shop/Order_System.md` ↔
`Technical_Design/Shop/Order_System.md`. UI screens have no separate tech doc; their
view and binding notes live in the mechanic's tech doc.

## Mechanic document template

```markdown
# <Mechanic> - Technical Design

> **Zone:** <Zone> · **Design:** [GDD/<Zone>/<Mechanic>](../../GDD/<Zone>/<Mechanic>.md) · **UI:** [<Screen>](../../GDD/UI/<Area>/<Screen>.md)

## Technical Specifications     <!-- limits, tick rates, budgets, evaluation order -->
## Architecture & Implementation Approaches
### Approach A: <name> (Recommended)   <!-- pros / cons -->
### Approach B: <name>
## Networking                   <!-- authority, replicated state, RPCs, late join, disconnect -->
## Unity C# Reference Code
## Testing Notes
```

## Rules

- **Networking-first:** every mechanic states who owns the state, what replicates
  (`SyncVar`, `SyncList`, `[ObserversRpc]`), which intents go through `[ServerRpc]`,
  and what happens on late join and on disconnect mid-action.
- Rules stay plain C# (no `MonoBehaviour` / FishNet dependency) so they are
  unit-testable; `NetworkBehaviour`s validate intents and replicate results.
- Randomness uses a host-seeded `System.Random`; timers use FishNet ticks.
- Reference code is illustrative but compilable in spirit: real namespaces
  (`Armotheca.*`), types from Technical Overview §5, names per
  `Guidelines/Assets_Naming.md` §6.
- Show at least two approaches when the choice is not obvious; mark one
  Recommended and say why.
- Stack-wide decisions (engine, netcode, UI framework) belong in Technical
  Overview, not in a mechanic doc. Open stack-wide questions go to its
  "Open Technical Decisions" section.

## Workflow

1. Read the GDD counterpart in full; list every rule and number the tech doc must
   honour.
2. Write or edit the doc; link to GDD sections instead of restating them.
3. When a shared type, namespace or principle changes, update Technical Overview
   and search all tech docs for affected code.
4. New doc: add it to the README tables and to the GDD header line's counterpart
   link (hand back to `docs-gdd` if the GDD doc does not exist yet).

## Checks

- Header line present; GDD counterpart exists at the mirrored path.
- No rule or tuning value that is absent from, or different in, the GDD.
- Networking section covers authority, replication, late join and disconnect.
- Links resolve (run the `docs-routing` link check).
