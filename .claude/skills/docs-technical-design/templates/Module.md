---
id: _<Module>_Module
type: module
module: <Module>
namespace: Armotheca.<Module>
status: Draft
---

# <Module> Module

> **Design:** [_<Module>_System](../../GDD/02_Systems/<Module>/_<Module>_System.md) · **Map:** [_Module_Map](../_Module_Map.md) · **Overview:** [Technical Overview](../Technical_Overview.md)

## Scope

| GDD doc | Implemented in |
| --- | --- |
| [M_<Name>](../../GDD/02_Systems/<Module>/M_<Name>.md) | [<Section>](#<section>) |

<!-- Topics: - [<Topic>](<Topic>.md): what it covers -->

## Technical Specifications

<!-- Limits, tick rates, budgets, evaluation order. Technical numbers only; design values are linked. -->

## Architecture & Implementation Approaches

### Approach A: <name> (Recommended)

<!-- Classes and responsibilities; pros and cons. -->

### Approach B: <name>

## Data

| Definition (SO) | Field | Supplied by |
| --- | --- | --- |
| `<Name>Definition` | `<field>` | [<System> › <Table>](../../GDD/06_Balancing/<System>.md#<table>) |

<!-- Runtime state: plain C# classes/structs, what identifies them over the network. -->

## Networking

<!-- Authority per piece of state; replicated state; ServerRpc intents; late join; disconnect mid-action; bandwidth if per-tick. -->

## Events

| Event | Raised when | Consumed by |
| --- | --- | --- |
| `On<Event>` |  | UI / audio / VFX |

## <One section per mechanic, entity or screen in Scope>

## Unity C# Reference Code

## Testing Notes

<!-- EditMode tests for pure rules; PlayMode / Multiplayer Play Mode checks for networking. -->

## Open Technical Questions

-
