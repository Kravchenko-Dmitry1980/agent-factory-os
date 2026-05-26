# Rollback Record — Task Triage Agent Specs v0.1

**Date:** 2026-05-26  
**Artifact:** task-triage-agent-specs-v0.1

---

## Rollback Target

If Task Triage specs must be reverted, remove or revert:

| Item | Action |
|------|--------|
| `agent-builder-kit/templates/task-triage-agent/` | Remove entire folder OR revert to pre-3.5-Impl commit |
| Sign-off records | Remove with folder |
| Navigation links | Revert in agent-builder-kit/README.md, governance/README.md |
| Freeze governance review | Revert or mark SUPERSEDED |

---

## Keep Unchanged

| Item | Reason |
|------|--------|
| Review Assistant template (frozen) | Independent agent line |
| review-assistant-thin v0.1 / v0.2 / v0.3 | Frozen implementation |
| Provider safety harness v0.1 | Frozen eval |
| Agent Builder Kit base structure | Shared kit |
| evaluation/scripts/* | Protected — no triage scripts added |
| governance/phase-3-5-plan/* | Historical plan record |
| governance/PHASE_3_5_TASK_TRIAGE_AGENT_SPECS_REVIEW.md | Impl phase record |

---

## Rollback Triggers

| Trigger | Severity |
|---------|----------|
| Spec drift into execution | Critical |
| Spec drift into orchestrator | Critical |
| Hidden provider behavior in specs | Critical |
| Hidden memory behavior in specs | High |
| Acceptance criteria incomplete | High |
| Safety gates missing or weakened | Critical |
| Baseline checks fail after spec change | Critical |
| Protected folders modified | Critical |
| Implementation created without GO/NO-GO | Critical |

---

## Rollback Steps

1. Stop any work treating Task Triage as implementation-ready
2. Remove or git-revert `agent-builder-kit/templates/task-triage-agent/`
3. Revert navigation entries in README files
4. Document rollback in new governance review (verdict: ROLLED_BACK)
5. Re-run baseline checks:

```powershell
cd C:\Dima\Projects\CURSOR\AGENT
python evaluation/scripts/check_review_assistant_provider_safety.py
python evaluation/scripts/check_review_assistant_thin.py
python evaluation/scripts/check_review_assistant_llm_mock.py
python evaluation/scripts/check_review_assistant_real_provider_contract.py
python evaluation/scripts/run_demo_smoke_checks.py
python evaluation/scripts/check_expected_text_traces.py
```

6. Confirm PASS on all six scripts before closing rollback

---

## Rollback Does Not Affect

- Review Assistant thin demo
- Provider safety harness
- Phase 3.0–3.4 frozen artifacts
- Agent Builder Kit v0.1 core (template-specs, safety-gates, etc.)

---

## Contact / Authority

Rollback requires explicit human approval. Automated agents must not silently delete frozen specs without governance record.
