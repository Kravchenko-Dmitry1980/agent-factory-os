# Rollback and Freeze Plan — Phase 3.2

---

## If future LLM adapter implementation fails

| Step | Action |
|------|--------|
| 1 | Stop work — do not patch frozen thin v0.1 to "fix" adapter |
| 2 | Remove or revert adapter folder only (e.g. `review-assistant-llm-mock/`) |
| 3 | Keep **Review Assistant thin v0.1** frozen impl unchanged |
| 4 | Keep frozen **spec** body unchanged |
| 5 | Re-run baselines |

```powershell
cd C:\Dima\Projects\CURSOR\AGENT
python evaluation/scripts/check_review_assistant_thin.py
python evaluation/scripts/run_demo_smoke_checks.py
python evaluation/scripts/check_expected_text_traces.py
```

| 6 | Document rollback in governance review |
| 7 | Do **not** weaken safety gates or eval scripts |

---

## Rollback triggers

- LLM output bypasses verification or approval
- Auto-publish appears
- Adapter grows into registry/router/framework
- Protected folders modified
- New dependency added without approval
- Mock eval fails

---

## Future successful adapter freeze

Separate from thin v0.1:

| Item | Action |
|------|--------|
| Freeze record | `prototypes-derived/review-assistant-llm-mock/freeze/` (future) |
| Tag | `review-assistant-llm-mock-v0.1` |
| Eval | New check script PASS before freeze |
| Thin v0.1 | Remains frozen — adapter is additive |

---

## Do not

- Merge adapter into shared runtime
- Patch observability examples to match adapter
- Edit frozen template spec to match broken adapter

---

## Reference

[prototypes-derived/review-assistant-thin/freeze/ROLLBACK_RECORD.md](../../prototypes-derived/review-assistant-thin/freeze/ROLLBACK_RECORD.md)
