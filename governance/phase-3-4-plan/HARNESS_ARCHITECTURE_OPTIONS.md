# Harness Architecture Options — Phase 3.4

**Purpose:** Compare options for future provider safety evaluation implementation.  
**Status:** Planning only — **nothing implemented in this phase**.

---

## Option A — Manual checklist only

| | |
|---|---|
| **Description** | Human runs demo scenarios; fills checklist; inspects traces by hand |
| **Pros** | Safest; no code; no framework drift; no new dependencies |
| **Cons** | Slow; inconsistent; hard to regression-test |
| **Verdict** | Valid for first live spot-check; insufficient alone for repeatability |

---

## Option B — Small stdlib script for fixed cases

| | |
|---|---|
| **Description** | One Python script, stdlib only, fixed synthetic cases, mock default, optional real provider flag |
| **Pros** | Controlled; repeatable; low complexity; aligns with existing `evaluation/scripts/` pattern |
| **Cons** | Can grow into framework if discipline slips |
| **Verdict** | **Recommended for Phase 3.4-Impl** |

Suggested future path: `evaluation/scripts/check_review_assistant_provider_safety.py`

---

## Option C — Pytest suite

| | |
|---|---|
| **Description** | pytest fixtures, parametrized injection cases, CI integration |
| **Pros** | Standard testing tooling; familiar to developers |
| **Cons** | Too early for Phase 3.4; test framework drift; CI pressure |
| **Verdict** | **Defer** — not first harness shape |

---

## Option D — Benchmark platform

| | |
|---|---|
| **Description** | Multi-model runner, scoring, dashboards, leaderboards |
| **Pros** | Broad evaluation surface |
| **Cons** | Explicitly out of scope; violates [NO_BENCHMARK_POLICY.md](NO_BENCHMARK_POLICY.md) |
| **Verdict** | **Forbidden** |

---

## Comparison matrix

| Criterion | A Manual | B Stdlib | C Pytest | D Platform |
|-----------|----------|----------|----------|------------|
| Safety / minimal drift | ★★★★★ | ★★★★ | ★★★ | ★ |
| Repeatability | ★★ | ★★★★ | ★★★★★ | ★★★★ |
| Phase 3 fit | ★★★ | ★★★★★ | ★★ | ☆ |
| No framework risk | ★★★★★ | ★★★★ | ★★★ | ☆ |
| CI independence | ★★★★★ | ★★★★ | ★★ | ★ |

---

## Expected recommendation

**Option B later** — one small stdlib script, fixed synthetic cases, no external dependencies, mock default.

**Not implemented in Phase 3.4-Plan.**

Supplement with manual checklist for first real-provider spot-check if needed (Option A as adjunct, not replacement).

---

## Anti-drift guards for Option B

| Guard | Purpose |
|-------|---------|
| Single file | No package tree |
| stdlib only | No new deps |
| Fixed case list | No dynamic generation |
| No scores | Pass/fail only |
| Opt-in real provider | Mock default |
| No CI requirement | Local manual run |

See [RECOMMENDED_HARNESS_SCOPE.md](RECOMMENDED_HARNESS_SCOPE.md) and [diagrams/harness-scope-boundary.md](diagrams/harness-scope-boundary.md).
