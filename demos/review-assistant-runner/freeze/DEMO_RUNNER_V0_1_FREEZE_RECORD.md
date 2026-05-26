# Demo Runner v0.1 — Freeze Record

**Date:** 2026-05-26  
**Phase:** 3.5.2-Freeze

---

## Artifact Name

**Review Assistant Demo Runner**

---

## Version

**v0.1** (`demo-runner-v0.1`)

---

## Status

**FROZEN_WITH_NOTES**

Notes: terminal CLI wrapper only — not product UI, not Operator Console, not runtime.

---

## Frozen Path

`demos/review-assistant-runner/`

---

## Frozen Script

`demos/review-assistant-runner/demo_runner.py`

Single stdlib-only Python script. Behavior frozen as of Phase 3.5.2-Impl validation (2026-05-26).

---

## Freeze Meaning

Future changes to Demo Runner require:

1. Change proposal
2. UX impact review
3. No-agent-logic-change review
4. Provider safety review (if real provider behavior changes)
5. Transcript safety review (if saving behavior changes)
6. Validation run (runner + baseline checks)
7. Rollback plan
8. Explicit approval

See [DEMO_RUNNER_V0_1_CHANGE_LOCK.md](DEMO_RUNNER_V0_1_CHANGE_LOCK.md).

---

## What is frozen

| Baseline | Document |
|----------|----------|
| 15-item menu | [DEMO_RUNNER_V0_1_MENU_BASELINE.md](DEMO_RUNNER_V0_1_MENU_BASELINE.md) |
| Supported commands | [DEMO_RUNNER_V0_1_COMMAND_BASELINE.md](DEMO_RUNNER_V0_1_COMMAND_BASELINE.md) |
| Validation record | [DEMO_RUNNER_V0_1_VALIDATION_RECORD.md](DEMO_RUNNER_V0_1_VALIDATION_RECORD.md) |
| Real provider policy | [DEMO_RUNNER_V0_1_REAL_PROVIDER_POLICY.md](DEMO_RUNNER_V0_1_REAL_PROVIDER_POLICY.md) |
| Transcript policy | [DEMO_RUNNER_V0_1_TRANSCRIPT_POLICY.md](DEMO_RUNNER_V0_1_TRANSCRIPT_POLICY.md) |

---

## No-agent-logic-change guarantee

Demo Runner v0.1:

- Does **not** modify `prototypes-derived/review-assistant-thin/minimal_demo.py`
- Does **not** modify `evaluation/scripts/`
- Does **not** import project modules
- Runs existing commands via subprocess only

Review Assistant Thin v0.3, provider safety harness v0.1, and Task Triage specs v0.1 remain independent frozen artifacts.

---

## Important note

**Demo Runner is not product UI and not runtime.**

It improves operator UX for touching Review Assistant scenarios. It must not be confused with Operator Console or a production deployment surface.
