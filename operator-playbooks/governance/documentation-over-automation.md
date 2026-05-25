# Documentation Over Automation

Phase 2.6 adds **guides**, not **runners**.

---

## Why

- Automation hides governance questions behind green/red
- New operators need mental model, not dashboard
- CI drift already rejected in Phase 2.5

---

## Use existing automation sparingly

Only Phase 2.5 scripts — invoked manually:

- `evaluation/scripts/run_demo_smoke_checks.py`
- `evaluation/scripts/check_expected_text_traces.py`
- `evaluation/scripts/summarize_evaluation_status.py`

**Do not add** Phase 2.6 scripts, CLI tools, or dashboards.

---

## When docs beat scripts

- Onboarding narrative
- Troubleshooting judgment calls
- Explaining *why* critic != truth
- Deciding rollback vs forward fix

---

## Test

If solution is "build a tool" — first write a runbook. Tool needs new phase charter.
