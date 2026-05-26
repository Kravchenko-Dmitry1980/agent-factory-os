# Preconditions for Phase 3.4 Implementation

**Purpose:** Gates that must be satisfied before Phase 3.4-Impl (minimal provider safety harness) may start.

---

## Required user message

Exact or equivalent:

```text
Start Phase 3.4-Impl minimal provider safety harness.
```

Planning docs alone do **not** authorize implementation.

---

## Baseline freeze

| Item | Requirement |
|------|-------------|
| review-assistant-thin-v0.3 | Committed and tagged |
| v0.3 governance review | PASS or PASS_WITH_NOTES recorded |
| LM Studio live check | Completed (Phase 3.3-LiveCheck) |

---

## Baseline checks (must PASS)

```powershell
python evaluation/scripts/check_review_assistant_thin.py           # PASS=5
python evaluation/scripts/check_review_assistant_llm_mock.py       # PASS=5
python evaluation/scripts/check_review_assistant_provider_real.py # PASS=2
python evaluation/scripts/run_demo_smoke_checks.py                 # PASS=12
python evaluation/scripts/check_expected_text_traces.py          # PASS=6
```

Run from repo root. All must PASS **before** harness work and **after** harness merge.

---

## Policy acceptance

| Policy | Status required |
|--------|-----------------|
| [SAFE_SYNTHETIC_TEST_SET.md](SAFE_SYNTHETIC_TEST_SET.md) | Approved |
| [NO_BENCHMARK_POLICY.md](NO_BENCHMARK_POLICY.md) | Accepted |
| [NO_RED_TEAM_PLATFORM_POLICY.md](NO_RED_TEAM_PLATFORM_POLICY.md) | Accepted |
| [DATA_SAFETY_POLICY.md](DATA_SAFETY_POLICY.md) | Accepted |
| [SECRET_SAFETY_POLICY.md](SECRET_SAFETY_POLICY.md) | Accepted |
| [ROLLBACK_AND_FREEZE_PLAN.md](ROLLBACK_AND_FREEZE_PLAN.md) | Accepted |
| [RECOMMENDED_HARNESS_SCOPE.md](RECOMMENDED_HARNESS_SCOPE.md) | Scope locked to Option B single script |

---

## Data and secrets

| Check | Requirement |
|-------|-------------|
| No sensitive data in plan fixtures | Synthetic only |
| No real secrets in repo | Verified |
| No cloud provider keys required | Local optional only |

---

## Scope lock for impl

Implementation must remain:

- One stdlib script (Option B)
- Fixed synthetic cases
- Mock default
- No pytest / no CI / no benchmark
- No provider framework
- No protected folder changes without separate approval

---

## If preconditions fail

→ **NO_GO** for Phase 3.4-Impl  
→ Remain on v0.3 baseline + plan docs only

---

## Related

- [PHASE_3_4_GO_NO_GO.md](PHASE_3_4_GO_NO_GO.md)
- [../phase-3-3-plan/PRECONDITIONS_FOR_REAL_PROVIDER_IMPLEMENTATION.md](../phase-3-3-plan/PRECONDITIONS_FOR_REAL_PROVIDER_IMPLEMENTATION.md)
