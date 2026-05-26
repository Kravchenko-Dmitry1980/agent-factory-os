# No Benchmark Policy — Phase 3.4

**Purpose:** Explicitly forbid benchmark/leaderboard drift in provider safety evaluation.

---

## This phase is not

| Forbidden framing | Why |
|-------------------|-----|
| Model leaderboard | Compares intelligence, not safety gates |
| Accuracy benchmark | Domain correctness out of scope |
| Latency benchmark | Performance not safety |
| Cost benchmark | Economics not safety |
| Multi-model comparison | Provider framework risk |
| Model quality certification | Implies production readiness we do not claim |

---

## Why

We are testing **safety boundary behavior**, not general model intelligence.

Question: *Can the system stay safe when output is wrong or hostile-shaped?*  
Not: *Which model scores highest?*

---

## Forbidden artifacts

| Artifact | Status |
|----------|--------|
| Scoreboards | **Forbidden** |
| Model rankings | **Forbidden** |
| Automated winner selection | **Forbidden** |
| Broad prompt suites (1000+ cases) | **Forbidden** — small fixed synthetic set only |
| Provider comparison claims | **Forbidden** in harness output |
| Published "best model" conclusions | **Forbidden** |

---

## Allowed

| Allowed | Notes |
|---------|-------|
| Pass/fail per synthetic case | Safety outcome |
| Trace event checklist | Observability |
| Regression PASS/FAIL vs v0.3 baseline | Chain integrity |
| Observation notes ("model complied with injection") | Not a score |

---

## Alignment

- [../phase-3-2-plan/LLM_EVALUATION_PLAN.md](../phase-3-2-plan/LLM_EVALUATION_PLAN.md) — mock-era eval discipline
- [../../evaluation/governance/anti-benchmark-platform-rules.md](../../evaluation/governance/anti-benchmark-platform-rules.md)
- [NO_RED_TEAM_PLATFORM_POLICY.md](NO_RED_TEAM_PLATFORM_POLICY.md)

---

## Rollback trigger

If harness output starts looking like a benchmark → rollback per [ROLLBACK_AND_FREEZE_PLAN.md](ROLLBACK_AND_FREEZE_PLAN.md).

---

## Diagram

See [diagrams/no-benchmark-boundary.md](diagrams/no-benchmark-boundary.md).
