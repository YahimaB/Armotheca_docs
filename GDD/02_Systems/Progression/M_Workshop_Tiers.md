---
id: M_Workshop_Tiers
type: mechanic
system: Progression
status: Draft
---

# Workshop Tiers

> **System:** [_Progression_System](_Progression_System.md) · **Technical:** [_Progression_Module › Tier Assets](../../../Technical_Design/Progression/_Progression_Module.md#tier-assets)

## Summary

Three workshop tiers, each bought with gold once the reputation threshold is met.

## Rules

```
+--------------------------------------------------------------------------+
|                        WORKSHOP PROGRESSION LADDER                       |
+--------------------------------------------------------------------------+
| TIER 1: RUSTIC FORGE       | 1 Door owned, 3 Workbench Stations          |
| TIER 2: ARCANE ATELIER     | +1 Door for sale, Lathe & Extractor         |
| TIER 3: ASTRAL ARMOTHECA   | +2 Doors for sale, The Great Crucible       |
+--------------------------------------------------------------------------+
```

| Workshop Tier | Unlocked Capabilities | Doors Made Available |
|---|---|---|
| **Tier 1: Rustic Forge** | Basic Anvil, Basic Smelter, Guild commissions | [L01_Verdant_Corruption](../../04_Locations/L01_Verdant_Corruption/L01_Verdant_Corruption.md) (owned at start) |
| **Tier 2: Arcane Atelier** | Woodworking Lathe, Arcane Extractor, Academy commissions | [L02_Pyroclastic_Trench](../../04_Locations/L02_Pyroclastic_Trench/L02_Pyroclastic_Trench.md) |
| **Tier 3: Astral Armotheca** | Quenching Basins, **The Great Crucible** (Uber-Weapon), Apex Arena gates | [L03_Astral_Quarry](../../04_Locations/L03_Astral_Quarry/L03_Astral_Quarry.md), [L04_Frostbite_Cavern](../../04_Locations/L04_Frostbite_Cavern/L04_Frostbite_Cavern.md) |

1. Upgrading costs gold; reputation is a threshold and is not consumed.
2. Doors are unlocked by **tier + gold price** ([M_Door_Purchase](../Exploration/M_Door_Purchase.md)).
3. Each upgrade physically expands the workshop: new rooms, more station slots, a larger Threshold of Portals ([L00_Workshop](../../04_Locations/L00_Workshop/L00_Workshop.md)).
4. The game signals when an upgrade becomes affordable: a HUD hint and a glow on the upgrade ledger in the workshop.

## Tunable Parameters

| Parameter | Meaning | Value |
| --- | --- | --- |
| Upgrade gold and reputation | Per tier | [Progression › Workshop Tiers](../../06_Balancing/Progression.md#workshop-tiers) |

## UI

- None yet; the affordability hint and upgrade ledger are planned in [_UI_Flow](../../05_UI/_UI_Flow.md).

## Used By

- [F05_Shop_Progression](../../01_Features/F05_Shop_Progression.md), [F06_Uber_Weapon](../../01_Features/F06_Uber_Weapon.md)

## Open Questions

- Tier 1 lists no lathe or extractor, yet every sword needs a hilt and every wand/staff needs a shaft and a core — should Tier 1 include a basic carving bench, or sell starter hilts? (The Phase 1 roadmap already includes the lathe and extractor.)
- Quenching Basins unlock at Tier 3, but the Tier 1 blade pipeline ends with quenching — is the Tier 3 basin an upgrade of a basic one?
- Are station placements fixed per tier, or can players rearrange the workshop (PlateUp!-style)?
