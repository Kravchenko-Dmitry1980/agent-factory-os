# Repository Inventory — MobileAgent

**Source:** `source/MobileAgent/`  
**Remote:** https://github.com/X-PLUG/MobileAgent  
**Clone:** shallow (`--depth 1`), commit `0e5065e9e7acf8f5bc8ee2971fe8b41539da0935`  
**Total files in clone:** ~1775 (per git checkout)

---

## Top-Level Layout

| Path | Files (approx) | Role |
|------|------------------|------|
| `assets/` | 6 | Logos, framework diagrams, result charts |
| `Mobile-Agent-v1/` | 38 | ICLR 2024 Workshop — single-agent mobile |
| `Mobile-Agent-v2/` | 14 | NeurIPS 2024 — multi-agent mobile |
| `Mobile-Agent-v3/` | 577 | GUI-Owl + MA3, OSWorld, AndroidWorld eval |
| `Mobile-Agent-v3.5/` | 603 | GUI-Owl 1.5, mobile/PC/browser use + benchmarks |
| `PC-Agent/` | 31 | ICLR 2025 Workshop — desktop multi-agent |
| `Mobile-Agent-E/` | 59 | Self-evolving mobile assistant |
| `GUI-Critic-R1/` | 9 | NeurIPS 2025 — pre-op GUI critic |
| `UI-S1/` | 432 | ACL 2026 — semi-online RL (VERL + vLLM) |
| `README.md`, `README_zh.md` | — | Family overview, citations, demos |
| `index.html` | — | Project landing page |
| `LICENSE` | — | Apache-style open source |

---

## Version Lineage

### Mobile-Agent-v1 (ICLR 2024 Workshop)

```
Mobile-Agent-v1/
├── run.py, run_api.py
├── requirements.txt
├── MobileAgent/
│   ├── controller.py, api.py, chat.py, prompt.py
│   ├── text_localization.py, icon_localization.py, crop.py
└── Mobile-Agent-qwen/   # Qwen-VL variants, demo scripts
```

- **Paper:** arXiv:2401.16158
- **Pattern:** Single LLM operator + OCR (ModelScope) + GroundingDINO icons + ADB
- **Entry:** `run.py`

### Mobile-Agent-v2 (NeurIPS 2024)

```
Mobile-Agent-v2/
├── run.py
├── requirements.txt
└── MobileAgent/
    ├── controller.py, prompt.py (action/reflect/memory/process prompts)
    └── text_localization.py, icon_localization.py
```

- **Paper:** arXiv:2406.01014
- **Pattern:** Same perception stack + 4 prompt roles (action, reflection, memory, progress)
- **Platforms:** Android, Harmony OS (≤4) via ADB

### Mobile-Agent-v3

```
Mobile-Agent-v3/
├── mobile_v3/              # Real device deployment
│   ├── run_mobileagentv3.py
│   └── utils/mobile_agent_e.py  # Manager/Executor/Reflector/Notetaker
├── os_world_v3/              # OSWorld benchmark integration
├── android_world_v3/         # Vendored AndroidWorld + MA3/GUI-Owl agents
└── cookbook/                 # Jupyter notebooks
```

- **Paper:** arXiv:2508.15144
- **Models:** GUI-Owl-7B, GUI-Owl-32B (HuggingFace mPLUG)
- **Benchmarks:** OSWorld, AndroidWorld, ScreenSpot, MMBench-GUI

### Mobile-Agent-v3.5

```
Mobile-Agent-v3.5/
├── mobile_use/               # GUI-Owl 1.5 on Android (ADB)
├── computer_use/             # GUI-Owl 1.5 on PC (pyautogui)
├── browser_use/              # Web agent (Playwright + SOM)
├── web_benchmark/            # WebArena, VisualWebArena, WebVoyager eval
├── android_world_v3.5/       # AndroidWorld eval for v3.5
├── grounding_and_kb/         # Grounding + GUI knowledge benchmarks
└── cookbook/
```

- **Paper:** arXiv:2602.16855
- **Models:** GUI-Owl-1.5 family (2B–235B, Instruct & Thinking)
- **Features:** MCP/tool calling, long-horizon memory, multi-platform

### PC-Agent (ICLR 2025 Workshop)

```
PC-Agent/
├── run.py, run_v1.py
├── pywin.py, pymac.py
├── PCAgent/                  # Current (OCR + pyautogui + multi-agent prompts)
├── PCAgent_v1/               # Legacy
├── PC-Eval.json              # Evaluation scenarios
└── requirements*.txt         # win/mac/v1 splits
```

- **Paper:** arXiv:2502.14282

### Mobile-Agent-E

```
Mobile-Agent-E/
├── inference_agent_E.py
├── MobileAgentE/agents.py    # Manager/Operator + experience evolution
├── data/Mobile-Eval-E/       # Evaluation scenarios
└── scripts/                  # Evolution batch scripts
```

- **Paper:** arXiv:2501.11733

### GUI-Critic-R1 (NeurIPS 2025)

```
GUI-Critic-R1/
├── test.py, statistic.py
├── requirement.txt
└── test_files/               # gui_i.jsonl, gui_s.jsonl, gui_web.jsonl
```

- **Paper:** arXiv:2506.04614
- **Scope:** Offline pre-operative critic inference only

### UI-S1 (ACL 2026)

```
UI-S1/
├── x/                        # Data pipelines, action spaces
├── verl/                     # RL training framework fork
├── examples/                 # GRPO/PPO trainers
└── requirements.txt          # vllm, ray, flash-attn, verl
```

- **Paper:** arXiv:2509.11543
- **Scope:** Training infrastructure, not deployment runtime

---

## Documentation

| Location | Content |
|----------|---------|
| Root `README.md` / `README_zh.md` | Family overview, news, citations, demo videos |
| Per-version `README.md` | Install, ADB setup, run commands, benchmark instructions |
| `Mobile-Agent-v3.5/browser_use/README.md` | Web agent detailed config |
| `UI-S1/verl/**/README.md` | Training subsystem docs |
| Cookbooks in v3/v3.5 | End-to-end usage notebooks |

---

## Scripts & Entry Points

| Script | Purpose |
|--------|---------|
| `Mobile-Agent-v1/run.py` | v1 single-agent loop |
| `Mobile-Agent-v2/run.py` | v2 multi-agent loop |
| `Mobile-Agent-v3/mobile_v3/run_mobileagentv3.py` | MA3 on real Android/Harmony |
| `Mobile-Agent-v3/os_world_v3/run_multienv_*.py` | OSWorld eval |
| `Mobile-Agent-v3/android_world_v3/run_ma3.py` | AndroidWorld eval |
| `Mobile-Agent-v3.5/mobile_use/run_gui_owl_1_5_for_mobile.py` | GUI-Owl 1.5 mobile E2E |
| `Mobile-Agent-v3.5/computer_use/run_gui_owl_1_5_for_pc.py` | GUI-Owl 1.5 PC E2E |
| `Mobile-Agent-v3.5/browser_use/run_gui_owl_1_5_for_web.py` | GUI-Owl 1.5 browser |
| `Mobile-Agent-v3.5/web_benchmark/main_for_eval.py` | Web benchmark runner |
| `PC-Agent/run.py` | Desktop multi-agent |
| `Mobile-Agent-E/inference_agent_E.py` | Self-evolving mobile |
| `GUI-Critic-R1/test.py` | Critic eval |

Shell wrappers: `run_guiowl.sh`, `run_ma3.sh`, `run_ma35.sh`, `run_guiowl15.sh`, `run_grounding.sh`, `run_gui_kb.sh`

---

## Model References

| Model | Where referenced | Role |
|-------|------------------|------|
| GPT-4 / GPT-4o | v1/v2 README | Primary reasoning (API) |
| Qwen-VL (plus/max/chat) | v1/v2, PC-Agent | Vision-language API or local |
| GUI-Owl-7B / 32B | v3 | Native GUI VLM |
| GUI-Owl-1.5 (2B–235B) | v3.5 | Next-gen multi-platform VLM |
| Qwen2.5-VL / Qwen3-VL | GUI-Critic, v3.5 | Critic inference, grounding eval |
| GroundingDINO + CLIP | v1/v2/E | Icon detection + caption |
| ModelScope OCR | v1/v2/E/PC | Text localization |

**External collections:** HuggingFace `mPLUG/GUI-Owl-*`, ModelScope `iic/GUI-Owl-*`, Bailian API (`gui-plus`).

---

## Benchmark References

| Benchmark | Integration path |
|-----------|------------------|
| OSWorld / OSWorld-Verified | `Mobile-Agent-v3/os_world_v3/` |
| AndroidWorld | `android_world_v3/`, `android_world_v3.5/` (vendored forks) |
| ScreenSpot-v2 / ScreenSpot-Pro | v3 assets, v3.5 `grounding_and_kb/` |
| OSWorld-G, MMBench-GUI | v3 README performance tables |
| OSWorld-MCP | External repo X-PLUG/OSWorld-MCP; v3.5 eval links |
| Mobile-World | External Tongyi-MAI/MobileWorld |
| WebArena / VisualWebArena / WebVoyager | `Mobile-Agent-v3.5/web_benchmark/` |
| Online Mind2Web | Judge scripts in browser_use/web_benchmark |
| GUI-Critic-Test | `GUI-Critic-R1/test_files/` |
| Mobile-Eval-E | `Mobile-Agent-E/data/` |
| PC-Eval | `PC-Agent/PC-Eval.json` |
| MemGUI-Bench | Referenced in v3.5 README (external) |

---

## Requirements / Dependencies (Summary)

| Subproject | Key deps |
|------------|----------|
| v1 | torch, modelscope, CLIP, tensorflow 2.9, opencv, supervision |
| v2 | v1 stack + dashscope, numpy 1.26 |
| v3 mobile | qwen_agent, qwen_vl_utils, numpy |
| v3 AndroidWorld | android_env, grpc, fuzzywuzzy |
| v3.5 browser | openai, playwright, playwright-stealth, oss2, dashscope |
| PC-Agent | PyAutoGUI, pywinauto, pynput, dashscope, OpenOCR |
| Mobile-Agent-E | torch, modelscope, dashscope, datasets |
| GUI-Critic-R1 | transformers, qwen_vl_utils, torch |
| UI-S1 | verl, vllm==0.8.2, flash-attn, ray, hydra, peft |

**Not installed in this workspace** — listed for future reference only.

---

## Notable Gaps (from README TODOs)

- v3: real-world PC deployment code still marked TODO (eval on OSWorld exists)
- v3.5: full benchmark eval code partially external-linked
- GUI-Critic-R1: integration into live agent loops not wired in repo
- v3.5 Python runtime: multi-agent class framework from v3 **not ported** — E2E single VLM loop instead
