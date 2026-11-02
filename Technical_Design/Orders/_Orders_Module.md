---
id: _Orders_Module
type: module
module: Orders
namespace: Armotheca.Orders
status: Draft
---

# Orders Module

> **Design:** [_Orders_System](../../GDD/02_Systems/Orders/_Orders_System.md) · **Map:** [_Module_Map](../_Module_Map.md) · **Overview:** [Technical Overview](../Technical_Overview.md)

## Scope

| GDD doc | Implemented in |
| --- | --- |
| [M_Commission_Criteria](../../GDD/02_Systems/Orders/M_Commission_Criteria.md) | [Technical Specifications](#technical-specifications) — evaluation order; `CommissionOrder.Validate()` |
| [M_Letter_Flow](../../GDD/02_Systems/Orders/M_Letter_Flow.md) | [Architecture](#architecture--implementation-approaches) — `OrderManager`; [Networking](#networking) |
| Clients ([E_Adventurers_Guild](../../GDD/03_Entities/NPCs/Clients/E_Adventurers_Guild.md), [E_Arcane_Academy](../../GDD/03_Entities/NPCs/Clients/E_Arcane_Academy.md), [E_City_Garrison](../../GDD/03_Entities/NPCs/Clients/E_City_Garrison.md), [E_SOS_Dispatch](../../GDD/03_Entities/NPCs/Clients/E_SOS_Dispatch.md), [E_Eccentric_Collectors](../../GDD/03_Entities/NPCs/Clients/E_Eccentric_Collectors.md)) | `ClientArchetypeDefinition` ([Data](#data)) |
| [E_Mailbox_Nexus](../../GDD/03_Entities/Props/Interactive/E_Mailbox_Nexus.md) | Outgoing Tube submission RPC ([Networking](#networking)) |
| [UI_Letter_Commission_Board](../../GDD/05_UI/Screens/UI_Letter_Commission_Board.md), [UI_Pinned_Letter](../../GDD/05_UI/Hud/UI_Pinned_Letter.md) | Events below; views in [_UI_Module](../UI/_UI_Module.md) |

---

## Technical Specifications

- **Active letter queue:** `maxActiveLetters` ([Orders › Letter Rules](../../GDD/06_Balancing/Orders.md#letter-rules)).
- **Letter lifespan:** per archetype in `ClientArchetypeDefinition` ([Orders › Client Archetypes](../../GDD/06_Balancing/Orders.md#client-archetypes)).
- **Evaluation:** Instant validation when a weapon is submitted to the Outgoing Tube. Criteria checked in order: weapon type → minimum quality tier → element → specific component material.
- **Stat model:** Validation reads only `AssembledWeapon.Type`, `Tier` (from `Quality`), `Element` and component material IDs. `BaseDamage` is not used by orders at this stage.
- **Generation:** `OrderGenerator` picks an archetype by weighted table gated by shop tier, then builds criteria only from materials obtainable through doors the team owns (purchased, see [Magic Doors](../Exploration/Door_Instances.md)).

---

## Architecture & Implementation Approaches

### Approach A: Data-Driven Archetypes + Pure Validation (Recommended)
- `ClientArchetypeDefinition` (SO): weights, lifespan range, allowed weapon types, quality tier range, reward ranges, failure penalty, tier requirement.
- `CommissionOrder`: runtime letter with criteria, timer and rewards; `Validate()` is pure.
- `OrderManager`: owns the queue, ticks timers, handles submissions, raises events.
- **Pros:** New archetypes are pure data; validation is unit-testable.

### Approach B: Subclass per Archetype
- **Cons:** Archetypes differ only in numbers and a few flags; subclasses add little.

---

## Networking

- `OrderManager` runs on the host only. Letters replicate as `{ id, archetype, criteria, remainingSeconds, rewards }` on creation; clients extrapolate timers locally and receive corrections every 5 s.
- Submissions are host RPCs carrying the held weapon's network ID and the target order ID.

---

## Data

| Definition (SO) | Field | Supplied by |
| --- | --- | --- |
| `ClientArchetypeDefinition` | lifespan range, batch size, rewards, failure penalty | [Orders › Client Archetypes](../../GDD/06_Balancing/Orders.md#client-archetypes) |
| `ClientArchetypeDefinition` | weights, tier requirement | Not yet in balancing |
| `OrderManager` | `maxActiveLetters`, Flawless bonus | [Orders › Letter Rules](../../GDD/06_Balancing/Orders.md#letter-rules) |

---

## Events

| Event | Raised when | Consumed by |
| --- | --- | --- |
| `OnOrderReceived` | A letter arrives | Board, audio |
| `OnOrderCompleted` | A delivery passes verification | Board, currencies, audio, VFX |
| `OnOrderRejected` | A delivery fails verification | Board rejection stamp |
| `OnOrderExpired` | A letter times out | Board, reputation |

---

## Unity C# Reference Code

```csharp
using System;
using System.Collections.Generic;
using UnityEngine;
using Armotheca.Core;
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

    [Serializable]
    public class OrderCriteria
    {
        public WeaponType RequiredWeaponType;
        public QualityTier MinimumQualityTier;
        public bool RequiresElement;
        public ElementType RequiredElement;
        [Min(1)] public int RequiredQuantity = 1;
        public string RequiredMaterialId; // optional, e.g. "AncientBogWood"
    }

    public class CommissionOrder
    {
        public string OrderId { get; }
        public ClientArchetype Archetype { get; }
        public string ClientName { get; }
        public string FlavorText { get; }
        public OrderCriteria Criteria { get; }

        public float TotalSeconds { get; }
        public float RemainingSeconds { get; private set; }
        public int RewardGold { get; }
        public int RewardReputation { get; }
        public int FailurePenaltyReputation { get; }
        public int DeliveredCount { get; private set; }

        public bool IsExpired => RemainingSeconds <= 0f;
        public bool IsFulfilled => DeliveredCount >= Criteria.RequiredQuantity;

        public CommissionOrder(string orderId, ClientArchetype archetype, string clientName, string flavor,
                               OrderCriteria criteria, float durationSeconds, int gold, int reputation, int failurePenalty)
        {
            OrderId = orderId;
            Archetype = archetype;
            ClientName = clientName;
            FlavorText = flavor;
            Criteria = criteria;
            TotalSeconds = durationSeconds;
            RemainingSeconds = durationSeconds;
            RewardGold = gold;
            RewardReputation = reputation;
            FailurePenaltyReputation = failurePenalty;
        }

        public void Tick(float deltaTime)
        {
            if (!IsFulfilled && RemainingSeconds > 0f) RemainingSeconds -= deltaTime;
        }

        public bool Validate(AssembledWeapon weapon, out string rejectionReason)
        {
            if (weapon.Type != Criteria.RequiredWeaponType)
            {
                rejectionReason = $"Wrong weapon type. Expected {Criteria.RequiredWeaponType}, received {weapon.Type}.";
                return false;
            }

            if (weapon.Tier < Criteria.MinimumQualityTier)
            {
                rejectionReason = $"Quality substandard. Required {Criteria.MinimumQualityTier}, got {weapon.Tier} ({weapon.Quality}).";
                return false;
            }

            if (Criteria.RequiresElement && weapon.Element != Criteria.RequiredElement)
            {
                rejectionReason = $"Element mismatch. Required {Criteria.RequiredElement}, got {weapon.Element}.";
                return false;
            }

            if (!string.IsNullOrEmpty(Criteria.RequiredMaterialId) &&
                weapon.Foundation.MaterialId != Criteria.RequiredMaterialId &&
                weapon.Payload.MaterialId != Criteria.RequiredMaterialId)
            {
                rejectionReason = $"Missing required material: {Criteria.RequiredMaterialId}.";
                return false;
            }

            rejectionReason = null;
            return true;
        }

        public void RegisterDelivery() => DeliveredCount++;
    }

    /// <summary>Host-side owner of the letter queue, timers and submissions.</summary>
    public class OrderManager : MonoBehaviour
    {
        [SerializeField] private int maxActiveLetters = 5;
        [SerializeField] private float flawlessGoldMultiplier = 1.5f;

        private readonly List<CommissionOrder> activeOrders = new();
        public IReadOnlyList<CommissionOrder> ActiveOrders => activeOrders;
        public bool HasFreeSlot => activeOrders.Count < maxActiveLetters;

        public event Action<CommissionOrder> OnOrderReceived;
        public event Action<CommissionOrder> OnOrderExpired;
        public event Action<CommissionOrder, int, int> OnOrderCompleted; // order, gold, rep
        public event Action<CommissionOrder, string, int> OnOrderRejected; // order, reason, rep penalty

        public bool TryAddOrder(CommissionOrder order)
        {
            if (!HasFreeSlot) return false;
            activeOrders.Add(order);
            OnOrderReceived?.Invoke(order);
            return true;
        }

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

        /// <summary>Called when a weapon is dropped into the Outgoing Tube for a chosen letter.</summary>
        public bool TrySubmitWeapon(AssembledWeapon weapon, string targetOrderId)
        {
            var order = activeOrders.Find(o => o.OrderId == targetOrderId);
            if (order == null) return false;

            if (!order.Validate(weapon, out string reason))
            {
                int penalty = order.Archetype == ClientArchetype.ArcaneAcademy ? order.FailurePenaltyReputation : 0;
                OnOrderRejected?.Invoke(order, reason, penalty);
                return false; // weapon returns to the player's hands
            }

            order.RegisterDelivery();
            if (!order.IsFulfilled) return true; // batch order: more units needed

            activeOrders.Remove(order);
            int gold = order.RewardGold;
            if (weapon.Tier == QualityTier.Flawless) gold = Mathf.RoundToInt(gold * flawlessGoldMultiplier);
            OnOrderCompleted?.Invoke(order, gold, order.RewardReputation);
            return true;
        }
    }
}
```

---

## Testing Notes

- Validation order produces the most useful rejection message (type before quality before element).
- Batch orders complete only on the last unit; expiry mid-batch forfeits the whole order.
- Generator never produces criteria for materials behind doors the team has not purchased.

---

Views: [_UI_Module › Letter Commission Board](../UI/_UI_Module.md#letter-commission-board).
