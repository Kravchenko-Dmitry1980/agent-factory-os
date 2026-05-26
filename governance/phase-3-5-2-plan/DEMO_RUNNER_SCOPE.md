# Demo Runner — Scope

**Date:** 2026-05-26  
**Status:** PLAN_ONLY

---

## In scope (future impl)

| Item | Detail |
|------|--------|
| Menu of existing scenarios | 9 demo scenarios + optional eval script shortcuts |
| Scenario explanations in Russian | Title + “what it proves” per item |
| Command execution wrapper | `subprocess` → existing `minimal_demo.py` |
| Readable result summary | Structured Russian block after run |
| Decision explanation | DELIVERED / BLOCKED / ESCALATED / FAILED |
| Key trace event explanation | Map from [TRACE_EXPLANATION_MAPPING_RU.md](TRACE_EXPLANATION_MAPPING_RU.md) |
| Optional transcript save | Explicit flag only — [TRANSCRIPT_SAVE_PLAN.md](TRANSCRIPT_SAVE_PLAN.md) |
| No-network default | Groups 1–2 + Group 4 eval scripts without provider |
| Real provider warning | Explicit confirmation — [REAL_PROVIDER_WARNING_POLICY.md](REAL_PROVIDER_WARNING_POLICY.md) |
| Stdlib only | No rich/typer/click dependencies |
| One script | `demos/review-assistant-runner/demo_runner.py` |

---

## Out of scope

| Item | Reason |
|------|--------|
| New agent logic | [NO_AGENT_LOGIC_CHANGE_POLICY.md](NO_AGENT_LOGIC_CHANGE_POLICY.md) |
| New scenarios | Frozen thin v0.3 set only |
| Modifying `minimal_demo.py` | Protected |
| Provider calls by default | Explicit confirm + env |
| UI / web app | Platform drift |
| Dashboard / Operator Console | Backlog |
| Persistent sessions | Out of scope |
| Memory / database | Out of scope |
| Runtime / factory | [NO_RUNTIME_NO_FACTORY_POLICY.md](NO_RUNTIME_NO_FACTORY_POLICY.md) |
| Orchestration | Not a router |
| Plugin system | Fixed menu only |
| Dependencies | Stdlib only |
| pytest / CI for runner | Manual + existing baselines |

---

## Boundary diagram

See [diagrams/demo-runner-boundary.md](diagrams/demo-runner-boundary.md).

---

## Comparison to hands-on docs

| Hands-on (3.5.1) | Demo Runner (3.5.2 future) |
|------------------|----------------------------|
| Static markdown report | Live summary after each run |
| Operator types full command | Menu selection |
| Manual trace reading | Mapped Russian explanations |
| No transcript file | Optional save |

Hands-on report **remains** — runner does not replace it.
