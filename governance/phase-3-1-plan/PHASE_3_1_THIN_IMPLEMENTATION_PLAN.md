# Phase 3.1 Thin Implementation Plan

**Date:** 2026-05-26  
**Type:** Plan only — no implementation  
**Target:** Review Assistant Agent v0.1 (frozen)

---

## Goal

Create a **future thin implementation** of Review Assistant only — proving the frozen v0.1 spec can be executed locally with gates, human approval, and readable traces — **without** building a factory, runtime platform, or second agent.

---

## What “thin implementation” means

A thin implementation:

| Property | Requirement |
|----------|-------------|
| Scope | Only frozen Review Assistant v0.1 behavior |
| Execution | Simple local execution (script/module) |
| Framework | **None** — no agent engine, no orchestration library |
| Generator | **None** — no template-to-code |
| Factory | **None** — no registry, no multi-agent |
| Human approval | **Mandatory** before final delivery |
| Fail-closed | Default on uncertainty, missing approval, verification fail |
| Trace | Human-readable text output |
| Evaluation | Checkable via existing scripts + frozen scenarios |
| Prototypes | **Reference only** — do not modify `prototypes/` |

---

## What it does NOT mean

- Agent factory or Builder Kit runtime
- Reusable generalized agent engine
- Template-to-code generator
- Production deployment (Telegram, FastAPI, SaaS)
- External integrations by default
- CV / digital twin / RAG / MCP / LangGraph / swarm
- Database, network API, persistent memory
- Mutation of frozen spec body or Phase 2 protected folders

---

## Recommended implementation style

**Local, minimal, readable.**

Prefer when code is allowed (Phase 3.1 implementation — **not now**):

| Prefer | Avoid |
|--------|-------|
| One small folder | Multiple packages |
| Simple Python script or small module | Framework abstraction layers |
| Stdlib only | New `requirements.txt` entries |
| In-memory / CLI | Database, network |
| Copy patterns from review-loop **into new folder** | Edit `prototypes/review-loop-agent/` |
| Explicit CLI approval flag or prompt | Auto-approval, inferred approval |

**Do not create code in Phase 3.1-Plan.**

---

## Recommended location

**Option B:** `prototypes-derived/review-assistant-thin/`

See [FILE_BOUNDARY_PLAN.md](FILE_BOUNDARY_PLAN.md) for rationale. Folder **not created** until implementation phase.

---

## Implementation phases (future)

```text
Phase 3.1-Plan     ← this document set (Markdown only)
Phase 3.1-Impl     ← future: create folder + minimal script (explicit user start)
Phase 3.1-Review   ← post-impl checklist + acceptance
```

---

## Behavior summary

See [BEHAVIOR_CONTRACT.md](BEHAVIOR_CONTRACT.md).

Flow: task → draft → critique (advisory) → verification → human approval → output or fail → trace.

---

## Evaluation summary

See [EVALUATION_PLAN.md](EVALUATION_PLAN.md).

Minimum: 5 frozen template scenarios + smoke/trace baseline + no forbidden folders.

---

## Rollback summary

See [ROLLBACK_PLAN.md](ROLLBACK_PLAN.md).

Tag before impl; revert new folder only; never patch frozen specs to “fix” bad impl.

---

## Approvals required before code

| Gate | Source |
|------|--------|
| P1–P12 | [PHASE_3_1_PRECONDITIONS.md](../PHASE_3_1_PRECONDITIONS.md) |
| H1–H5 | [PHASE_3_START_CONDITIONS.md](../PHASE_3_START_CONDITIONS.md) |
| Human lead | [sign-off/REVIEW_ASSISTANT_V0_1_SIGN_OFF.md](../../agent-builder-kit/templates/review-assistant-agent/sign-off/REVIEW_ASSISTANT_V0_1_SIGN_OFF.md) |
| Go/No-Go | [PHASE_3_1_GO_NO_GO.md](PHASE_3_1_GO_NO_GO.md) |

---

## References

| Resource | Path |
|----------|------|
| Frozen template | `agent-builder-kit/templates/review-assistant-agent/` |
| Prototype reference | `prototypes/review-loop-agent/` |
| Scenarios | `evaluation/scenarios/review-loop-scenarios.md` |
| Events | `observability/event-taxonomy/canonical-events.md` |
| No runtime policy | `agent-builder-kit/governance/no-runtime-policy.md` |

---

## Plan verdict

**CONDITIONAL_GO_FOR_IMPLEMENTATION** — see [PHASE_3_1_GO_NO_GO.md](PHASE_3_1_GO_NO_GO.md) and [FINAL_PHASE_3_1_PLAN_REPORT.md](FINAL_PHASE_3_1_PLAN_REPORT.md).
