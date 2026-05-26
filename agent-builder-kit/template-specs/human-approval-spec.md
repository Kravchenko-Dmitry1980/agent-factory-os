# Human Approval Spec

Human-in-the-loop (HITL) requirements for agent templates.

---

## What Requires Approval

| Action | Approval required |
|--------|-------------------|
| Final delivery to user / publish | **yes** |
| External send (email, API, message) | **yes** |
| Destructive or irreversible action | **yes** |
| Long-term memory writeback | **yes** |
| Escalation override | **yes** |
| Draft generation (internal) | no (marked unverified) |
| Read-only analysis | no |

---

## Approval States

| State | Meaning |
|-------|---------|
| `pending` | Waiting for human decision |
| `approved` | Human explicitly allowed action |
| `denied` | Human rejected; terminal fail |
| `timeout` | No response; deny-by-default |
| `escalated` | Routed to supervisor / operator |

Canonical events: `approval_requested`, `verification_passed` (human), `approval_denied`, `approval_timeout`

---

## Approval Timeout

- Configurable per template (document default)
- On timeout: **deny-by-default** → emit `approval_timeout`
- No auto-approve on timeout
- Reference: `integrations-real/telegram-review-gate/` (research)

---

## Deny-by-Default

**No approval = no risky action.**

- Missing approval blocks publish
- Ambiguous approval blocks publish
- Expired approval blocks publish

---

## Approval Fingerprint

Each approval record should capture (conceptual, text trace):

- approver identity (role, not secret)
- timestamp
- artifact hash or id
- decision (approve/deny)
- reason (optional for approve, recommended for deny)

Enables trace review and rollback decisions.

---

## Rejection Path

```
approval_requested → approval_denied → task_failed
```

- Document reason in trace
- No silent retry without new human request
- User may revise input and restart task

---

## Escalation Path

```
verification_failed OR repeated_denial OR policy_conflict
  → escalation_triggered
  → human/supervisor review
  → approve / deny / rollback
```

---

## Related

- [safety-gates/human-approval-gate.md](../safety-gates/human-approval-gate.md)
- [trace-templates/approval-trace-template.md](../trace-templates/approval-trace-template.md)
- `prototypes/review-loop-agent/governance.md`
