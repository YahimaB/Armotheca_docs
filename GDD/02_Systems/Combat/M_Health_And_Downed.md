---
id: M_Health_And_Downed
type: mechanic
system: Combat
status: Draft
---

# Health, Downed & Revive

> **System:** [_Combat_System](_Combat_System.md) · **Technical:** [_Combat_Module › Player Downed Flow](../../../Technical_Design/Combat/_Combat_Module.md#player-downed-flow-host)

## Summary

Players have a health pool; at zero they are downed and can be revived until they bleed out.

## Rules

1. Players have a health pool. Mobs deal fixed damage per attack defined in mob data ([_Mob_Roster](../../03_Entities/Mobs/_Mob_Roster.md)).
2. **Invulnerability:** players are invulnerable during the first part of a roll ([M_Roll](../Movement/M_Roll.md)) and briefly after taking a hit.
3. **Downed:** at 0 health a player becomes *Downed*: they cannot act and a bleed-out timer starts.
4. **Revive:** a teammate revives them with a continuous interaction ([M_Continuous_Interaction](../Interaction/M_Continuous_Interaction.md)); revived players return with part of their health.
5. **Bleed-out:** if the timer runs out (or a solo player goes down), the player is **ejected to the workshop**. Backpack and hands contents are dropped in the realm; the equipped weapon is kept.
6. As an expedition member, an ejected player can re-enter to recover the cargo while a teammate is still inside; if nobody is left, the realm and its dropped cargo are gone ([M_Door_Lifecycle](../Exploration/M_Door_Lifecycle.md)).
7. Health regenerates fully on returning through a door.

## Tunable Parameters

| Parameter | Meaning | Value |
| --- | --- | --- |
| Player health | Pool size | [Combat › Health and Downed](../../06_Balancing/Combat.md#health-and-downed) |
| Post-hit invulnerability | After taking a hit | [Combat › Health and Downed](../../06_Balancing/Combat.md#health-and-downed) |
| Bleed-out timer | Time to revive | [Combat › Health and Downed](../../06_Balancing/Combat.md#health-and-downed) |
| Revive duration / revive health | Revive interaction | [Combat › Health and Downed](../../06_Balancing/Combat.md#health-and-downed) |

## UI

- None yet; health and downed display planned in [_UI_Flow](../../05_UI/_UI_Flow.md).

## Dependencies

- [M_Carry_Model](../Interaction/M_Carry_Model.md): dropped cargo.

## Used By

- [F04_Combat](../../01_Features/F04_Combat.md), [F07_Co_Op](../../01_Features/F07_Co_Op.md)

## Open Questions

-
