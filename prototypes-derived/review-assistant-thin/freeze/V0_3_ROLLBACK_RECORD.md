# Rollback Record — Review Assistant Thin v0.3

Rollback procedure if real provider boundary or v0.3 state becomes unsafe or unstable.

---

## Rollback target

Return to **v0.2 mock LLM boundary baseline**:

- `review-assistant-thin-v0.2`
- 10 scenarios (5 original + 5 LLM mock)
- No real provider network path
- Records: [V0_2_FREEZE_RECORD.md](V0_2_FREEZE_RECORD.md), [V0_2_ROLLBACK_RECORD.md](V0_2_ROLLBACK_RECORD.md)

Alternative partial rollback: **disable real provider boundary** while keeping v0.1 + v0.2 scenarios — equivalent to reverting Phase 3.3 impl changes in `minimal_demo.py` and related docs.

---

## Rollback triggers

| Trigger | Severity |
|---------|----------|
| Real provider call without explicit `--real-provider` | **Critical** |
| Secret appears in logs or traces | **Critical** |
| Secret appears in repo | **Critical** |
| Cloud provider call happens unexpectedly | **Critical** |
| Provider framework starts forming | **High** |
| Runtime / factory drift appears | **High** |
| Provider output bypasses verification | **Critical** |
| Provider output bypasses approval | **Critical** |
| Unsafe provider output delivered | **Critical** |
| Baseline checks fail after provider change | **High** |
| Local endpoint causes unstable demo behavior | **Medium** |

---

## Rollback steps

1. **Stop** live provider testing immediately
2. **Revert** Phase 3.3 real provider boundary changes in `minimal_demo.py` and provider docs (git revert or manual restore to v0.2 tag)
3. **Keep** v0.2 mock baseline intact
4. **Keep** frozen Agent Builder Kit specs unchanged
5. **Remove or archive** v0.3 freeze claims if rollback is permanent
6. **Re-run** validation:

```powershell
cd C:\Dima\Projects\CURSOR\AGENT

python evaluation/scripts/check_review_assistant_thin.py
python evaluation/scripts/check_review_assistant_llm_mock.py
python evaluation/scripts/run_demo_smoke_checks.py
python evaluation/scripts/check_expected_text_traces.py
```

Expected after rollback to v0.2:

- PASS=5 FAIL=0 (thin)
- PASS=5 FAIL=0 (mock)
- PASS=12 FAIL=0 (smoke)
- PASS=6 FAIL=0 (trace)
- Real provider script absent or not applicable

7. **Document** rollback in governance (incident note — no secrets in note)
8. **Update** freeze index to point current version back to v0.2 if permanent

---

## Git reference

If tagged:

```powershell
git checkout review-assistant-thin-v0.2 -- prototypes-derived/review-assistant-thin/
```

Review diff before commit. Do not force-push without explicit approval.

---

## What rollback does NOT do

| Item | Status |
|------|--------|
| Change frozen Agent Builder Kit spec | no |
| Delete v0.1 / v0.2 history | no — preserved |
| Add provider framework | no |
| Add cloud provider | no |

---

## Version history

| Version | Rollback record |
|---------|-----------------|
| v0.1 | [ROLLBACK_RECORD.md](ROLLBACK_RECORD.md) |
| v0.2 | [V0_2_ROLLBACK_RECORD.md](V0_2_ROLLBACK_RECORD.md) |
| **v0.3** | **This file** — rollback to v0.2 |

---

## Post-rollback next step

Pause provider work. Re-plan under new phase with security review before re-adding real boundary.
