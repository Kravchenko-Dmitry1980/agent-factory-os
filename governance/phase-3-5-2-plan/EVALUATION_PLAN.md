# Evaluation Plan — Demo Runner (Future)

**Date:** 2026-05-26  
**Status:** PLAN_ONLY — no pytest, no CI

Future Demo Runner v0.1 validated by **manual checks + existing baseline scripts**.

---

## Runner-specific checks (manual)

| # | Check | Expected |
|---|-------|----------|
| R01 | Menu displays all groups 1–4 | All items visible with Russian titles |
| R02 | happy scenario runs via menu | subprocess success, summary printed |
| R03 | missing_approval via menu | decision=BLOCKED in summary |
| R04 | unsafe_publish_attempt via menu | FAILED + unsafe mentioned |
| R05 | Russian summary appears | Structured block in Russian |
| R06 | Final decision parsed correctly | Matches raw stdout decision= line |
| R07 | Key trace events listed | At least 2 events for each demo scenario |
| R08 | Real provider menu shows warning | Warning text before confirm |
| R09 | Real provider default N | Enter → no subprocess with --real-provider |
| R10 | Direct CLI unchanged | Same output if run minimal_demo.py directly |
| R11 | Group 4 harness item | PASS=16 FAIL=0 displayed |
| R12 | No secrets in default summary | Env not dumped |

---

## Real provider optional check (manual only)

| # | Check | Condition |
|---|-------|-----------|
| P01 | real_provider_synthetic with yes + LM Studio | Operator manual; not Cursor CI |
| P02 | DELIVERED summary mentions unverified | Russian text |
| P03 | Env missing → abort | No network call |

**Cursor must not run P01 in automation.**

---

## Regression checks (must remain PASS)

After runner impl, re-run unchanged:

```powershell
python evaluation/scripts/check_review_assistant_provider_safety.py
python evaluation/scripts/check_review_assistant_thin.py
python evaluation/scripts/check_review_assistant_llm_mock.py
python evaluation/scripts/check_review_assistant_real_provider_contract.py
python evaluation/scripts/run_demo_smoke_checks.py
python evaluation/scripts/check_expected_text_traces.py
```

| Script | Expected |
|--------|----------|
| provider safety | PASS=16 FAIL=0 |
| thin | PASS=5 FAIL=0 |
| mock LLM | PASS=5 FAIL=0 |
| real provider contract | PASS=2 FAIL=0 |
| smoke | PASS=12 FAIL=0 |
| trace | PASS=6 FAIL=0 |

---

## Not in evaluation scope

- pytest suite for runner
- CI job for runner
- Benchmark runner performance
- Live injection through runner
- Cross-platform TUI testing matrix

---

## Fail criteria

| Fail | Action |
|------|--------|
| Baseline any FAIL | Block release, rollback runner |
| Runner changes demo output | Violation — rollback |
| Provider runs without confirm | Violation — fix or rollback |
| Dependency added | Violation — reject impl |

See [ACCEPTANCE_CRITERIA.md](ACCEPTANCE_CRITERIA.md).
