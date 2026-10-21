# UI Design: Letter Commission Board (Mailbox Nexus)

> **Mechanic:** [GDD/Shop/OrderSystem](../../GDD/Shop/OrderSystem.md) · **Technical:** [TechnicalDesign/Shop/OrderSystem](../../TechnicalDesign/Shop/OrderSystem.md)

## Screen Overview
The Letter Commission Board is the informational and commercial hub of the Armotheca workshop. Located beside the incoming pneumatic dispatch tube, this physical board/diegetic screen lets players review pending letters, inspect customer requirements, track remaining deadlines, pin priority commissions, and dispatch finished weapons.

**Implementation:** uGUI World Space Canvas on the board (TextMeshPro text, built-in uGUI navigation for gamepad). The pinned-letter HUD widget is a uGUI Screen Space Overlay canvas. Both views only listen to `OrderManager` events (see the technical doc).

---

## Layout Structure

```
+-------------------------------------------------------------------------------+
| [NEXUS DISPATCH MAILBOX]                [SHOP REPUTATION: LVL 2 (340/500)]    |
+-------------------------------------------------------------------------------+
|  PENDING LETTERS (Max 5)       |           ACTIVE COMMISSION DETAILS          |
|                                |                                              |
|  [#01] Guild: Iron Sword       | CLIENT: Arcane Academy of Oakhaven           |
|        [Time: 03:15]           | ARCHETYPE: Arcane Academy (Perfectionist)    |
|                                |                                              |
|  [#02] Academy: Frost Wand     | REQUIRED WEAPON:                             |
|        [Time: 05:40] (FOCUSED) | - Type: Wand (1-Handed)                      |
|                                | - Foundation (Shaft): Any Hardwood           |
|  [#03] SOS: Fire Sword         | - Payload (Core): Frost Core                 |
|        [Time: 00:45] [CRITICAL]| - Minimum Quality: Masterwork (75+)          |
|                                |                                              |
|  [#04] Garrison: 3x Iron Swords| REWARD:                                      |
|        [Time: 08:00]           | - Gold: 450 G                                |
|                                | - Rep: +35 Academy Standing                  |
|  [ + Empty Slot ]              | - Bonus: Blueprint "Glacial Conduit"         |
|                                |                                              |
|                                | PENALTY ON FAILURE: -50 Rep, Contract Void   |
+--------------------------------+----------------------------------------------+
| [PIN TO HUD] (Space/A)         | [DISPATCH COMPLETED WEAPON] (E/X)            |
+-------------------------------------------------------------------------------+
```

---

## Panel Breakdown

### 1. Left Panel: Letter Queue (Pending Contracts)
- **Ticket Cards (Up to 5):**
  - **Color-Coded Faction Trim:**
    - Brown/Bronze: Adventurers Guild
    - Blue/Silver: Arcane Academy
    - Red/Brass: City Garrison
    - Flashing Crimson: SOS Emergency Order
    - Gold/Purple: Eccentric Collector
  - **Urgency Progress Bar:** Real-time depleting bar showing remaining time before expiration.
  - **Thumbnail Icons:** Silhouette of the requested weapon type (Sword / Wand / Staff) and element badge.
  - **Batch Counter:** For batch orders, delivered / required units (e.g. `1/3`).

### 2. Right Panel: Active Commission Dossier
- **Flavor Text & Lore Snippet:** Brief context (e.g. *"Our expeditionary scholars require a stabilized frost wand to extract specimens from the volcanic vents."*).
- **Criteria Breakdown:**
  - **Weapon Type.**
  - **Foundation Component:** Required material, if any (e.g. Ash Wood, Ironwood, Bone).
  - **Payload Component:** Required element / material, if any.
  - **Minimum Quality:** Tier name and its numeric threshold (Crude 1+ / Standard 40+ / Masterwork 75+ / Flawless 95+).
- **Reward & Penalty Breakdown:**
  - Gold payout (with Flawless bonus shown).
  - Faction reputation gains.
  - Special unlock tokens (Academy research, Emergency Tokens, or Uber-Weapon catalysts).

### 3. Bottom Action Bar
- **Pin to HUD (Space / Controller A):** Pins the contract criteria to the players' corner HUD so players at the forge or in realms can check requirements without returning to the board.
- **Dispatch Drop-Slot (E / Controller X):** Validates and delivers the weapon held in the player's hands.

---

## Visual & Audio Feedback

- **New Letter Arrival:**
  - *Audio:* Brass pneumatic tube hiss followed by a satisfying parchment "thwack" on the wooden table.
  - *VFX:* Soft ethereal spark above the inbox slot.
- **SOS Critical Alert (< 60 s remaining):**
  - *Audio:* Pulsing magical beacon chime with rising pitch.
  - *VFX:* Flashing red parchment edges and vignette warning.
- **Successful Dispatch:**
  - *Audio:* Cash register chime + arcane resonance tone.
  - *VFX:* Letter dissolves into golden motes flying into the ceiling nexus; gold and rep counters animate upward.
- **Contract Rejection / Failure:**
  - *Audio:* Low dull thud / buzzer.
  - *VFX:* Rejection stamp slammed onto the document in red ink with the reason displayed (*"Quality Substandard: Required Masterwork, got Standard (61)"*).
