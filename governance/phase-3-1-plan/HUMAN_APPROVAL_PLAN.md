# Human Approval Plan — Phase 3.1 Thin Review Assistant

**Context:** Local thin implementation — no production HITL service.

---

## Approval model

Human approval is the **final gate** before delivery. Critic and verification are **necessary but not sufficient**.

**Core rule:** **No approval = no final delivery.**

---

## Allowed approval modes (Phase 3.1)

| Mode | Description | Example |
|------|-------------|---------|
| CLI prompt | Interactive y/n | `Approve delivery? [y/N]:` |
| Explicit CLI flag | Non-interactive test | `--human approve` / `--human reject` |
| Local mock approval | Scenario-driven for demos | `--scenario happy` sets mock approve |

All modes must emit trace events: `approval_requested` → human decision event.

---

## Forbidden approval modes

| Mode | Why forbidden |
|------|---------------|
| Auto-approval | Violates frozen template |
| Default approval | Deny-by-default required |
| Approval inferred from critic | Critic ≠ truth |
| Approval inferred from verification alone | Human gate separate |
| External Telegram approval | Production adapter — out of scope |
| Production approval service | Out of scope |
| Timeout → auto-approve | Must emit `approval_timeout` → fail |

---

## Approval states

| State | Trace | Delivery |
|-------|-------|----------|
| pending | `approval_requested` | blocked |
| approved | `verification_passed actor=human decision=approve` | allowed |
| rejected | `approval_denied` | `task_failed` |
| timeout | `approval_timeout` | `task_failed` |

Reference: [human-approval-spec.md](../../agent-builder-kit/template-specs/human-approval-spec.md)

---

## Scenario mapping

| Scenario | Approval behavior |
|----------|-------------------|
| happy | mock or flag → approve |
| bad draft rejected | flag → reject |
| uncertain critic | hold until explicit human decision |
| missing approval | no flag → block delivery |
| bypass attempt | block before approval |

---

## Fingerprint (lightweight)

For CLI impl, record in trace:

- `decision=approve|reject`
- optional `reason=...`
- `artifact_id` or task hash

No secrets. No production identity system required.

---

## Operator guidance

1. Never pass `--human approve` in scripts without understanding scenario  
2. Reject path must print reason in trace  
3. Compare impl trace to [expected-traces.md](../../agent-builder-kit/templates/review-assistant-agent/expected-traces.md)

---

## Frozen template alignment

Must match [human-approval.md](../../agent-builder-kit/templates/review-assistant-agent/human-approval.md) — no semantic deviation without change proposal.
