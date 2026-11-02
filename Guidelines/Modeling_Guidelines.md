# 3D Modeling Guidelines

> Requirements for 3D artists so that every model in *Armotheca* matches the same style, complexity and technical budget.
> **Visual references:** `Visual_Design/References/` (see §2) · **Naming:** [Assets Naming](Assets_Naming.md) · **Game context:** [Vision](../GDD/00_Overview/Vision.md) · **Tech stack:** [Technical Overview](../Technical_Design/Technical_Overview.md)

---

## 1. Target Look in One Paragraph

**Stylized, chunky, hand-crafted PBR.** Shapes are simplified and slightly exaggerated (thick planks, oversized rivets, heavy bevels), surfaces carry soft hand-painted color variation instead of photo noise, and lighting does the heavy lifting. No outlines, no cel shading. Everyday materials (wood, iron, stone, plaster) stay muted and warm; **magic is the only thing allowed to be saturated and glowing** (runes, cores, portals, potions). The workshop feels cozy and daylit; the realms behind the Magic Doors are darker and moodier, lit by strong colored accents.

---

## 2. Reference Breakdown

Two shipped games define the target. Use them for **complexity and style**, not for copying designs.

| Reference | Use it for | Do not take |
|---|---|---|
| **Alchemy Factory** | Workshop architecture, props, workstations, daylight palette, foliage, the portal frame | HUD/UI style (ours is defined in `GDD/05_UI`) |
| **Goblin Cleanup** | Realm (dungeon) environments, dark mood lighting, magical devices, creature/mob tone, character readability | First-person hands, gore decals, specific character costume designs |

Character style (Alchemy Factory's semi-realistic people vs Goblin Cleanup's more cartoony proportions) is still open — see §11.

### Per-image notes

| Image | What to study |
|---|---|
| [AF_1](../Visual_Design/References/Alchemy_Factory/AF_1.jpg) | Interior scale of the workshop: timber frame with large chamfered beams, plaster walls with soft painted variation, herringbone floor. Props stay simple; detail lives in silhouette and bevels. |
| [AF_2](../Visual_Design/References/Alchemy_Factory/AF_2.jpg) | Foliage complexity: simple leaf shapes, berry clusters as a few spheres. Stone border blocks are chunky, irregular and heavily beveled — the target for all stone. |
| [AF_3](../Visual_Design/References/Alchemy_Factory/AF_3.jpg) | Mechanical props: pipes, stone planters, glowing flasks used as emissive accents. Shows how repeated props must stay cheap because they are instanced many times. |
| [AF_4](../Visual_Design/References/Alchemy_Factory/AF_4.jpg) | **Magic Door reference.** Stone arch with iron bands and glowing runes, ornament carved into a single panel, portal surface handled by VFX. Also: roof tiles and town buildings for silhouette density. |
| [AF_5](../Visual_Design/References/Alchemy_Factory/AF_5.jpg) | **The prop detail benchmark.** Barrels, mugs and crate: thick staves, iron bands with oversized rivets, brass tap, rope. Every edge beveled; wood grain lives in the normal map and albedo, not in geometry. |
| [GC_1](../Visual_Design/References/Goblin_Cleanup/GC_1.jpg) | Character readability: strong color blocking per character, clear silhouettes at distance. Hero magical device (gold rings + glowing orb) as the visual centerpiece of a room. |
| [GC_2](../Visual_Design/References/Goblin_Cleanup/GC_2.jpg) | Prop density in an interior hub: clutter that reads as cozy without hurting readability; emissive candles as light accents. |
| [GC_3](../Visual_Design/References/Goblin_Cleanup/GC_3.png) | **Realm environment reference.** Gothic stone corridors, chunky blocks, cracks in the normal map, teal/orange accent lighting, coffins and skeletons as themed set dressing. |
| [GC_4](../Visual_Design/References/Goblin_Cleanup/GC_4.png) | **Mob tone reference.** The mimic chest: exaggerated, slightly comedic creature design built from a recognizable object. Modular stone walls and arches. |

---

## 3. Shape Language

1. **Silhouette first.** Every model must be recognizable as a flat black shape from the gameplay camera (third person, roughly 4–8 m away).
2. **Chunky proportions.** Make things 20–40% thicker than real life: planks, beams, iron bands, handles, rims. Thin parts disappear at gameplay distance.
3. **No sharp edges.** Every hard edge gets a visible bevel/chamfer. Rule of thumb: bevel width ≈ 5–10% of the smaller dimension of the part (a 10 cm beam gets a 0.5–1 cm chamfer, 1–2 segments).
4. **Hand-made imperfection.** Slight warps, uneven plank lengths, stones that are not perfect boxes, edges that lean a few degrees. Avoid CAD-perfect symmetry on environment and props (weapons and stations may be more regular).
5. **Oversized key details.** Rivets, bolts, hinges, knots and runes are larger and fewer than in reality.
6. **Simplify the rest.** If a detail does not change the silhouette, it belongs in the normal map or the albedo, not in geometry.

### What goes where

| Detail | Geometry | Normal map | Albedo paint |
|---|---|---|---|
| Overall form, bevels, large ornaments | ✅ | | |
| Rivets / bolts on hero objects and workstations | ✅ | | |
| Rivets / bolts on small or repeated props | | ✅ | |
| Wood grain, plank seams on one surface, stone chips, cracks | | ✅ | ✅ (soft) |
| Wear, dirt, edge highlights, color variation | | | ✅ |
| Runes and magical glyphs | ✅ or ✅ normal | | ✅ + emission mask |

---

## 4. Polygon Budgets (LOD0)

Triangle counts are for the final in-engine mesh (triangulated), LOD0. These are **initial targets**; they will be confirmed by a performance test in Phase 1 against the 60 FPS targets (GTX 1660 desktop, Steam Deck).

| Category | Examples | LOD0 triangles |
|---|---|---|
| **Player character** (body + clothes + hair) | The 4 playable artisans | 20,000 – 30,000 |
| **Minor mob** | Bramble Stalker, Void Slime | 5,000 – 10,000 |
| **Elemental beast** | Fire Salamander, Frost Wraith | 10,000 – 18,000 |
| **Apex Guardian** | Frost Wyrm, Verdant Elder | 30,000 – 50,000 |
| **Weapon component** | Hilt, Blade, Short/Long Shaft, Core | 500 – 1,500 each |
| **Small prop / carried item** | Ore chunk, ingot, mug, bottle, letter, tools | 200 – 1,200 |
| **Medium prop** | Barrel, crate, bucket, chair, sack | 800 – 3,000 |
| **Large prop / furniture** | Shelf, table, counter, wardrobe | 2,000 – 6,000 |
| **Workstation** (hero, interactive) | Forge + bellows, anvil, lathe, assembly bench, extractor | 6,000 – 15,000 |
| **Magic Door** (frame) | Threshold of Portals doors, realm Exit Portal | 8,000 – 15,000 |
| **Great Crucible** (endgame centerpiece) | Uber-Weapon forge | 20,000 – 35,000 |
| **Resource node** (per state) | Ore vein, arcane tree, crystal cluster | 2,000 – 6,000 |
| **Modular architecture piece** | Wall 2 m / 4 m, floor tile, beam, arch, stairs | 300 – 2,500 |
| **Foliage** | Grass clump / bush / tree | 50 – 300 / 1,000 – 4,000 / 5,000 – 12,000 |

### Scene budgets (for level art and lighting)

|                     | Desktop (1080p)                      | Steam Deck |
| ------------------- | ------------------------------------ | ---------- |
| Visible triangles   | ≤ 1,500,000                          | ≤ 800,000  |
| Draw calls          | ≤ 1,000                              | ≤ 600      |
| Materials per frame | Keep low via trim sheets and atlases |            |

---

## 5. LODs

| Category | LOD0 | LOD1 | LOD2 | Cull |
|---|---|---|---|---|
| Characters, mobs, Apex Guardians | 100% | 50% | 25% | ~3% screen size |
| Workstations, doors, large props | 100% | 50% | 25% | ~2% |
| Medium props, nodes, architecture pieces | 100% | 50% | — | ~2% |
| Small props, weapon components | 100% | — | — | ~1% |

- LODs must keep the silhouette; remove bevels and interior loops first.
- Name LODs `_LOD0`, `_LOD1`, `_LOD2` inside the FBX so Unity builds the LOD Group automatically.

---

## 6. Textures & Materials

The project targets **URP with the standard Lit shader (metallic workflow)**; stylization comes from the painted textures and lighting, not from a toon shader. *(Render pipeline to be confirmed in the Technical Overview before production.)*

### Texel density

| Asset type | Texel density |
|---|---|
| Environment, architecture, props, workstations | 512 px/m (5.12 px/cm) |
| Player characters, mobs | 1024 px/m |
| Weapon components and carried items (seen up close in hands and on the bench) | 1024 px/m |

### Texture sets

| Map | Content | Suffix |
|---|---|---|
| Base Color | Hand-painted albedo, soft gradients, subtle edge wear. No baked hard shadows. | `_BC` |
| Normal | OpenGL format (Y+), as Unity expects | `_N` |
| Metallic / Smoothness | Metallic in R, Smoothness in A | `_MS` |
| Ambient Occlusion | Grayscale | `_AO` |
| Emission (only when needed) | Runes, cores, flasks, portals | `_E` |

### Resolutions

| Asset | Max texture size |
|---|---|
| Small prop | 512 |
| Medium prop, weapon component | 1024 |
| Large prop, workstation, door, node | 2048 |
| Character / mob | 2048 (body) + 1024 (head/face if separate) |
| Apex Guardian | 2 × 2048 |
| Tileable / trim sheet | 1024 – 2048 |

### Materials and reuse

- **Max 2 materials per prop/workstation, 3 per character.**
- Use **shared trim sheets and tileables** for wood planks, iron bands, stone blocks, plaster and roof tiles (as in AF_1, AF_5). Unique textures are for hero objects only.
- Static environment meshes need a **second UV channel (UV1) for lightmaps**: non-overlapping, ~8 px padding at 1024.

### Palette rules

- **Mundane materials:** muted and warm (honey/grey wood, blue-grey iron, cool grey stone, cream plaster). Smoothness mostly low (matte look).
- **Magic and elements:** the only saturated colors, always with emission. Element colors must match the UI:

| Element | Color |
|---|---|
| Physical | Neutral steel |
| Fire | Orange-red |
| Frost | Cyan |
| Lightning | Yellow |
| Arcane | Purple-magenta |
| Holy | Warm gold-white |

---

## 7. Scale, Pivots & Export

- **Units:** 1 unit = 1 m. Model at real scale, then apply the chunky exaggeration from §3.
- **Reference heights:** player character ~1.8 m; workstation working surface 0.9–1.0 m (waist height, so items on it stay visible); doorways at least 1.4 m wide × 2.4 m tall (players carry items and pass side by side).
- **Pivots:**
  - Props and furniture: bottom center.
  - Doors and portals: bottom center of the threshold.
  - Weapon components: at the connection point (see §8).
  - Carried items: at the grip point.
- **Export:** FBX, Y-up in Unity, transforms applied (scale 1, rotation 0), triangulated or with clean quads; no n-gons, no zero-area faces, no flipped normals.
- **Smoothing:** use hard edges at UV seams and weighted/custom normals on beveled hard-surface parts so bevels shade cleanly with few segments.

---

## 8. Asset-Specific Rules

### Modular weapons (critical for gameplay)

Weapons are assembled in game from **exactly two parts** (see [Weapon Crafting](../GDD/02_Systems/Crafting/_Crafting_System.md)), so every part must fit every compatible counterpart.

| Weapon | Foundation | Payload | Total length |
|---|---|---|---|
| Sword | Hilt | Blade | 1.0 – 1.2 m |
| Wand | Short Shaft | Core | 0.35 – 0.45 m |
| Staff | Long Shaft | Core | 1.6 – 1.8 m |

- Every foundation contains an empty/locator named **`Socket_Payload`** at the connection point, Y axis pointing along the weapon.
- Every payload has its **pivot at its own connection point**, oriented the same way, so it snaps onto `Socket_Payload` without offsets.
- Connection areas use a **standard connector size** per weapon type (a hilt collar and blade tang that match across all materials; a shaft tip and core cradle that match across all materials).
- The material of the part must read from color and silhouette alone (iron vs star metal blade, oak vs bog-wood shaft). Element shows through the emissive core or blade accents.
- Quality tiers are **not modeled**; the Flawless glow is a VFX added by code.

### Workstations

- Hero objects: highest detail in the workshop, unique silhouette per station so players identify them across the room.
- Model **sockets and interaction points as named empties** (`Socket_Input`, `Socket_Output`, `Interact_Point`) for the interaction system.
- Moving parts (bellows, lathe chuck, mallet, valves) are **separate objects** named `Part_<Name>` with their own pivots so they can be animated.

### Resource nodes

- Each node needs **3 states**: intact, damaged (after first hits), broken/depleted — or intact + broken with damage handled by VFX. Same pivot for all states.
- Node material must be readable from far away by color: each ore/wood/crystal type gets a distinct hue consistent with its element.

### Magic Doors

- Frame only; the portal surface, swirl and runes animation are VFX/shader work (see AF_4).
- Runes get an emission mask so the door can light up per state (Locked / Ready / Entry Open / In Progress — see [Magic Doors](../GDD/02_Systems/Exploration/_Exploration_System.md)).
- Leave space on the frame for a **price plaque** (worldspace UI) and for the names of expedition members.

### Characters and mobs

- **Player characters:** stylized proportions with clear color blocking so 4 players are distinguishable at a glance (GC_1). Hands slightly oversized to read when holding items.
- **Rigging:** player characters use a Unity **Humanoid**-compatible skeleton (shared animations); ≤ 75 bones excluding face; max **4 bone influences per vertex**.
- **Mobs:** generic rigs allowed; attack telegraphs need readable body motion, so give mobs clear "wind-up" parts (jaws, tails, claws).
- **Apex Guardians:** may exceed bone limits (≤ 120 bones) — agree per guardian.

---

## 9. Naming Conventions

All asset, folder and in-model object names follow **[Assets Structure & Naming](Assets_Naming.md)**. The most common ones for 3D work:

| Type | Example |
|---|---|
| Static mesh | `SM_Shop_AssemblyBench` |
| Skeletal mesh | `SK_Mob_BrambleStalker` |
| Weapon component | `SM_Weapon_Blade_StarMetal` |
| Texture | `T_Shop_AssemblyBench_BC` (`_BC`, `_N`, `_MS`, `_AO`, `_E`) |
| Trim sheet | `T_Trim_WoodPlanks_N` |
| Material | `M_Shop_AssemblyBench` |
| Inside the FBX | `_LOD0..2`, `Socket_Payload`, `Interact_Point`, `COL_<Name>`, `Part_<Name>` |

Deliver files into `Assets/_Project/Art/<Zone>/...` as described in the naming guide (one folder per asset). Source files (`.blend`, `.spp`, `.psd`) stay outside `Assets/`.

---

## 10. Delivery Checklist

- [ ] Triangle count within the category budget (§4)
- [ ] Silhouette readable from 6–8 m; bevels on all hard edges
- [ ] LODs present and named per §5
- [ ] Texel density within ±20% of target (§6); maps named with correct suffixes
- [ ] ≤ 2 materials (≤ 3 for characters); trim sheets used where possible
- [ ] UV1 lightmap channel for static environment meshes
- [ ] Real-world scale, pivot per §7, transforms applied
- [ ] Required sockets/empties present (weapons, workstations)
- [ ] Moving parts separated (workstations, doors)
- [ ] Turntable render + one in-engine screenshot next to a reference image

---

## 11. Open Questions

- Render pipeline: confirm URP (assumed here) in the Technical Overview.
- Camera: final third-person distance and angle affect detail budgets; revisit §3–§4 once the camera is locked in the prototype.
- Character style: closer to Alchemy Factory's semi-realistic people or Goblin Cleanup's more cartoony proportions? Lock this with a character style test.
