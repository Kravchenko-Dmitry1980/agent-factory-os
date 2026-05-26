# Behavior Contract — Phase 3.1 Thin Review Assistant

**Normative for:** future implementation  
**Source of truth for spec semantics:** frozen [review-assistant-agent/](../../agent-builder-kit/templates/review-assistant-agent/README.md) v0.1  
**Reference behavior:** `prototypes/review-loop-agent/contracts.md`

---

## Inputs

| Input | Type | Required | Notes |
|-------|------|----------|-------|
| `task_text` | string | yes | User task description |
| `draft_context` | string | no | Optional prior draft / notes |
| `approval_decision` | enum | at approval step | `approve` \| `reject` \| unset |
| `scenario_mode` | string | no | e.g. `happy`, `uncertain-critic`, `bypass-attempt` |

---

## Outputs

| Output | When | Verified |
|--------|------|----------|
| `draft` | after draft step | no |
| `critique_notes` | after critique | advisory |
| `critique_verdict` | after critique | `pass` \| `fail` \| `uncertain` |
| `verification_result` | after verification | pass/fail + reason |
| `approval_status` | after approval gate | pending/approved/rejected/timeout |
| `final_decision` | terminal | delivered \| blocked \| failed |
| `trace` | always | list of event lines |

---

## Required states

Implementation state machine (conceptual):

| State | Meaning |
|-------|---------|
| `RECEIVED` | Task accepted |
| `DRAFTED` | Draft produced |
| `CRITIQUED` | Advisory critique recorded |
| `VERIFIED` | Verification gate completed |
| `APPROVAL_REQUESTED` | Waiting for human |
| `APPROVED` | Human approved |
| `REJECTED` | Human rejected |
| `BLOCKED` | Fail-closed stop (bypass, missing approval) |
| `ESCALATED` | Uncertainty / policy — human required |
| `COMPLETED` | Approved delivery terminal |
| `FAILED` | Terminal failure |

---

## Transitions (safe)

```text
RECEIVED → DRAFTED → CRITIQUED → VERIFIED → APPROVAL_REQUESTED
  → APPROVED → COMPLETED
  → REJECTED → FAILED
  → (timeout) → FAILED

VERIFIED + uncertain critic → ESCALATED → APPROVAL_REQUESTED (no auto COMPLETED)

bypass attempt → BLOCKED → FAILED
missing approval at delivery → BLOCKED → FAILED
```

---

## Required safe behavior

| Rule | Enforcement |
|------|-------------|
| Missing approval blocks final output | No `COMPLETED` without `APPROVED` |
| Uncertainty blocks or escalates | `uncertain` → no auto delivery |
| Critic is advisory | Critic pass ≠ `APPROVED` |
| Verification is mandatory | Cannot skip to approval without verify event |
| Trace is mandatory | Every transition emits audit line |
| No hidden memory writeback | No persistent store in Phase 3.1 |
| No external action | No network/send/publish API |

---

## Verification points (from prototype contracts)

1. **Post-draft:** draft non-empty  
2. **Post-critique:** verdict recorded; critic cannot publish  
3. **Pre-delivery:** `human_decision == approve` AND `critique_verdict != uncertain` (unless human explicitly overrides with audit — document in trace)

---

## Failure states (align with prototype)

| State | Meaning |
|-------|---------|
| `BLOCKED_UNCERTAIN` | Critic uncertain — human must decide |
| `REJECTED` | Human rejected |
| `BYPASS_DENIED` | Publish without approval attempted |

---

## Forbidden behavior

- Auto-publish on critic pass
- Auto-approve on timeout
- Silent delivery (no trace)
- LLM output treated as verified truth without gate

---

## Diagram

[diagrams/review-assistant-flow.md](diagrams/review-assistant-flow.md)
