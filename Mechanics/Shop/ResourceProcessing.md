# Manual Resource Processing System

## Design Intent

The Resource Processing System is the tactile core of workshop life in *Armotheca*. Raw materials hauled from dimensional expeditions cannot be slapped directly onto a weapon; they require physical labor and careful refinement. In accordance with early-phase design constraints, **all processing is strictly manual without automation**. Each station involves direct physical handling, multi-step procedures, and optional timing/precision mini-games that modulate the resulting component's **QualityScore (0–100%)**.

---

## Player Experience Goals

- **Physical Choreography:** Players move purposefully around the workshop: transferring heated ingots with tongs, operating bellows, and shaving wood at the lathe.
- **Mastery Through Feel:** Skilled players learn the rhythm of stations to produce *Flawless* components consistently without relying on heavy UI gauges.
- **Emergent Cooperative Assistance:** One player can pump the bellows while another strikes the anvil, doubling operational speed and building camaraderie.
- **Fail-Safe Forgiving Design:** Botched mini-games do not destroy materials completely; they yield *Crude* or *Standard* items rather than causing frustrating zero-gain losses.

---

## References (Specific Examples)

- **PlateUp! & Overcooked:** Multi-step food transformation pipelines (Chopping -> Cooking -> Plating) with burn/overcook risk.
- **Kingdom Come: Deliverance (Blacksmithing / Sharpening):** Angle and timing-dependent blade maintenance giving physical weight to smithing.
- **Potion Craft:** Physical stirring, heating with bellows, and grinding ingredients in a mortar to reach precision coordinates.
- **Ale & Tale Tavern:** Hands-on station interactions involving carrying logs, stirring pots, and cleaning up work areas.

---

## Workshop Stations & Transformation Pipelines

```
Raw Ores (Mines) --------> [SMELTING FORGE] -------> Hot Ingot
                                                            |
                                                            v
                                                   [ANVIL SHAPING] (Timing Strike)
                                                            |
                                                            v
                                                   [QUENCHING BASIN] ---> Refined BLADE

Arcane Timber (Groves) --> [WOODWORKING LATHE] ----> [CARVING BENCH] ---> Refined SHAFT / HILT

Mob Drops (Monsters) ----> [ARCANE EXTRACTOR] -----> [PURITY DISTILLER] -> Refined CORE
```

### 1. The Smelting Forge & Anvil (Blades)
1. **Heating:** Raw ore placed into the forge. Player works the bellows to reach glowing orange heat (3–6s).
2. **Transfer:** Picked up with tongs and transferred to the anvil.
3. **Hammering (Mini-Game):** 3 rhythmic strikes. A sweeping cursor crosses a green target zone.
   - *Perfect Strike:* +15% Quality.
   - *Missed Strike:* Normal Quality, slight stamina cost.
4. **Quenching:** Plunged into cold water/oil to lock in hardness.

### 2. The Woodworking Lathe & Carving Bench (Hilts & Shafts)
1. **Rough Cut:** Arcane lumber placed onto the lathe. Player holds the chisel while wood rotates.
2. **Selection:** Player chooses between shaping a **Hilt**, a **Short Wand Shaft**, or a **Long Staff Shaft**.
3. **Sanding / Polishing:** Rubbed with beeswax or resin for smooth grip.

### 3. The Arcane Extractor & Alembic (Cores)
1. **Maceration:** Monster essence (e.g. Phoenix Feather, Void Slime Core) loaded into the extraction mortar.
2. **Heat Regulation (Mini-Game):** Keeping distillation temperature inside the sweet-spot zone using flame valves for 4 seconds.
3. **Crystallization:** Extracted magical fluid condenses into a socketable **Aether Core**.

---

## Optional Mini-Game Philosophy

- Mini-games are **lightweight, rhythmic micro-interactions**, not full-screen pausing puzzles.
- **Accessibility Guarantee:** If a player chooses not to participate in the mini-game timing (or has accessibility aids enabled), the station produces a baseline **Standard (60% Quality)** component automatically upon completion.
- Engaging with the mini-game enables players to shoot for **Masterwork (80%+)** and **Flawless (95%+)**, which are essential for top-paying Collector and Academy commissions.

---

## Production-Ready C# Architecture

```csharp
using System;
using UnityEngine;
using Armotheca.Crafting;

namespace Armotheca.Shop
{
    public interface IWorkstation
    {
        bool CanAcceptItem(string itemID);
        void InsertItem(string itemID);
        void StartInteraction(int playerID);
        void TickInteraction(float deltaTime);
        void FinishInteraction();
        bool HasCompletedOutput { get; }
        WeaponComponentData RetrieveOutput();
    }

    /// <summary>
    /// Anvil station where heated ingots are struck to forge weapon blades.
    /// Features optional rhythm/timing precision for quality bonus.
    /// </summary>
    public class AnvilWorkstation : MonoBehaviour, IWorkstation
    {
        [Header("Station Settings")]
        [SerializeField] private float requiredStrikes = 3;
        [SerializeField] private float sweetSpotWindow = 0.25f; // Normalized timing window

        private int currentStrikes = 0;
        private float accumulatedQuality = 50f; // Base standard quality
        private bool isProcessing = false;
        private string currentIngotID;

        public bool HasCompletedOutput => currentStrikes >= requiredStrikes;
        public event Action<float> OnStrikeTimingFeedback; // -1 = miss, 1 = perfect

        public bool CanAcceptItem(string itemID)
        {
            return !isProcessing && currentIngotID == null && itemID.StartsWith("Ingot_");
        }

        public void InsertItem(string itemID)
        {
            currentIngotID = itemID;
            currentStrikes = 0;
            accumulatedQuality = 50f;
            isProcessing = true;
        }

        public void StartInteraction(int playerID)
        {
            // Lock player in subtle interaction pose or enable tool equip
        }

        public void TickInteraction(float deltaTime)
        {
            // Update rotating / swinging timing indicator if player is holding hammer
        }

        /// <summary>
        /// Triggered when the player presses the strike key / swings hammer.
        /// </summary>
        /// <param name="normalizedTiming">0.0 to 1.0 representing stroke timing</param>
        public void PerformHammerStrike(float normalizedTiming)
        {
            if (!isProcessing || HasCompletedOutput) return;

            // Target sweet spot is centered at 0.5f
            float deviation = Mathf.Abs(normalizedTiming - 0.5f);

            if (deviation <= sweetSpotWindow * 0.5f)
            {
                // Perfect hit!
                accumulatedQuality += 15f;
                OnStrikeTimingFeedback?.Invoke(1.0f);
            }
            else if (deviation <= sweetSpotWindow)
            {
                // Good hit
                accumulatedQuality += 5f;
                OnStrikeTimingFeedback?.Invoke(0.5f);
            }
            else
            {
                // Off-beat hit
                accumulatedQuality -= 5f;
                OnStrikeTimingFeedback?.Invoke(-1.0f);
            }

            currentStrikes++;
            accumulatedQuality = Mathf.Clamp(accumulatedQuality, 10f, 100f);

            if (HasCompletedOutput)
            {
                isProcessing = false;
            }
        }

        public void FinishInteraction()
        {
            // Release player control
        }

        public WeaponComponentData RetrieveOutput()
        {
            if (!HasCompletedOutput) return default;

            var result = new WeaponComponentData
            {
                ComponentID = "Blade_" + currentIngotID,
                DisplayName = "Forged Blade",
                Element = ElementType.Physical,
                QualityScore = accumulatedQuality,
                PowerModifier = 1.0f + (accumulatedQuality / 100f) * 0.5f,
                SpeedModifier = 1.0f
            };

            // Reset station
            currentIngotID = null;
            currentStrikes = 0;
            return result;
        }
    }
}
```
