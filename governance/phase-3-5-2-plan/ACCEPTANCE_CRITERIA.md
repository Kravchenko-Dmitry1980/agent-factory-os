# Acceptance Criteria — Demo Runner (Future Impl)

**Date:** 2026-05-26  
**Status:** PLAN_ONLY — evidence filled in Phase 3.5.2-Impl

Future implementation accepted only if all criteria pass.

---

## Checklist

| Criterion | Required | Future Evidence |
|-----------|----------|-----------------|
| One script only | yes | `demos/review-assistant-runner/demo_runner.py` |
| Stdlib only | yes | No imports from rich/typer/click; no requirements.txt |
| No agent logic change | yes | git diff clean on `minimal_demo.py` |
| No new scenarios | yes | Menu matches SCENARIO_MENU_PLAN only |
| No provider call by default | yes | Group 3 requires confirm; default N |
| Russian summary exists | yes | OPERATOR_OUTPUT_FORMAT block printed |
| Menu exists | yes | Groups 1–4 selectable |
| Final decision shown | yes | Parsed decision= in summary |
| Trace explanation shown | yes | Key events from mapping table |
| Unsafe scenario remains blocked | yes | unsafe_publish_attempt → FAILED in summary |
| Real provider warning | yes | REAL_PROVIDER_WARNING_POLICY text |
| Baseline checks pass | yes | All 6 scripts PASS |
| No runtime/factory drift | yes | Single script, no plugins |
| No UI/web | yes | Terminal only |
| Transcript optional only | yes | Not auto-save |
| README in runner folder | yes | Run instructions + warnings |
| Governance impl review | yes | PHASE_3_5_2_IMPL review doc |

---

## Scope compliance

- [ ] Does not modify evaluation/scripts/
- [ ] Does not modify prototypes-derived/review-assistant-thin/ (except none)
- [ ] Does not add dependencies
- [ ] Does not call provider in CI

---

## Sign-off gate (future)

| Reviewer | Date | Verdict |
|----------|------|---------|
| | | PASS / FAIL |

Not applicable in Plan phase.
