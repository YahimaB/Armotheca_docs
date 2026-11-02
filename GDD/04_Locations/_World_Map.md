---
id: _World_Map
type: world-map
status: Draft
---

# World Map

> **Overview:** [Vision](../00_Overview/Vision.md) · **Technical:** [Realm_Loading](../../Technical_Design/Exploration/Realm_Loading.md)

## Structure

The workshop floats in the ethereal void; its Threshold of Portals holds Magic Doors, each opening onto one **separate realm** — a compact, hand-crafted pocket dimension with its own look, resources and monsters. Variety comes from four strongly themed realms, each with a fresh resource and mob arrangement every time its door opens ([M_Realm_Instancing](../02_Systems/Exploration/M_Realm_Instancing.md)).

| ID | Location | Theme | Main Materials | Main Elements | Apex Guardian → Catalyst | Unlock |
|---|---|---|---|---|---|---|
| [L00_Workshop](L00_Workshop/L00_Workshop.md) | The Armotheca workshop | Extradimensional emporium | — | — | — | Start |
| [L01_Verdant_Corruption](L01_Verdant_Corruption/L01_Verdant_Corruption.md) | Verdant Corruption | Overgrown corrupted grove | Timber (Bog Oak, Ironwood), Iron Vein, beast parts | Physical, Arcane | Verdant Elder → *Sylvan Spire* | Owned at start |
| [L02_Pyroclastic_Trench](L02_Pyroclastic_Trench/L02_Pyroclastic_Trench.md) | Pyroclastic Trench | Volcanic chasm | Obsidian, Brimstone, salamander essence | Fire | Pyroclastic Apex → *Ignis Core* | Tier 2 + gold |
| [L03_Astral_Quarry](L03_Astral_Quarry/L03_Astral_Quarry.md) | Astral Quarry | Floating starlit rock | Quartz, Star Metal, void essence | Arcane, Lightning | Astral Sovereign → *Astral Prism* | Tier 3 + gold |
| [L04_Frostbite_Cavern](L04_Frostbite_Cavern/L04_Frostbite_Cavern.md) | Frostbite Cavern | Ice caves | Glacial Ice-Ore, wraith essence | Frost | Frost Wyrm → *Glacial Heart* | Tier 3 + gold |

Unlock rules: [M_Door_Purchase](../02_Systems/Exploration/M_Door_Purchase.md). Each realm is the main source of specific materials, so active letters dictate which door to open.

## Realm Bands

Every realm follows the same layout:

```
 [ENTRY]  ----->  [OUTER GROUNDS]  ----->  [DEEP GROUNDS]  ----->  [APEX ARENA]
 Arrival point,   Common nodes,            Rare nodes,             Apex Guardian,
 Exit Portal,     weak mobs                stronger mobs           catalyst
 Aether Chute
 (safe zone)
```

- **Entry:** arrival point, the always-open [E_Exit_Portal](../03_Entities/Props/Interactive/E_Exit_Portal/E_Exit_Portal.md) and the [E_Aether_Chute](../03_Entities/Props/Interactive/E_Aether_Chute/E_Aether_Chute.md). No mobs spawn here.
- **Outer Grounds:** close to the entry; common nodes and minor fauna. Suited to short supply runs and kept small enough to cross quickly.
- **Deep Grounds:** further away; rare nodes and elemental beasts that drop cores. Reaching them means staying longer under rising Realm Pressure ([M_Realm_Pressure](../02_Systems/Exploration/M_Realm_Pressure.md)).
- **Apex Arena:** gated area holding the realm's Apex Guardian. Since realms have no time limit, the fight fits in a normal expedition; the gate opens once the shop reaches Tier 3.

Layout targets (crossing time) are in [Exploration › Targets](../06_Balancing/Exploration.md#targets).

## Open Questions

- Should the Apex Arena gate open with Tier 3 for every realm, or require a per-realm key (e.g. an Academy portal stabiliser formula)?
- Should element-specific hazards exist (lava floors, slippery ice) and interact with movement?
