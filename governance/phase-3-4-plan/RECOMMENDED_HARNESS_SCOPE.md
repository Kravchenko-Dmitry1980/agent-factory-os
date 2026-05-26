# Recommended Harness Scope — Phase 3.4

**Purpose:** Define recommended future implementation scope for Phase 3.4-Impl.  
**Status:** Plan only — **no code in this phase**.

---

## Future phase name

**Phase 3.4-Impl — Minimal Provider Safety Harness**

---

## Scope (in)

| Item | Detail |
|------|--------|
| One script | Single entry point |
| stdlib only | No pip dependencies |
| Fixed synthetic cases | Groups A–G from [SAFE_SYNTHETIC_TEST_SET.md](SAFE_SYNTHETIC_TEST_SET.md) |
| Mock mode default | Simulated provider outputs; no network |
| Local provider optional | Opt-in flag + env; skip if missing (NOT_RUN) |
| Pass/fail output | Per case + summary; no scores |
| Trace inspection | Required events + secret grep |
| Baseline regression | Run existing five eval scripts after harness |

---

## Scope (out)

| Item | Reason |
|------|--------|
| Benchmark | [NO_BENCHMARK_POLICY.md](NO_BENCHMARK_POLICY.md) |
| Provider comparison | Single provider baseline |
| CI integration | Too early |
| pytest | Option C deferred |
| External dependencies | Phase 3 discipline |
| Real private data | [DATA_SAFETY_POLICY.md](DATA_SAFETY_POLICY.md) |
| Provider framework | Forbidden |
| Second agent | Out of scope |
| Red-team platform | [NO_RED_TEAM_PLATFORM_POLICY.md](NO_RED_TEAM_PLATFORM_POLICY.md) |

---

## Suggested script (future)

```text
evaluation/scripts/check_review_assistant_provider_safety.py
```

**Behavior sketch (future, not implemented):**

```powershell
# Default: mock safety cases, no network
python evaluation/scripts/check_review_assistant_provider_safety.py

# Optional: include live local provider cases
$env:REVIEW_ASSISTANT_PROVIDER_SAFETY_LIVE = "1"
python evaluation/scripts/check_review_assistant_provider_safety.py
```

Exact env names deferred to impl phase — must follow opt-in/skip pattern from v0.3 provider scripts.

---

## Optional adjunct (future)

Manual checklist markdown (no code required):

```text
evaluation/review-assistant-thin/provider-safety-checklist.md
```

For human spot-check after first harness run — not a substitute for script.

---

## Statement

> This is a **narrow safety check**, not a framework, not a benchmark, not a red-team platform.

If the script grows beyond one file, adds dependencies, or starts scoring models → **rollback** per [ROLLBACK_AND_FREEZE_PLAN.md](ROLLBACK_AND_FREEZE_PLAN.md).

---

## Success freeze (future)

If Phase 3.4-Impl passes governance review:

- Freeze as **provider safety harness v0.1**
- Do not expand until explicit new phase approval

---

## Architecture choice

**Option B** from [HARNESS_ARCHITECTURE_OPTIONS.md](HARNESS_ARCHITECTURE_OPTIONS.md).

---

## Preconditions

See [PRECONDITIONS_FOR_3_4_IMPLEMENTATION.md](PRECONDITIONS_FOR_3_4_IMPLEMENTATION.md).
