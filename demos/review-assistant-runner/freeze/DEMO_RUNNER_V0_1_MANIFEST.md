# Demo Runner v0.1 — Manifest

**Version:** demo-runner-v0.1  
**Date:** 2026-05-26  
**Status:** FROZEN_WITH_NOTES

---

## File manifest

| File | Purpose | Frozen? | Notes |
|------|---------|---------|-------|
| `demo_runner.py` | Single stdlib CLI wrapper | **yes** | Subprocess only; no agent logic |
| `README.md` | English overview + freeze status | yes | Navigation/status updates allowed |
| `USAGE_RU.md` | Russian step-by-step usage | yes | Operator guide |
| `SCENARIO_GUIDE_RU.md` | All 15 menu items | yes | Fixed menu reference |
| `TRACE_SUMMARY_MAPPING_RU.md` | TRACE event → RU mapping | yes | Summary helper |
| `TRANSCRIPT_POLICY_RU.md` | Transcript + secret safety (RU) | yes | Operator-facing policy |
| `ROLLBACK.md` | How to remove runner | yes | Rollback guide |
| `freeze/` | Freeze records (this folder) | yes | Documentation only |
| `transcripts/` | Optional saved transcripts | no | Operator-local; not part of freeze artifact |
| `governance/PHASE_3_5_2_DEMO_RUNNER_IMPL_REVIEW.md` | Impl review | yes | Phase 3.5.2-Impl |
| `governance/PHASE_3_5_2_FREEZE_DEMO_RUNNER_V0_1_REVIEW.md` | Freeze review | yes | Phase 3.5.2-Freeze |

---

## Technical properties (frozen)

| Property | Value |
|----------|-------|
| Language | Python 3.12+ |
| Dependencies | **stdlib only** |
| Integration | subprocess wrapper only |
| Agent logic change | **no** |
| Provider call by default | **no** |
| Runtime / factory | **no** |
| External packages | **no** |
| UI / web app | **no** |

---

## Wrapped commands (not modified)

| Target | Path |
|--------|------|
| Review Assistant Thin demo | `prototypes-derived/review-assistant-thin/minimal_demo.py` |
| Evaluation scripts | `evaluation/scripts/check_*.py`, `run_demo_smoke_checks.py` |

Runner invokes these; it does not embed or alter their logic.
