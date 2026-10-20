# UI Design: Letter Commission Board (Mailbox Nexus)

## Screen Overview
The Letter Commission Board is the informational and commercial hub of the Armotheca workshop. Located beside the incoming pneumatic dispatch tube, this physical board/diegetic screen allows players to review pending letters, inspect customer requirements, track remaining deadlines, accept priority commissions, and dispatch finished weapons.

---

## Layout Structure

```
+-------------------------------------------------------------------------------+
| [NEXUS DISPATCH MAILBOX]                [SHOP REPUTATION: LVL 2 (340/500)]    |
+-------------------------------------------------------------------------------+
|  PENDING LETTERS (Max 5)       |           ACTIVE COMMISSION DETAILS          |
|                                |                                              |
|  [#01] Guild: Iron Broadsword  | CLIENT: Arcane Academy of Oakhaven           |
|        [Time: 03:15]           | ARCHETYPE: Arcane Academy (Perfectionist)    |
|                                |                                              |
|  [#02] Academy: Frost Wand     | REQUIRED WEAPON:                             |
|        [Time: 05:40] (FOCUSED) | - Type: Wand (1-Handed)                      |
|                                | - Component 1 (Shaft): Any Hardwood          |
|  [#03] SOS: Fire Claymore      | - Component 2 (Core): Frost Core (Min 75% Q) |
|        [Time: 00:45] [CRITICAL]|                                              |
|                                | REWARD:                                      |
|  [#04] Garrison: 3x Spears     | - Gold: 450 G                                |
|        [Time: 08:00]           | - Rep: +35 Academy Standing                  |
|                                | - Bonus: Blueprint "Glacial Conduit"         |
|  [ + Empty Slot ]              |                                              |
|                                | PENALTY ON FAILURE: -50 Rep, Contract Void   |
+--------------------------------+----------------------------------------------+
| [PIN TO WORKBENCH] (Space/A)   | [DISPATCH COMPLETED WEAPON] (E/X)            |
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
  - **Thumbnail Icons:** Visual silhouette of requested weapon type (Sword / Wand / Staff) and elemental badge.

### 2. Right Panel: Active Commission Dossier
- **Flavor Text & Lore Snippet:** Brief context (e.g. *“Our expeditionary scholars require a stabilized frost wand to extract specimens from the volcanic vents.”*).
- **Component Criteria Breakdown:**
  - **Base Component:** Required material type (e.g. Ash Wood, Ironwood, Bone).
  - **Payload Component:** Required elemental affinity and **Minimum Quality Threshold** (Crude / Standard / Masterwork / Flawless).
- **Reward & Penalty Breakdown:**
  - Gold payout (with dynamic Flawless bonus calculator).
  - Faction reputation gains.
  - Special unlock tokens (Academy Research, Emergency Tokens, or Uber-Weapon Catalysts).

### 3. Bottom Action Bar
- **Pin to Workshop HUD (Space / Controller Button A):** Pins the contract criteria to the players' corner HUD so players working at the forge or in portals can reference requirements without returning to the board.
- **Dispatch Drop-Slot (E / Controller Button X):** Validates and delivers the weapon held in the player's hands.

---

## Visual & Audio Feedback

- **New Letter Arrival:**
  - *Audio:* Brass pneumatic tube hiss followed by a satisfying parchment "thwack" on the wooden table.
  - *VFX:* Soft ethereal spark above the inbox slot.
- **SOS Critical Alert (< 60s remaining):**
  - *Audio:* Pulsing magical beacon chime with rising pitch.
  - *VFX:* Flashing red parchment edges and vignette warning.
- **Successful Dispatch:**
  - *Audio:* Cash register chime + arcane resonance tone.
  - *VFX:* Letter dissolves into golden motes flying into the ceiling nexus; gold and rep counters animate upward.
- **Contract Rejection / Failure:**
  - *Audio:* Low dull thud / buzzer.
  - *VFX:* Rejection stamp slammed onto the document in red ink with reason displayed (*“Quality Substandard: Crude core detected”*).
