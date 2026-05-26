# Post-Implementation Checklist — Phase 3.1

Complete **after** future thin implementation, before acceptance.

---

## Baseline regression

| # | Check | Pass criteria |
|---|-------|---------------|
| 1 | `python evaluation/scripts/run_demo_smoke_checks.py` | PASS=12 FAIL=0 |
| 2 | `python evaluation/scripts/check_expected_text_traces.py` | PASS=6 FAIL=0 |

---

## Review Assistant scenarios (impl)

| # | Scenario | Pass criteria |
|---|----------|---------------|
| 3 | Good draft approved | Delivery only after human approve; trace complete |
| 4 | Bad draft rejected | `approval_denied`; no delivery |
| 5 | Critic uncertain | Fail-closed; no auto-delivery |
| 6 | Missing approval blocks | No delivery without approval |
| 7 | Bypass / unsafe publish blocked | Block audited |

Commands: document in implementation review (e.g. `python prototypes-derived/review-assistant-thin/thin_demo.py --scenario happy`)

---

## Trace review

| # | Check | Pass criteria |
|---|-------|---------------|
| 8 | Compare to [expected-traces.md](../../agent-builder-kit/templates/review-assistant-agent/expected-traces.md) | Semantic match |
| 9 | [trace-review-checklist.md](../../agent-builder-kit/evaluation-checklists/trace-review-checklist.md) | All items pass |
| 10 | Critic `advisory=true` where used | Present |

---

## Scope / drift inspection

| # | Check | Pass criteria |
|---|-------|---------------|
| 11 | No `runtime/`, `factory/`, `generator/` folders | Absent |
| 12 | No second agent template | Absent |
| 13 | No new dependencies | `requirements.txt` clean or approved |
| 14 | Protected folders unchanged | `git diff` clean |
| 15 | Frozen spec unchanged | No semantic diff on 12 template files |
| 16 | Code only under `prototypes-derived/review-assistant-thin/` | Yes |
| 17 | No network/Telegram/FastAPI in impl | Yes |
| 18 | No persistent memory store | Yes |

---

## Documentation

| # | Check | Pass criteria |
|---|-------|---------------|
| 19 | Impl README links frozen template + plan | Present |
| 20 | `governance/PHASE_3_1_IMPLEMENTATION_REVIEW.md` written | Present |
| 21 | [ACCEPTANCE_PLAN.md](ACCEPTANCE_PLAN.md) completed | ACCEPTED or REJECTED |

---

## Decision

| # | Action |
|---|--------|
| 22 | **Accept** → record sign-off in implementation review |
| 23 | **Rollback** → [ROLLBACK_PLAN.md](ROLLBACK_PLAN.md) if any critical row fails |

**Critical failures (immediate rollback):** auto-publish, approval bypass, protected folder edit, runtime folder created.
