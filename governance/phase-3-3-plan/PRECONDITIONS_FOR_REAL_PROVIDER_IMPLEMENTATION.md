# Preconditions for Real Provider Implementation

**Phase 3.3-Plan** — all required before **Phase 3.3-Impl** (future code phase).

---

## Mandatory user gate

User must explicitly send:

```text
Start Phase 3.3 real provider boundary implementation.
```

Plan completion **does not** satisfy this gate.

---

## Approval checklist

| # | Precondition | Plan doc reference |
|---|--------------|-------------------|
| 1 | Provider **selected** (name + type) | [PROVIDER_SELECTION_REVIEW.md](PROVIDER_SELECTION_REVIEW.md) |
| 2 | Provider type approved (local vs cloud) | Selection review + user message |
| 3 | Data class approved for first test | [ALLOWED_DATA_POLICY.md](ALLOWED_DATA_POLICY.md) — synthetic only |
| 4 | API key handling approved | [SECRET_HANDLING_POLICY.md](SECRET_HANDLING_POLICY.md) |
| 5 | Timeout policy approved | [PROVIDER_ERROR_HANDLING.md](PROVIDER_ERROR_HANDLING.md) |
| 6 | Error policy approved | Same |
| 7 | Logging policy approved | [SECRET_HANDLING_POLICY.md](SECRET_HANDLING_POLICY.md) |
| 8 | Trace policy approved | [REAL_PROVIDER_TRACE_PLAN.md](REAL_PROVIDER_TRACE_PLAN.md) |
| 9 | Rollback plan approved | [REAL_PROVIDER_ROLLBACK_PLAN.md](REAL_PROVIDER_ROLLBACK_PLAN.md) |
| 10 | Evaluation scenarios selected | [REAL_PROVIDER_EVALUATION_PLAN.md](REAL_PROVIDER_EVALUATION_PLAN.md) |
| 11 | Mock remains default | [SINGLE_PROVIDER_DECISION.md](SINGLE_PROVIDER_DECISION.md) |
| 12 | Real mode requires explicit flag | Same |
| 13 | No provider framework approved | [NO_PROVIDER_FRAMEWORK_POLICY.md](NO_PROVIDER_FRAMEWORK_POLICY.md) — framework **not** approved |
| 14 | No sensitive data in first test | [FORBIDDEN_DATA_POLICY.md](FORBIDDEN_DATA_POLICY.md) |
| 15 | Security checklist complete | [REAL_PROVIDER_SECURITY_REVIEW.md](REAL_PROVIDER_SECURITY_REVIEW.md) |
| 16 | v0.2 frozen baseline intact | `review-assistant-thin-v0.2` |

---

## Validation baseline (must PASS before impl starts)

```powershell
cd C:\Dima\Projects\CURSOR\AGENT
python evaluation/scripts/check_review_assistant_thin.py
python evaluation/scripts/check_review_assistant_llm_mock.py
python evaluation/scripts/run_demo_smoke_checks.py
python evaluation/scripts/check_expected_text_traces.py
```

Expected: **PASS=5, PASS=5, PASS=12, PASS=6**

---

## Implementation scope cap (future)

Allowed to touch (when preconditions met):

- `prototypes-derived/review-assistant-thin/minimal_demo.py` (provider boundary only)
- Related docs in same folder
- New opt-in eval script under `evaluation/`
- v0.3 freeze records

Forbidden: protected folders, frozen spec body, framework, runtime, factory.

---

## Optional but recommended before impl

- Git tag `review-assistant-thin-v0.2` at baseline commit
- Change proposal document referencing this plan folder

---

## If any precondition fails

**Do not implement.** Remain on v0.2 mock.
