---
id: E_Magic_Door
type: entity
category: Props
status: Draft
---

# Magic Door

> **Roster:** [_Prop_List](../_Prop_List.md) · **Technical:** [Magic Doors (tech)](../../../../Technical_Design/Exploration/Magic_Doors.md)

## Description & Role

A door in the workshop's Threshold of Portals that opens onto one realm. Doors are the resource lifeline of the shop and are **bought, not granted**.

| Door | Realm |
| --- | --- |
| Door 1 | [L01_Verdant_Corruption](../../../04_Locations/L01_Verdant_Corruption/L01_Verdant_Corruption.md) |
| Door 2 | [L02_Pyroclastic_Trench](../../../04_Locations/L02_Pyroclastic_Trench/L02_Pyroclastic_Trench.md) |
| Door 3 | [L03_Astral_Quarry](../../../04_Locations/L03_Astral_Quarry/L03_Astral_Quarry.md) |
| Door 4 | [L04_Frostbite_Cavern](../../../04_Locations/L04_Frostbite_Cavern/L04_Frostbite_Cavern.md) |

## Behaviour & States

| State | Enters when | Does | Exits when |
| --- | --- | --- | --- |
| Locked | Required tier not reached | Not shown | Tier reached |
| Sealed for sale | Tier reached | Shows a price plaque | Gold paid ([M_Door_Purchase](../../../02_Systems/Exploration/M_Door_Purchase.md)) |
| Ready | Owned, closed | Can be opened | A player opens it |
| Entry Open | Opened | Anyone may pass | Entry window ends |
| In Progress | Window closed with players inside | Shimmering sealed surface with member names; only members pass | Realm empties |
| Cooldown | Realm empty | Rests | Cooldown ends |

Full rules: [M_Door_Lifecycle](../../../02_Systems/Exploration/M_Door_Lifecycle.md).

## Stats

Price and required tier: [Progression › Doors](../../../06_Balancing/Progression.md#doors). Timings: [Exploration › Doors](../../../06_Balancing/Exploration.md#doors).

## Mechanics

- [M_Door_Purchase](../../../02_Systems/Exploration/M_Door_Purchase.md), [M_Door_Lifecycle](../../../02_Systems/Exploration/M_Door_Lifecycle.md), [M_Realm_Instancing](../../../02_Systems/Exploration/M_Realm_Instancing.md)

## UI

- [UI_Interaction_Prompt](../../../05_UI/World/UI_Interaction_Prompt.md): open, enter and the price plaque.

## Art & Audio References

- Magic Door reference image AF_4 in [Modeling Guidelines](../../../../Guidelines/Modeling_Guidelines.md).

## Appears In

- [L00_Workshop](../../../04_Locations/L00_Workshop/L00_Workshop.md) (Threshold of Portals)
- [F03_Expeditions](../../../01_Features/F03_Expeditions.md), [F05_Shop_Progression](../../../01_Features/F05_Shop_Progression.md)

## Open Questions

-
