# No Runtime / No Factory Policy

**Date:** 2026-05-26  
**Status:** PLAN_ONLY — **non-negotiable**

---

## Demo Runner is not

| Role | Detail |
|------|--------|
| Runtime | Does not host agent loop |
| Factory | Does not generate agents or scenarios |
| Framework | No plugin API for third parties |
| Orchestrator | Does not chain agents or route tasks |
| Plugin system | No dynamic loading |
| Scenario registry | Fixed dict in one file |
| Provider registry | No model catalog |

---

## Future implementation must stay

| Constraint | Detail |
|------------|--------|
| One small script | `demos/review-assistant-runner/demo_runner.py` |
| Stdlib only | `subprocess`, `sys`, `re`, `pathlib`, `datetime` — no pip deps |
| Fixed menu | Hardcoded menu from [SCENARIO_MENU_PLAN.md](SCENARIO_MENU_PLAN.md) |
| Explicit commands | Each item maps to known command line |
| No dynamic plugin loading | No importlib discovery |
| No config server | No YAML-driven scenario engine in v0.1 |
| No background daemon | Run interactively, exit |

---

## Size guardrails (impl phase)

| Metric | Soft limit |
|--------|------------|
| Lines of Python | ≤ 400 (guideline) |
| Files in runner folder | demo_runner.py + README + optional transcripts/ |
| External dependencies | 0 |

If runner exceeds limits → stop and split plan, do not grow into framework.

---

## Comparison to forbidden platforms

| Platform drift | Demo Runner |
|----------------|-------------|
| Operator Console | Single-purpose menu wrapper |
| Agent Builder runtime | Calls frozen demo |
| pytest platform | Optional link to existing scripts |
| CI orchestrator | Manual operator tool |

---

## Red flags

- “Let’s add a plugin hook for Task Triage”
- “Let’s load scenarios from YAML”
- “Let’s use typer for CLI framework”
- “Let’s run as a service”

→ NO_GO or rollback.

See [DEMO_RUNNER_NON_GOALS.md](DEMO_RUNNER_NON_GOALS.md).
