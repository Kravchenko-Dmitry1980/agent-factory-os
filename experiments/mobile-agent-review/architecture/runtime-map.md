# Runtime Map — MobileAgent

Карта исполняемых runtime-путей по платформам и версиям.

---

## Mobile (Real Device)

```
run_mobileagentv3.py (v3)
run_gui_owl_1_5_for_mobile.py (v3.5)
         │
         ├── ADB/HDC controller
         │     android_controller.py / harmonyos_controller.py (v3)
         │     AdbTools in utils.py (v3.5)
         │
         ├── Screenshot capture → base64 / file
         │
         ├── Model client (OpenAI-compatible)
         │     call_mobile_agent_e.py / GUIOwlWrapper
         │
         └── Action parse → shell commands
```

**Pre-requisites (documented, not configured here):** ADB, ADB Keyboard APK, API key + vLLM base URL.

---

## Desktop (PC-Agent)

```
PC-Agent/run.py
         │
         ├── OCR + icon merge (text_localization, merge_strategy)
         ├── Optional SOM overlay (--use_som)
         ├── Multi-prompt loop (subtask, action, reflect, memory, process)
         └── pyautogui + platform helpers (pywin.py / pymac.py)
```

---

## Desktop (GUI-Owl 1.5)

```
Mobile-Agent-v3.5/computer_use/run_gui_owl_1_5_for_pc.py
         │
         ├── pyautogui, pyperclip
         └── Single VLM loop (coordinates 0–1000)
```

---

## Browser (GUI-Owl 1.5)

```
Mobile-Agent-v3.5/browser_use/run_gui_owl_1_5_for_web.py
         │
         ├── Playwright (Chromium, headless option)
         ├── SOM / CSS-SOM (--use_css_som)
         ├── OSS image upload (optional)
         └── Action execution via browser automation layer
              browser_playwright.py, som.py
```

---

## Benchmark Runtimes

### OSWorld (v3)

```
os_world_v3/
├── run_multienv_mobileagent_v3.py  → MobileAgentV3 multi-agent
├── run_multienv_owl.py             → GUI-Owl E2E
└── mm_agents/
    ├── mobileagent_v3/mobile_agent.py
    └── owl_agent.py
```

Uses **pyautogui code strings** as actions; accessibility tree in owl path.

### AndroidWorld (v3 / v3.5)

```
android_world_v3/ | android_world_v3.5/
├── Vendored android_world package
├── agents/mobile_agent_v3.py, gui_owl.py, infer_ma3.py
├── run_ma3.py / run_ma35.py
└── Docker emulator runner (scripts/run_suite_on_docker.py)
```

Uses **JSON action API** of AndroidWorld environment.

### Web benchmarks (v3.5)

```
web_benchmark/main_for_eval.py
├── WebArena / VisualWebArena task maps
├── WebVoyager tasks
└── Online_Mind2Web_judge/ (trajectory scoring)
```

---

## Training Runtime (Out of Scope for Deployment)

```
UI-S1/
├── verl/ PPO/GRPO workers
├── vLLM rollout
└── Action spaces: x/data/agent/space/*.py
```

---

## Runtime Comparison Table

| Runtime | Entry | Agent model | Env interface | Verification |
|---------|-------|-------------|---------------|--------------|
| v1 mobile | `run.py` | GPT + perception | ADB | Loop retry |
| v2 mobile | `run.py` | GPT + 4 prompts | ADB | Reflect A/B/C |
| v3 mobile | `run_mobileagentv3.py` | GUI-Owl + 4 classes | ADB/HDC | Reflector + replan |
| v3.5 mobile | `run_gui_owl_1_5_for_mobile.py` | GUI-Owl 1.5 E2E | ADB | Model + screenshot delta |
| PC-Agent | `run.py` | Qwen prompts | pyautogui | Reflect + progress |
| MA-E | `inference_agent_E.py` | Multi + experience | ADB | Reflect + evolution |
| OSWorld eval | `run_multienv_*.py` | MA3 or Owl | pyautogui VM | Env reward + reflect |
| Web eval | `main_for_eval.py` | GUI-Owl 1.5 | Playwright | External judges |

---

## External Dependencies at Runtime

| Dependency | Used by |
|------------|---------|
| ADB platform-tools | All mobile paths |
| Android emulator + AndroidWorld install | Benchmark only |
| OSWorld VM setup | Benchmark only |
| vLLM or cloud VLM API | v3+ |
| Playwright + Chromium | Browser paths |
| HuggingFace model weights | Local GUI-Owl inference |

None of these were installed during research ingestion.
