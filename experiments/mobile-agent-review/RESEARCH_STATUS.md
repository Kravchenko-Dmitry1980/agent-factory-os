# MobileAgent Research Status

**Workspace:** `experiments/mobile-agent-review/`  
**Ingestion date:** 2026-05-25  
**Method:** Shallow clone + static architecture audit (no runtime, no deps, no emulator)

---

## Current Understanding

MobileAgent — семейство GUI-агентов (Tongyi Lab / Alibaba) с эволюцией:

1. **v1** — single-agent + OCR/GroundingDINO perception + ADB  
2. **v2** — multi-prompt agents (action/reflect/memory/progress) — NeurIPS 2024  
3. **v3** — GUI-Owl VLM + class-based Manager/Executor/Reflector/Notetaker + benchmarks  
4. **v3.5** — GUI-Owl 1.5 native E2E on mobile/PC/browser + MCP/tool claims  
5. **Satellites** — PC-Agent (desktop), Mobile-Agent-E (self-evolution), GUI-Critic-R1 (pre-op critic), UI-S1 (RL training)

Репозиторий — **коллекция research prototypes и eval harnesses**, не единый production SDK. Orchestration зрелее в v3 mobile; v3.5 смещается к monolithic VLM loop в open-source runners.

---

## Repository Inventory

| Item | Status |
|------|--------|
| Clone path | `source/MobileAgent/` ✅ |
| Commit | `0e5065e` (shallow depth 1) |
| ~Files | 1775 |
| Major folders | v1, v2, v3, v3.5, PC-Agent, MA-E, GUI-Critic-R1, UI-S1 |
| Entry points | 12+ `run*.py` scripts documented |
| Requirements | 14 requirements files (not installed) |

Full detail: `repository-inventory.md`

---

## Key Architecture Findings

1. **GUI agent loop** — observe screenshot → reason → single action → verify → update state (see `architecture/gui-agent-loop.md`)

2. **InfoPool pattern (v3)** — shared dataclass coordinates Manager/Executor/Reflector/Notetaker without IPC

3. **Perception shift** — external OCR+DINO (v1/v2) → native GUI-Owl grounding (v3/v3.5)

4. **Action contracts differ by platform** — NL DSL (v2), JSON (v3 mobile), pyautogui strings (OSWorld), Playwright (web)

5. **Coordinate spaces** — absolute pixels vs Qwen 0–1000 normalization (`--coor_type`)

6. **Benchmarks embedded** — OSWorld, AndroidWorld forks, web_benchmark in v3.5

7. **GUI-Critic** — pre-operative verification research; **not wired** into agent loops

8. **v3.5 gap** — README multi-agent roles at model level; Python MA3 class framework **not ported** to `mobile_use/`

---

## Useful Patterns

| Pattern | Location in workspace |
|---------|----------------------|
| GUI as environment | `extracted-patterns/gui-as-environment.md` |
| Screen-reason-action-feedback | `extracted-patterns/screen-reason-action-feedback-loop.md` |
| Visual grounding (list / VLM / SOM) | `extracted-patterns/visual-grounding-pattern.md` |
| A/B/C action verification | `extracted-patterns/action-verification-pattern.md` |
| Recovery ladder + replan | `extracted-patterns/failure-recovery-pattern.md` |
| InfoPool coordination | `multi-agent/coordination-patterns.md` |

---

## Useful Anti-Patterns

| Anti-pattern | Location |
|--------------|----------|
| Brittle OCR-list automation | `anti-patterns/brittle-gui-automation.md` |
| Unverified clicks (reflection off) | `anti-patterns/unverified-clicks.md` |
| Weak NL/JSON parsing | `anti-patterns/weak-action-parsing.md` |
| Model output fragility, no circuit breakers | `anti-patterns/model-output-fragility.md` |

---

## Relation to Agent-OS

- **Complements** Claude Code corpus (code harness) with **GUI/OS modality**
- **Maps to** `04_multi-agent/`, `02_memory/`, future verification extensions
- **Does not replace** permissions, hooks, terminal states, MCP protocol docs
- **Taxonomy unchanged** — per experiment boundaries
- Comparison: `comparisons/mobileagent-vs-agent-os.md`

---

## Relation to MCP

- GUI-Owl 1.5 advertises native MCP/tool calling (model capability)
- OSWorld-MCP benchmark external to this clone
- No MCP server in MobileAgent repo — see `mcp-integration/mcp-relevance.md`
- Proposed tool contracts: `mcp-integration/possible-tool-contracts.md`

---

## Relation to Digital Twins

High relevance:
- Android emulator (AndroidWorld vendored)
- Cloud phone (Wuying — README links)
- Desktop VM (OSWorld)
- Browser (Playwright twin)

Digital twin section `agent-os/06_digital-twins/` can absorb **observation/action adapter** patterns before live device control.

Detail: `integration-candidates.md` Tier 3

---

## What Not To Integrate Yet

- Full MobileAgent runtime into Agent-OS
- v1/v2 OCR pipeline as default perception
- UI-S1 training stack as runtime
- Unmodified ADB runners without permission model
- GUI-Critic scripts with hardcoded API keys
- GUI-Owl weights / vLLM serving
- Android emulator setup in AGENT repo root

---

## Recommended Next Steps

1. **Charter GUI modality** for Agent-OS Phase 2 — decide section placement (`13_gui-agents/` vs extend `01_agent-runtime/`)

2. **Promote 5–8 canonical notes** from `extracted-patterns/` + `anti-patterns/` into `agent-os/` after review (not automatic)

3. **Ingest related repos** — OSWorld-MCP, ToolCUA, MobileWorld (separate experiments)

4. **Complete Hermes comparison** when `experiments/hermes-agent-review/` exists

5. **Prototype MCP tool contracts** in isolated sandbox — screenshot capture + mock verify (no real ADB in Agent-OS root)

6. **Deep-read** `Mobile-Agent-v3/mobile_v3/run_mobileagentv3.py` + `mobile_agent_e.py` for golden-path sequence diagram adaptation

7. **Optional:** fetch GUI-Owl 1.5 technical report (arXiv:2602.16855) into `source/papers/` subfolder (PDF not fetched in this step)

---

## Workspace Artifacts Created

```
experiments/mobile-agent-review/
├── README.md
├── RESEARCH_STATUS.md          ← this file
├── repository-inventory.md
├── integration-candidates.md
├── source/MobileAgent/         ← git clone
├── architecture/               (4 files)
├── perception/                 (3 files)
├── action-runtime/             (4 files)
├── multi-agent/                (4 files)
├── memory/                     (2 files)
├── mcp-integration/            (2 files)
├── extracted-patterns/         (5 files)
├── anti-patterns/              (4 files)
├── comparisons/                (4 files)
└── diagrams/                   (3 files)
```

**Total research docs:** 36 markdown files + cloned upstream repo

---

## Boundaries Confirmed

- ✅ No changes outside `experiments/mobile-agent-review/`
- ✅ No Agent-OS taxonomy edits
- ✅ No pip install / model run / emulator
- ✅ No global MobileAgent install
