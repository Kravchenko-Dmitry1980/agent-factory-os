# Provider Safety Harness — Freeze Index

**Freeze record for Provider Safety Harness v0.1** (`provider-safety-harness-v0.1`)

---

## What this folder is

Governance and baseline documentation for the **frozen** minimal provider safety harness created in Phase 3.4-Impl and frozen in Phase 3.4.1.

This is a **freeze phase** — no new behavior, no new cases, no expansion.

---

## What was frozen

| Artifact | Path |
|----------|------|
| Harness script | `evaluation/scripts/check_review_assistant_provider_safety.py` |
| Case matrix | 16 synthetic cases (groups A–G) |
| Classification rules | Local deterministic v0.3-aligned logic in script |
| Documentation | `evaluation/review-assistant-thin/provider-safety/` |

---

## What freeze means

- No new cases without change proposal
- No behavior change without approval
- No benchmark expansion
- No red-team platform expansion
- No provider calls without separate phase
- No pytest/CI without separate phase

---

## Current status

**FROZEN_WITH_NOTES**

Harness is useful and validated, but still local/synthetic and not production QA or live prompt-injection proof.

---

## Freeze documents

| File | Purpose |
|------|---------|
| [HARNESS_V0_1_FREEZE_RECORD.md](HARNESS_V0_1_FREEZE_RECORD.md) | Official freeze record |
| [HARNESS_V0_1_MANIFEST.md](HARNESS_V0_1_MANIFEST.md) | Frozen file manifest |
| [HARNESS_V0_1_CASE_MATRIX.md](HARNESS_V0_1_CASE_MATRIX.md) | 16-case matrix (frozen) |
| [HARNESS_V0_1_VALIDATION_RECORD.md](HARNESS_V0_1_VALIDATION_RECORD.md) | Observed validation results |
| [HARNESS_V0_1_SCOPE_LOCK.md](HARNESS_V0_1_SCOPE_LOCK.md) | In/out of scope |
| [HARNESS_V0_1_LIMITATIONS.md](HARNESS_V0_1_LIMITATIONS.md) | What v0.1 proves and does not prove |
| [HARNESS_V0_1_CHANGE_LOCK.md](HARNESS_V0_1_CHANGE_LOCK.md) | Change control after freeze |
| [HARNESS_V0_1_ROLLBACK_RECORD.md](HARNESS_V0_1_ROLLBACK_RECORD.md) | Rollback procedure |

---

## Related

- Implementation baseline: [review-assistant-thin-v0.3](../../../../prototypes-derived/review-assistant-thin/freeze/V0_3_FREEZE_RECORD.md)
- Phase 3.4-Impl review: [PHASE_3_4_PROVIDER_SAFETY_HARNESS_REVIEW.md](../../../../governance/PHASE_3_4_PROVIDER_SAFETY_HARNESS_REVIEW.md)
- Phase 3.4.1 review: [PHASE_3_4_1_FREEZE_PROVIDER_SAFETY_HARNESS_V0_1_REVIEW.md](../../../../governance/PHASE_3_4_1_FREEZE_PROVIDER_SAFETY_HARNESS_V0_1_REVIEW.md)
