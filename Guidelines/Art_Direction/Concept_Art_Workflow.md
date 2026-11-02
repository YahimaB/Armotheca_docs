# Concept Art Workflow

> How every contributor generates concept art for an entity, from a free-pose concept to the orthographic views a 3D artist models from, and where the results are recorded.
> **Style:** [3D Modeling Guidelines](../Modeling_Guidelines.md) §1, §3, §6, §8 · **References:** `Art_Direction/References/` · **Example:** [Player_Art](../../GDD/03_Entities/Player/Player_Art.md)

## 1. Stages

Three stages, used in order. Each stage passes its approved result to the next one as reference image 1.

1. **[Concept](#3-concept)**: one image of the entity, free pose. Iterate on this until the look is approved.
2. **[T-Pose](#4-t-pose)**: the approved concept set into a T-pose, front view.
3. **[Views](#5-views)**: the T-pose image as four separate orthographic images (front, back, right, left) for the 3D artist.

Tools:

- Concept: `Gemini` {Argon -> Medium}.
- T-Pose: the concept art is fed to `Tripo3D` {Generate Image -> T-Pose -> Nano Banana Pro}.

## 2. Recording Results

- Every image that is kept goes into the History of the entity's Art doc (`E_<Name>_Art.md`, or `Player_Art.md`) with its image, AI model and prompt; rejected variants are not recorded.
- The concept prompt is written for each entity and lives only in that History. The T-Pose and Views prompts below are templates: an entity's History records the prompt as actually sent.

## 3. Concept

### Settings

| Parameter | Value |
|---|---|
| Aspect ratio | 3:4 (portrait, full body) |
| Resolution | 2K for exploration, highest available for the final pick |
| Variants | 4 per pass |
| Reference images | None for the first pass; pass the best result back when refining |

### Prompt

Write the prompt in plain paragraphs, in this order: subject, pose and background; face; each clothing or body part in its own paragraph; proportions; style; lighting; exclusions (`No text, no labels, no watermark, no logos, no frame or border.`). See [Player_Art › 01 Male](../../GDD/03_Entities/Player/Player_Art.md#01-male).

## 4. T-Pose

Use only after the concept is approved. Pass the approved concept image as **reference image 1** with reference fidelity set to high.

### Settings

| Parameter        | Value                                           |
| ---------------- | ----------------------------------------------- |
| Aspect ratio     | 1:1 (arm span is about equal to height)         |
| Resolution       | Highest available (2K / 4K)                     |
| Variants         | 4 for the first pass, then 1 when refining      |
| Reference images | Reference image 1 = approved concept (required) |

### Prompt

```
Reference image 1 is the approved concept of the character. Show exactly this character, with the same hood, cape, coat, belt, tools, hands, boots, colors, proportions and style, now standing in a clean rigging T-pose.

Front view, full body, centered, fully visible from the top of the hood to the soles of the boots. Arms extended straight out to the sides at shoulder height, perfectly horizontal, elbows straight, palms facing down, fingers straight and slightly apart. Both hands are open and empty; all tools hang from the belt. Legs straight, feet shoulder-width apart and pointing forward. Head level, facing straight ahead.

Soft, even, neutral studio light with a faint contact shadow under the boots; the inside of the hood stays in complete darkness. Seamless pure white background. A single figure. No text, no labels, no watermark.
```

## 5. Views

Use only after the T-pose is approved. Pass the approved T-pose image as **reference image 1** with reference fidelity set to high.

### Settings

| Parameter        | Value                                           |
| ---------------- | ----------------------------------------------- |
| Aspect ratio     | 1:1 (same as the T-pose image)                  |
| Resolution       | Highest available (2K / 4K)                     |
| Variants         | 1                                               |
| Reference images | Reference image 1 = approved T-pose (required)  |

### Prompt

```
Reference image 1 shows the character in a T-pose. Create four separate images of exactly this character in exactly this pose, one image per view: front, back, right side and left side.

Each image is an orthographic view with the same scale and camera height, the full figure centered and visible from the top of the hood to the soles of the boots. The side views are true 90-degree profiles. Outfit, colors, proportions and lighting stay identical in all four images. The inside of the hood stays in complete darkness: in the side views the eyes show only as a soft glow at the edge of the hood, and the back view shows only the back of the hood.

Soft, even, neutral studio light, seamless pure white background, a single figure per image. No text, no labels, no watermark.
```

If the model returns one combined sheet or fewer than four images, run the prompt once per view and replace the first paragraph with `Reference image 1 shows the character in a T-pose. Create one image of exactly this character in exactly this pose, seen from the [back / right side / left side].`

The T-Pose and Views prompts were written for the Player; for another entity, replace the listed parts and the hood sentences with that entity's key visual elements.

## 6. Common Failures and Fixes

Fixes found on the Player; reuse the wording when the same failure appears.

- The teeth read as creepy → replace the smile phrase with `a small, friendly glowing smile drawn as a single soft curved line`.
- A human face or chin appears inside the hood → repeat `the hood opening shows only flat black darkness; no skin, nose, chin or hair is visible`.
- The hood tip grows into a long tail → `the hood ends in a short point that stays close to the back of the head`.
- The cape drapes down the sides of the shoulders or over the upper arms → `the cape lies only on top of the shoulders and ends exactly at the shoulder points`.
- The coat grows to the thighs or knees → `the coat is short and ends at the hips, with the trousers visible from the hips down`.
- Hands vanish inside the sleeves → `the sleeves end at the wrists and the whole hand is visible`.
- Arms droop into an A-pose → repeat `arms perfectly horizontal at shoulder height, forming a straight line through the shoulders`.
- Views differ in outfit or height → regenerate with the best view as an extra reference and add `identical outfit and proportions in all four views`.
- Side views drawn at 3/4 → add `true 90-degree orthographic profile, only one arm visible in front of the body`.
- Tools appear in the hands in the T-pose → repeat `both hands are open and empty; all tools hang from the belt`.
- Trying another player accent colour → change only `cobalt-blue` (e.g. `forest-green`, `crimson`, `mustard-yellow`); the grey hood and leather stay shared (GC_1 colour blocking).

## 7. Open Questions

-
