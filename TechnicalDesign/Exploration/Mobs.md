# Mobs - Technical Design

> **Zone:** Exploration · **Design:** [GDD/Exploration/Mobs](../../GDD/Exploration/Mobs.md) · **Related:** [Combat](../Common/Combat.md) · [Realms](Realms.md)

## Technical Specifications

- **Mob definition:** `MobDefinition` (SO): mob ID, prefab, category, archetype, max health, attack damage, telegraph/attack/recover timings, move speed, aggro radius, staggerable flag, drop table, provided material IDs.
- **Health & damage:** Uses the shared `Health` / `IDamageable` from [Combat](../Common/Combat.md). Mob attacks deal fixed `AttackDamage` from data.
- **AI:** Lightweight finite state machine per mob (`Idle → Chase/Reposition → Telegraph → Attack → Recover`), driven by archetype. Movement on a baked NavMesh per realm scene (`NavMeshAgent`).
- **Spawning:** `MobDirector` populates spawn zones on realm load, then runs wandering spawns driven by **Realm Pressure**.
- **Realm Pressure:** Integer level, +1 every 60 s of *occupied* time (paused while the realm is empty during the entry window). Each level shortens the wandering spawn interval (30 s − 5 s/level, min 8 s) and raises the alive cap (12 + 2/level, hard cap 20). From level 3, Outer zones may draw from the Deep group table. Pressure never resets within a realm instance.
- **Ambushers:** Spawned dormant next to nodes; wake on the node's first `OnStruck`.
- **Drops:** On death, roll the drop table with the realm RNG and spawn `WorldItem` pickups.
- **Performance:** AI ticks at 10 Hz (staggered across mobs); target ≤ 0.5 ms total AI cost at the 20-mob hard cap (high Realm Pressure).

---

## Architecture & Implementation Approaches

### Approach A: Data-Driven FSM with Archetype Strategies (Recommended)
- One `MobBrain` component; behaviour differences live in small `IMobArchetype` strategies (Chaser, Ranged, Swarm, Ambusher).
- **Pros:** New mobs are mostly data; archetypes are reusable across realms.

### Approach B: Behaviour Trees
- **Pros:** Expressive for complex bosses.
- **Cons:** Overkill for simple mobs; reserve for Apex Guardians if needed.

Approach A for regular mobs; Apex Guardians may use a dedicated phase controller or behaviour tree (decided when the first guardian is built).

---

## Networking

- AI runs only on the host. Mob transforms replicate at 10–20 Hz with interpolation; state changes (telegraph start, attack, death) replicate as events so clients play telegraphs on time.
- Hits on mobs are resolved by the host combat code.

---

## Unity C# Reference Code

```csharp
using System;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.AI;
using Armotheca.Core;
using Armotheca.Combat;

namespace Armotheca.Exploration
{
    public enum MobCategory { MinorFauna, ElementalBeast, ApexGuardian }
    public enum MobArchetype { Chaser, Ranged, Swarm, Ambusher }

    [CreateAssetMenu(menuName = "Armotheca/Exploration/Mob Definition")]
    public class MobDefinition : ScriptableObject
    {
        public string MobId;                    // "BrambleStalker"
        public MobBrain Prefab;
        public MobCategory Category;
        public MobArchetype Archetype;
        [Min(1)] public int MaxHealth = 30;
        [Min(0)] public int AttackDamage = 10;
        public float MoveSpeed = 3.5f;
        public float AggroRadius = 8f;
        public float AttackRange = 1.5f;
        public float TelegraphTime = 0.6f;
        public float AttackTime = 0.2f;
        public float RecoverTime = 0.8f;
        public bool Staggerable = true;
        public List<DropEntry> Drops = new();
        public List<string> ProvidesMaterialIds = new();
    }

    [Serializable]
    public struct MobGroupEntry
    {
        public MobDefinition Mob;
        public int MinCount;
        public int MaxCount;
        [Min(0f)] public float Weight;
    }

    [CreateAssetMenu(menuName = "Armotheca/Exploration/Mob Spawn Table")]
    public class MobSpawnTable : ScriptableObject
    {
        public List<MobGroupEntry> OuterGroups = new();
        public List<MobGroupEntry> DeepGroups = new();
        [Range(0f, 1f)] public float ActiveZoneFraction = 0.6f;

        [Header("Realm Pressure")]
        public float PressureLevelSeconds = 60f;     // occupied time per level
        public float BaseSpawnInterval = 30f;
        public float SpawnIntervalStepPerLevel = 5f;
        public float MinSpawnInterval = 8f;
        public int BaseMaxAlive = 12;
        public int MaxAlivePerLevel = 2;
        public int HardMaxAlive = 20;                // performance cap
        public int DeepInOuterFromLevel = 3;

        public float SpawnInterval(int level) => Mathf.Max(MinSpawnInterval, BaseSpawnInterval - SpawnIntervalStepPerLevel * level);
        public int MaxAlive(int level) => Mathf.Min(HardMaxAlive, BaseMaxAlive + MaxAlivePerLevel * level);
    }

    public class MobSpawnZone : MonoBehaviour
    {
        public RealmBand Band;
        public float Radius = 3f;

        public Vector3 RandomPoint(System.Random rng)
        {
            double a = rng.NextDouble() * Math.PI * 2, r = Math.Sqrt(rng.NextDouble()) * Radius;
            return transform.position + new Vector3((float)(Math.Cos(a) * r), 0f, (float)(Math.Sin(a) * r));
        }
    }

    /// <summary>Host-side population and Realm Pressure escalation for one realm instance.</summary>
    public class MobDirector : MonoBehaviour
    {
        private MobSpawnTable table;
        private List<MobSpawnZone> zones;
        private System.Random rng;
        private readonly List<MobBrain> alive = new();
        private float occupiedTime;
        private float spawnTimer;
        private bool occupied;

        public int PressureLevel { get; private set; }
        public event Action<int> OnPressureLevelChanged; // HUD distortion + audio cue

        public static MobDirector Create(MobSpawnTable table, List<MobSpawnZone> zones, System.Random rng, ISet<string> requiredMaterials)
        {
            var director = new GameObject("MobDirector").AddComponent<MobDirector>();
            director.table = table;
            director.zones = zones;
            director.rng = rng;
            director.InitialPopulate(requiredMaterials);
            return director;
        }

        public void SetOccupied(bool value) => occupied = value;

        private void InitialPopulate(ISet<string> required)
        {
            var missing = new HashSet<string>(required);
            foreach (var zone in zones)
            {
                if (zone.Band == RealmBand.Apex) continue;
                var groups = zone.Band == RealmBand.Outer ? table.OuterGroups : table.DeepGroups;

                var forced = groups.Find(g => g.Mob.ProvidesMaterialIds.Exists(missing.Contains));
                bool active = forced.Mob != null || rng.NextDouble() < table.ActiveZoneFraction;
                if (!active) continue;

                var group = forced.Mob != null ? forced : PickWeighted(groups);
                foreach (var id in group.Mob.ProvidesMaterialIds) missing.Remove(id);
                SpawnGroup(group, zone);
            }
        }

        private void Update()
        {
            alive.RemoveAll(m => m == null || !m.IsAlive);
            if (!occupied) return; // pressure and wandering spawns pause while the realm is empty

            float dt = Time.deltaTime;
            occupiedTime += dt;
            int level = Mathf.FloorToInt(occupiedTime / table.PressureLevelSeconds);
            if (level != PressureLevel)
            {
                PressureLevel = level;
                OnPressureLevelChanged?.Invoke(level);
            }

            spawnTimer += dt;
            if (spawnTimer < table.SpawnInterval(PressureLevel)) return;
            spawnTimer = 0f;

            if (alive.Count >= table.MaxAlive(PressureLevel)) return;
            var zone = zones[rng.Next(zones.Count)];
            if (zone.Band == RealmBand.Apex) return;

            bool deepAllowedOutside = PressureLevel >= table.DeepInOuterFromLevel && rng.NextDouble() < 0.5;
            var groups = zone.Band == RealmBand.Deep || deepAllowedOutside ? table.DeepGroups : table.OuterGroups;
            SpawnGroup(PickWeighted(groups), zone);
        }

        private void SpawnGroup(MobGroupEntry group, MobSpawnZone zone)
        {
            int count = rng.Next(group.MinCount, group.MaxCount + 1);
            int cap = table.MaxAlive(PressureLevel);
            for (int i = 0; i < count && alive.Count < cap; i++)
            {
                var mob = Instantiate(group.Mob.Prefab, zone.RandomPoint(rng), Quaternion.identity, zone.transform);
                mob.Initialize(group.Mob, rng);
                alive.Add(mob);
            }
        }

        private MobGroupEntry PickWeighted(List<MobGroupEntry> groups)
        {
            float total = 0f;
            foreach (var g in groups) total += g.Weight;
            double roll = rng.NextDouble() * total;
            foreach (var g in groups) { roll -= g.Weight; if (roll <= 0d) return g; }
            return groups[^1];
        }
    }

    /// <summary>Simple host-side mob FSM. Archetype-specific decisions live in Decide().</summary>
    [RequireComponent(typeof(NavMeshAgent), typeof(Health))]
    public class MobBrain : MonoBehaviour
    {
        private enum State { Idle, Chase, Telegraph, Attack, Recover, Dead }

        [SerializeField] private LayerMask playerMask;
        [SerializeField] private float thinkInterval = 0.1f;

        private MobDefinition def;
        private NavMeshAgent agent;
        private Health health;
        private System.Random rng;
        private State state;
        private float stateTime, thinkTimer;
        private Transform target;
        private readonly Collider[] buffer = new Collider[4];

        public bool IsAlive => state != State.Dead;
        public event Action<MobBrain> OnTelegraph;              // clients play wind-up VFX/SFX
        public event Action<Vector3, List<string>> OnDropsRolled;

        public void Initialize(MobDefinition definition, System.Random random)
        {
            def = definition;
            rng = random;
            agent = GetComponent<NavMeshAgent>();
            agent.speed = def.MoveSpeed;
            health = GetComponent<Health>();
            health.SetMax(def.MaxHealth);
            health.OnDepleted += Die;
            health.OnDamaged += OnDamaged;
            state = def.Archetype == MobArchetype.Ambusher ? State.Recover : State.Idle; // ambushers wait dormant
            thinkTimer = (float)rng.NextDouble() * thinkInterval; // stagger AI ticks
        }

        public void Wake() { if (state == State.Recover && target == null) Enter(State.Idle); }

        private void Update()
        {
            if (state == State.Dead) return;
            stateTime += Time.deltaTime;
            thinkTimer -= Time.deltaTime;
            if (thinkTimer <= 0f) { thinkTimer = thinkInterval; Decide(); }

            switch (state)
            {
                case State.Telegraph when stateTime >= def.TelegraphTime: Enter(State.Attack); break;
                case State.Attack when stateTime >= def.AttackTime: ResolveAttack(); Enter(State.Recover); break;
                case State.Recover when stateTime >= def.RecoverTime && def.Archetype != MobArchetype.Ambusher: Enter(State.Idle); break;
            }
        }

        private void Decide()
        {
            if (state is State.Telegraph or State.Attack or State.Recover) return;

            target = FindTarget();
            if (target == null) { Enter(State.Idle); agent.ResetPath(); return; }

            float dist = Vector3.Distance(transform.position, target.position);
            float desiredRange = def.Archetype == MobArchetype.Ranged ? def.AttackRange * 0.8f : def.AttackRange;

            if (dist <= desiredRange) { agent.ResetPath(); Enter(State.Telegraph); OnTelegraph?.Invoke(this); }
            else { agent.SetDestination(target.position); Enter(State.Chase); }
        }

        private Transform FindTarget()
        {
            int n = Physics.OverlapSphereNonAlloc(transform.position, def.AggroRadius, buffer, playerMask);
            Transform best = null; float bestDist = float.MaxValue;
            for (int i = 0; i < n; i++)
            {
                if (!buffer[i].TryGetComponent(out Health h) || !h.IsAlive) continue;
                float d = (buffer[i].transform.position - transform.position).sqrMagnitude;
                if (d < bestDist) { bestDist = d; best = buffer[i].transform; }
            }
            return best;
        }

        private void ResolveAttack()
        {
            // Melee archetypes: check range at the moment of impact (rolling out avoids the hit).
            // Ranged archetypes would launch a slow projectile here instead.
            if (target == null || !target.TryGetComponent(out IDamageable victim)) return;
            if (Vector3.Distance(transform.position, target.position) > def.AttackRange * 1.1f) return;
            Vector3 dir = (target.position - transform.position).normalized;
            victim.ApplyDamage(new DamageInfo(def.AttackDamage, target.position, dir, gameObject));
        }

        private void OnDamaged(DamageInfo info)
        {
            if (def.Archetype == MobArchetype.Ambusher && state == State.Recover && target == null) Wake();
            if (def.Staggerable && state == State.Telegraph) Enter(State.Recover); // sword hits interrupt small mobs
        }

        private void Die()
        {
            Enter(State.Dead);
            agent.enabled = false;
            var drops = new List<string>();
            DropRoller.Roll(def.Drops, rng, drops);
            OnDropsRolled?.Invoke(transform.position, drops); // spawner creates WorldItem pickups
            Destroy(gameObject, 1.5f); // allow death animation
        }

        private void Enter(State next) { state = next; stateTime = 0f; }
    }
}
```
