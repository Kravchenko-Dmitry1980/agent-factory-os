# Phase 3.3-Plan — Real LLM Provider Boundary

**Date:** 2026-05-26  
**Status:** planning-only — **no implementation**, **no API calls**, **no code**

---

## What this phase is

Phase 3.3-Plan defines how **one real LLM provider** may be connected to Review Assistant Thin **later**, with the same safety chain as mock v0.2:

```text
task → provider boundary → response → parse → safety → verification → approval → delivery/block → trace
```

**Provider response is never truth.**

---

## Why it exists

- Mock LLM (review-assistant-thin-v0.2) proves boundary **logic** locally
- Real provider adds: network, secrets, timeouts, rate limits, live malformed output, cost, privacy, prompt injection
- Planning must precede any implementation approval

---

## Why no API is called

- Current frozen baseline: mock only
- No keys, no network, no external dependencies
- Implementation requires separate explicit user message

---

## Why no provider framework

- Hermes Desktop triage showed registry/router drift risk
- Phase 3 discipline: **one explicit provider mode**, mock default, real behind flag
- Framework comes only after multiple individually approved providers — not in Phase 3.3

---

## Key documents (reading order)

| # | Document |
|---|----------|
| 1 | [PHASE_3_3_REAL_PROVIDER_BOUNDARY_PLAN.md](PHASE_3_3_REAL_PROVIDER_BOUNDARY_PLAN.md) |
| 2 | [PROVIDER_SELECTION_REVIEW.md](PROVIDER_SELECTION_REVIEW.md) |
| 3 | [SINGLE_PROVIDER_DECISION.md](SINGLE_PROVIDER_DECISION.md) |
| 4 | [PROVIDER_BOUNDARY_CONTRACT.md](PROVIDER_BOUNDARY_CONTRACT.md) |
| 5 | [SECRET_HANDLING_POLICY.md](SECRET_HANDLING_POLICY.md) |
| 6 | [REAL_PROVIDER_SECURITY_REVIEW.md](REAL_PROVIDER_SECURITY_REVIEW.md) |
| 7 | [PRECONDITIONS_FOR_REAL_PROVIDER_IMPLEMENTATION.md](PRECONDITIONS_FOR_REAL_PROVIDER_IMPLEMENTATION.md) |
| 8 | [FINAL_PHASE_3_3_PLAN_REPORT.md](FINAL_PHASE_3_3_PLAN_REPORT.md) |

Supporting: data policies, error handling, eval/trace/rollback, diagrams, GO/NO-GO.

---

## How to decide if implementation can start later

All must be true:

1. User message: **"Start Phase 3.3 real provider boundary implementation."**
2. [PRECONDITIONS_FOR_REAL_PROVIDER_IMPLEMENTATION.md](PRECONDITIONS_FOR_REAL_PROVIDER_IMPLEMENTATION.md) satisfied
3. [PHASE_3_3_GO_NO_GO.md](PHASE_3_3_GO_NO_GO.md) → CONDITIONAL_GO_FOR_IMPLEMENTATION
4. Provider selected and approved (not chosen in plan-only phase)
5. Mock remains default; real mode explicit flag only
6. All four baseline checks still PASS

Until then: **plan only.**

---

## Current baseline (unchanged)

- **Frozen:** review-assistant-thin-v0.2
- **Path:** `prototypes-derived/review-assistant-thin/`
- **Hermes triage:** research-only; no Phase 3.3 scope expansion

---

## Prior art

- Phase 3.2 mock impl + v0.2 freeze
- [../phase-3-2-plan/LLM_BOUNDARY_CONTRACT.md](../phase-3-2-plan/LLM_BOUNDARY_CONTRACT.md) (mock-era; superseded for real provider by this plan's contract)
- [../phase-3-2-2/FINAL_PHASE_3_2_2_REPORT.md](../phase-3-2-2/FINAL_PHASE_3_2_2_REPORT.md)
