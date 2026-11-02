---
name: docs-technical-design
description: Write and maintain Armotheca technical-design documents in Technical_Design/, organised by code module (one per Armotheca.<Module> namespace) and traced to the GDD docs they implement. Use for architecture, data assets, networking authority, events, performance targets and Unity C# reference code.
---

# Technical Design documents

A Technical_Design document says **how the game is built** in Unity. It is
organised **by code module**, because that is how the code is organised: one module
is one `Armotheca.<Module>` namespace, one assembly and one `Scripts/<Module>/`
folder (`Guidelines/Assets_Naming.md` §3). It implements GDD docs and never
redefines them; when they differ, the GDD wins and the tech doc is updated, or
the conflict is raised to the user.

Read `Technical_Design/Technical_Overview.md` first (stack, targets, architecture
principles), then `_Module_Map.md` to find the module that owns the work.

## Layout

```
Technical_Design/
├── Technical_Overview.md   # stack, targets, principles, networking setup, upgrade plan, open decisions
├── _Module_Map.md          # module ↔ namespace ↔ GDD system, features, entities and UI it implements
└── <Module>/               # Core, Networking, Movement, Interaction, Combat, Crafting, ...
    ├── _<Module>_Module.md # the module: architecture, data, networking, events, code, tests
    └── <Topic>.md          # optional deep dive: Mob_AI.md, Realm_Loading.md
```

- **One vocabulary.** A GDD system and its module share a name
  (`GDD/02_Systems/Combat/` ↔ `Technical_Design/Combat/` ↔ `Armotheca.Combat`).
  Each GDD system maps to exactly one module. Technical-only modules (`Core`,
  `Networking`, `UI`) have no GDD system; `_Module_Map.md` lists what they serve.
- **Entities and UI have no tech docs of their own.** A mob, workstation or screen
  is implemented inside the module that owns its behaviour; the module doc has a
  section for it and `_Module_Map.md` records the mapping.
- **Topics** split out of a module doc when it passes ~400 lines or when one subject
  needs its own approaches and trade-offs. Topic names describe the technical
  subject in the docs naming rule (`Mob_AI.md`), not a GDD ID. The module doc
  links every topic.
- A new module needs the user's approval and the same change in `_Module_Map.md`,
  the GDD system list (via `docs-gdd`) and `Assets_Naming.md` §3 (via
  `docs-guidelines`).

## Templates

| Doc | Template |
| --- | --- |
| Module | [Module](templates/Module.md) |
| Topic | [Topic](templates/Topic.md) |
| Module map | [Module_Map](templates/Module_Map.md) |

Every doc starts with YAML properties (`id`, `type`, `module`, `status`), then
`# <Title>`, then a `>` line linking the GDD docs it implements. Status is one of
`Draft`, `Review`, `Approved`, `Implemented`, `Cut`.

## Rules

1. **Trace both ways.** A module doc's Scope table lists every GDD ID it implements
   with the section that does it. The GDD doc's `Technical:` field links back to
   that section (`_Combat_Module.md#sword-swing`). An untraced section is either
   technical-only (say so) or a gap.
2. **No design values.** Rules and tuning come from the GDD and `06_Balancing/`;
   link them, do not restate them. The Data section maps each `*Definition`
   ScriptableObject field to the balancing table that supplies its value.
   Technical budgets (tick rates, bandwidth, memory, frame time) are owned here.
3. **Networking-first.** Every module states who owns each piece of state, what
   replicates (`SyncVar`, `SyncList`, `[ObserversRpc]`), which intents go through
   `[ServerRpc]`, and what happens on late join and on disconnect mid-action.
4. **Thin network layer.** Rules stay plain C# (no `MonoBehaviour` / FishNet
   dependency) so they are unit-testable; `NetworkBehaviour`s validate intents and
   replicate results. Randomness uses a host-seeded `System.Random`; timers use
   FishNet ticks.
5. **Events out.** Each module lists the C# events (`OnX`) it raises for UI, audio
   and VFX; presentation subscribes and never polls.
6. **Reference code** is illustrative but consistent: real namespaces
   (`Armotheca.<Module>`), shared types from `Core`, names per `Assets_Naming.md`
   §6. Show at least two approaches when the choice is not obvious; mark one
   Recommended and say why.
7. **Stack-wide decisions** (engine, netcode, UI framework, save format) belong in
   Technical Overview. Open ones go to its "Open Technical Decisions" table.

## Workflow

1. Read the GDD docs the work implements (system hub, mechanics, entities, UI) and
   the balancing tables they link; list every rule the code must honour.
2. Find the owning module in `_Module_Map.md`; extend its doc or add a topic.
3. Write the change; update the Scope table and set the GDD docs' `Technical:`
   links (hand back to `docs-gdd` if a GDD doc is missing).
4. When a shared type, namespace or principle changes, update `Core` or Technical
   Overview and search all tech docs for affected code.
5. New module or topic: update `_Module_Map.md` and the README hub.

## Checks

- Every GDD system, entity and UI doc appears in `_Module_Map.md`.
- Scope tables and GDD `Technical:` links agree in both directions.
- No rule or tuning value that is absent from, or different in, the GDD or
  balancing sheets.
- Networking section covers authority, replication, late join and disconnect.
- Links resolve (run the `docs-routing` link check).

## Migration

The current docs mirror the old GDD zones (`Common/`, `Shop/`, `Exploration/`).
Edit them in place until the user approves the reform. The planned split is in
[references/Migration_Map.md](references/Migration_Map.md); migrate after the GDD
docs they implement, so links can point to their new IDs.
