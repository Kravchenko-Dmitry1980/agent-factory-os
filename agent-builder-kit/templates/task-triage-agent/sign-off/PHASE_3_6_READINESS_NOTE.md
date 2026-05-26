# Phase 3.6 Readiness Note — Task Triage Agent

**Date:** 2026-05-26  
**Specs status:** FROZEN_WITH_NOTES (`task-triage-agent-specs-v0.1`)

---

## Current State

Task Triage Agent **specs v0.1 are frozen**.

| Item | Status |
|------|--------|
| Spec freeze | FROZEN_WITH_NOTES |
| Sign-off | SIGNED_OFF_WITH_NOTES |
| Implementation | NOT_STARTED |
| Code | NONE |
| Evaluation script | NONE |

**This freeze does not authorize implementation.**

---

## Next Phase (Plan Only)

Phase 3.6 may only start as:

**Phase 3.6-Plan — Task Triage Thin Implementation Plan**

Not implementation. Not code. Plan documents only.

---

## Phase 3.6-Plan Must Decide

| Decision | Required |
|----------|----------|
| Where thin implementation would live | e.g. prototypes-derived/task-triage-agent/ |
| What files may be created | Explicit allow-list |
| What behavior is allowed | Rule-based classifier first |
| What behavior is forbidden | No execution, no orchestrator, no provider default |
| What evaluation is required | Cases from frozen evaluation.md |
| Rollback plan | Before any code |
| GO/NO-GO for actual implementation | Separate gate |

---

## Implementation Remains Forbidden Until

1. Phase 3.6-Plan complete
2. GO/NO-GO = GO (or CONDITIONAL_GO with preconditions)
3. Pre-flight baselines PASS
4. Change proposal approved
5. Explicit human approval for code

---

## Recommended Discipline (Mirror Review Assistant)

```text
Specs v0.1 (frozen — current)
  → Phase 3.6-Plan (thin impl plan)
  → Phase 3.6-Impl (only if GO)
  → Harden + eval script
  → Freeze thin v0.1
```

---

## Do Not Skip

| Skip | Risk |
|------|------|
| Plan → straight to code | Scope drift, orchestrator creep |
| Provider before mock/rules | Injection surface, cost |
| Eval script after impl | Untestable boundaries |
| Baseline regression | Break Review Assistant chain |

---

## Reference

- [implementation-notes.md](../implementation-notes.md)
- [SPEC_FREEZE_RECORD.md](SPEC_FREEZE_RECORD.md)
- [CHANGE_LOCK.md](CHANGE_LOCK.md)
- [governance/phase-3-5-plan/PHASE_3_5_GO_NO_GO.md](../../../../governance/phase-3-5-plan/PHASE_3_5_GO_NO_GO.md)

Governance freeze: [PHASE_3_5_FREEZE_TASK_TRIAGE_AGENT_SPECS_V0_1_REVIEW.md](../../../../governance/PHASE_3_5_FREEZE_TASK_TRIAGE_AGENT_SPECS_V0_1_REVIEW.md)
