# Task Triage Agent — Human Approval Policy

**Date:** 2026-05-26  
**Status:** PLAN_ONLY

---

## Core rule

**Triage output is advisory.** Human decides next action.

Triage does not authorize implementation, execution, routing, or spec changes.

---

## Human approval required before (recommended by triage)

| Action | approval_required |
|--------|-------------------|
| Treating triage as accepted plan | yes — human confirms |
| Starting implementation | yes — separate from triage |
| Changing frozen specs | yes — always |
| Adding provider boundary | yes — always |
| Adding tools / MCP | yes — always |
| Escalating to execution (human's choice) | yes — human initiates |
| Creating tasks/tickets | yes — outside agent |
| Delegating to other agents | **forbidden** — not approval-gated, blocked |

---

## Risk-based approval recommendation

| risk_level | approval_required |
|------------|-------------------|
| low | false* |
| medium | **true** |
| high | **true** |
| critical | **true** + ESCALATE |

\*Low-risk triage still reviewed by human before action — `approval_required=false` means triage does not **mandate** extra gate, not that human skips review entirely.

---

## What triage must never do

- Auto-grant `approval_granted` for implementation
- Output "approved to proceed" as final authority
- Skip escalation on frozen/provider/security tasks
- Replace governance GO/NO-GO reviews

---

## Sequence with Review Assistant

```text
1. Task Triage → TRIAGED (advisory)
2. Human → decides "create impl plan" / "defer" / "reject"
3. (Later) Implementation work
4. (Later) Review Assistant → draft review path
5. Human → approval before delivery
```

Two separate approval moments — triage HITL ≠ delivery HITL.

---

## Trace

Emit `approval_required: required=true|false, reason=...` on every triage where risk ≥ medium or policy touch.

Never emit `approval_granted` from triage agent.

---

## Related

- Review Assistant: [human-approval.md](../../agent-builder-kit/templates/review-assistant-agent/human-approval.md)
- [TASK_TRIAGE_AGENT_SAFETY_GATES.md](TASK_TRIAGE_AGENT_SAFETY_GATES.md)
