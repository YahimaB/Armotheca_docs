---
id: F04_Combat
type: feature
status: Draft
priority: Must
owner:
milestone: Phase 1
pillars: [Dimensional Contract Cycle]
---

# Combat

> **Hub:** [_Feature_List](_Feature_List.md) · **Technical:** [_Module_Map › Features](../../Technical_Design/_Module_Map.md#features)

## Purpose

Combat is a means to an end: it protects the team while they harvest and it produces the mob drops that wand and staff cores need. It is **simple, readable and satisfying**, never a deep action system that competes with the shop for attention. There are two attacks, one per weapon family, and damage comes straight from the weapon's Base Damage, so there are no hidden modifiers to learn. Mobs are simple, readable enemies built on a few behaviour archetypes, and they are what makes staying longer in a realm a gamble.

## Player Experience

- **Pick up and fight:** a workshop player can grab any sword or wand, run through a door and contribute immediately.
- **Clear roles without classes:** swords protect miners up close; wands and staves pick off threats from range.
- **Protect the gatherers:** mobs pressure players locked into harvesting, making bodyguarding a real role.
- **Readable danger:** every enemy attack is telegraphed so that the roll is the answer, not a guess.
- **Hunt with purpose:** players hunt specific mobs because a letter needs their essence.
- **Crafting pride:** players wield weapons they forged themselves.

## References

- **Moonlighter:** few weapon types with one simple attack each, roll as defence; readable enemies dropping themed materials.
- **Hades:** crisp hit feedback (hit-stop, flash, knockback); short dash with brief invulnerability.
- **Deep Rock Galactic:** combat as protection for a gathering objective, with hold-to-revive; escalating swarms.
- **Enter the Gungeon:** readable, slow projectiles avoided by rolling.
- **Monster Hunter:** monster parts defining crafted weapon identity.

## Mechanics

- [M_Sword_Swing](../02_Systems/Combat/M_Sword_Swing.md), [M_Magic_Orb](../02_Systems/Combat/M_Magic_Orb.md), [M_Health_And_Downed](../02_Systems/Combat/M_Health_And_Downed.md)
- [M_Roll](../02_Systems/Movement/M_Roll.md): the main defensive tool.
- [M_Mob_Spawning](../02_Systems/Exploration/M_Mob_Spawning.md), [M_Realm_Pressure](../02_Systems/Exploration/M_Realm_Pressure.md)

## Entities

- [Player](../03_Entities/Player/Player.md)
- [E_Sword](../03_Entities/Items/Weapons/E_Sword/E_Sword.md), [E_Wand](../03_Entities/Items/Weapons/E_Wand/E_Wand.md), [E_Staff](../03_Entities/Items/Weapons/E_Staff/E_Staff.md)
- [_Mob_Roster](../03_Entities/Mobs/_Mob_Roster.md)

## Locations

- Realms only; no combat in [L00_Workshop](../04_Locations/L00_Workshop/L00_Workshop.md). See [_World_Map](../04_Locations/_World_Map.md).

## UI

- None yet. Player health and the downed / bleed-out display are planned in [_UI_Flow](../05_UI/_UI_Flow.md).

## Scope

| Item | MVP | Stretch |
| --- | --- | --- |
| Sword swing, magic orb, health and downed state | Phase 1 | |
| Apex Guardian encounters | Phase 3 | |
| Element and Quality effects in combat | | After a deliberate revision of the stat lock |

## Open Questions

-
