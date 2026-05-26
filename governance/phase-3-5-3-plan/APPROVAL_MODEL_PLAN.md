# Approval Model Plan — Free-Form CLI

**Date:** 2026-05-26  
**Status:** PLAN_ONLY

---

## Options compared

### Option A — Simulated approval prompt (recommended)

Operator sees draft summary, then:

```text
Approve result? yes/no [no]:
```

| Pros | Cons |
|------|------|
| Tangible HITL demo | Not real approval workflow |
| Simple, no UI | Operator can type yes carelessly |
| Matches thin demo philosophy | Simulated only |

### Option B — Auto-deny by default (no prompt)

Always BLOCKED unless separate impl adds prompt later.

| Pros | Cons |
|------|------|
| Safest | Frustrating for demo touchability |
| No false sense of HITL | Poor operator UX |

### Option C — No approval in free-form

**Rejected.**

Delivery without approval gate violates Review Assistant doctrine and thin demo model.

---

## Recommendation

**Option A with safe default `no`**

---

## Rules (future impl)

| Rule | Value |
|------|-------|
| Default answer | **no** (Enter = no) |
| Approval required for DELIVERED | yes |
| No approval | → BLOCKED |
| Verification failed | cannot approve → FAILED |
| Unsafe output detected | cannot approve → FAILED/BLOCKED |
| Bypass phrases in task | unsafe_action_blocked |

---

## Flow

```text
verification_passed
  → approval_requested
  → prompt: Approve result? yes/no [no]
  → if yes AND safe → approval_granted → DELIVERED
  → if no → approval_denied or missing → BLOCKED
```

See [diagrams/approval-flow.md](diagrams/approval-flow.md).

---

## Not in v1

- Real human approval UI
- Multi-reviewer workflow
- Timeout with policy config UI
- Persistent approval audit store

Simulated terminal prompt only.
