# Magic Doors - Technical Design

> **Zone:** Exploration · **Design:** [GDD/Exploration/MagicDoors](../../GDD/Exploration/MagicDoors.md) · **Related:** [Realms](Realms.md) · [Shop Progression](../Shop/ShopProgression.md)

## Technical Specifications

- **Door data:** `DoorDefinition` (SO): door ID, destination `RealmDefinition`, required shop tier, gold price, owned-at-start flag.
- **Ownership:** Stored in `ShopProgressionState.OwnedDoorIds` and persisted with progression. Purchases go through `ShopProgressionManager.TryPurchaseDoor` (see [Shop Progression](../Shop/ShopProgression.md)).
- **States:** `Locked → Ready → EntryOpen → InProgress → Cooldown → Ready`.
  - `Locked`: tier not reached or not purchased (the door shows its price plaque once the tier is reached).
  - `EntryOpen` (90 s): anyone may enter; every entrant is added to the expedition's member set.
  - `InProgress`: only members may enter. The expedition ends when the realm becomes empty.
  - If the entry window closes with nobody inside, the expedition ends immediately.
  - `Cooldown` (20 s) after the expedition ends.
- **No timer inside realms.** Door timestamps (`entryClosesAt`, `readyAt`) are host-authoritative and replicated as absolute server times; clients compute countdowns locally.
- **Leaving:** Realm-side `ExitPortal` (always open) and the downed bleed-out ejection both call `DimensionalDoor.Exit` / `Eject`.
- **Realm lifetime:** The door owns its `RealmInstance` and unloads it when the expedition ends. One realm per door at a time.
- **Aether Drop-Chute:** Realm interactable that converts deposited items into spawns at the workshop receiving basket for the same door.
- **Performance:** Up to 4 concurrent realms (one per owned door) within memory budget (target ≤ 150 MB per loaded realm).

---

## Architecture & Implementation Approaches

### Approach A: Host-side Door State Machine with Membership Set (Recommended)
- `DimensionalDoor` evaluates timestamps in `Update` on the host and tracks `members` (player IDs) and `inside` (travelers currently in the realm).
- Entry permission is a single rule: `EntryOpen || (InProgress && members.Contains(player))`.
- **Pros:** All door rules live in one place; trivially serializable; no coroutine lifetime issues.

### Approach B: Realm-owned Lifecycle
- The realm instance decides when it ends; the door just forwards players.
- **Cons:** Entry rules and realm lifetime get split across two objects; harder to show door state in the workshop UI.

---

## Networking

- Door state, `entryClosesAt` and the member list replicate on change (members are shown on the sealed door surface).
- Entry/exit are `[ServerRpc]` requests; the host validates `CanEnter`, adds the connection to the realm scene (FishNet `SceneManager`, so the client loads it and starts observing its objects), then tells the owning client to teleport via `[TargetRpc]` (movement is client-authoritative, see [Movement](../Common/Movement.md)).
- Door purchase is a host RPC from the price plaque's hold interaction; the host validates tier and gold.
- Drop-chute deposits are host RPCs; spawned workshop items are host-spawned network objects.

---

## Unity C# Reference Code

```csharp
using System;
using System.Collections.Generic;
using UnityEngine;
using Armotheca.Progression;

namespace Armotheca.Exploration
{
    public enum DoorState : byte { Locked, Ready, EntryOpen, InProgress, Cooldown }

    [CreateAssetMenu(menuName = "Armotheca/Exploration/Door Definition")]
    public class DoorDefinition : ScriptableObject
    {
        public string DoorId;                  // "PyroclasticTrench"
        public RealmDefinition Realm;
        [Min(1)] public int RequiredTier = 1;
        [Min(0)] public int GoldPrice;
        public bool OwnedAtStart;
    }

    public interface IRealmTraveler
    {
        ulong PlayerId { get; }
        void TeleportTo(Vector3 position, Quaternion rotation);
        void DropCarriedCargo();   // backpack + hands, keeps equipped weapon
        void SetInRealm(bool value);
    }

    public class DimensionalDoor : MonoBehaviour
    {
        [Header("Configuration")]
        [SerializeField] private DoorDefinition definition;
        [SerializeField] private float entryWindowSeconds = 90f;
        [SerializeField] private float cooldownSeconds = 20f;
        [SerializeField] private Transform workshopAnchor;
        [SerializeField] private RealmInstanceService realmService;
        [SerializeField] private ShopProgressionManager progression;

        private RealmInstance instance;
        private double entryClosesAt;
        private double readyAt;
        private readonly HashSet<ulong> members = new();
        private readonly HashSet<IRealmTraveler> inside = new();

        public DoorDefinition Definition => definition;
        public DoorState State { get; private set; } = DoorState.Locked;
        public IReadOnlyCollection<ulong> Members => members;
        public float EntryRemainingSeconds => State == DoorState.EntryOpen ? Mathf.Max(0f, (float)(entryClosesAt - Now)) : 0f;

        public event Action<DoorState> OnStateChanged;
        public event Action<IReadOnlyCollection<ulong>> OnMembersChanged;

        private static double Now => Time.timeAsDouble; // production: FishNet TimeManager server tick converted to seconds

        private void Start()
        {
            progression.OnDoorPurchased += HandleDoorPurchased;
            SetState(progression.IsDoorOwned(definition.DoorId) ? DoorState.Ready : DoorState.Locked);
        }

        private void OnDestroy() => progression.OnDoorPurchased -= HandleDoorPurchased;

        private void HandleDoorPurchased(string doorId)
        {
            if (doorId == definition.DoorId && State == DoorState.Locked) SetState(DoorState.Ready);
        }

        // ---------- Opening ----------

        public bool CanOpen => State == DoorState.Ready;

        public void Open()
        {
            if (!CanOpen) return;
            realmService.Load(definition.Realm, onReady: realm =>
            {
                instance = realm;
                instance.ExitPortal.OnUsed += Exit;
                members.Clear();
                entryClosesAt = Now + entryWindowSeconds;
                SetState(DoorState.EntryOpen);
            });
        }

        private void Update()
        {
            switch (State)
            {
                case DoorState.EntryOpen when Now >= entryClosesAt:
                    SetState(DoorState.InProgress);
                    if (inside.Count == 0) EndExpedition(); // nobody went in
                    break;

                case DoorState.Cooldown when Now >= readyAt:
                    SetState(DoorState.Ready);
                    break;
            }
        }

        // ---------- Entering / leaving ----------

        public bool CanEnter(IRealmTraveler traveler) =>
            State == DoorState.EntryOpen ||
            (State == DoorState.InProgress && members.Contains(traveler.PlayerId));

        public bool Enter(IRealmTraveler traveler)
        {
            if (!CanEnter(traveler)) return false;

            traveler.TeleportTo(instance.EntryAnchor.position, instance.EntryAnchor.rotation);
            traveler.SetInRealm(true);
            inside.Add(traveler);
            if (members.Add(traveler.PlayerId)) OnMembersChanged?.Invoke(members);
            instance.SetOccupied(true);
            return true;
        }

        /// <summary>Exit Portal, or stepping back through the door from the realm side.</summary>
        public void Exit(IRealmTraveler traveler)
        {
            if (!inside.Remove(traveler)) return;

            traveler.TeleportTo(workshopAnchor.position, workshopAnchor.rotation);
            traveler.SetInRealm(false);

            if (inside.Count > 0) return;
            instance.SetOccupied(false);              // Realm Pressure pauses while empty
            if (State == DoorState.InProgress) EndExpedition();
        }

        /// <summary>Downed bleed-out (see Combat): cargo stays in the realm, player can re-enter as a member.</summary>
        public void Eject(IRealmTraveler traveler)
        {
            traveler.DropCarriedCargo();
            Exit(traveler);
        }

        private void EndExpedition()
        {
            instance.ExitPortal.OnUsed -= Exit;
            realmService.Unload(instance);
            instance = null;
            members.Clear();
            OnMembersChanged?.Invoke(members);

            readyAt = Now + cooldownSeconds;
            SetState(DoorState.Cooldown);
        }

        private void SetState(DoorState next)
        {
            State = next;
            OnStateChanged?.Invoke(next);
        }
    }

    /// <summary>Always-open portal in every realm's Entry area. Used via an instant interaction.</summary>
    public class ExitPortal : MonoBehaviour
    {
        public event Action<IRealmTraveler> OnUsed;

        public void Use(IRealmTraveler traveler) => OnUsed?.Invoke(traveler);
    }

    /// <summary>Realm-side chute that ships deposited items to the workshop basket.</summary>
    public class AetherDropChute : MonoBehaviour
    {
        public event Action<string> OnItemShipped; // workshop basket listens and spawns the item

        public void Deposit(IEnumerable<string> itemIds)
        {
            foreach (var id in itemIds) OnItemShipped?.Invoke(id);
        }
    }
}
```

---

## Testing Notes

- Door stays `Locked` below the required tier even with enough gold; purchase moves it to `Ready` and persists.
- A non-member is refused after the entry window; a member who used the Exit Portal can re-enter while a teammate is inside.
- Last player leaving during `InProgress` unloads the realm and starts cooldown; leaving during `EntryOpen` does not.
- Entry window closing with nobody inside ends the expedition immediately.
