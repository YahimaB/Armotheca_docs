---
id: Combat
type: balancing
system: Combat
status: Draft
---

# Combat Balancing

> **System:** [_Combat_System](../02_Systems/Combat/_Combat_System.md)

Values marked `*` are initial values not yet validated by playtest. Docs link here by table anchor and never repeat the value.

## Sword Swing

Owner: [M_Sword_Swing](../02_Systems/Combat/M_Sword_Swing.md)

| Parameter | Value | Notes |
| --- | --- | --- |
| Chain length | 2 swings |  |
| Windup / active / recovery | 0.10 s / 0.12 s / 0.25 s* |  |
| Arc angle / reach | 120° / 1.8 m* |  |
| Chain input window | last 50% of a swing* |  |
| Knockback | light* | Staggers small mobs only |

## Magic Orb

Owner: [M_Magic_Orb](../02_Systems/Combat/M_Magic_Orb.md)

| Parameter | Value | Notes |
| --- | --- | --- |
| Cast time | 0.15 s* |  |
| Cooldown between orbs | 0.6 s* |  |
| Orb speed / max range | 14 m/s / 12 m* |  |
| Aim assist cone | 15°* |  |

## Health and Downed

Owner: [M_Health_And_Downed](../02_Systems/Combat/M_Health_And_Downed.md)

| Parameter | Value | Notes |
| --- | --- | --- |
| Player health | 100* |  |
| Post-hit invulnerability | 0.5 s* |  |
| Bleed-out timer | 20 s* |  |
| Revive duration | 3 s |  |
| Revive health | 50% |  |

## Mobs

Owner: [_Mob_Roster](../03_Entities/Mobs/_Mob_Roster.md)

| ID | Health | Attack damage | Notes |
| --- | --- | --- | --- |
| [E_Bramble_Stalker](../03_Entities/Mobs/Minor_Fauna/E_Bramble_Stalker.md) | — | — |  |
| [E_Void_Slime](../03_Entities/Mobs/Minor_Fauna/E_Void_Slime.md) | — | — |  |
| [E_Fire_Salamander](../03_Entities/Mobs/Elemental_Beasts/E_Fire_Salamander.md) | — | — |  |
| [E_Frost_Wraith](../03_Entities/Mobs/Elemental_Beasts/E_Frost_Wraith.md) | — | — |  |
| [E_Verdant_Elder](../03_Entities/Mobs/Apex_Guardians/E_Verdant_Elder.md) | — | — | Health scales with player count |
| [E_Pyroclastic_Apex](../03_Entities/Mobs/Apex_Guardians/E_Pyroclastic_Apex.md) | — | — | Health scales with player count |
| [E_Astral_Sovereign](../03_Entities/Mobs/Apex_Guardians/E_Astral_Sovereign.md) | — | — | Health scales with player count |
| [E_Frost_Wyrm](../03_Entities/Mobs/Apex_Guardians/E_Frost_Wyrm.md) | — | — | Health scales with player count |

Not yet defined.
