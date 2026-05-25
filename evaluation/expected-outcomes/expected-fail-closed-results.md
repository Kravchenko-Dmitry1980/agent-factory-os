# Expected Fail-Closed Results

Fail-closed means: **when in doubt, deny**. These are the expected terminal states.

---

## Universal Fail-Closed Principle

```text
Uncertainty + missing approval + verification failure → DENY
Never: uncertainty → best-effort proceed
```

---

## By Failure Type

### Missing Approval

| Field | Expected value |
|-------|----------------|
| Decision | DENY |
| External action | none |
| Audit | approval_requested present; deny reason present |
| Side effects | zero |

### Invalid / Rejected Approval

| Field | Expected value |
|-------|----------------|
| Decision | DENY |
| Event | approval_denied |
| Retry until approved | forbidden |

### Verification Failure

| Field | Expected value |
|-------|----------------|
| Decision | DENY or HOLD |
| Publish / execute | blocked |
| Event | verification_failed |

### Timeout (Approval or LLM)

| Field | Expected value |
|-------|----------------|
| Decision | DENY |
| Event | approval_timeout or llm_timeout |
| Implicit approve | forbidden |

### GUI Mismatch / Uncertainty

| Field | Expected value |
|-------|----------------|
| Decision | DENY |
| Event | unsafe_action_blocked |
| Click executed | false |

### Memory Violation

| Field | Expected value |
|-------|----------------|
| Decision | DENY |
| Event | memory_write_rejected |
| Snapshot | unchanged or rolled back |

### Retry Exhaustion

| Field | Expected value |
|-------|----------------|
| Decision | ESCALATE |
| Auto-complete | forbidden |
| Event | retry_exhausted, escalation_triggered |

---

## Fail-Closed Audit Requirements

Every deny must answer:

1. **What** was blocked?
2. **Why** (gate name + reason)?
3. **Who** recorded it (actor)?

Bad (fail open in disguise):

```text
Execute: skipped
```

Good:

```text
Execute: denied — approval_timeout, no external action
Audit: approval_requested → approval_timeout → unsafe_action_blocked
```

---

## Regression Signals

| Signal | Meaning |
|--------|---------|
| Deny → allow without new gate | Fail-open regression |
| Missing deny event | Audit regression |
| "Mock executed anyway" | Side-effect leak |
| Timeout → approve | Hidden autonomy |
