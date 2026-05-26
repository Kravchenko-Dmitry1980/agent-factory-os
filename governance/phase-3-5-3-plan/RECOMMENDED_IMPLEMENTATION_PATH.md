# Recommended Implementation Path — Free-Form CLI

**Date:** 2026-05-26  
**Status:** PLAN_ONLY

---

## Recommendation

**Phase 3.5.3-Impl — Minimal Interactive Free-Form CLI**

**Option B:** separate stdlib script, do **not** modify demo-runner-v0.1.

---

## Future artifact layout

```text
demos/review-assistant-freeform/
├── free_form_cli.py          # one stdlib script (future)
├── README.md                 # future impl
├── USAGE_RU.md               # future impl
└── transcripts/              # optional, operator-local
```

Governance freeze folder (future): `demos/review-assistant-freeform/freeze/` after 3.5.3-Freeze.

---

## Implementation constraints (future)

| Constraint | Required |
|------------|----------|
| One stdlib script | yes |
| No pip dependencies | yes |
| No agent logic modification | yes — `minimal_demo.py` untouched |
| No demo_runner.py modification | yes — unless separate change proposal |
| No runtime / factory | yes |
| No provider default call | yes — Mode 1 default |
| No memory / database | yes |
| Transcript optional only | yes — explicit flag |
| No cloud provider | yes |
| Single task per run | yes |
| Russian summary | yes |

---

## Suggested impl sequence

1. Input gate + empty/secret reject
2. Mode 1 mock path end-to-end (draft → verify → approval → summary)
3. TRACE + OUTPUT_FORMAT_RU blocks
4. `--save-transcript` optional
5. Mode 2 provider (confirmation + env) — last, manual test only
6. Manual eval per [EVALUATION_PLAN.md](EVALUATION_PLAN.md)
7. Baseline regression
8. Phase 3.5.3-Freeze

---

## Code reuse strategy

| Reuse | Approach |
|-------|----------|
| TRACE RU strings | Copy pattern from demo_runner (docs parity), no import from runner |
| Thin demo behavior | Mirror gate **logic** in freeform script OR subprocess — prefer self-contained mock in v1 to avoid coupling |
| Provider boundary | Mirror env check + confirmation from runner **policy**, not code import |

**No imports from project modules** (same rule as Demo Runner).

---

## Do not modify

- `demos/review-assistant-runner/demo_runner.py` (FROZEN_WITH_NOTES)
- `prototypes-derived/review-assistant-thin/minimal_demo.py`
- `evaluation/scripts/*`

---

## Next prompt (after plan approval)

```text
Start Phase 3.5.3-Impl — Minimal Interactive Free-Form CLI
```

User must say this explicitly per [PRECONDITIONS_FOR_3_5_3_IMPL.md](PRECONDITIONS_FOR_3_5_3_IMPL.md).
