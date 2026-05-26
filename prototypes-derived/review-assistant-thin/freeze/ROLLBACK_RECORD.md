# Rollback Record — Review Assistant Thin v0.1

**Recorded:** 2026-05-26

---

## When to rollback

- Auto-publish or approval bypass in impl
- Scenario baseline check fails after change
- Runtime/factory/second-agent drift
- Protected folder accidentally modified

---

## Rollback steps

1. Stop changes
2. Revert or delete:

   ```text
   prototypes-derived/review-assistant-thin/
   ```

   (except if only rolling back impl body — keep `freeze/` history if useful)

3. **Do not** modify frozen Review Assistant **spec** body
4. **Do not** modify `prototypes/`, `integrations-real/`, `evaluation/scripts/` (except removing `check_review_assistant_thin.py` if full rollback of hardening)

5. Re-run baselines:

   ```powershell
   cd C:\Dima\Projects\CURSOR\AGENT
   python evaluation/scripts/run_demo_smoke_checks.py
   python evaluation/scripts/check_expected_text_traces.py
   python evaluation/scripts/check_review_assistant_thin.py
   ```

6. Document in `governance/PHASE_3_1_1_FREEZE_HARDEN_REVIEW.md` or new rollback note

---

## Git

```powershell
git revert <commits>
# optional restore tag review-assistant-thin-v0.1
```

---

## Preserve

- Frozen template v0.1 spec
- Phase 3.1-Plan docs
- Phase 2 prototypes and harness

---

## Pre-freeze tag

Suggested: `review-assistant-thin-v0.1` at freeze commit.
