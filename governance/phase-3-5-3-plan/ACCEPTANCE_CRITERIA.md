# Acceptance Criteria — Free-Form CLI

**Date:** 2026-05-26  
**Status:** PLAN_ONLY — for future Phase 3.5.3-Impl

Future implementation accepted **only if** all required criteria pass.

---

## Criteria table

| Criterion | Required | Future Evidence |
|-----------|----------|-----------------|
| Separate script or approved modification path | yes | `free_form_cli.py` exists; demo_runner unchanged |
| Stdlib only | yes | No new dependencies in requirements |
| Free-form input accepted | yes | Demo task runs end-to-end |
| Empty input rejected | yes | INPUT_REJECTED output |
| Secret-like input warned/rejected | yes | Test with `sk-fake...` pattern |
| No provider call by default | yes | Mode 1 default; no network in default run |
| Approval required for delivery | yes | approval_requested in trace |
| Approval no blocks delivery | yes | BLOCKED after no |
| Unsafe task blocks delivery | yes | bypass attempt → FAILED/BLOCKED |
| Russian summary printed | yes | OUTPUT_FORMAT_RU blocks |
| TRACE printed | yes | TRACE section with key events |
| Transcript off by default | yes | No file without flag |
| Transcript only with flag | yes | `--save-transcript` creates file |
| No secrets in transcript | yes | Manual inspect saved file |
| Existing baselines pass | yes | PASS counts unchanged |
| Demo Runner v0.1 unchanged | yes | `--list` still 15 items |
| No protected folder changes | yes | git diff scope check |

---

## Optional (nice to have, not blocking v1)

| Criterion | Notes |
|-----------|-------|
| Mode 2 local provider | Manual LM Studio test |
| `--debug` flag | Like Demo Runner |
| Input max length config | Document in freeze |

---

## Fail conditions

Any of:

- Provider called without confirmation
- DELIVERED without approval_granted
- Secrets in transcript
- Baseline FAIL count > 0
- demo_runner.py modified without approval
- minimal_demo.py modified without separate phase

→ **Impl not accepted**; rollback per [ROLLBACK_PLAN.md](ROLLBACK_PLAN.md).
