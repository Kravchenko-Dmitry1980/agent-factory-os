# Real Provider Evaluation Plan

**Phase 3.3-Plan** — future eval requirements. **No benchmark leaderboard. No model scoring.**

---

## Goals

Prove real provider path preserves v0.2 safety chain:

```text
parse → safety → verification → approval → delivery/block
```

---

## Required behaviors (future)

| # | Behavior | Pass criterion |
|---|----------|----------------|
| 1 | Valid provider output | DELIVERED only after parse + verify + approval |
| 2 | Malformed live response | Rejected; no approval |
| 3 | Timeout | Escalates; no fallback draft |
| 4 | Unsafe output | Blocked before delivery |
| 5 | Uncertain output | Escalates; no delivery |
| 6 | Injection-like output | Blocked or escalated |
| 7 | No key leakage | Grep traces/logs for key patterns — none |
| 8 | No external call by default | Mock mode: zero network |
| 9 | No provider framework | Code review: no registry/router |
| 10 | Regression | All v0.2 checks still PASS in mock mode |

---

## Script baseline (must remain passing)

```powershell
python evaluation/scripts/check_review_assistant_thin.py      # PASS=5
python evaluation/scripts/check_review_assistant_llm_mock.py  # PASS=5
python evaluation/scripts/run_demo_smoke_checks.py            # PASS=12
python evaluation/scripts/check_expected_text_traces.py       # PASS=6
```

---

## Future scripts (impl phase — not created now)

| Script | Purpose |
|--------|---------|
| `check_review_assistant_provider_real.py` | Live provider scenarios — **opt-in**, requires env + flag |
| Manual checklist | `evaluation/review-assistant-thin/provider-scenario-checklist.md` |

Real-provider check must:

- Skip automatically if env var missing (NOT_RUN, not FAIL)
- Never run in CI by default
- Use synthetic scenarios only for first test

---

## Scenario set (future — mirrors mock)

| Scenario | Expected |
|----------|----------|
| provider_valid_draft | DELIVERED (live) |
| provider_malformed_output | FAILED |
| provider_timeout | ESCALATED |
| provider_uncertain | ESCALATED |
| provider_unsafe_output | FAILED |

May reuse mock scenario names with `--provider-mode real` or parallel names — decided at impl.

---

## Explicit non-goals

- Model quality benchmarks
- Multi-provider comparison runs
- Leaderboards / scoring platforms
- pytest suite expansion as "framework"
- Production load testing

---

## Acceptance gate (future freeze v0.3)

All mock checks PASS + real provider check PASS (when env present) + security checklist signed + freeze record.

---

## References

- v0.2 validation: `prototypes-derived/review-assistant-thin/freeze/V0_2_VALIDATION_RECORD.md`
- Phase 3.2 eval plan: [../phase-3-2-plan/LLM_EVALUATION_PLAN.md](../phase-3-2-plan/LLM_EVALUATION_PLAN.md)
