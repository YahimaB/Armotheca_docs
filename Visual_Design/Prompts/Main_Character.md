# Main Character — Image Prompts

> Target model: **Gemini 4 Argon** (text → image). Style source: [3D Modeling Guidelines](../../Guidelines/Modeling_Guidelines.md) §1, §3, §6, §8 and references GC_1 / AF_1.
> Hood reference: a medieval **gugel** (hood sewn to a short shoulder cape, laced front) worn over a long-sleeve strap-and-clasp coat.

Three prompts, used in order. Each step passes its approved result to the next one as the reference image:

1. **[Concept](#1-concept)** — one image of the character, free pose. Iterate on this until the look is approved.
2. **[T-Pose](#2-t-pose)** — the approved concept set into a T-pose, front view.
3. **[Views](#3-views)** — the T-pose image as four separate orthographic images (front, back, right, left) for the 3D artist.

---

## 1. Concept

### Settings

| Parameter | Value |
|---|---|
| Aspect ratio | 3:4 (portrait, full body) |
| Resolution | 2K for exploration, highest available for the final pick |
| Variants | 4 per pass |
| Reference images | None for the first pass; pass the best result back when refining |

### Prompt

```
A stylized 3D character concept render of a mysterious hooded artisan, a weapon-smith from a magical workshop that floats between worlds. Full-body three-quarter front view, the character standing in a relaxed, confident pose with one hand resting on the belt. A single character alone in the frame on a plain, light warm-grey background.

Face: the character has no visible face. The opening of the hood is filled with flat, pure black darkness, an empty void with no skin, hair, nose or ears. Floating in this darkness are two large, rounded, softly glowing pale-gold eyes and a small, friendly, slightly crooked smile drawn as a thin glowing line with a few small rounded teeth. The eyes and mouth look painted onto the darkness, simple and expressive like a cartoon, giving the character a cozy, mischievous personality.

Hood and cape: a deep hood of soft heather-grey felted wool, stiff enough that its thick rim keeps the inside in complete shadow. The hood ends in a short, natural point just behind the back of the head. It is sewn to a short shoulder cape of the same wool, in the style of a medieval gugel. The cape lies only on top of the shoulders and ends in a clean edge at the shoulder points, so the rounded outer sides of the shoulders and the upper arms show the coat. It closes down the chest with a laced front: four large cross-laces of dark cord and a small tied bow at the throat.

Coat: a fitted long-sleeve work coat of deep cobalt-blue heavy canvas that ends at the hips, closed down the front by three chunky black leather straps fastened with dark iron hook clasps. The sleeves run all the way down to the wrists and end in a wide cuff band.

Belt: a broad dark-brown leather belt, about a hand wide, with a large brass buckle, worn over the coat at the waist. Hanging from the belt: a small forging hammer in a leather loop at the right hip, a pair of iron tongs and a chisel in a tool sheath beside it, and a sturdy honey-brown leather satchel with a brass clasp on the left hip.

Hands: large, sturdy human hands with warm-toned skin and short nails, emerging directly from the coat cuffs.

Lower body: dark grey canvas trousers tucked into chunky brown leather boots with blue-grey iron toe caps.

Proportions: an adult of average height, about 180 cm tall from the soles of the boots to the top of the hood. Stylized, about six heads tall counting the hood, sturdy build with broad shoulders, oversized hands and boots that read clearly from a distance.

Style: stylized, chunky, hand-crafted PBR 3D render, like a modern cozy fantasy co-op game. Simplified, slightly exaggerated shapes 20 to 40 percent thicker than real life, softly beveled edges on every strap, buckle, clasp and boot, oversized buckles and rivets, simplified cloth folds. Surfaces carry soft hand-painted color variation and subtle edge wear, with a matte finish. Mundane materials stay muted and warm: grey wool, cobalt canvas, honey and dark-brown leather, blue-grey iron, warm brass. The eyes and mouth are the only glowing elements on the character. Smooth shading without outlines or cel shading.

Lighting: soft, warm key light from the front-left with a gentle fill so every material reads clearly, a faint rim light separating the hood from the background, and a soft contact shadow under the boots. The inside of the hood stays in complete darkness.

No text, no labels, no watermark, no logos, no frame or border.
```

---

## 2. T-Pose

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

---

## 3. Views

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

---

## Workflow
-  [[#1. Concept]] prompt is fed to `Gemini` {Argon -> Medium}
- Concept art is fed to `Tripo3D` {Generate Image -> T-Pose -> Nano Banana Pro}
## Notes

- **Mouth.** If the teeth read as creepy, replace the smile phrase with `a small, friendly glowing smile drawn as a single soft curved line`.
- **Player accent.** The coat carries the per-player accent color (GC_1 color blocking). To try a variant, change only `cobalt-blue` (e.g. `forest-green`, `crimson`, `mustard-yellow`); the grey hood and leather stay shared.
- **Apron dropped.** The coat and broad belt replace the smith's apron. The forge identity comes from the tools on the belt.
- **Common failures and fixes:**
  - A human face or chin appears inside the hood → repeat `the hood opening shows only flat black darkness; no skin, nose, chin or hair is visible`.
  - The hood tip grows into a long tail → `the hood ends in a short point that stays close to the back of the head`.
  - The cape drapes down the sides of the shoulders or over the upper arms → `the cape lies only on top of the shoulders and ends exactly at the shoulder points`.
  - The coat grows to the thighs or knees → `the coat is short and ends at the hips, with the trousers visible from the hips down`.
  - Hands vanish inside the sleeves → `the sleeves end at the wrists and the whole hand is visible`.
  - Arms droop into an A-pose → repeat `arms perfectly horizontal at shoulder height, forming a straight line through the shoulders`.
  - Views differ in outfit or height → regenerate with the best view as an extra reference and add `identical outfit and proportions in all four views`.
  - Side views drawn at 3/4 → add `true 90-degree orthographic profile, only one arm visible in front of the body`.
  - Tools appear in the hands in the T-pose → repeat `both hands are open and empty; all tools hang from the belt`.
