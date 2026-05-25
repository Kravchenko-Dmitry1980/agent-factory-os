# OCR and UI Elements

Structured extraction of on-screen text and icons in pre-VLM-heavy versions.

---

## OCR Stack

**Module:** `text_localization.py` (v1, v2, E, PC-Agent variants)

- ModelScope OCR pipeline
- Outputs bounding regions → center coordinates for tap targets
- Merged with icon detections into unified element list

**PC-Agent additions:**
- OpenOCR integration path in requirements
- `merge_strategy.py` — dedupe overlapping text/icon boxes

---

## Icon Detection

**Module:** `icon_localization.py`

- GroundingDINO for icon/button regions
- Caption model assigns semantic label:
  - Local: `qwen-vl-chat`, `qwen-vl-chat-int4`
  - API: `qwen-vl-plus`, `qwen-vl-max`

Output format in prompts:
```
[x, y]; Settings
[x, y]; icon: search
```

---

## UI Element List Contract (v2)

Each `clickable_info` dict:
- `text` — OCR string or icon caption
- `coordinates` — `(x, y)` center pixel
- Filter: skip empty, `"icon: None"`, `(0,0)`

Injected into:
- Action prompt (current screen)
- Reflect prompt (before AND after screenshots)

---

## Keyboard State

Separate detection (not OCR):
- Determines if `Type` action is legal
- Included in action and reflect prompts as boolean status

---

## Limitations (Documented in Prompts)

> "Please note that this information is not necessarily accurate. You need to combine the screenshot to understand."

Implications:
- OCR drift on stylized fonts
- Icon caption errors on ambiguous glyphs
- Duplicate/overlapping boxes
- Non-clickable text included as candidates

These limitations motivated shift to **native VLM** in v3+.

---

## AndroidWorld / OSWorld

Benchmark environments expose **structured UI state** instead of OCR:

- AndroidWorld: JSON element representations via emulator API
- OSWorld: accessibility tree + screenshot

MobileAgent eval agents consume these in `android_world/agents/` rather than ModelScope OCR.

---

## Migration Path (Architectural)

```
OCR+DINO list ──► VLM raw screenshot ──► VLM + SOM/a11y augment
     v1/v2              v3 mobile              v3.5 web/OSWorld
```

For Agent-OS research: OCR list pattern = **explicit perception tool**; VLM path = **multimodal observation**.
