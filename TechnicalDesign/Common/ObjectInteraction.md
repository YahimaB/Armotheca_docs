# Object Interaction - Technical Design

> **Zone:** Common · **Design:** [GDD/Common/ObjectInteraction](../../GDD/Common/ObjectInteraction.md)

## Technical Specifications

- **Two interaction contracts:** `IInstantInteractable` (resolve on press) and `IContinuousInteractable` (start / tick / stop with progress). One object may implement both (e.g. a forge: instant to load ore, continuous to pump bellows).
- **Targeting:** `Physics.OverlapSphere` around a point in front of the player (reach 1.8 m) on an `Interactable` layer, scored by distance and facing angle. Runs at 10 Hz on the local client for prompts; validated by the host on use.
- **Carry state:** `PlayerCarrier` component holds the Hands item, the equipped weapon and the backpack contents.
- **Prompts:** Interactables return a `InteractionPrompt` (verb + object name + kind) for the current player context; UI reads it via an event.
- **Progress retention:** Continuous interactables keep progress for `ProgressRetentionSeconds` (5 s) after the last tick before decaying.
- **Performance budget:** Targeting query < 0.02 ms per local player; no per-frame allocations (use `OverlapSphereNonAlloc`).

---

## Architecture & Implementation Approaches

### Approach A: Interface Contracts + Central Interactor (Recommended)
- `PlayerInteractor` finds the best target, shows its prompt and forwards input to it.
- Objects implement only the contract(s) they need. Workstations, nodes, doors, sockets and downed players all plug into the same flow.
- **Pros:** New object types need no changes to the player code; easy to test interactables in isolation.
- **Cons:** Context rules (what the verb is with a given item in hand) live in each interactable and must stay consistent.

### Approach B: Data-Driven Interaction Table
- A ScriptableObject maps `(item in hands, target type) → action`.
- **Pros:** Designers edit rules without code.
- **Cons:** Harder to express station-specific logic (mini-games, multi-helper rules).

Approach A is chosen; context rules are kept in a shared helper to stay consistent.

---

## Networking

- Clients send an **intent RPC**: `RequestInteract(targetNetworkId, kind, phase)` where phase is `Press`, `HoldStart`, `HoldStop`.
- The **host** re-runs `CanInteract` (distance, line of sight, busy state) and executes the interaction; item ownership changes are host-authoritative.
- Continuous progress is **ticked on the host** and replicated as a normalized value (≤ 10 Hz) for progress bars. Clients predict the bar locally and correct on update.
- Busy/exclusive locks (one player per anvil) live on the host to prevent double use.

---

## Unity C# Reference Code

```csharp
using System;
using System.Collections.Generic;
using UnityEngine;

namespace Armotheca.Interaction
{
    public enum InteractionKind
    {
        Instant,
        Continuous
    }

    public readonly struct InteractionPrompt
    {
        public readonly InteractionKind Kind;
        public readonly string Verb;       // "Pick up", "Pump"
        public readonly string TargetName; // "Iron Ore", "Bellows"
        public readonly string BlockedReason; // null if allowed

        public InteractionPrompt(InteractionKind kind, string verb, string targetName, string blockedReason = null)
        {
            Kind = kind;
            Verb = verb;
            TargetName = targetName;
            BlockedReason = blockedReason;
        }

        public bool IsBlocked => !string.IsNullOrEmpty(BlockedReason);
    }

    /// <summary>Anything that can be targeted by the interactor.</summary>
    public interface IInteractable
    {
        Transform Transform { get; }
        bool TryGetPrompt(PlayerCarrier player, out InteractionPrompt prompt);
    }

    public interface IInstantInteractable : IInteractable
    {
        bool CanInteractInstant(PlayerCarrier player);
        void InteractInstant(PlayerCarrier player);
    }

    public interface IContinuousInteractable : IInteractable
    {
        int MaxHelpers { get; }                // 1 = exclusive
        float Progress01 { get; }
        bool CanBeginContinuous(PlayerCarrier player);
        void BeginContinuous(PlayerCarrier player);
        void TickContinuous(PlayerCarrier player, float deltaTime);
        void EndContinuous(PlayerCarrier player, bool completed);
    }

    /// <summary>
    /// Base class handling helper counting, progress retention and completion for continuous interactions.
    /// </summary>
    public abstract class ContinuousInteractableBase : MonoBehaviour, IContinuousInteractable
    {
        [SerializeField] private float durationSeconds = 3f;
        [SerializeField] private int maxHelpers = 1;
        [SerializeField] private float extraHelperSpeedBonus = 0.5f;
        [SerializeField] private float progressRetentionSeconds = 5f;

        private readonly HashSet<PlayerCarrier> helpers = new();
        private float progress;
        private float lastTickTime;

        public Transform Transform => transform;
        public int MaxHelpers => maxHelpers;
        public float Progress01 => Mathf.Clamp01(progress / durationSeconds);
        public event Action<float> OnProgressChanged;

        public abstract bool TryGetPrompt(PlayerCarrier player, out InteractionPrompt prompt);
        protected abstract bool IsReady(PlayerCarrier player);
        protected abstract void OnCompleted();

        public virtual bool CanBeginContinuous(PlayerCarrier player) =>
            IsReady(player) && (helpers.Contains(player) || helpers.Count < maxHelpers);

        public void BeginContinuous(PlayerCarrier player)
        {
            if (Time.time - lastTickTime > progressRetentionSeconds) progress = 0f;
            helpers.Add(player);
        }

        public void TickContinuous(PlayerCarrier player, float deltaTime)
        {
            if (!helpers.Contains(player)) return;

            // Each helper ticks individually; scale so that N helpers progress at 1 + (N-1)*bonus.
            float speed = (1f + (helpers.Count - 1) * extraHelperSpeedBonus) / helpers.Count;
            progress += deltaTime * speed;
            lastTickTime = Time.time;
            OnProgressChanged?.Invoke(Progress01);

            if (progress >= durationSeconds)
            {
                progress = 0f;
                var finished = new List<PlayerCarrier>(helpers);
                helpers.Clear();
                OnCompleted();
                foreach (var p in finished) p.Interactor.NotifyContinuousEnded(this, true);
            }
        }

        public void EndContinuous(PlayerCarrier player, bool completed) => helpers.Remove(player);
    }

    /// <summary>What a player is holding: hands, equipped weapon, expedition backpack.</summary>
    public class PlayerCarrier : MonoBehaviour
    {
        [SerializeField] private int backpackCapacity = 6;

        public PlayerInteractor Interactor { get; private set; }
        public GameObject HandsItem { get; private set; }
        public GameObject EquippedWeapon { get; private set; }
        public IReadOnlyList<string> Backpack => backpack;
        public bool HandsEmpty => HandsItem == null;

        private readonly List<string> backpack = new();
        public event Action OnCarryChanged;

        private void Awake() => Interactor = GetComponent<PlayerInteractor>();

        public bool TryTakeIntoHands(GameObject item)
        {
            if (!HandsEmpty) return false;
            HandsItem = item;
            OnCarryChanged?.Invoke();
            return true;
        }

        public GameObject ReleaseHands()
        {
            var item = HandsItem;
            HandsItem = null;
            OnCarryChanged?.Invoke();
            return item;
        }

        /// <summary>Moves the weapon in hands to the weapon slot, swapping any equipped weapon into hands.</summary>
        public bool TryEquipFromHands(Func<GameObject, bool> isWeapon)
        {
            if (HandsEmpty || !isWeapon(HandsItem)) return false;
            (EquippedWeapon, HandsItem) = (HandsItem, EquippedWeapon);
            OnCarryChanged?.Invoke();
            return true;
        }

        public bool TryAddToBackpack(string itemId)
        {
            if (backpack.Count >= backpackCapacity) return false;
            backpack.Add(itemId);
            OnCarryChanged?.Invoke();
            return true;
        }

        public List<string> EmptyBackpack()
        {
            var contents = new List<string>(backpack);
            backpack.Clear();
            OnCarryChanged?.Invoke();
            return contents;
        }
    }

    /// <summary>Finds the best target in front of the player and routes input to it.</summary>
    [RequireComponent(typeof(PlayerCarrier))]
    public class PlayerInteractor : MonoBehaviour
    {
        [SerializeField] private float reach = 1.8f;
        [SerializeField] private float facingWeight = 2f;
        [SerializeField] private LayerMask interactableMask;

        private readonly Collider[] hits = new Collider[16];
        private PlayerCarrier carrier;
        private IContinuousInteractable activeContinuous;

        public IInteractable CurrentTarget { get; private set; }
        public bool IsInContinuous => activeContinuous != null;

        public event Action<InteractionPrompt?> OnPromptChanged;
        public event Action<bool> OnContinuousStateChanged; // true = started (lock movement)

        private void Awake() => carrier = GetComponent<PlayerCarrier>();

        public void RefreshTarget()
        {
            Vector3 origin = transform.position + transform.forward * (reach * 0.5f);
            int count = Physics.OverlapSphereNonAlloc(origin, reach * 0.5f, hits, interactableMask);

            IInteractable best = null;
            float bestScore = float.MaxValue;
            for (int i = 0; i < count; i++)
            {
                if (!hits[i].TryGetComponent(out IInteractable candidate)) continue;
                Vector3 to = candidate.Transform.position - transform.position;
                float angle = Vector3.Angle(transform.forward, to);
                float score = to.magnitude + facingWeight * (angle / 180f);
                if (score < bestScore) { bestScore = score; best = candidate; }
            }

            CurrentTarget = best;
            if (best != null && best.TryGetPrompt(carrier, out var prompt)) OnPromptChanged?.Invoke(prompt);
            else OnPromptChanged?.Invoke(null);
        }

        public void OnInteractPressed()
        {
            if (CurrentTarget is IInstantInteractable instant && instant.CanInteractInstant(carrier))
            {
                instant.InteractInstant(carrier);
                return;
            }

            if (CurrentTarget is IContinuousInteractable continuous && continuous.CanBeginContinuous(carrier))
            {
                activeContinuous = continuous;
                continuous.BeginContinuous(carrier);
                OnContinuousStateChanged?.Invoke(true);
            }
        }

        public void TickHeld(float deltaTime) => activeContinuous?.TickContinuous(carrier, deltaTime);

        /// <summary>Called on button release, roll, hit taken or moving out of reach.</summary>
        public void CancelContinuous()
        {
            if (activeContinuous == null) return;
            activeContinuous.EndContinuous(carrier, false);
            activeContinuous = null;
            OnContinuousStateChanged?.Invoke(false);
        }

        public void NotifyContinuousEnded(IContinuousInteractable source, bool completed)
        {
            if (activeContinuous != source) return;
            activeContinuous = null;
            OnContinuousStateChanged?.Invoke(false);
        }
    }
}
```

- `OnContinuousStateChanged(true)` sets `PlayerMovementController.Lock = LockReason.Interaction` (and `false` clears it); `PlayerCarrier.OnCarryChanged` updates `IsCarrying`. `PlayerMovementController.OnRollStarted` calls `CancelContinuous()` (see [Movement](Movement.md)).
- Instant interactions take priority over continuous ones on the same target, so pressing interact on a forge with ore in hands loads it, and holding with empty hands pumps the bellows.
