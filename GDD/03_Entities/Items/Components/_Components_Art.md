---
id: _Components_Art
type: group-art
folder: Components
status: Draft
---

# Weapon Components — Art

> **Roster:** [_Item_List](../_Item_List.md) · **Guidelines:** [3D Modeling Guidelines](../../../../Guidelines/Modeling_Guidelines.md) · **Pairs:** [M_Assembly](../../../02_Systems/Crafting/M_Assembly.md)

## Modeling Requirements

A weapon is built in game from one foundation and one payload ([M_Assembly](../../../02_Systems/Crafting/M_Assembly.md)), so every part must fit every compatible counterpart.

| Weapon | Total length (foundation + payload) |
|---|---|
| Sword | 1.0 – 1.2 m |
| Wand | 0.35 – 0.45 m |
| Staff | 1.6 – 1.8 m |

- Every foundation contains an empty named `Socket_Payload` at the connection point, with its Y axis pointing along the weapon.
- Every payload has its pivot at its own connection point, oriented the same way, so it snaps onto `Socket_Payload` without offsets.
- Connection areas use a standard connector size per weapon type: a hilt collar and blade tang, or a shaft tip and core cradle, that match across all materials.
- The material of a part reads from colour and silhouette alone (iron vs star metal blade, oak vs bog-wood shaft). The element shows through the emissive core or blade accents.
- Quality tiers are not modelled; the Flawless glow is VFX ([M_Quality](../../../02_Systems/Crafting/M_Quality.md)).

## Open Questions

-
