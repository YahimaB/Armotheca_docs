---
id: E_Primordial_Catalyst
type: entity
category: Items
status: Draft
---

# Primordial Catalysts

> **Roster:** [_Item_List](../_Item_List.md) · **Technical:** [_Endgame_Module › Technical Specifications](../../../../Technical_Design/Endgame/_Endgame_Module.md#technical-specifications)

## Description & Role

Four unique catalysts, each guarded by an Apex Guardian deep inside one realm. Together they are the ingredients of the Uber-Weapon ([F06_Uber_Weapon](../../../01_Features/F06_Uber_Weapon.md)).

```
                        [THE PRIMORDIAL ARMAMENT]
                                   |
       +---------------+-----------+-----------+---------------+
       |               |                       |               |
       v               v                       v               v
 [Ignis Core]    [Sylvan Spire]          [Astral Prism]   [Glacial Heart]
 (Pyroclastic    (Verdant Elder)         (Astral          (Frost Wyrm)
  Apex)                                   Sovereign)
```

| Catalyst | Guardian | Realm | Ritual use |
| --- | --- | --- | --- |
| Ignis Core | [E_Pyroclastic_Apex](../../Mobs/Apex_Guardians/E_Pyroclastic_Apex.md) | [L02_Pyroclastic_Trench](../../../04_Locations/L02_Pyroclastic_Trench/L02_Pyroclastic_Trench.md) | Phase 1, melted |
| Astral Prism | [E_Astral_Sovereign](../../Mobs/Apex_Guardians/E_Astral_Sovereign.md) | [L03_Astral_Quarry](../../../04_Locations/L03_Astral_Quarry/L03_Astral_Quarry.md) | Phase 1, melted |
| Sylvan Spire | [E_Verdant_Elder](../../Mobs/Apex_Guardians/E_Verdant_Elder.md) | [L01_Verdant_Corruption](../../../04_Locations/L01_Verdant_Corruption/L01_Verdant_Corruption.md) | Phase 2, carved into the Adamantine Shaft |
| Glacial Heart | [E_Frost_Wyrm](../../Mobs/Apex_Guardians/E_Frost_Wyrm.md) | [L04_Frostbite_Cavern](../../../04_Locations/L04_Frostbite_Cavern/L04_Frostbite_Cavern.md) | Phase 3, the quench solution |

## Behaviour & States

- Dropped by its Guardian on defeat; Guardians do not respawn once their catalyst is taken (except in Prestige mode).
- Stored on a dedicated display pedestal in the workshop so progress is always visible.
- Never destroyed by a failed ritual phase ([M_Forging_Ritual](../../../02_Systems/Endgame/M_Forging_Ritual.md)).

## UI

None yet; the pedestal is a world object (planned in [_Prop_List](../../Props/_Prop_List.md)).

## Appears In

- Apex Arenas of all four realms; [L00_Workshop](../../../04_Locations/L00_Workshop/L00_Workshop.md) pedestal.
- [F06_Uber_Weapon](../../../01_Features/F06_Uber_Weapon.md)

## Open Questions

-
