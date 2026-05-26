# Phase 3.1 Preconditions

**Purpose:** Exact requirements before any Phase 3.1 **code** work on Review Assistant.

**Phase 3.0-Freeze does NOT start Phase 3.1.** This document defines gates only.

---

## Required before code

| # | Requirement | Verification |
|---|-------------|--------------|
| P1 | User explicitly says: **«Start Phase 3.1 thin implementation of Review Assistant.»** | User message |
| P2 | Smoke checks pass | `python evaluation/scripts/run_demo_smoke_checks.py` → PASS=12 FAIL=0 |
| P3 | Trace checks pass | `python evaluation/scripts/check_expected_text_traces.py` → PASS=6 FAIL=0 |
| P4 | Review Assistant v0.1 **frozen** | [FREEZE_RECORD.md](../agent-builder-kit/templates/review-assistant-agent/sign-off/FREEZE_RECORD.md) FROZEN_WITH_NOTES |
| P5 | Human lead sign-off recorded or explicitly acknowledged pending | [REVIEW_ASSISTANT_V0_1_SIGN_OFF.md](../agent-builder-kit/templates/review-assistant-agent/sign-off/REVIEW_ASSISTANT_V0_1_SIGN_OFF.md) |
| P6 | Scope limited to **one thin implementation** | This document |
| P7 | No factory | [no-factory-yet-policy.md](../agent-builder-kit/governance/no-factory-yet-policy.md) |
| P8 | No second agent template | phase-3-0-scope-lock |
| P9 | No external templates | phase-2-10 research-only |
| P10 | No CV / digital twin / RAG / MCP | kit policies |
| P11 | Rollback plan exists | change-proposal + git tag strategy |
| P12 | Evaluation checklist selected | frozen [evaluation.md](../agent-builder-kit/templates/review-assistant-agent/evaluation.md) scenarios |

### Additional (from PHASE_3_START_CONDITIONS — for code)

| # | Gate |
|---|------|
| H1 | Mentor pass: operator or developer assessment |
| H2 | Lead pass: project-lead assessment |
| H3 | Architect co-sign: phase-3-readiness assessment |
| H4 | phase-2-8/PHASE_3_FREEZE_POLICY.md acknowledged |
| H5 | Explicit user implementation message (same as P1) |

---

## Phase 3.1 allowed paths (only after P1–P12 + H1–H5)

**Do not create until approved:**

```
agent-builder-kit/implementations/review-assistant-thin/
```

or

```
prototypes-derived/review-assistant-thin/
```

Exact path chosen at Phase 3.1 kickoff. Must not modify frozen v0.1 spec files except via change proposal.

---

## Phase 3.1 forbidden paths

```
agent-builder-kit/runtime/
agent-builder-kit/generator/
agent-builder-kit/factory/
agent-builder-kit/templates/cv/
agent-builder-kit/templates/digital-twin/
agent-builder-kit/templates/rag/
agent-builder-kit/templates/mcp/
agent-builder-kit/templates/swarm/
```

Also forbidden:

- Modify `prototypes/` core demos without separate approval
- Modify `integrations-real/`
- Modify `evaluation/scripts/`
- Modify `observability/examples/`
- New dependencies in `requirements.txt` without approval

---

## What Phase 3.1 thin implementation means

- Minimal wrapper aligning **one** agent behavior to frozen Review Assistant v0.1 spec
- Reuse patterns from `prototypes/review-loop-agent/` (reference/copy locally in new folder, not edit prototype)
- Same gates: fail-closed, verification, human approval, trace
- No generalized agent OS runtime
- No template → code generator

---

## What Phase 3.1 does NOT mean

- Agent Factory
- Multi-template platform
- Production Telegram/FastAPI deploy
- Auto-publish agent
- Second reference template

---

## Pre-flight commands (run on Phase 3.1 start day)

```powershell
cd C:\Dima\Projects\CURSOR\AGENT
python evaluation/scripts/run_demo_smoke_checks.py
python evaluation/scripts/check_expected_text_traces.py
```

Expected: PASS=12 FAIL=0 and PASS=6 FAIL=0.

---

## Current status (2026-05-26)

| Precondition | Met |
|--------------|-----|
| P2, P3 | yes (freeze review run) |
| P4 | yes — frozen with notes |
| P5 | **pending** human lead |
| P1 | **not met** — user has not started 3.1 |
| H1–H5 | **not met** — assessments pending |

**Verdict:** NOT READY for code. READY for planning.

See [PHASE_3_1_READINESS_NOTE.md](../agent-builder-kit/templates/review-assistant-agent/sign-off/PHASE_3_1_READINESS_NOTE.md)
