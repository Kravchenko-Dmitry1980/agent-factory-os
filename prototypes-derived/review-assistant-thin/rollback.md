# Rollback — Review Assistant Thin

## When to rollback

- Auto-publish or approval bypass observed
- Smoke/trace baseline fails after impl added
- Scope creep (runtime folder, deps, second agent)
- Protected folder accidentally modified

## Steps

1. Stop further changes
2. Delete or revert only:

   ```text
   prototypes-derived/review-assistant-thin/
   ```

   (Keep `prototypes-derived/README.md` if other demos added later)

3. **Do not** modify frozen template specs to match bad code
4. **Do not** modify `prototypes/`, `evaluation/scripts/`, observability examples

5. Re-run baseline:

   ```powershell
   cd C:\Dima\Projects\CURSOR\AGENT
   python evaluation/scripts/run_demo_smoke_checks.py
   python evaluation/scripts/check_expected_text_traces.py
   python evaluation/scripts/check_review_assistant_thin.py
   python evaluation/scripts/check_review_assistant_llm_mock.py
   ```

6. Document in governance review

## Rollback LLM mock only (Phase 3.2)

Revert `minimal_demo.py` to pre-LLM commit or remove LLM scenarios/functions while keeping original 5 scenarios. Remove `check_review_assistant_llm_mock.py` if full LLM rollback. Re-run thin check PASS=5.

## Steps (full rollback)

```powershell
git revert <impl-commits>
# or remove folder if uncommitted
```

Optional pre-impl tag: `phase-3.1-pre-impl`

## Preserve

- Frozen Review Assistant v0.1 spec
- Phase 3.1-Plan documents
- Phase 2 prototypes and harness

See `governance/phase-3-1-plan/ROLLBACK_PLAN.md`
