# Concept Art Workflow

> How every contributor makes the concept art of an entity: the image that best shows how it should look in game, and where the results are recorded.
> **Style:** [3D Modeling Guidelines](../Modeling_Guidelines.md) §1, §3, §6, §8 and the entity's Art doc · **References:** `Art_Direction/References/` · **Example:** [E_Player_Art](../../GDD/03_Entities/Player/E_Player/E_Player_Art.md)

## 1. Scope and Tools

- The goal is an image that best shows the entity as it should look in game. No pose, camera or framing is imposed: choose whatever shows the entity best.
- Reference sheets for modeling (a strict-front sheet in a T-pose or A-pose, isolated parts, side and back views) are made from the approved concept as a separate step.
- Tools:
  - Concept: `Gemini` {Argon -> Medium}.
  - Reference sheets: `Tripo3D` {Generate Image -> T-Pose -> Nano Banana Pro}, or the providers in `character-sheet-pipeline`.
- AI agents use two skills from the Armotheca project repository (`.claude/skills/`):
  - `image-reference-workflow`: concept exploration and faithful edits of an accepted image.
  - `character-sheet-pipeline`: reference sheets for modeling from the approved concept, with `{CHARACTER_POSE}` set to T-pose or A-pose.

## 2. Recording Results

- Record every image you keep, concepts and reference sheets alike, in the History of the entity's Art doc (`E_<Name>_Art.md`), with its AI model and prompt. Rejected variants are not recorded.
- A generated image records its full prompt. An edited image (a reference sheet, a view, or a fix to an earlier version) records only the prompt that changed the version it was made from.
- The concept prompt is written for each entity and lives only in that History.
- Every generation request is also logged next to its images, in a `prompts.json` in the last-level folder of `Sources/<Entity>/Art/` ([Assets Naming › Sources folder](../Assets_Naming.md#sources-folder)). The file is an array with one object per request, oldest first; `request_id` is `null` when the tool shows none. Rejected images stay in that folder and are not copied into the Art doc.

  ```json
  [
    {
      "name": "01 Male",
      "date_time": "2026-11-03T14:05:00+01:00",
      "request_id": "a1b2c3d4-...",
      "prompt": "A mysterious hooded artisan...",
      "aspect_ratio": "3:4",
      "resolution": "2K",
      "num_images": 4
    }
  ]
  ```

## 3. Concept

### Settings

| Parameter | Value |
|---|---|
| Aspect ratio | 3:4 (portrait, full body) |
| Resolution | 2K for exploration, highest available for the final pick |
| Variants | 4 per pass |
| Reference images | None for the first pass; pass the best result back when refining |

### Prompt

Write the prompt in plain paragraphs, in this order: subject, pose and background; face; each clothing or body part in its own paragraph; proportions; style; lighting; exclusions (`No text, no labels, no watermark, no logos, no frame or border.`). See [E_Player_Art › 01 Male](../../GDD/03_Entities/Player/E_Player/E_Player_Art.md#01-male).

## 4. Common Failures and Fixes

Fixes found on the Player's concept; reuse the wording when the same failure appears.

- The teeth read as creepy → replace the smile phrase with `a small, friendly glowing smile drawn as a single soft curved line`.
- A human face or chin appears inside the hood → repeat `the hood opening shows only flat black darkness; no skin, nose, chin or hair is visible`.
- The hood tip grows into a long tail → `the hood ends in a short point that stays close to the back of the head`.
- The cape drapes down the sides of the shoulders or over the upper arms → `the cape lies only on top of the shoulders and ends exactly at the shoulder points`.
- The coat grows to the thighs or knees → `the coat is short and ends at the hips, with the trousers visible from the hips down`.
- Hands vanish inside the sleeves → `the sleeves end at the wrists and the whole hand is visible`.
- Trying another player accent colour → change only `cobalt-blue` (e.g. `forest-green`, `crimson`, `mustard-yellow`); the grey hood and leather stay shared (GC_1 colour blocking).

## 5. Open Questions

-
