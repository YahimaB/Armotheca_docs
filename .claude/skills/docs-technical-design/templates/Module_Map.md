---
id: _Module_Map
type: map
status: Draft
---

# Module Map

> **Overview:** [Technical Overview](Technical_Overview.md) · **Naming:** [Assets Naming §3](../Guidelines/Assets_Naming.md)

Each module is one `Armotheca.<Module>` namespace, one assembly
(`Scripts/<Module>/Armotheca.<Module>.asmdef`) and one folder here.

## Modules

| Module | Namespace | GDD system | Doc | Depends on |
| --- | --- | --- | --- | --- |
| Core | `Armotheca.Core` | — | [_Core_Module](Core/_Core_Module.md) | — |

## Entities and UI

Where each GDD entity and screen is implemented.

| GDD doc | Module | Section |
| --- | --- | --- |
| [E_<Name>](../GDD/03_Entities/<Category>/<Group>/E_<Name>.md) | <Module> | [<Section>](<Module>/_<Module>_Module.md#<section>) |

## Features

| Feature | Modules |
| --- | --- |
| [F<NN>_<Name>](../GDD/01_Features/F<NN>_<Name>.md) |  |
