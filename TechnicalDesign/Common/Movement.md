# Movement - Technical Design

> **Zone:** Common · **Design:** [GDD/Common/Movement](../../GDD/Common/Movement.md)

## Technical Specifications

- **Controller type:** Kinematic capsule (Unity `CharacterController` or a custom kinematic mover with `Physics.CapsuleCast`). No rigidbody physics on players.
- **Update:** Movement simulated in `Update` with frame-rate-independent integration; ground checks use a sphere cast below the capsule.
- **Moves:** Walk, Sprint, Jump, Roll — implemented with the **State pattern**: one class per state (`GroundedState`, `AirborneState`, `RollingState`, `LockedState`), owned by `PlayerMovementController`.
- **Forgiveness:** Coyote time and jump buffering timers, shared by all states through the controller.
- **Tuning:** All values in a `MovementSettings` ScriptableObject so designers tune without code changes.
- **Performance budget:** < 0.05 ms per character per frame on target hardware.

---

## Architecture & Implementation Approaches

### Approach A: Single Controller with Explicit State Enum
- One controller owns velocity and a state enum; every transition lives in one `switch`.
- **Pros:** Very small and easy to debug for a 4-move set.
- **Cons:** Each new move (climb, swim, ledge grab, glide) adds branches to the same method; transition rules become tangled.

### Approach B: State Pattern — One Class per State (Chosen)
- `PlayerMovementController` is the **context**: it owns the motor (velocities, timers, `CharacterController`), inputs and flags, and exposes shared helpers (locomotion, gravity, jump consumption).
- Each `MovementState` subclass owns its own `Enter` / `Tick` / `Exit` logic, its outgoing transitions and its **capability flags** (`AllowsSprint`, `AllowsRoll`, `IsInvulnerable`).
- Other systems never read state internals; they query `CanRoll`, `CanSprint`, `IsInvulnerable` and set `Lock` / `IsCarrying` (see [Object Interaction](ObjectInteraction.md) and [Combat](Combat.md)).
- **Pros:** The move set is expected to grow; new moves are added as new classes without touching existing ones (Open/Closed). States are testable in isolation.
- **Cons:** More files and some indirection for the current 4 states; shared motor logic must stay in the controller to avoid duplication between states.

### Adding a New Move (e.g. Climbing)
1. Add an entry to `MovementStateId` (keep values stable — they are sent over the network).
2. Create `ClimbingState : MovementState` with its `Enter` / `Tick` / `Exit` and capability flags.
3. Register it in `PlayerMovementController.RegisterStates()`.
4. Add the entry transition in the state(s) it starts from (e.g. `AirborneState` detects a climbable surface) and the exit transition inside `ClimbingState`.
5. Add tuning fields to `MovementSettings` and update the state table in the [GDD](../../GDD/Common/Movement.md).

---

## Networking

FishNet (see [Technical Overview](../TechnicalOverview.md)):

- **Owner-authoritative movement:** `PlayerMovementController` lives on a `NetworkObject` with FishNet's `NetworkTransform` set to **client authoritative**. The owning client simulates immediately; the transform is sent at the FishNet tick (initial value: 30 Hz) and other clients interpolate.
- **State replication:** On `OnStateChanged`, the owner sends the new `MovementStateId` (and roll start tick) through a `[ServerRpc]`; the host stores it in a `SyncVar<MovementStateId>` that drives animation on all clients.
- **Host validation:** The host rejects implausible moves (speed above sprint max with tolerance, teleport distances) and corrects the owner via a `[TargetRpc]`.
- **Roll invulnerability** is evaluated on the host using the replicated roll start tick to avoid client-side cheating of i-frames.
- **Portal transitions:** Because movement is client-authoritative, the host asks the owning client to teleport (`[TargetRpc]`, see [Magic Doors](../Exploration/MagicDoors.md)); the owner moves itself and clears interpolation.
- **Prediction:** FishNet's client-side prediction is not used initially; revisit only if playtests show movement or roll timing problems under latency.

---

## Input Mapping (Input System)

| Action | Keyboard / Mouse | Gamepad |
|---|---|---|
| Move | WASD | Left stick |
| Sprint (hold) | Left Shift | Left stick press / LB |
| Jump | Space | A / Cross |
| Roll | Left Ctrl / Right Mouse | B / Circle |

---

## Unity C# Reference Code

### Settings, IDs and Base State

```csharp
using System;
using System.Collections.Generic;
using UnityEngine;

namespace Armotheca.Movement
{
    [CreateAssetMenu(menuName = "Armotheca/Movement Settings")]
    public class MovementSettings : ScriptableObject
    {
        [Header("Locomotion")]
        public float WalkSpeed = 4.0f;
        public float SprintSpeed = 6.5f;
        public float CarryingSpeedMultiplier = 0.85f;
        public float Acceleration = 60f;
        public float TurnSpeedDegrees = 900f;

        [Header("Jump")]
        public float JumpHeight = 1.2f;
        public float Gravity = -25f;
        public float AirControl = 0.4f;
        public float CoyoteTime = 0.12f;
        public float JumpBufferTime = 0.12f;

        [Header("Roll")]
        public float RollDistance = 3.5f;
        public float RollDuration = 0.45f;
        public float RollInvulnerableTime = 0.25f;
        public float RollCooldown = 0.6f;
    }

    /// <summary>Stable IDs, replicated over the network and used by animation.</summary>
    public enum MovementStateId : byte
    {
        Grounded = 0,
        Airborne = 1,
        Rolling = 2,
        Locked = 3
    }

    /// <summary>Why the character is rooted. Interaction locks can be cancelled by rolling; Downed cannot.</summary>
    public enum LockReason : byte
    {
        None,
        Interaction,
        Downed
    }

    public abstract class MovementState
    {
        protected readonly PlayerMovementController Ctx;
        protected MovementSettings Settings => Ctx.Settings;

        protected MovementState(PlayerMovementController context) => Ctx = context;

        public abstract MovementStateId Id { get; }

        // Capability flags queried by other systems through the controller.
        public virtual bool AllowsSprint => false;
        public virtual bool AllowsRoll => false;
        public virtual bool IsInvulnerable => false;

        public virtual void Enter() { }
        public virtual void Exit() { }
        public abstract void Tick(float deltaTime);
    }
}
```

### Controller (Context)

```csharp
using System;
using System.Collections.Generic;
using UnityEngine;

namespace Armotheca.Movement
{
    [RequireComponent(typeof(CharacterController))]
    public class PlayerMovementController : MonoBehaviour
    {
        [SerializeField] private MovementSettings settings;

        private readonly Dictionary<MovementStateId, MovementState> states = new();

        public MovementSettings Settings => settings;
        public CharacterController Body { get; private set; }
        public MovementState Current { get; private set; }
        public MovementStateId State => Current.Id;

        // Shared motor data (used by states)
        public Vector3 PlanarVelocity { get; set; }
        public float VerticalVelocity { get; set; }
        public float LastGroundedTime { get; private set; } = float.NegativeInfinity;
        public float LastJumpPressedTime { get; private set; } = float.NegativeInfinity;
        public float LastRollEndTime { get; set; } = float.NegativeInfinity;

        // Inputs (set by the input/network layer)
        public Vector2 MoveInput { get; set; }
        public bool SprintHeld { get; set; }

        // Flags set by other systems
        public bool IsCarrying { get; set; }
        public LockReason Lock { get; set; } = LockReason.None;
        public bool IsLocked => Lock != LockReason.None;

        // Capability queries for other systems
        public bool IsInvulnerable => Current.IsInvulnerable;
        public bool CanSprint => Current.AllowsSprint && !IsLocked;
        public bool CanRoll => Current.AllowsRoll && !IsCarrying && Body.isGrounded &&
                               Time.time - LastRollEndTime >= settings.RollCooldown;

        public event Action<MovementStateId> OnStateChanged;
        public event Action OnJumped;
        public event Action OnRollStarted; // PlayerInteractor listens and cancels any continuous interaction

        private void Awake()
        {
            Body = GetComponent<CharacterController>();
            RegisterStates();
            ChangeState(MovementStateId.Grounded);
        }

        /// <summary>Extension point: new moves register their state here.</summary>
        protected virtual void RegisterStates()
        {
            Register(new GroundedState(this));
            Register(new AirborneState(this));
            Register(new RollingState(this));
            Register(new LockedState(this));
        }

        protected void Register(MovementState state) => states[state.Id] = state;

        public void ChangeState(MovementStateId id)
        {
            if (Current != null && Current.Id == id) return;
            Current?.Exit();
            Current = states[id];
            Current.Enter();
            OnStateChanged?.Invoke(id);
        }

        public void PressJump() => LastJumpPressedTime = Time.time;

        public bool TryRoll()
        {
            if (!CanRoll) return false;
            ChangeState(MovementStateId.Rolling);
            return true;
        }

        private void Update()
        {
            if (Body.isGrounded) LastGroundedTime = Time.time;

            // A lock from outside (interaction, downed) pre-empts every state except an active roll.
            if (IsLocked && State != MovementStateId.Locked && State != MovementStateId.Rolling)
                ChangeState(MovementStateId.Locked);

            Current.Tick(Time.deltaTime);
        }

        // ---------- Shared motor helpers used by states ----------

        public Vector3 WishDirection =>
            Vector3.ClampMagnitude(new Vector3(MoveInput.x, 0f, MoveInput.y), 1f); // input already camera-relative

        public float CurrentTopSpeed()
        {
            float speed = SprintHeld && Current.AllowsSprint ? settings.SprintSpeed : settings.WalkSpeed;
            return IsCarrying ? speed * settings.CarryingSpeedMultiplier : speed;
        }

        public void ApplyLocomotion(float deltaTime, float topSpeed, float control)
        {
            Vector3 wish = WishDirection;
            PlanarVelocity = Vector3.MoveTowards(PlanarVelocity, wish * topSpeed, settings.Acceleration * control * deltaTime);

            if (wish.sqrMagnitude > 0.01f)
            {
                Quaternion look = Quaternion.LookRotation(wish);
                transform.rotation = Quaternion.RotateTowards(transform.rotation, look, settings.TurnSpeedDegrees * deltaTime);
            }
        }

        public void ApplyGravityAndMove(float deltaTime)
        {
            if (Body.isGrounded && VerticalVelocity < 0f) VerticalVelocity = -2f; // keep snapped to ground
            VerticalVelocity += settings.Gravity * deltaTime;
            Body.Move((PlanarVelocity + Vector3.up * VerticalVelocity) * deltaTime);
        }

        /// <summary>Consumes a buffered jump if within coyote time. Returns true if a jump happened.</summary>
        public bool TryConsumeJump()
        {
            bool buffered = Time.time - LastJumpPressedTime <= settings.JumpBufferTime;
            bool coyote = Time.time - LastGroundedTime <= settings.CoyoteTime;
            if (!buffered || !coyote || IsLocked) return false;

            VerticalVelocity = Mathf.Sqrt(-2f * settings.Gravity * settings.JumpHeight);
            LastJumpPressedTime = float.NegativeInfinity;
            LastGroundedTime = float.NegativeInfinity; // prevents a second coyote jump
            OnJumped?.Invoke();
            return true;
        }

        internal void RaiseRollStarted() => OnRollStarted?.Invoke();
    }
}
```

### States

```csharp
using UnityEngine;

namespace Armotheca.Movement
{
    public sealed class GroundedState : MovementState
    {
        public GroundedState(PlayerMovementController ctx) : base(ctx) { }

        public override MovementStateId Id => MovementStateId.Grounded;
        public override bool AllowsSprint => true;
        public override bool AllowsRoll => true;

        public override void Tick(float dt)
        {
            Ctx.ApplyLocomotion(dt, Ctx.CurrentTopSpeed(), 1f);

            if (Ctx.TryConsumeJump())
            {
                Ctx.ApplyGravityAndMove(dt);
                Ctx.ChangeState(MovementStateId.Airborne);
                return;
            }

            Ctx.ApplyGravityAndMove(dt);

            // Walked off a ledge: stay grounded during coyote time, then fall.
            if (!Ctx.Body.isGrounded && Time.time - Ctx.LastGroundedTime > Settings.CoyoteTime)
                Ctx.ChangeState(MovementStateId.Airborne);
        }
    }

    public sealed class AirborneState : MovementState
    {
        public AirborneState(PlayerMovementController ctx) : base(ctx) { }

        public override MovementStateId Id => MovementStateId.Airborne;

        public override void Tick(float dt)
        {
            // Sprint momentum is kept from the ground, but airborne input cannot accelerate past walk/sprint speed.
            Ctx.ApplyLocomotion(dt, Mathf.Max(Ctx.CurrentTopSpeed(), Ctx.PlanarVelocity.magnitude), Settings.AirControl);
            Ctx.TryConsumeJump(); // late coyote jump
            Ctx.ApplyGravityAndMove(dt);

            if (Ctx.Body.isGrounded && Ctx.VerticalVelocity <= 0f)
                Ctx.ChangeState(MovementStateId.Grounded);
        }
    }

    public sealed class RollingState : MovementState
    {
        private Vector3 direction;
        private float startTime;

        public RollingState(PlayerMovementController ctx) : base(ctx) { }

        public override MovementStateId Id => MovementStateId.Rolling;
        public override bool IsInvulnerable => Time.time - startTime <= Settings.RollInvulnerableTime;

        public override void Enter()
        {
            Vector3 wish = Ctx.WishDirection;
            direction = wish.sqrMagnitude > 0.01f ? wish.normalized : Ctx.transform.forward;
            startTime = Time.time;
            Ctx.transform.rotation = Quaternion.LookRotation(direction);

            if (Ctx.Lock == LockReason.Interaction) Ctx.Lock = LockReason.None; // rolling cancels interactions
            Ctx.RaiseRollStarted();
        }

        public override void Tick(float dt)
        {
            Ctx.PlanarVelocity = direction * (Settings.RollDistance / Settings.RollDuration);
            Ctx.ApplyGravityAndMove(dt);

            if (Time.time - startTime >= Settings.RollDuration)
            {
                Ctx.LastRollEndTime = Time.time;
                Ctx.PlanarVelocity = direction * Settings.WalkSpeed;
                Ctx.ChangeState(Ctx.Body.isGrounded ? MovementStateId.Grounded : MovementStateId.Airborne);
            }
        }
    }

    /// <summary>Rooted by an interaction or by being downed.</summary>
    public sealed class LockedState : MovementState
    {
        public LockedState(PlayerMovementController ctx) : base(ctx) { }

        public override MovementStateId Id => MovementStateId.Locked;
        public override bool AllowsRoll => Ctx.Lock == LockReason.Interaction;

        public override void Enter() => Ctx.PlanarVelocity = Vector3.zero;

        public override void Tick(float dt)
        {
            Ctx.PlanarVelocity = Vector3.zero;
            Ctx.ApplyGravityAndMove(dt);

            if (!Ctx.IsLocked)
                Ctx.ChangeState(Ctx.Body.isGrounded ? MovementStateId.Grounded : MovementStateId.Airborne);
        }
    }
}
```

---

## Testing Notes

- Edit-mode tests per state: each state's capability flags and transitions can be tested with a stub context.
- Play-mode tests: jump height within ±5% of `JumpHeight`; roll covers `RollDistance` ±10% on flat ground.
- Roll is blocked while `IsCarrying` and while `Lock == Downed`; allowed while `Lock == Interaction` (and cancels the interaction).
- Network soak test with 4 players at 150 ms simulated latency: no visible rubber-banding during sprint/roll; remote animation follows replicated `MovementStateId`.
