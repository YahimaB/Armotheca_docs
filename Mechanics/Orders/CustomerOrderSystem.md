# Customer Order & Letter Commission System

## Design Intent

The Customer Order System governs the commercial pulse and narrative context of *Armotheca*. Instead of generic faceless customers lining up at a counter, orders arrive as physical and magical **commission letters** through the shop's Mailbox Nexus. Each letter embodies a specific client faction, explicit requirements (weapon type, element, minimum quality tier), deadlines, and variable stakes. This mechanism transforms shop operations from mindless inventory stockpiling into focused, tactical problem-solving for the player team.

---

## Player Experience Goals

- **Analytical Prioritization:** Players gather around the letterboard/mailbox to evaluate incoming contracts, debate feasibility, and coordinate material requirements.
- **Narrative Personality:** Flavor text and specific client demands make the extradimensional world feel alive and reactive.
- **Dramatic Pacing (SOS Moments):** High-urgency emergency orders trigger frantic team coordination, contrasting with relaxed, perfectionist academy commissions.
- **Consequential Choices:** Accepting an order stakes reputation; failing it or delivering subpar craftsmanship impacts the workshop's standing.

---

## References (Specific Examples)

- **Papers, Please:** Verification of multiple criteria (stamp, date, document parameters) against a strict set of rules.
- **Overcooked / PlateUp!:** Order ticket queues with expiration bars, rewarding fast execution with combo bonuses and tip multipliers.
- **Potion Craft:** Customer dialogues demanding specific effects where players can either meet the bare minimum or exceed expectations for bonus reputation.
- **Dave the Diver:** VIP and party events requiring specific dishes by a set deadline, unlocking game progression upon success.

---

## Customer Archetypes

```
+--------------------------------------------------------------------------+
|                        COMMISSION LETTER ARCHETYPES                      |
+--------------------------------------------------------------------------+
| 1. ADVENTURERS GUILD | High volume, balanced stats, steady gold & rep    |
| 2. ARCANE ACADEMY    | Zero tolerance for defects, rare cores, blueprints|
| 3. CITY GARRISON     | Identical batch orders (2-4 units), bulk profits  |
| 4. SOS DISPATCH      | Extreme time pressure (<120s), high-risk windfall |
| 5. COLLECTOR NOBLES  | Exotic element combinations, Uber-Weapon catalyst |
+--------------------------------------------------------------------------+
```

### Detailed Breakdown

#### 1. Adventurers Guild (The Bread & Butter)
- **Profile:** Pragmatic monster hunters needing durable gear.
- **Demand Pattern:** 1 Sword or 1 Wand; accepts `Standard` or `Masterwork`; general elemental affinities.
- **Timing:** Relaxed (4–6 minutes).
- **Consequence:** Steady cash flow; failure incurs negligible reputation loss.

#### 2. Arcane Academy (The Perfectionists)
- **Profile:** Elitist scholars and archmages researching planar anomalies.
- **Demand Pattern:** Staves and Wands only; strict demand for `Masterwork` or `Flawless` quality and specific arcane cores.
- **Tolerance:** **Zero tolerance for `Crude` components.** Delivering anything below requested tier results in immediate contract rejection and severe reputation penalty.
- **Rewards:** Unlocks rare research blueprints and portal stabilizer formulas.

#### 3. City Garrison (The Mass Contractors)
- **Profile:** Quartermasters supplying frontline defense battalions.
- **Demand Pattern:** Batch orders (e.g., *3x Iron-Flame Swords* with identical specifications).
- **Gameplay Impact:** Forces the workshop into an efficient assembly-line mindset where players pre-smelt and mass-forge identical components.
- **Rewards:** Massive lump-sum gold payouts.

#### 4. SOS Emergency Dispatch (The Adrenaline Spike)
- **Profile:** Desperate distress calls magically intercepted from ongoing battles.
- **Demand Pattern:** *“A cave troll is breaking our line! Send an Acid Blade within 90 seconds!”*
- **Timing:** 60 to 120 seconds maximum.
- **Rewards:** 2.5x standard gold, Emergency Tokens (used for instant workshop buffs).
- **Penalty:** None upon expiration (they perished or fled); only shame and lost opportunity.

#### 5. Eccentric Collectors (The Milestone Givers)
- **Profile:** Interdimensional oligarchs seeking bizarre vanity weapons.
- **Demand Pattern:** Exotic combos (e.g., *Lightning Core inside Ancient Bog-Wood Staff*).
- **Rewards:** Modest gold, but rewards **Uber-Weapon Blueprints** and **Prismatic Catalysts**.

---

## Technical Specifications

- **Active Letter Queue:** Maximum 5 simultaneous letters on the Mailbox Board.
- **Letter Lifespan:** Between 90s (SOS) and 360s (Standard Guild) before expiring.
- **Evaluation Accuracy:** Instantaneous component inspection against commission criteria upon deposit into the Outgoing Pneumatic Tube.

---

## Production-Ready C# Architecture

```csharp
using System;
using System.Collections.Generic;
using UnityEngine;
using Armotheca.Crafting;

namespace Armotheca.Orders
{
    public enum ClientArchetype
    {
        AdventurersGuild,
        ArcaneAcademy,
        CityGarrison,
        EmergencySOS,
        EccentricCollector
    }

    [System.Serializable]
    public class OrderCriteria
    {
        public WeaponType RequiredWeaponType;
        public ElementType RequiredElement;
        public QualityTier MinimumQualityTier;
        public int RequiredQuantity;
        public string SpecificComponentRequiredID; // Optional filter (e.g. "DragonBoneHilt")
    }

    public class CommissionOrder
    {
        public string OrderID { get; }
        public ClientArchetype Archetype { get; }
        public string ClientName { get; }
        public string FlavorDescription { get; }
        public OrderCriteria Criteria { get; }

        public float TotalDurationSeconds { get; }
        public float RemainingSeconds { get; private set; }
        public int RewardGold { get; }
        public int RewardReputation { get; }

        public bool IsExpired => RemainingSeconds <= 0f;
        public bool IsFulfilled { get; private set; }

        public CommissionOrder(
            string orderID, 
            ClientArchetype archetype, 
            string clientName, 
            string flavor, 
            OrderCriteria criteria, 
            float duration, 
            int baseGold, 
            int baseRep)
        {
            OrderID = orderID;
            Archetype = archetype;
            ClientName = clientName;
            FlavorDescription = flavor;
            Criteria = criteria;
            TotalDurationSeconds = duration;
            RemainingSeconds = duration;
            RewardGold = baseGold;
            RewardReputation = baseRep;
        }

        public void Tick(float deltaTime)
        {
            if (!IsFulfilled && RemainingSeconds > 0f)
            {
                RemainingSeconds -= deltaTime;
            }
        }

        public bool ValidateSubmission(AssembledWeapon weapon, out string rejectionReason)
        {
            rejectionReason = string.Empty;

            if (weapon.Type != Criteria.RequiredWeaponType)
            {
                rejectionReason = $"Wrong weapon type. Expected {Criteria.RequiredWeaponType}, received {weapon.Type}.";
                return false;
            }

            if (Criteria.RequiredElement != ElementType.Physical && weapon.FinalElement != Criteria.RequiredElement)
            {
                rejectionReason = $"Element mismatch. Required {Criteria.RequiredElement}, got {weapon.FinalElement}.";
                return false;
            }

            if (weapon.OverallQuality < Criteria.MinimumQualityTier)
            {
                rejectionReason = $"Quality substandard. Required {Criteria.MinimumQualityTier}, got {weapon.OverallQuality}.";
                return false;
            }

            return true;
        }

        public void MarkFulfilled()
        {
            IsFulfilled = true;
        }
    }

    /// <summary>
    /// Manages letter generation, board display, and outgoing verification.
    /// </summary>
    public class OrderManager : MonoBehaviour
    {
        [SerializeField] private int maxActiveLetters = 5;
        private readonly List<CommissionOrder> activeOrders = new();

        public event Action<CommissionOrder> OnOrderReceived;
        public event Action<CommissionOrder> OnOrderExpired;
        public event Action<CommissionOrder, int, int> OnOrderCompleted; // order, gold, rep
        public event Action<string> OnOrderRejected;

        private void Update()
        {
            float dt = Time.deltaTime;
            for (int i = activeOrders.Count - 1; i >= 0; i--)
            {
                var order = activeOrders[i];
                order.Tick(dt);

                if (order.IsExpired && !order.IsFulfilled)
                {
                    activeOrders.RemoveAt(i);
                    OnOrderExpired?.Invoke(order);
                }
            }
        }

        /// <summary>
        /// Called when an assembled weapon is submitted into the Outgoing Mail Tube.
        /// </summary>
        public bool TrySubmitWeapon(AssembledWeapon weapon, string targetOrderID)
        {
            var targetOrder = activeOrders.Find(o => o.OrderID == targetOrderID);
            if (targetOrder == null)
            {
                OnOrderRejected?.Invoke("Order no longer exists or expired.");
                return false;
            }

            if (!targetOrder.ValidateSubmission(weapon, out string rejectionReason))
            {
                OnOrderRejected?.Invoke(rejectionReason);

                // Penalty for Academy failure
                if (targetOrder.Archetype == ClientArchetype.ArcaneAcademy)
                {
                    // Apply heavy reputation deduction
                }
                return false;
            }

            targetOrder.MarkFulfilled();
            activeOrders.Remove(targetOrder);

            // Calculate bonus for Flawless or fast delivery
            int finalGold = targetOrder.RewardGold;
            if (weapon.OverallQuality == QualityTier.Flawless)
            {
                finalGold = Mathf.RoundToInt(finalGold * 1.5f);
            }

            OnOrderCompleted?.Invoke(targetOrder, finalGold, targetOrder.RewardReputation);
            return true;
        }
    }
}
```
