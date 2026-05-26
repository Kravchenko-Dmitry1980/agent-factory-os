# Evaluation Plan — Free-Form CLI

**Date:** 2026-05-26  
**Status:** PLAN_ONLY

No pytest. No CI. Manual + existing baseline scripts.

---

## No-network cases (future impl)

| Case | Expected |
|------|----------|
| Empty input | Rejected, INPUT_REJECTED |
| Normal demo task | Accepted, flow runs |
| Approval yes + safe draft | DELIVERED if gates pass |
| Approval no | BLOCKED |
| Unsafe task text (bypass) | FAILED/BLOCKED, unsafe_action_blocked |
| Secret-like input (`sk-...`) | Rejected/warned |
| Transcript default | No file created |
| Transcript with `--save-transcript` | File created, no secrets |
| Mode default | Mock, no network |

---

## Provider mode cases (manual, not in automated freeze)

| Case | Expected |
|------|----------|
| Provider not default | Mode 1 default |
| Mode 2 requires confirmation | Cancel on non-yes |
| Missing RA_LLM_BASE_URL | Abort, no call |
| Mode 2 after yes + env | Local call only (operator manual) |

**Do not run in plan phase or automated CI.**

---

## Regression — existing baselines must stay PASS

After future impl, rerun from repo root:

| Script | Expected |
|--------|----------|
| `check_review_assistant_provider_safety.py` | PASS=16 FAIL=0 |
| `check_review_assistant_thin.py` | PASS=5 FAIL=0 |
| `check_review_assistant_llm_mock.py` | PASS=5 FAIL=0 |
| `check_review_assistant_real_provider_contract.py` | PASS=2 FAIL=0 |
| `run_demo_smoke_checks.py` | PASS=12 FAIL=0 |
| `check_expected_text_traces.py` | PASS=6 FAIL=0 |

---

## Demo Runner v0.1 regression

| Check | Expected |
|-------|----------|
| `demo_runner.py --list` | 15 items unchanged |
| `--scenario happy` | DELIVERED unchanged |
| Frozen menu | No drift without proposal |

---

## Future free-form smoke (manual checklist)

Plan for impl phase — not run now:

```powershell
python demos/review-assistant-freeform/free_form_cli.py
# enter demo task, mode 1, approval no → BLOCKED

python demos/review-assistant-freeform/free_form_cli.py
# enter demo task, mode 1, approval yes → DELIVERED (if safe)
```

---

## Evidence record

Future impl review must cite:

- Manual run outputs (decision + gates)
- Baseline PASS lines
- Confirmation no provider call in default path

See [ACCEPTANCE_CRITERIA.md](ACCEPTANCE_CRITERIA.md).
