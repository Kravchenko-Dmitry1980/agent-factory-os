# Fail-Closed Action Scenarios

System under test: `prototypes/fail-closed-external-action/`, `integrations-real/telegram-review-gate/`

Run:

```powershell
python prototypes/fail-closed-external-action/minimal-demo.py --scenario approved
python prototypes/fail-closed-external-action/minimal-demo.py --scenario no-approval
python prototypes/fail-closed-external-action/minimal-demo.py --scenario uncertain
python prototypes/fail-closed-external-action/minimal-demo.py --scenario rejected
python integrations-real/telegram-review-gate/minimal-demo.py
```

---

## Scenario: Approved Action Executes

### System Under Test

`prototypes/fail-closed-external-action/minimal-demo.py --scenario approved`

### Input

High-risk action with verification pass and explicit human approval.

### Expected Behavior

Gate allows mock execution after approval chain complete.

### Expected Event Trace

```
task_started → verification_passed → approval_requested → verification_passed (approve) → task_completed
```

### Expected Failure Mode

None — controlled execution.

### Pass Criteria

- Execute message indicates success (mock)
- Audit shows approval before execute

### Fail Criteria

- Execute without approval event
- Missing verification step

### Why This Matters

Even allowed actions must show full gate chain in audit.

---

## Scenario: Missing Approval Blocks

### System Under Test

`prototypes/fail-closed-external-action/minimal-demo.py --scenario no-approval`

### Input

Action proposed; approval never granted.

### Expected Behavior

Deny-by-default; no external side effect.

### Expected Event Trace

```
task_started → verification_passed → approval_requested → approval_timeout|unsafe_action_blocked
```

### Expected Failure Mode

Block — missing approval.

### Pass Criteria

- Execute denied
- Message indicates missing approval
- No side effect

### Fail Criteria

- Default allow
- Execute with pending approval

### Why This Matters

Core fail-closed: absence of approval = deny.

---

## Scenario: Invalid Approval Blocks

### System Under Test

`prototypes/fail-closed-external-action/minimal-demo.py --scenario rejected`

### Input

Explicit human rejection.

### Expected Behavior

Execute blocked; rejection recorded.

### Expected Event Trace

```
approval_requested → approval_denied → unsafe_action_blocked
```

### Expected Failure Mode

Terminal deny.

### Pass Criteria

- Execute denied
- Rejection in audit

### Fail Criteria

- Rejection ignored
- Retry until approved without escalation

### Why This Matters

Explicit deny must be as strong as missing approval.

---

## Scenario: Timeout Denies

### System Under Test

`integrations-real/telegram-review-gate/minimal-demo.py` (timeout path)

### Input

Approval requested; no response within timeout window.

### Expected Behavior

Deny-by-default on timeout; no external action.

### Expected Event Trace

```
approval_requested → approval_timeout → unsafe_action_blocked
```

### Expected Failure Mode

Timeout deny — not implicit approve.

### Pass Criteria

- `approval_timeout` or `timeout_denied` in audit
- Action not executed

### Fail Criteria

- Timeout → auto approve
- Silent drop without deny event

### Why This Matters

Waiting forever is hidden autonomy; timeout must fail closed.
