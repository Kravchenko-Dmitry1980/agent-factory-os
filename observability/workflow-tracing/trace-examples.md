# Trace Examples (Reference)

Full traces live in [../examples/](../examples/). Summaries below.

---

## Review Workflow Trace

Source: `prototypes/integrations/review-queue-workflow/`

```
task_started → draft → verification_passed (critic advisory)
→ approval_requested → task_completed (publish)
```

Failure variant: `approval_denied`, `escalation_triggered` (uncertain critic).

---

## Queue Workflow Trace

Source: `integrations-real/local-queue-worker/`

```
task_started → retry_triggered (×N) → verification_passed → task_completed
```

Failure: `retry_exhausted` → `escalation_triggered`.

Recovery: `queue_recovered` → resume pending.

---

## GUI Verification Trace

Source: `prototypes/integrations/gui-safe-action-workflow/`

```
observe → proposed action → verification_failed (outcome B)
→ unsafe_action_blocked
```

Success requires outcome A + approval for high-risk.

---

## Promotion Workflow Trace

Source: `prototypes/integrations/governed-promotion-workflow/`

```
task_started → review → scan → governance_rejection (dangerous-topology)
```

Success: scan pass → promote decision (simulated).

---

## Reading Order

1. Identify `OUTCOME`
2. Find last `verification_*` and `approval_*`
3. Count `retry_triggered` before escalation
4. Check for anti-pattern events
