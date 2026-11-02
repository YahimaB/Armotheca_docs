---
id: M_Instant_Interaction
type: mechanic
system: Interaction
status: Draft
---

# Instant Interaction

> **System:** [_Interaction_System](_Interaction_System.md) · **Technical:** [Object Interaction (tech)](../../../Technical_Design/Common/Object_Interaction.md)

## Summary

Triggered on a button press and resolved immediately.

## Rules

| Interaction | Target | Result |
|---|---|---|
| Pick up | Loose item in the world | Item moves to hands |
| Drop | Empty floor (hands full) | Item placed in front of the player |
| Place / Snap | Station socket, counter, crate | Item moves from hands into the socket |
| Take | Filled socket / output tray | Item moves into empty hands |
| Hand over | Teammate with empty hands | Item moves directly between players |
| Open / Use | Door, letter, mailbox, lever | Object-specific action |
| Dispatch | Outgoing mail tube (hands hold a weapon) | Submits the weapon to an order ([M_Letter_Flow](../Orders/M_Letter_Flow.md)) |

## Player Input

Interact button.

## UI

- [UI_Interaction_Prompt](../../05_UI/World/UI_Interaction_Prompt.md)

## Used By

- [F01_Commissions](../../01_Features/F01_Commissions.md), [F02_Weapon_Crafting](../../01_Features/F02_Weapon_Crafting.md), [F03_Expeditions](../../01_Features/F03_Expeditions.md), [F07_Co_Op](../../01_Features/F07_Co_Op.md)

## Open Questions

-
