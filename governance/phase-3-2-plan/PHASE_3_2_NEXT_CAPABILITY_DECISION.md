# Phase 3.2 — Next Capability Decision

**Date:** 2026-05-26  
**Type:** Planning decision only

---

## What is the next decision?

Choose between:

| Option | Next capability |
|--------|-----------------|
| **A** | **LLM adapter boundary** for existing Review Assistant |
| **B** | **Second text agent template** (e.g. Task Triage, Safe Content Draft, Meeting Summary Review) |

**Decision:** **Option A — LLM Adapter Plan (mock-first)** should be planned next. Option B is **postponed**.

---

## Why decide now?

Review Assistant Thin v0.1 is:

- implemented and working (5 scenarios)
- frozen (FROZEN_WITH_NOTES)
- hardened (`check_review_assistant_thin.py` PASS=5)
- aligned with frozen template spec

Without an explicit next-step decision, the repo risks ad-hoc expansion (second template, runtime extraction, or premature LLM integration).

---

## What must not happen (Phase 3.2-Plan)

- No runtime, factory, generator
- No second agent template created
- No external LLM code or API calls
- No modification of frozen impl, eval scripts, prototypes, specs
- No RAG, MCP, CV, digital twin, production bots

---

## Expected decision

### Plan LLM Adapter First

**Reasons:**

1. **Strengthens existing Review Assistant** — one agent, deeper boundary testing
2. **Tests real LLM failure modes** — malformed, timeout, uncertain — without new template surface
3. **Avoids template proliferation** — second template increases governance burden and factory illusion
4. **Avoids early factory drift** — triage/routing templates tend toward orchestrator runtime
5. **Reuses frozen eval + trace patterns** — extend rather than duplicate

Option B remains valuable **after** LLM boundary is safe and mock-first eval extended.

---

## Decision outputs

| Artifact | Content |
|----------|---------|
| [RECOMMENDED_NEXT_STEP.md](RECOMMENDED_NEXT_STEP.md) | Official recommendation |
| [OPTION_COMPARISON_MATRIX.md](OPTION_COMPARISON_MATRIX.md) | A vs B scoring |
| [LLM_BOUNDARY_CONTRACT.md](LLM_BOUNDARY_CONTRACT.md) | Future adapter contract |
| [PRECONDITIONS_FOR_3_2_IMPLEMENTATION.md](PRECONDITIONS_FOR_3_2_IMPLEMENTATION.md) | Gates before any code |

---

## Verdict for implementation

**CONDITIONAL_GO_FOR_LLM_ADAPTER_PLAN** — planning approved; implementation **not** started.

See [FINAL_PHASE_3_2_PLAN_REPORT.md](FINAL_PHASE_3_2_PLAN_REPORT.md)
