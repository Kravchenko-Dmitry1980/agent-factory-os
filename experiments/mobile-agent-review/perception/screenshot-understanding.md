# Screenshot Understanding

Как MobileAgent превращает скриншот в контекст для модели.

---

## v1/v2 Mobile Pipeline

```
ADB screencap
    → local image file
    → OCR (ModelScope) → text regions
    → GroundingDINO → icon regions
    → optional icon caption (Qwen-VL / CLIP)
    → merge into clickable_infos[]
    → inject into prompt as "coordinates; content" lines
    → keyboard status detection (separate heuristic)
```

**Prompt framing** (`get_action_prompt`):
- Explicit width/height in pixels
- Disclaimer: extracted info "not necessarily accurate"
- Keyboard activation gates `Type` action availability

---

## v3 Mobile

Primary input: **raw screenshot** to GUI-Owl via multimodal API.

Supporting context in InfoPool:
- `ui_elements_list_before/after` — optional structured lists
- History: summaries, actions, outcomes

Image handling:
- `qwen_vl_utils` for resize / aspect ratio
- OpenAI-compatible multimodal messages in `call_mobile_agent_e.py`

---

## v3.5 Mobile / PC / Web

`mobile_use/utils.py` patterns:
- `annotate_screenshot` — may draw action history overlays
- `smart_resize` — Qwen-VL compatible dimensions
- GUI-Owl 1.5 expects image + instruction in chat template

Web path additional:
- Base64 or file image modes (`--image_type`)
- Playwright page screenshots after each action
- Optional CSS-SOM annotated captures

---

## OSWorld (Desktop VM)

- Screenshot from virtual desktop environment
- Accessibility tree XML/text alongside image (owl_agent)
- OSS upload for API-based VLMs (reduce payload size)

---

## Dual-Screenshot Reasoning

Used in **reflection** and **GUI-Critic**:

| Use case | Inputs |
|----------|--------|
| v2 reflect | before/after + both perception lists |
| v3 reflector | before/after screenshots + action description |
| GUI-Critic-R1 | current state + proposed action context |

Pattern: **delta understanding** — model judges whether action changed UI as intended.

---

## Image Preprocessing Concerns

- Resolution mismatch between model training and device → coordinate mapping required
- Long screenshots (web pages) → scrolling actions or tiled views
- Dark mode / themes → OCR degradation in v1/v2
- Video elements / canvas → task-specific manager notes in v3 (e.g. `.html` tasks)

---

## Not Implemented as First-Class

- Continuous video stream perception
- Multi-screen / foldable layout explicit handling
- Unified screenshot schema across platforms (each runner differs)
