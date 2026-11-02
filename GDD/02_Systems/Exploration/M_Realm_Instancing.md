---
id: M_Realm_Instancing
type: mechanic
system: Exploration
status: Draft
---

# Realm Instancing

> **System:** [_Exploration_System](_Exploration_System.md) · **Technical:** [Realms (tech)](../../../Technical_Design/Exploration/Realms.md)

## Summary

Each door opening creates a realm instance with a hand-made layout and freshly rolled contents, which lives until the last player leaves.

## Rules

1. A realm exists from the moment its door is opened until the **last player leaves it**.
2. While at least one player is inside, expedition members can leave and re-enter; dropped cargo stays where it fell.
3. When the realm empties it is discarded; the next opening generates a fresh one.
4. Each opening keeps the realm's hand-made layout ([_World_Map](../../04_Locations/_World_Map.md)) but re-rolls:
   - which resource nodes appear and where ([M_Node_Spawning](M_Node_Spawning.md));
   - which mob groups appear and where ([M_Mob_Spawning](M_Mob_Spawning.md));
   - optional realm modifiers in Prestige mode (e.g. denser mobs, doubled rare nodes).

## UI

- None.

## Dependencies

- [M_Door_Lifecycle](M_Door_Lifecycle.md)

## Used By

- [F03_Expeditions](../../01_Features/F03_Expeditions.md)

## Open Questions

- One hand-made layout per realm, or a few layout variants selected at random?
