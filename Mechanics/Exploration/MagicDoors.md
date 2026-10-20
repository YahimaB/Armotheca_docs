# Magic Doors & Dimensional Exploration System

## Design Intent

The Magic Doors system serves as the resource lifeline for *Armotheca*. The shop does not rest upon ordinary geography; its cellar opens directly onto extradimensional tears in reality. Each door leads to a bite-sized, dangerous pocket dimension containing specialized raw materials. By combining **static resource nodes (ores, arcane trees)** with **hostile creature encounters (slimes, elemental beasts, golems)**, expeditions provide tactical variety and high-stakes teamwork while feeding raw inputs into the workshop.

---

## Player Experience Goals

- **Targeted Harvesting:** Teams pick specific doors based on active commission letters (e.g., *“We need a Frost Core and Iron Ore — open the Glacial Chasm!”*).
- **Punchy, Focused Sorties:** Expeditions last **2 to 4 minutes**, keeping the pace brisk and eliminating long downtime for players back in the workshop.
- **Combat & Gathering Synergy:** Foragers must protect their miners from aggressive fauna, turning every gathering run into a cooperative survival exercise.
- **Tension of the Return Portal:** Doors exhibit gradual dimensional instability; staying too long risks portal collapse and cargo drop.

---

## References (Specific Examples)

- **Moonlighter:** Running into procedurally populated dungeon rooms to loot materials for the morning shop open.
- **Deep Rock Galactic:** Cooperative class roles (mining mineral veins while fending off swarms of environmental horrors).
- **Lethal Company:** Quick, high-intensity extraction runs where inventory carry capacity and time limits force strategic prioritization.
- **Risk of Rain 2:** Dynamic teleporter events and escalating realm timers.

---

## Dimensional Realms & Resource Distribution

```
+--------------------------------------------------------------------------+
|                       DIMENSIONAL BIOME DIRECTORY                        |
+--------------------------------------------------------------------------+
| 1. PYROCLASTIC TRENCH | Nodes: Obsidian, Brimstone | Mobs: Fire Salamander|
| 2. VERDANT CORRUPTION | Nodes: Bog Oak, Ironwood   | Mobs: Bramble Stalker|
| 3. ASTRAL QUARRY      | Nodes: Quartz, Star Metal  | Mobs: Void Slimes    |
| 4. FROSTBITE CAVERN   | Nodes: Glacial Ice-Ore     | Mobs: Frost Wraiths  |
+--------------------------------------------------------------------------+
```

### Resource Acquisition Types

| Source Type | Gathering Method | Primary Yield | Used For |
|---|---|---|---|
| **Mineral Vein (Node)** | Pickaxe Mining (3–5 swings) | Ores, Crystals, Flux | Blades, Ingot Smelting |
| **Arcane Flora (Node)** | Lumber Axe (3–4 swings) | Heartwood, Ancient Bark | Hilts, Wand/Staff Shafts |
| **Minor Fauna (Mob)** | Basic Combat / Traps | Pelts, Claws, Fangs | Hilt Grips, Physical Traits |
| **Elemental Beasts (Mob)**| Tactical Magic/Melee Combat | Cores, Essences, Ichor | Wand & Staff Magical Cores |

---

## Pacing & Anti-Downtime Design

To solve the classic pitfall where workshop players wait with nothing to do while others crawl through dungeons:

1. **Strict 180-Second Instability Timer:**
   - When a door is opened, a dimensional tether countdown begins (180 seconds).
   - At 30 seconds remaining, the portal emits an audible warning chime inside the workshop and the dungeon.
   - Foragers must return through the portal before it snaps shut.
2. **Backpack Extraction Basket:**
   - Players inside the dungeon can toss harvested items into an *Aether Drop-Chute* near the entrance, immediately sending goods to the workshop floor in real time.
3. **Seamless Multi-Presence:**
   - Any player can walk through the door at will. If a fight turns dangerous, a workshop player can grab a sword and rush in as reinforcements.

---

## Technical Specifications

- **Instance Management:** Biomes are loaded additively in Unity or pre-allocated on separate physics layers.
- **Network Synchronization:** Portal transitions use seamless coordinate translation without hard loading screens.
- **Loot Drop Determinism:** Mob drops and node yields are synchronized across the network using network object spawning.

---

## Production-Ready C# Architecture

```csharp
using System;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

namespace Armotheca.Exploration
{
    public enum BiomeType
    {
        PyroclasticTrench,
        VerdantCorruption,
        AstralQuarry,
        FrostbiteCavern
    }

    [System.Serializable]
    public struct DropProbability
    {
        public string ItemID;
        [Range(0f, 1f)] public float Chance;
        public int MinQuantity;
        public int MaxQuantity;
    }

    /// <summary>
    /// Controls dimensional door state, portal stability timer, and transitions.
    /// </summary>
    public class DimensionalDoor : MonoBehaviour
    {
        [Header("Door Configuration")]
        [SerializeField] private BiomeType destinationBiome;
        [SerializeField] private float stabilityDuration = 180f; // 3 minutes
        [SerializeField] private Transform dungeonSpawnPoint;
        [SerializeField] private Transform shopReturnPoint;

        public bool IsOpen { get; private set; }
        public float RemainingStabilitySeconds { get; private set; }

        public event Action<BiomeType> OnPortalOpened;
        public event Action OnPortalDestabilized; // 30s warning
        public event Action OnPortalClosed;

        private Coroutine timerCoroutine;

        public void OpenDoor()
        {
            if (IsOpen) return;

            IsOpen = true;
            RemainingStabilitySeconds = stabilityDuration;
            OnPortalOpened?.Invoke(destinationBiome);

            timerCoroutine = StartCoroutine(PortalStabilityRoutine());
        }

        private IEnumerator PortalStabilityRoutine()
        {
            bool warningTriggered = false;

            while (RemainingStabilitySeconds > 0f)
            {
                RemainingStabilitySeconds -= Time.deltaTime;

                if (!warningTriggered && RemainingStabilitySeconds <= 30f)
                {
                    warningTriggered = true;
                    OnPortalDestabilized?.Invoke();
                }

                yield return null;
            }

            CloseDoor();
        }

        public void CloseDoor()
        {
            if (!IsOpen) return;

            IsOpen = false;
            RemainingStabilitySeconds = 0f;
            if (timerCoroutine != null) StopCoroutine(timerCoroutine);

            OnPortalClosed?.Invoke();
        }

        /// <summary>
        /// Teleports player entity into the pocket realm.
        /// </summary>
        public void TeleportToDungeon(Transform playerTransform)
        {
            if (!IsOpen) return;
            playerTransform.position = dungeonSpawnPoint.position;
        }

        /// <summary>
        /// Returns player entity back to the safety of the workshop.
        /// </summary>
        public void TeleportToShop(Transform playerTransform)
        {
            playerTransform.position = shopReturnPoint.position;
        }
    }

    /// <summary>
    /// Interactive resource node in dimensional dungeons (Ore vein, Ancient tree).
    /// </summary>
    public class ResourceNode : MonoBehaviour
    {
        [SerializeField] private string nodeName;
        [SerializeField] private int hitsRequired = 4;
        [SerializeField] private List<DropProbability> potentialDrops;
        [SerializeField] private GameObject breakVFX;

        private int currentHits = 0;

        public event Action<Vector3, List<string>> OnNodeHarvested;

        public bool HitNode(int damage = 1)
        {
            currentHits += damage;
            // Spawn hit dust/sound

            if (currentHits >= hitsRequired)
            {
                Harvest();
                return true;
            }

            return false;
        }

        private void Harvest()
        {
            List<string> droppedItems = new();
            foreach (var drop in potentialDrops)
            {
                if (UnityEngine.Random.value <= drop.Chance)
                {
                    int qty = UnityEngine.Random.Range(drop.MinQuantity, drop.MaxQuantity + 1);
                    for (int i = 0; i < qty; i++)
                    {
                        droppedItems.Add(drop.ItemID);
                    }
                }
            }

            if (breakVFX != null)
            {
                Instantiate(breakVFX, transform.position, Quaternion.identity);
            }

            OnNodeHarvested?.Invoke(transform.position, droppedItems);
            Destroy(gameObject);
        }
    }
}
```
