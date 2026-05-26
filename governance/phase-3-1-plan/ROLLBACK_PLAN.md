# Rollback Plan — Phase 3.1 Thin Review Assistant

---

## Before code (pre-implementation)

| Step | Action |
|------|--------|
| 1 | `git status` — working tree clean or intentional commits only |
| 2 | Commit plan + any governance docs |
| 3 | Optional tag: `git tag phase-3.1-pre-impl` |
| 4 | Record smoke/trace baseline output in implementation review prep |
| 5 | Confirm [PRE_IMPLEMENTATION_CHECKLIST.md](PRE_IMPLEMENTATION_CHECKLIST.md) complete |

---

## If implementation fails

| Step | Action |
|------|--------|
| 1 | **Do not patch blindly** — read trace first |
| 2 | Compare behavior to [BEHAVIOR_CONTRACT.md](BEHAVIOR_CONTRACT.md) and frozen [evaluation.md](../../agent-builder-kit/templates/review-assistant-agent/evaluation.md) |
| 3 | Identify failure class: approval / trace / scope drift |
| 4 | **Revert** only `prototypes-derived/review-assistant-thin/` (delete folder or `git revert` commits) |
| 5 | **Do not modify** frozen Review Assistant spec to match bad impl |
| 6 | **Do not modify** prototypes/, eval scripts, observability examples |
| 7 | Re-run smoke + trace scripts — must return PASS=12, PASS=6 |
| 8 | Document in `governance/PHASE_3_1_IMPLEMENTATION_REVIEW.md` (rollback section) |

---

## Rollback triggers (stop and revert)

| Trigger | Severity |
|---------|----------|
| Auto-publish appears | critical |
| Approval bypass appears | critical |
| Runtime/framework folder appears | critical |
| Shared abstraction `shared/` / `engine/` extracted | high |
| Tests/evaluation fail on safety scenarios | high |
| Trace missing on any scenario | high |
| Behavior unclear vs frozen spec | medium — hold, do not expand scope |
| New dependency added without approval | medium |
| Protected folder modified | critical |

---

## Rollback commands (reference)

```powershell
cd C:\Dima\Projects\CURSOR\AGENT
# If impl was committed:
git log --oneline -5
git revert <commit-range>   # or remove folder if uncommitted

# Verify baseline
python evaluation/scripts/run_demo_smoke_checks.py
python evaluation/scripts/check_expected_text_traces.py
```

---

## What rollback preserves

- Frozen Review Assistant v0.1 spec
- Phase 2 prototypes and harness
- Phase 3.1-Plan documents (this folder)
- Builder Kit spec-only status

---

## What rollback removes

- `prototypes-derived/review-assistant-thin/` implementation only
- Any unauthorized deps in `requirements.txt` (revert commit)

---

## Diagram

[diagrams/rollback-flow.md](diagrams/rollback-flow.md)

---

## Post-rollback decision

| Outcome | Next step |
|---------|-----------|
| Fixable in impl scope | New impl attempt after root-cause doc |
| Spec gap discovered | Change proposal on frozen template — not silent spec edit |
| Scope creep detected | Re-read [NO_RUNTIME_DECISION.md](NO_RUNTIME_DECISION.md); shrink scope |
