# Demo Runner v0.1 — Limitations

**Version:** demo-runner-v0.1  
**Date:** 2026-05-26  
**Status:** FROZEN_WITH_NOTES

---

## What v0.1 proves

| Capability | Status |
|------------|--------|
| Operator can list 15 scenarios | yes |
| Operator can run scenario by name (`--scenario`) | yes |
| Operator can use interactive menu | yes |
| Operator receives Russian summary | yes |
| TRACE events are explained in Russian | yes |
| Safety status is visible (OK/BLOCKED/ESCALATED/FAILED/WARNING) | yes |
| Baseline checks runnable from menu (Group 4) | yes |
| Real provider protected behind confirmation | yes |
| No agent logic change | yes |
| Stdlib only, no new dependencies | yes |

---

## What v0.1 does not prove

| Gap | Notes |
|-----|-------|
| Product readiness | Lab CLI wrapper only |
| Real UI usability | Terminal only |
| Free-form task input | Fixed frozen scenarios only |
| Real human approval UI | Mock/scenario approval only |
| Session management | No history browser |
| Dashboard | None |
| Operator Console | Explicitly out of scope |
| Production deployment | Not a deployable service |
| Task Triage implementation | Specs only (separate artifact) |
| Model quality on arbitrary prompts | Synthetic/frozen scenarios only |

---

## Weakest area (from Phase 3.5.2-Impl)

Runner is still **terminal CLI**, not product UI. Risk: operators may confuse Demo Runner with Operator Console or production product.

Mitigation: freeze status, limitations doc, governance disclaimers in README and START_HERE_RU.

---

## Why this is acceptable

v0.1 is a **CLI demo wrapper**, not product UI.

Goal: make Review Assistant **touchable** for operators and trainees with Russian explanations — without changing agent behavior or introducing platform drift.

---

## Acceptable next steps (not part of v0.1)

- Phase 3.5.3-Plan — Interactive Free-Form CLI
- Phase 3.6-Plan — Task Triage Thin Implementation Plan
- Git tag `demo-runner-v0.1` after commit

Any expansion requires new phase + change lock process.
