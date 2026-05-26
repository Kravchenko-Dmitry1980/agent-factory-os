# Final Phase 3.2 Plan Report

**Date:** 2026-05-26  
**Phase:** 3.2-Plan — Next Capability Decision  
**Type:** Markdown planning only

---

## Files created

**governance/phase-3-2-plan/** (22 Markdown files):

| Category | Files |
|----------|-------|
| Index & decision | README, PHASE_3_2_NEXT_CAPABILITY_DECISION, RECOMMENDED_NEXT_STEP, FINAL (this) |
| Options | OPTION_A_LLM_ADAPTER_PLAN, OPTION_B_SECOND_TEMPLATE_REVIEW, OPTION_COMPARISON_MATRIX |
| LLM design | LLM_BOUNDARY_CONTRACT, LLM_FAILURE_MODES, LLM_EVALUATION_PLAN, LLM_TRACE_PLAN, LLM_SECURITY_REVIEW |
| Governance | SECOND_TEMPLATE_RISK_REVIEW, NO_RUNTIME_NO_FACTORY_POLICY, PRECONDITIONS_FOR_3_2_IMPLEMENTATION, ROLLBACK_AND_FREEZE_PLAN |
| Diagrams | 5 Mermaid files in diagrams/ |

---

## Files updated

| File | Change |
|------|--------|
| governance/README.md | Navigation links |

**Not modified:** prototypes-derived/review-assistant-thin/, evaluation/scripts/, prototypes/, integrations-real/, observability/examples/, Books/, experiments/, frozen specs.

---

## Decision

# Option A — LLM Adapter Boundary (mock-first)

**Not:** Second template (Option B deferred)

---

## Why

| Factor | Rationale |
|--------|-----------|
| Safety | Extends one known agent; mock-first |
| Learning | Real LLM failure boundary (parse, timeout, injection) |
| Reuse | Builds on frozen thin v0.1 + template |
| Drift risk | Lower than second template / orchestrator |
| Phase fit | Natural layer before catalog expansion |

Option B wins on long-term catalog value but **loses on next-step safety** — postpone to Phase 3.3+.

---

## What is allowed next

- Phase 3.2-Impl **only after** user approval: mock LLM adapter in new folder
- Extend eval with new script (not modify existing without gate)
- LLM trace events (text)
- Security/mock failure scenarios

---

## What is forbidden next

- Second template creation
- Runtime, factory, registry, router
- Default external API / OpenAI
- RAG, MCP, CV, twin, production bots
- Edit frozen thin v0.1 or eval scripts without proposal

---

## Main risks (Option A)

| Risk | Mitigation |
|------|------------|
| Adapter becomes provider framework | NO_RUNTIME_NO_FACTORY policy; one file |
| LLM output trusted as truth | Boundary contract + verification |
| Secret leakage | Mock-first; no real calls without P8 |
| Thin v0.1 drift | Separate folder; freeze preserved |
| Prompt injection | Policy stub + fail-closed |

## Second template risks (Option B — deferred)

| Risk | Notes |
|------|-------|
| Factory illusion | Two templates → generator pressure |
| Orchestrator drift | Task Triage |
| Duplication | Safe Content Draft |
| Scope creep | Meeting Summary + PII + LLM |

---

## Evaluation plan summary

Mock scenarios: malformed, timeout, uncertain, unsafe, empty. Regression: thin PASS=5, smoke PASS=12, trace PASS=6. No model leaderboard.

See [LLM_EVALUATION_PLAN.md](LLM_EVALUATION_PLAN.md)

---

## Security summary

Mock-first; no secrets in prompts; no command exec from output; no cloud default; explicit approval for real provider.

See [LLM_SECURITY_REVIEW.md](LLM_SECURITY_REVIEW.md)

---

## Preconditions before implementation

[P1–P12](PRECONDITIONS_FOR_3_2_IMPLEMENTATION.md) — including **no API without explicit approval**.

---

## GO / CONDITIONAL GO / NO-GO

# CONDITIONAL_GO_FOR_LLM_ADAPTER_PLAN

- **Plan:** GO (this phase complete)
- **Implementation:** NO-GO until user message + preconditions

---

## Compliance

| Check | Result |
|-------|--------|
| Markdown only | yes |
| No code | yes |
| No API calls | yes |
| No second template | yes |
| No runtime/factory plan drift | yes |
| Protected folders unchanged | yes |

---

## Next recommended prompt

> «Start Phase 3.2 mock LLM adapter for Review Assistant.»

Only after acknowledging [PRECONDITIONS_FOR_3_2_IMPLEMENTATION.md](PRECONDITIONS_FOR_3_2_IMPLEMENTATION.md) and [LLM_BOUNDARY_CONTRACT.md](LLM_BOUNDARY_CONTRACT.md).

Alternative (not recommended now):

> «Start Phase 3.3 second template spec only.»

---

## Summary

Phase 3.2-Plan selects **LLM adapter mock-first** as next capability. Second template deferred. Implementation not started.

**Verdict: CONDITIONAL_GO_FOR_LLM_ADAPTER_PLAN**
