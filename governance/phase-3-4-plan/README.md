# Phase 3.4-Plan — Provider Evaluation / Prompt Injection Harness

**Date:** 2026-05-26  
**Status:** planning-only — **no implementation**, **no provider calls**, **no code**

---

## What this phase is

Phase 3.4-Plan defines how to **plan and later build** a minimal safety evaluation layer for Review Assistant Thin **real provider boundary** (v0.3 baseline).

We already proved a local model can respond (LM Studio live check PASS). This phase plans how to test whether the **system stays safe** when model output is messy, unsafe, injected, or wrong.

**This is not a benchmark. This is not a leaderboard. This is not a red-team platform.**

---

## What this phase is not

| Not in scope | Reason |
|--------------|--------|
| Implementation | Separate Phase 3.4-Impl with explicit user approval |
| Benchmark / leaderboard | Safety boundary behavior only |
| Model comparison | One local provider validated; no ranking |
| Red-team platform | Small synthetic checks only |
| Provider framework | Forbidden by Phase 3 discipline |
| pytest / CI / automation | Too early; deferred |
| Second agent / template | Out of scope |
| Cloud / RU providers | Out of scope |

---

## Current baseline (unchanged)

- **Frozen:** review-assistant-thin-v0.3
- **Real provider:** local OpenAI-compatible (LM Studio validated)
- **Safety chain:**

```text
provider output → parse → safety check → verification → human approval → delivery or block → trace
```

- **Provider response is never truth.**

---

## Reading order

| # | Document |
|---|----------|
| 1 | [PHASE_3_4_PROVIDER_EVALUATION_PLAN.md](PHASE_3_4_PROVIDER_EVALUATION_PLAN.md) |
| 2 | [EVALUATION_SCOPE.md](EVALUATION_SCOPE.md) |
| 3 | [PROMPT_INJECTION_TAXONOMY.md](PROMPT_INJECTION_TAXONOMY.md) |
| 4 | [SAFE_SYNTHETIC_TEST_SET.md](SAFE_SYNTHETIC_TEST_SET.md) |
| 5 | [PASS_FAIL_CRITERIA.md](PASS_FAIL_CRITERIA.md) |
| 6 | [RECOMMENDED_HARNESS_SCOPE.md](RECOMMENDED_HARNESS_SCOPE.md) |
| 7 | [FINAL_PHASE_3_4_PLAN_REPORT.md](FINAL_PHASE_3_4_PLAN_REPORT.md) |

Supporting: behavior checks, risk matrix, expected responses, trace/human review requirements, policies, architecture options, preconditions, rollback, GO/NO-GO, diagrams.

---

## How to decide if implementation can start later

All must be true:

1. User message: **"Start Phase 3.4-Impl minimal provider safety harness."**
2. [PRECONDITIONS_FOR_3_4_IMPLEMENTATION.md](PRECONDITIONS_FOR_3_4_IMPLEMENTATION.md) satisfied
3. [PHASE_3_4_GO_NO_GO.md](PHASE_3_4_GO_NO_GO.md) → CONDITIONAL_GO_FOR_IMPLEMENTATION
4. review-assistant-thin-v0.3 committed/tagged
5. All baseline checks still PASS
6. Synthetic test set and policies approved

Until then: **plan only.**

---

## Prior art

- [../phase-3-3-plan/README.md](../phase-3-3-plan/README.md) — real provider boundary plan
- [../phase-3-3-livecheck/README.md](../phase-3-3-livecheck/README.md) — LM Studio live validation
- [../PHASE_3_3_1_FREEZE_REAL_PROVIDER_V0_3_REVIEW.md](../PHASE_3_3_1_FREEZE_REAL_PROVIDER_V0_3_REVIEW.md) — v0.3 freeze
