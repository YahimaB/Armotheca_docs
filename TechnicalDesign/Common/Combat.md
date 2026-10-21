# Combat - Technical Design

> **Zone:** Common · **Design:** [GDD/Common/Combat](../../GDD/Common/Combat.md)

## Technical Specifications

- **Damage source:** Every hit deals the attacker weapon's `BaseDamage` (integer). No quality, element or other modifiers are applied at this stage (see [Weapon Crafting](../Shop/WeaponCrafting.md)).
- **Attack profiles vs weapon stats:** Timing, reach and projectile parameters are **attack profile** data defined once per weapon category (`SwordSwingProfile`, `MagicOrbProfile`). They are not per-weapon stats and do not vary between crafted weapons.
- **Sword hit detection:** During the active window, an arc test (`OverlapSphereNonAlloc` + angle filter) runs each physics step; a per-swing `HashSet` prevents hitting the same target twice.
- **Orb projectile:** Pooled projectile moved kinematically with a `SphereCast` per step; destroyed on first `IDamageable` or environment hit, or at max range.
- **Health:** `Health` component implements `IDamageable`; supports invulnerability windows (roll, post-hit) and a downed state for players.
- **Performance budget:** ≤ 40 active orbs and ≤ 20 mobs per realm (Realm Pressure hard cap) with no GC allocations in combat loops (pooling, NonAlloc queries).

---

## Architecture & Implementation Approaches

### Approach A: Profile ScriptableObjects + Attack Executors (Recommended)
- `AttackProfile` subclasses hold timing data; `PlayerCombatController` picks the executor from the equipped weapon's category.
- **Pros:** Adding a new attack type is a new profile + executor; designers tune timings in data.
- **Cons:** Two small class hierarchies to maintain.

### Approach B: Animation-Event-Driven Hit Windows
- Hit windows opened/closed by animation events.
- **Pros:** Perfect sync with animation.
- **Cons:** Logic depends on animation assets; harder to unit test and to run on a headless host.

Approach A is chosen. Animations follow the profile timings; animation events are used only for VFX/SFX.

---

## Networking

- **Host-authoritative damage:** Clients call a `[ServerRpc] RequestAttack(aimDirection)`; the host runs hit detection and applies damage. The attacking client plays the swing/cast animation immediately for responsiveness.
- **Orbs:** Replicated as an `[ObserversRpc]` spawn event (origin, direction, tick) with deterministic flight on every client; only the host resolves hits. Preferred over spawning a `NetworkObject` per orb for bandwidth.
- **Health:** `SyncVar<int>` on the mob/player `NetworkBehaviour`, with change callbacks for UI and hit flashes.
- **Lag compensation:** FishNet's lag compensation is available if host-side hit detection feels unfair to remote players; not used initially.
- **Invulnerability checks** use host time and replicated roll start time.

---

## Unity C# Reference Code

```csharp
using System;
using System.Collections.Generic;
using UnityEngine;

namespace Armotheca.Combat
{
    public readonly struct DamageInfo
    {
        public readonly int Amount;
        public readonly Vector3 HitPoint;
        public readonly Vector3 Direction;
        public readonly GameObject Source;

        public DamageInfo(int amount, Vector3 hitPoint, Vector3 direction, GameObject source)
        {
            Amount = amount;
            HitPoint = hitPoint;
            Direction = direction;
            Source = source;
        }
    }

    public interface IDamageable
    {
        bool IsAlive { get; }
        bool IsHostileTo(GameObject source);
        void ApplyDamage(in DamageInfo info);
    }

    public class Health : MonoBehaviour, IDamageable
    {
        public enum Faction { Player, Mob }

        [SerializeField] private Faction faction;
        [SerializeField] private int maxHealth = 100;
        [SerializeField] private float postHitInvulnerability = 0.5f;

        public int Current { get; private set; }
        public int Max => maxHealth;
        public bool IsAlive => Current > 0;
        public Func<bool> ExternalInvulnerability; // e.g. roll i-frames from PlayerMovementController

        public event Action<DamageInfo> OnDamaged;
        public event Action OnDepleted;

        private float lastHitTime = float.NegativeInfinity;

        private void Awake() => Current = maxHealth;

        public void SetMax(int value, bool refill = true)
        {
            maxHealth = value;
            if (refill) Current = maxHealth;
        }

        public bool IsHostileTo(GameObject source) =>
            source.TryGetComponent(out Health other) && other.faction != faction; // friendly fire off

        public void ApplyDamage(in DamageInfo info)
        {
            if (!IsAlive) return;
            if (Time.time - lastHitTime < postHitInvulnerability) return;
            if (ExternalInvulnerability != null && ExternalInvulnerability()) return;

            lastHitTime = Time.time;
            Current = Mathf.Max(0, Current - info.Amount);
            OnDamaged?.Invoke(info);
            if (Current == 0) OnDepleted?.Invoke();
        }

        public void Restore(float fraction) => Current = Mathf.Clamp(Mathf.RoundToInt(maxHealth * fraction), 1, maxHealth);
    }

    public abstract class AttackProfile : ScriptableObject { }

    [CreateAssetMenu(menuName = "Armotheca/Combat/Sword Swing Profile")]
    public class SwordSwingProfile : AttackProfile
    {
        public float Windup = 0.10f;
        public float Active = 0.12f;
        public float Recovery = 0.25f;
        public float ArcAngle = 120f;
        public float Reach = 1.8f;
        public int ChainLength = 2;
        [Range(0f, 1f)] public float ChainInputWindowStart = 0.5f; // normalized swing time
        public float MovementMultiplierDuringSwing = 0.3f;
    }

    [CreateAssetMenu(menuName = "Armotheca/Combat/Magic Orb Profile")]
    public class MagicOrbProfile : AttackProfile
    {
        public float CastTime = 0.15f;
        public float Cooldown = 0.6f;
        public float Speed = 14f;
        public float MaxRange = 12f;
        public float Radius = 0.25f;
        public float AimAssistAngle = 15f;
        public MagicOrbProjectile ProjectilePrefab;
    }

    /// <summary>Host-side sword swing executor. Driven by PlayerCombatController.</summary>
    public class SwordSwingExecutor
    {
        private readonly SwordSwingProfile profile;
        private readonly Transform owner;
        private readonly LayerMask hitMask;
        private readonly Collider[] buffer = new Collider[16];
        private readonly HashSet<IDamageable> hitThisSwing = new();

        private float swingStart = float.NegativeInfinity;
        private int chainIndex;
        private bool queued;

        public SwordSwingExecutor(SwordSwingProfile profile, Transform owner, LayerMask hitMask)
        {
            this.profile = profile;
            this.owner = owner;
            this.hitMask = hitMask;
        }

        private float SwingLength => profile.Windup + profile.Active + profile.Recovery;
        public bool IsSwinging => Time.time - swingStart < SwingLength;
        public int ChainIndex => chainIndex;

        public bool TryStartOrQueue()
        {
            if (!IsSwinging) { Begin(0); return true; }

            float normalized = (Time.time - swingStart) / SwingLength;
            if (normalized >= profile.ChainInputWindowStart && chainIndex + 1 < profile.ChainLength)
            {
                queued = true;
                return true;
            }
            return false;
        }

        public void CancelRecovery() // called when the player rolls
        {
            if (Time.time - swingStart > profile.Windup + profile.Active) swingStart = float.NegativeInfinity;
            queued = false;
        }

        public void Tick(int baseDamage)
        {
            float t = Time.time - swingStart;
            if (t >= profile.Windup && t <= profile.Windup + profile.Active)
                DetectHits(baseDamage);

            if (t >= SwingLength && queued) Begin(chainIndex + 1);
        }

        private void Begin(int index)
        {
            chainIndex = index;
            queued = false;
            swingStart = Time.time;
            hitThisSwing.Clear();
        }

        private void DetectHits(int baseDamage)
        {
            int count = Physics.OverlapSphereNonAlloc(owner.position, profile.Reach, buffer, hitMask);
            for (int i = 0; i < count; i++)
            {
                if (!buffer[i].TryGetComponent(out IDamageable target)) continue;
                if (!target.IsAlive || !target.IsHostileTo(owner.gameObject) || !hitThisSwing.Add(target)) continue;

                Vector3 to = buffer[i].transform.position - owner.position;
                if (Vector3.Angle(owner.forward, to) > profile.ArcAngle * 0.5f) continue;

                target.ApplyDamage(new DamageInfo(baseDamage, buffer[i].ClosestPoint(owner.position), to.normalized, owner.gameObject));
            }
        }
    }

    /// <summary>Pooled orb projectile. Hits the first hostile damageable or wall.</summary>
    public class MagicOrbProjectile : MonoBehaviour
    {
        [SerializeField] private LayerMask hitMask;

        private Vector3 direction;
        private float speed, radius, remainingRange;
        private int damage;
        private GameObject source;
        public event Action<MagicOrbProjectile> OnDespawn;

        public void Launch(Vector3 dir, MagicOrbProfile profile, int baseDamage, GameObject owner)
        {
            direction = dir.normalized;
            speed = profile.Speed;
            radius = profile.Radius;
            remainingRange = profile.MaxRange;
            damage = baseDamage;
            source = owner;
            gameObject.SetActive(true);
        }

        private void FixedUpdate()
        {
            float step = speed * Time.fixedDeltaTime;
            if (Physics.SphereCast(transform.position, radius, direction, out RaycastHit hit, step, hitMask))
            {
                if (hit.collider.TryGetComponent(out IDamageable target) && target.IsAlive && target.IsHostileTo(source))
                    target.ApplyDamage(new DamageInfo(damage, hit.point, direction, source));
                Despawn();
                return;
            }

            transform.position += direction * step;
            remainingRange -= step;
            if (remainingRange <= 0f) Despawn();
        }

        private void Despawn()
        {
            gameObject.SetActive(false);
            OnDespawn?.Invoke(this);
        }
    }
}
```

### Player Downed Flow (host)
1. `Health.OnDepleted` on a player → set `PlayerMovementController.Lock = LockReason.Downed`, start bleed-out timer (20 s), enable a `ReviveInteractable` (a `ContinuousInteractableBase` with 3 s duration, see [Object Interaction](ObjectInteraction.md)).
2. Revive completed → `Health.Restore(0.5f)`, set `Lock = LockReason.None`.
3. Timer expired or no other living player in the realm → eject to workshop (see [Magic Doors](../Exploration/MagicDoors.md)): drop backpack + hands at the downed position, keep the equipped weapon, `Health.Restore(1f)`.
