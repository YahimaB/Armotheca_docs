---
id: M_Door_Lifecycle
type: mechanic
system: Exploration
status: Draft
---

# Door Lifecycle

> **System:** [_Exploration_System](_Exploration_System.md) · **Technical:** [Door_Instances](../../../Technical_Design/Exploration/Door_Instances.md)

## Summary

An owned door opens into a fresh realm, accepts entrants for a short window, then seals until the realm empties and the door rests.

## Rules

```
 [LOCKED] --(tier reached + gold paid)--> [READY] --(open)--> [ENTRY OPEN] --(window)--> [IN PROGRESS] --(realm empty)--> [COOLDOWN] --(rest)--> [READY]
                                                                                 \___(nobody inside when window closes)___/
```

1. **Ready:** the door is owned and closed. Any player can open it (instant interaction). A fresh realm is generated ([M_Realm_Instancing](M_Realm_Instancing.md)).
2. **Entry open:** anyone can step through, and players may come and go freely. Every player who enters becomes an **expedition member** for this run.
3. **In progress:** the door seals **for entry**. Only expedition members can pass back in (e.g. after dropping cargo in the workshop or being ejected). Other players see a shimmering sealed surface and the names of the members inside. If nobody is inside when the window closes, the expedition ends at once.
4. **Realm empty:** when the last player leaves the realm (by any route) after the entry window has closed, the expedition ends and the realm is discarded.
5. **Cooldown:** the door rests, then returns to Ready and can be opened into a newly generated realm.

### Leaving a realm

6. An [E_Exit_Portal](../../03_Entities/Props/Interactive/E_Exit_Portal.md) stands in every realm's Entry area and is **always open**. Using it (instant interaction) returns the player to the workshop in front of the door.
7. Being **downed and bleeding out** also returns the player to the workshop, dropping backpack and hands contents in the realm ([M_Health_And_Downed](../Combat/M_Health_And_Downed.md)). As an expedition member they may re-enter to recover the cargo as long as at least one teammate is still inside.
8. If a solo player (or the last member inside) steps out, the realm empties and the expedition ends.

## Tunable Parameters

| Parameter | Meaning | Value |
| --- | --- | --- |
| Entry window | Time anyone may enter | [Exploration › Doors](../../06_Balancing/Exploration.md#doors) |
| Cooldown | Rest before Ready | [Exploration › Doors](../../06_Balancing/Exploration.md#doors) |

## Feedback

Sealed doors show a shimmering surface and the names of the members inside.

## UI

- [UI_Interaction_Prompt](../../05_UI/World/UI_Interaction_Prompt.md)

## Dependencies

- [M_Door_Purchase](M_Door_Purchase.md), [M_Realm_Instancing](M_Realm_Instancing.md)

## Used By

- [F03_Expeditions](../../01_Features/F03_Expeditions.md), [F07_Co_Op](../../01_Features/F07_Co_Op.md)

## Open Questions

- Is the current entry window right, or should it scale with the number of players still in the workshop?
- Should non-members ever be able to join after the window closes (e.g. a paid "breach" using Emergency Tokens) to keep emergency reinforcement possible?
