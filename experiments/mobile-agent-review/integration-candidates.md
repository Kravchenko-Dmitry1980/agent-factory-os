# Integration Candidates

Рекомендации по интеграции находок MobileAgent в Agent-OS — **без выполнения интеграции в этом эксперименте**.

---

## Tier 1 — Promote to Agent-OS Later (High Value)

| Candidate | Source | Target in Agent-OS |
|-----------|--------|-------------------|
| Visual verification A/B/C | v2/v3 reflectors | `00_foundations/verification.md` or new GUI appendix |
| InfoPool shared state pattern | v3 `mobile_agent_e.py` | `02_memory/shared-state.md`, `04_multi-agent/coordination.md` |
| Screen→reason→act→feedback loop | All versions | `01_agent-runtime/` GUI modality note |
| Failure recovery ladder (replan threshold) | v3 Manager | `01_agent-runtime/error-recovery-ladder.md` |
| GUI-as-environment framing | v1 + UI-S1 spaces | `00_foundations/execution-loops.md` |
| GUI antipatterns catalog | This workspace `anti-patterns/` | `09_antipatterns/` new files |

---

## Tier 2 — MCP / Tooling (Medium Term)

| Candidate | Notes |
|-----------|-------|
| `gui_capture_screenshot` tool | See `mcp-integration/possible-tool-contracts.md` |
| `gui_execute_action` with coord_space | Unified driver adapter |
| `gui_verify_action_delta` | Post-op verification tool |
| GUI + MCP hybrid routing | From GUI-Owl 1.5 + OSWorld-MCP research |
| Runtime bridges | Extend `05_mcp/runtime-bridges.md` |

---

## Tier 3 — Digital Twins (Strategic)

| Candidate | Notes |
|-----------|-------|
| Android emulator twin | AndroidWorld vendored env pattern |
| Cloud phone twin | Wuying / Bailian demos — hosted observation |
| Desktop VM twin | OSWorld integration |
| Browser twin | Playwright `browser_use` stack |
| Persona + skill graphs for GUI tasks | Link `06_digital-twins/skill-graphs.md` |

---

## Tier 4 — Research Only (Do Not Integrate Yet)

| Item | Reason |
|------|--------|
| Full MobileAgent run scripts | Not production harness; duplicate per version |
| OCR+DINO v1/v2 pipeline | Superseded by GUI-Owl for new work |
| UI-S1 VERL training stack | Training infra, not agent runtime |
| GUI-Critic offline eval scripts | Needs integration design + secret hygiene |
| Hardcoded benchmark hints in Manager | Overfit, not general |
| GUI-Owl model weights | External HF dependency, not knowledge |
| ADB-first mobile driver | Platform-specific; use adapter pattern first |

---

## Tier 5 — External Repos to Ingest Next

| Repo | Why |
|------|-----|
| X-PLUG/OSWorld-MCP | MCP benchmark + eval patterns |
| X-PLUG/ToolCUA | GUI vs tool orchestration |
| Tongyi-MAI/MobileWorld | Mobile MCP scenarios |
| google-research/android_world | Env contract reference |
| xlang-ai/OSWorld | Desktop env reference |

---

## Suggested Agent-OS Source Entry (Future)

When promoting, add to `agent-os/10_research/sources.md`:

```markdown
| MobileAgent | experiments/mobile-agent-review/ | GUI/OS agent family, GUI-Owl, visual grounding | Research ingested 2026-05-25 |
```

---

## Decision Principles

1. **Patterns before code** — import concepts, not Alibaba scripts wholesale
2. **Harness before model** — Agent-OS strength is engineering knowledge
3. **Adapter boundary** — never merge ADB into core runtime without permission layer
4. **Keep experiments isolated** until Phase 2 charter for GUI modality

---

## Verification of This Experiment

```powershell
# Clone present
Test-Path C:\Dima\Projects\CURSOR\AGENT\experiments\mobile-agent-review\source\MobileAgent\README.md

# Agent-OS untouched
git -C C:\Dima\Projects\CURSOR\AGENT status agent-os/
```

No dependencies installed. No emulator configured. No models run.
