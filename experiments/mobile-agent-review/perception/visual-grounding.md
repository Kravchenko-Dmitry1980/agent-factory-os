# Visual Grounding

Visual grounding в MobileAgent — связывание языкового описания или намерения с **координатами или UI-элементами** на скриншоте.

---

## Three Eras in This Repo

### Era 1: Perception Pipeline (v1, v2, E, PC-Agent)

External CV stack produces grounded candidates **before** LLM sees the screen:

| Stage | Module | Output |
|-------|--------|--------|
| Text OCR | `text_localization.py` | Text boxes + coordinates |
| Icon detection | `icon_localization.py` (GroundingDINO) | Icon regions |
| Icon caption | CLIP / Qwen-VL caption | `"icon: Settings"` strings |
| Merge | `crop.py`, `merge_strategy.py` (PC) | Unified `clickable_infos` list |

LLM grounding = **select from list** or **pick coordinates** informed by list.

**Key insight:** Grounding is split between CV pipeline and LLM; list may be inaccurate (explicitly noted in v2 prompts).

### Era 2: Native GUI-Owl (v3)

Model performs grounding internally from raw screenshot. Optional modules:

- **Grounding agent** (OSWorld): given `element_description`, LLM returns coordinates
- **Accessibility tree** (owl_agent.py): structural grounding supplement

Coordinate post-processing:
- `--coor_type qwen-vl` maps 0–1000 → device resolution
- `coordinate_resize.py` — smart_resize for Qwen-VL tile constraints

### Era 3: GUI-Owl 1.5 (v3.5)

- Default output: **relative coordinates 0–1000**
- Benchmark suite: `grounding_and_kb/eval_grounding_benchmarks.py`
- Datasets: ScreenSpot-v2, ScreenSpot-Pro, OSWorld-G (download externally)

---

## Grounding Benchmarks Referenced

| Benchmark | What it measures |
|-----------|------------------|
| ScreenSpot-v2 | Single-element grounding accuracy |
| ScreenSpot-Pro | High-resolution / professional UI |
| OSWorld-G | Grounding in desktop context |
| MMBench-GUI L1/L2 | Multimodal GUI understanding |
| GUI Knowledge Bench | Action + knowledge on annotated images |

---

## SOM (Set-of-Mark) Overlays

Used in v3.5 web/PC paths for **explicit visual indexing**:

- `som.py`, `--use_css_som` in browser runner
- PC-Agent `--use_som` option

Pattern: overlay numbered regions → model references mark ID → map back to coordinates.

---

## Design Trade-offs

| Approach | Pros | Cons |
|----------|------|------|
| OCR+DINO list | Interpretable, smaller LLM context | Brittle on custom UI, duplicate boxes |
| Native VLM | End-to-end, cross-platform | Needs large VLM, coord format coupling |
| SOM overlays | Reduces free-form coord error | Extra rendering step, layout dependency |
| a11y tree (OSWorld) | Semantic structure | Not available on all mobile apps |

---

## Files to Read

- `Mobile-Agent-v2/MobileAgent/text_localization.py`
- `Mobile-Agent-v2/MobileAgent/icon_localization.py`
- `Mobile-Agent-v3/os_world_v3/mm_agents/mobileagent_v3/mobile_agent_modules.py` (Grounding class)
- `Mobile-Agent-v3.5/grounding_and_kb/eval_grounding_benchmarks.py`
- `Mobile-Agent-v3.5/browser_use/browser/som.py`
