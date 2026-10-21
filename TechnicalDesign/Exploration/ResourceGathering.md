# Resource Spawning & Gathering - Technical Design

> **Zone:** Exploration · **Design:** [GDD/Exploration/ResourceGathering](../../GDD/Exploration/ResourceGathering.md) · **Related:** [Realms](Realms.md) · [Object Interaction](../Common/ObjectInteraction.md)

## Technical Specifications

- **Node definition:** `ResourceNodeDefinition` (SO): node ID, prefab, hits required, strike interval, drop table, rare variant drop table, tool animation type (Pickaxe / Axe).
- **Spawn tables:** `NodeSpawnTable` per realm with per-band active fraction and weighted node entries.
- **Harvesting:** `ResourceNode` implements `IContinuousInteractable` with `MaxHelpers = 2`. While held, each helper lands a strike every `strikeInterval` seconds (initial 0.6 s); each strike = 1 hit.
- **Drops:** Rolled with `DropRoller` (see [Technical Overview](../TechnicalOverview.md)) using the realm seed's RNG; spawned as `WorldItem` pickups with a small scatter. Walking over a pickup auto-adds it to the harvester's backpack if there is room.
- **No respawn** within a realm instance.
- **Performance:** ≤ 40 nodes per realm; nodes are static colliders, no per-frame update unless being harvested.

---

## Architecture & Implementation Approaches

### Approach A: Hit-Count Nodes on Continuous Interaction (Recommended)
- Harvest is a hold interaction that emits discrete strikes; reuses interaction prompts, interruption and helper limits.
- **Pros:** One input model for all world objects; strikes give crunchy per-hit feedback.

### Approach B: Nodes Damaged by Weapon Hits (combat system)
- **Cons:** Couples gathering to the equipped weapon and combat hit detection; mixes two concerns. Kept as an open design question.

---

## Networking

- Host owns node hit counts and spawning; clients receive `OnStruck(hitIndex)` events for VFX/SFX and a `Harvested` event.
- Drops are host-spawned network objects; backpack additions are host-validated.

---

## Unity C# Reference Code

```csharp
using System;
using System.Collections.Generic;
using UnityEngine;
using Armotheca.Core;
using Armotheca.Interaction;

namespace Armotheca.Exploration
{
    public enum HarvestTool { Pickaxe, Axe }

    [CreateAssetMenu(menuName = "Armotheca/Exploration/Resource Node")]
    public class ResourceNodeDefinition : ScriptableObject
    {
        public string NodeId;                       // "IronVein"
        public string DisplayName;
        public ResourceNode Prefab;
        public HarvestTool Tool;
        [Min(1)] public int HitsRequired = 4;
        public float StrikeInterval = 0.6f;
        public List<DropEntry> Drops = new();
        public List<DropEntry> RareVariantDrops = new();
        public List<string> ProvidesMaterialIds = new(); // for letter guarantees
    }

    [Serializable]
    public struct WeightedNode
    {
        public ResourceNodeDefinition Node;
        [Min(0f)] public float Weight;
    }

    [Serializable]
    public class BandNodeTable
    {
        public RealmBand Band;
        [Range(0f, 1f)] public float MinActiveFraction = 0.6f;
        [Range(0f, 1f)] public float MaxActiveFraction = 0.8f;
        public List<WeightedNode> Entries = new();

        public ResourceNodeDefinition Pick(System.Random rng)
        {
            float total = 0f;
            foreach (var e in Entries) total += e.Weight;
            double roll = rng.NextDouble() * total;
            foreach (var e in Entries)
            {
                roll -= e.Weight;
                if (roll <= 0d) return e.Node;
            }
            return Entries[^1].Node;
        }
    }

    [CreateAssetMenu(menuName = "Armotheca/Exploration/Node Spawn Table")]
    public class NodeSpawnTable : ScriptableObject
    {
        public List<BandNodeTable> Bands = new();
        [Range(0f, 1f)] public float RareVariantChance = 0.1f;
    }

    public class NodeSpawnPoint : MonoBehaviour
    {
        public RealmBand Band;
    }

    public static class NodePopulator
    {
        public static void Populate(NodeSpawnTable table, List<NodeSpawnPoint> points, System.Random rng, ISet<string> requiredMaterials)
        {
            var spawned = new List<ResourceNodeDefinition>();

            foreach (var band in table.Bands)
            {
                var bandPoints = points.FindAll(p => p.Band == band.Band);
                Shuffle(bandPoints, rng);

                float fraction = Mathf.Lerp(band.MinActiveFraction, band.MaxActiveFraction, (float)rng.NextDouble());
                int activeCount = Mathf.RoundToInt(bandPoints.Count * fraction);

                for (int i = 0; i < activeCount; i++)
                {
                    var def = ForceRequiredIfMissing(band, requiredMaterials, spawned) ?? band.Pick(rng);
                    Spawn(def, bandPoints[i], rng.NextDouble() < table.RareVariantChance);
                    spawned.Add(def);
                }
            }
        }

        /// <summary>Returns a node providing a still-missing required material, if this band can supply one.</summary>
        private static ResourceNodeDefinition ForceRequiredIfMissing(BandNodeTable band, ISet<string> required, List<ResourceNodeDefinition> spawned)
        {
            foreach (var materialId in required)
            {
                if (spawned.Exists(n => n.ProvidesMaterialIds.Contains(materialId))) continue;
                var candidate = band.Entries.Find(e => e.Node.ProvidesMaterialIds.Contains(materialId));
                if (candidate.Node != null) return candidate.Node;
            }
            return null;
        }

        private static void Spawn(ResourceNodeDefinition def, NodeSpawnPoint point, bool rare)
        {
            var node = UnityEngine.Object.Instantiate(def.Prefab, point.transform.position, point.transform.rotation, point.transform);
            node.Initialize(def, rare);
        }

        private static void Shuffle<T>(IList<T> list, System.Random rng)
        {
            for (int i = list.Count - 1; i > 0; i--)
            {
                int j = rng.Next(i + 1);
                (list[i], list[j]) = (list[j], list[i]);
            }
        }
    }

    /// <summary>Harvestable node: continuous interaction producing discrete strikes.</summary>
    public class ResourceNode : MonoBehaviour, IContinuousInteractable
    {
        private ResourceNodeDefinition definition;
        private bool isRare;
        private bool isHarvested;
        private int hitsTaken;
        private readonly Dictionary<PlayerCarrier, float> strikeTimers = new();

        public Transform Transform => transform;
        public int MaxHelpers => 2;
        public float Progress01 => definition == null ? 0f : (float)hitsTaken / definition.HitsRequired;

        public event Action<int> OnStruck;                 // hit index, for VFX/SFX
        public event Action<Vector3, List<string>> OnHarvested;

        public static System.Random DropRng = new();       // replaced by the realm-seeded RNG on the host

        public void Initialize(ResourceNodeDefinition def, bool rare)
        {
            definition = def;
            isRare = rare;
            hitsTaken = 0;
        }

        public bool TryGetPrompt(PlayerCarrier player, out InteractionPrompt prompt)
        {
            string verb = definition.Tool == HarvestTool.Pickaxe ? "Mine" : "Chop";
            prompt = new InteractionPrompt(InteractionKind.Continuous, verb, definition.DisplayName,
                                           player.HandsEmpty ? null : "Hands full");
            return true;
        }

        public bool CanBeginContinuous(PlayerCarrier player) =>
            !isHarvested && player.HandsEmpty && (strikeTimers.ContainsKey(player) || strikeTimers.Count < MaxHelpers);

        public void BeginContinuous(PlayerCarrier player) => strikeTimers[player] = 0f;

        public void TickContinuous(PlayerCarrier player, float deltaTime)
        {
            if (!strikeTimers.TryGetValue(player, out float t)) return;

            t += deltaTime;
            if (t >= definition.StrikeInterval)
            {
                t -= definition.StrikeInterval;
                Strike();
                if (isHarvested) return; // Destroy is deferred to end of frame
            }
            strikeTimers[player] = t;
        }

        public void EndContinuous(PlayerCarrier player, bool completed) => strikeTimers.Remove(player);

        private void Strike()
        {
            hitsTaken++;
            OnStruck?.Invoke(hitsTaken);
            if (hitsTaken >= definition.HitsRequired) Harvest();
        }

        private void Harvest()
        {
            isHarvested = true;
            var drops = new List<string>();
            DropRoller.Roll(definition.Drops, DropRng, drops);
            if (isRare) DropRoller.Roll(definition.RareVariantDrops, DropRng, drops);

            OnHarvested?.Invoke(transform.position, drops); // spawner creates WorldItem pickups

            foreach (var player in strikeTimers.Keys) player.Interactor.NotifyContinuousEnded(this, true);
            strikeTimers.Clear();
            Destroy(gameObject);
        }
    }
}
```
