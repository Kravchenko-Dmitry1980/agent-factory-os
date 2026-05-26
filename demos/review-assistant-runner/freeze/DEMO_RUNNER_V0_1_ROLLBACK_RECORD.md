# Demo Runner v0.1 — Rollback Record

**Version:** demo-runner-v0.1  
**Date:** 2026-05-26

---

## Rollback target

Remove or revert Demo Runner while keeping Review Assistant and evaluation baseline intact.

---

## Files to remove/revert

| Path | Action |
|------|--------|
| `demos/review-assistant-runner/demo_runner.py` | remove |
| `demos/review-assistant-runner/*.md` | remove (runner docs) |
| `demos/review-assistant-runner/freeze/` | remove (freeze docs) |
| `demos/review-assistant-runner/transcripts/` | remove (operator-local) |
| Navigation links in `START_HERE_RU.md`, `governance/README.md`, etc. | revert |

Optional: remove `governance/PHASE_3_5_2_DEMO_RUNNER_IMPL_REVIEW.md` and freeze governance review if full rollback of phase.

---

## Keep unchanged

| Artifact | Reason |
|----------|--------|
| Review Assistant Thin v0.3 | Independent frozen demo |
| Provider safety harness v0.1 | Independent eval |
| Hands-on demo report (Phase 3.5.1) | Independent operator record |
| Task Triage specs v0.1 | Independent specs |
| `minimal_demo.py` | Agent logic — never modified by runner |

---

## Rollback triggers

| Trigger | Severity |
|---------|----------|
| Runner changes agent behavior | **critical** |
| Runner calls provider by default | **critical** |
| Runner introduces dependencies | **high** |
| Runner becomes framework / plugin system | **high** |
| Runner becomes UI platform | **high** |
| Secrets appear in transcript | **critical** |
| Baseline checks fail after runner change | **high** |
| Protected folders modified by runner phase | **critical** |

---

## Rollback steps

1. Stop using Demo Runner in operator docs
2. Remove or git-revert `demos/review-assistant-runner/` (except if keeping docs-only)
3. Revert navigation links in governance / START_HERE / playbooks
4. Rerun baseline checks:

```powershell
cd C:\Dima\Projects\CURSOR\AGENT
python evaluation/scripts/check_review_assistant_provider_safety.py
python evaluation/scripts/check_review_assistant_thin.py
python evaluation/scripts/check_review_assistant_llm_mock.py
python evaluation/scripts/check_review_assistant_real_provider_contract.py
python evaluation/scripts/run_demo_smoke_checks.py
python evaluation/scripts/check_expected_text_traces.py
```

5. Document rollback in governance (new review or amendment)
6. Confirm direct demo still works:

```powershell
python prototypes-derived/review-assistant-thin/minimal_demo.py --scenario happy
```

---

## Post-rollback operator path

Use direct commands from [../../review-assistant-hands-on/COMMANDS_RUN.md](../../review-assistant-hands-on/COMMANDS_RUN.md).

Demo Runner v0.1 is optional UX — Review Assistant remains usable without it.
