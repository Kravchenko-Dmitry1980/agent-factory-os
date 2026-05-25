# Architecture Overview — MobileAgent Family

MobileAgent — семейство GUI-агентов от Tongyi Lab (Alibaba), эволюционирующее от **perception-heavy single-agent** (v1) к **native VLM end-to-end agents** (GUI-Owl 1.5) с опциональным **multi-agent orchestration** (v2/v3/PC/E).

---

## Architectural Layers (Conceptual)

```
┌─────────────────────────────────────────────────────────────┐
│  User instruction + optional domain hints (add_info)        │
└───────────────────────────┬─────────────────────────────────┘
                            ▼
┌─────────────────────────────────────────────────────────────┐
│  Orchestration (version-dependent)                          │
│  v1: single loop │ v2: prompt-roles │ v3/E: class agents    │
│  v3.5: mostly single VLM loop (roles in model, not Python)  │
└───────────────────────────┬─────────────────────────────────┘
                            ▼
┌─────────────────────────────────────────────────────────────┐
│  Perception                                                 │
│  v1/v2: OCR + icon det + captions → structured UI list      │
│  v3+: screenshot (+ optional a11y tree in OSWorld)          │
│  v3.5: annotated screenshots, smart_resize (Qwen-VL utils)  │
└───────────────────────────┬─────────────────────────────────┘
                            ▼
┌─────────────────────────────────────────────────────────────┐
│  Reasoning / Planning                                       │
│  LLM or VLM: thought → action JSON or natural language      │
└───────────────────────────┬─────────────────────────────────┘
                            ▼
┌─────────────────────────────────────────────────────────────┐
│  Action execution                                           │
│  ADB (mobile) │ pyautogui (PC) │ Playwright (web)           │
└───────────────────────────┬─────────────────────────────────┘
                            ▼
┌─────────────────────────────────────────────────────────────┐
│  Verification & memory                                        │
│  Reflection A/B/C │ progress tracking │ notetaker │ critic  │
└─────────────────────────────────────────────────────────────┘
```

---

## Evolution Axis

| Generation | Perception | Reasoning | Orchestration | Verification |
|------------|------------|-----------|---------------|--------------|
| v1 | OCR + DINO + captions | Single GPT/Qwen chat | Monolithic loop | Implicit (retry in loop) |
| v2 | Same + richer prompts | Multi-prompt same LLM | Action→Reflect→Memory→Progress | Explicit reflect agent |
| v3 | GUI-Owl VLM primary | Class-based agents | Manager→Executor→Reflector→Notetaker | A/B/C + replan threshold |
| v3.5 | GUI-Owl 1.5 native | E2E VLM (+ thinking variant) | Model-internal multi-role | Benchmark judges; less Python reflect |
| PC-Agent | Desktop OCR + SOM option | Qwen prompts | Same as v2 pattern | Reflect + progress |
| MA-E | v1-like perception | + experience retrieval | Self-evolution agents | Reflect + experience reflect |
| GUI-Critic | Screenshot pair | Pre-op critic only | N/A (offline) | Before action, not after |

---

## Shared Design Primitives

### InfoPool (v3, Mobile-Agent-E)

Central dataclass holding instruction, plan, action history, outcomes, errors, notes. All agents read/write the same pool — no inter-process messaging.

**Source:** `Mobile-Agent-v3/mobile_v3/utils/mobile_agent_e.py`

### Prompt roles (v2, PC-Agent)

Separate prompt templates simulate agents without separate model instances:
- Action, Reflection, Memory, Progress (Planning)

**Source:** `Mobile-Agent-v2/MobileAgent/prompt.py`, `PC-Agent/PCAgent/prompt_qwen.py`

### Coordinate systems

- **Absolute pixels** — v1/v2 perception lists, pyautogui
- **Normalized 0–1000** — Qwen-VL family, GUI-Owl 1.5 default
- **Resolution mapping** — `convert_xy`, `smart_resize`, `--coor_type qwen-vl`

---

## Platform Boundaries

| Platform | Controller | Versions |
|----------|------------|----------|
| Android | ADB shell (`input tap`, swipe, text) | v1–v3.5 mobile |
| Harmony OS | HDC path variant | v3 mobile |
| Desktop Windows/Mac | pyautogui, pywinauto | PC-Agent, v3.5 computer_use |
| Desktop Linux | pyautogui | PC-Agent (limited) |
| Browser | Playwright async + SOM overlays | v3.5 browser_use |
| Emulator benchmarks | AndroidWorld JSON actions, OSWorld pyautogui strings | v3/v3.5 eval trees |

iOS explicitly **not supported** in READMEs.

---

## Model Serving Assumptions

- **Cloud API:** OpenAI-compatible endpoints (vLLM, DashScope, Bailian)
- **Local:** Qwen-VL, GUI-Owl via transformers / vLLM
- **Multimodal message format:** qwen_agent + qwen_vl_utils image handling
- **Optional OSS upload:** screenshots as URLs in OSWorld/web eval paths

---

## What This Repo Is NOT

- Not a unified agent runtime SDK (each version is largely standalone)
- Not a production harness with permissions, hooks, circuit breakers (contrast Claude Code)
- Not MCP-native server (MCP appears as model capability + external OSWorld-MCP benchmark)
- UI-S1 is **training** code, not deployment architecture

---

## Key Files for Deep Dive

| Topic | Path |
|-------|------|
| MA3 agent classes | `Mobile-Agent-v3/mobile_v3/utils/mobile_agent_e.py` |
| MA3 main loop | `Mobile-Agent-v3/mobile_v3/run_mobileagentv3.py` |
| v2 multi-agent loop | `Mobile-Agent-v2/run.py` |
| v2 action contract | `Mobile-Agent-v2/MobileAgent/prompt.py` |
| GUI-Owl 1.5 mobile runtime | `Mobile-Agent-v3.5/mobile_use/utils.py` |
| OSWorld orchestrator | `Mobile-Agent-v3/os_world_v3/mm_agents/mobileagent_v3/mobile_agent.py` |
| Self-evolution | `Mobile-Agent-E/MobileAgentE/agents.py` |
| Pre-op critic | `GUI-Critic-R1/test.py` |
