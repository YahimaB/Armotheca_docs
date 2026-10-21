# Realms - Technical Design

> **Zone:** Exploration · **Design:** [GDD/Exploration/Realms](../../GDD/Exploration/Realms.md) · **Related:** [Magic Doors](MagicDoors.md) · [Resource Gathering](ResourceGathering.md) · [Mobs](Mobs.md)

## Technical Specifications

- **One scene per realm layout** (`Realm_VerdantCorruption`, ...), authored by hand with tagged anchors: Entry anchor, Exit Portal, Aether Chute, node spawn points, mob spawn zones, Apex Arena gate.
- **Lifetime:** Loaded when its door opens, unloaded when the door ends the expedition (realm empty after the entry window). There is no realm timer.
- **Occupancy:** `RealmInstance.SetOccupied` is called by the door whenever the realm goes from empty to occupied and back; Realm Pressure only advances while occupied (see [Mobs](Mobs.md)).
- **Bands:** Every spawn point/zone is tagged `Outer`, `Deep` or `Apex`.
- **Population:** On load, the host populates nodes and mobs from the realm's spawn tables with a seed generated per opening (`RealmSeed`), so results are reproducible for debugging and replays.
- **Letter guarantees:** The populator receives the set of materials required by active letters and forces at least one matching node / mob group if this realm can supply it.
- **Isolation:** Realms are positioned far from the workshop origin (or in their own physics scene) so physics queries and audio never leak between spaces.

---

## Architecture & Implementation Approaches

### Approach A: Additive Scene Loading Placed at Remote Offsets (Recommended)
- `SceneManager.LoadSceneAsync(realm, LoadSceneMode.Additive)`, root moved to a unique world offset per door slot.
- **Pros:** Simple, matches FishNet's additive scene loading, lighting baked per scene.
- **Cons:** Load hitch must be hidden by the door-opening animation; precision fine within ±10 km.

### Approach B: Separate Physics Scenes (`LocalPhysicsMode.Physics3D`)
- **Pros:** Total physics isolation, no offsets needed.
- **Cons:** Every physics query must target the right scene; more complexity in combat/interaction code.

### Approach C: Pre-loaded Realms
- All realms kept loaded and toggled.
- **Cons:** Memory cost grows with every realm; only viable for the Phase 1 prototype.

Approach A is chosen for production; Approach C is acceptable for the Phase 1 single-realm prototype.

---

## Networking

- Realm scenes are loaded on the host and, per connection, on clients that enter, using FishNet's `SceneManager` (additive). Clients that never enter a realm do not load it, saving memory on non-hosts.
- A scene observer condition limits replication of realm objects (nodes, mobs, drops) to connections inside that realm, so players in the workshop do not receive realm traffic.
- The realm root offset is applied identically on every machine that loads the scene.
- Populated nodes and mobs are host-spawned network objects; only the seed and the guarantee list need to be logged for debugging.

---

## Unity C# Reference Code

> The sample uses Unity's `SceneManager` for brevity. In production, the host loads realms through FishNet's `SceneManager` (`LoadConnectionScenes` for the connections entering the realm, `UnloadConnectionScenes` when the expedition ends), and population runs only on the host.

```csharp
using System;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;
using Armotheca.Core;

namespace Armotheca.Exploration
{
    public enum RealmBand { Outer, Deep, Apex }

    [CreateAssetMenu(menuName = "Armotheca/Exploration/Realm Definition")]
    public class RealmDefinition : ScriptableObject
    {
        public string RealmId;                 // "VerdantCorruption"
        public string DisplayName;
        public string SceneName;
        public ElementType[] MainElements;
        public NodeSpawnTable NodeTable;       // see Resource Gathering
        public MobSpawnTable MobTable;         // see Mobs
        public string ApexGuardianId;
        public string CatalystId;
    }

    /// <summary>Placed in each realm scene; collects anchors for the populator.</summary>
    public class RealmLayout : MonoBehaviour
    {
        public Transform EntryAnchor;
        public ExitPortal ExitPortal;
        public AetherDropChute DropChute;
        public List<NodeSpawnPoint> NodeSpawnPoints = new();
        public List<MobSpawnZone> MobSpawnZones = new();
    }

    public class RealmInstance
    {
        public RealmDefinition Definition { get; }
        public RealmLayout Layout { get; }
        public Scene Scene { get; }
        public int Seed { get; }
        public Transform EntryAnchor => Layout.EntryAnchor;
        public ExitPortal ExitPortal => Layout.ExitPortal;
        public MobDirector Mobs { get; set; }
        public bool IsOccupied { get; private set; }

        public RealmInstance(RealmDefinition definition, RealmLayout layout, Scene scene, int seed)
        {
            Definition = definition;
            Layout = layout;
            Scene = scene;
            Seed = seed;
        }

        public void SetOccupied(bool occupied)
        {
            IsOccupied = occupied;
            Mobs?.SetOccupied(occupied); // Realm Pressure pauses while nobody is inside
        }
    }

    public class RealmInstanceService : MonoBehaviour
    {
        [SerializeField] private Vector3 slotSpacing = new(5000f, 0f, 0f);
        [SerializeField] private ActiveLetterRequirements letterRequirements; // provided by the Order System

        private int nextSlot = 1;

        public void Load(RealmDefinition realm, Action<RealmInstance> onReady)
        {
            var op = SceneManager.LoadSceneAsync(realm.SceneName, LoadSceneMode.Additive);
            Vector3 offset = slotSpacing * nextSlot++;

            op.completed += _ =>
            {
                Scene scene = SceneManager.GetSceneByName(realm.SceneName);
                RealmLayout layout = null;
                foreach (var root in scene.GetRootGameObjects())
                {
                    root.transform.position += offset;
                    layout ??= root.GetComponentInChildren<RealmLayout>();
                }

                int seed = Environment.TickCount;
                var instance = new RealmInstance(realm, layout, scene, seed);
                var rng = new System.Random(seed);
                var required = letterRequirements.GetRequiredMaterialIds();

                NodePopulator.Populate(realm.NodeTable, layout.NodeSpawnPoints, rng, required);
                instance.Mobs = MobDirector.Create(realm.MobTable, layout.MobSpawnZones, rng, required);

                onReady(instance);
            };
        }

        public void Unload(RealmInstance instance)
        {
            if (instance == null) return;
            if (instance.Mobs != null) Destroy(instance.Mobs.gameObject); // director lives outside the realm scene
            SceneManager.UnloadSceneAsync(instance.Scene);
        }
    }

    /// <summary>Thin adapter over the Order System listing material IDs required by active letters.</summary>
    public abstract class ActiveLetterRequirements : MonoBehaviour
    {
        public abstract ISet<string> GetRequiredMaterialIds();
    }
}
```

> Note: loading the same realm scene twice (two doors to the same realm) requires unique scene instances; with additive loading this is supported, but `GetSceneByName` must be replaced by tracking the scene from the load handle (`SceneManager.GetSceneAt(SceneManager.sceneCount - 1)`, or FishNet's scene-loaded event, which reports the loaded scene handles).
