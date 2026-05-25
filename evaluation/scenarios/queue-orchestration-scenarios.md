# Queue Orchestration Scenarios

System under test: `prototypes/queue-orchestration/`, `prototypes/integrations/escalation-workflow/`, `integrations-real/local-queue-worker/`

Run:

```powershell
python prototypes/queue-orchestration/minimal-demo.py --scenario happy
python prototypes/queue-orchestration/minimal-demo.py --scenario max-retries
python prototypes/integrations/escalation-workflow/minimal-demo.py
python integrations-real/local-queue-worker/minimal-demo.py
```

---

## Scenario: Task Succeeds

### System Under Test

`prototypes/queue-orchestration/minimal-demo.py --scenario happy`

### Input

Task with verifiable outcome on first attempt.

### Expected Behavior

Enqueue → process → verify → complete; no retry.

### Expected Event Trace

```
task_started → verification_passed → task_completed
```

### Expected Failure Mode

None.

### Pass Criteria

- Terminal status=completed
- retry count = 0

### Fail Criteria

- Unnecessary retries
- Missing completion event

### Why This Matters

Happy path must not add retry noise or mask failures.

---

## Scenario: Task Hits Retry Ceiling

### System Under Test

`prototypes/queue-orchestration/minimal-demo.py --scenario max-retries`

### Input

Persistent verification failure through all retries.

### Expected Behavior

Stop at ceiling; no further automated attempts.

### Expected Event Trace

```
verification_failed → retry_triggered (×N) → retry_exhausted
```

Reference: `observability/examples/escalation-trace.txt`

### Expected Failure Mode

Hard stop at max retries.

### Pass Criteria

- `retry_exhausted` present
- No retry N+1

### Fail Criteria

- Ceiling silently increased
- Task marked completed despite failures

### Why This Matters

Retry storms mask bugs; ceiling is governance invariant.

---

## Scenario: Task Escalates

### System Under Test

`prototypes/integrations/escalation-workflow/minimal-demo.py`

### Input

Retry ceiling reached on ambiguous task.

### Expected Behavior

Escalation to human/supervisor; unsafe auto-completion blocked.

### Expected Event Trace

```
retry_exhausted → escalation_triggered → unsafe_action_blocked (if auto-complete attempted)
```

### Expected Failure Mode

Escalated — requires human path.

### Pass Criteria

- `escalated=yes` in governance summary
- No silent auto-complete

### Fail Criteria

- Escalation skipped
- Auto-complete after exhaustion

### Why This Matters

Automation must stop when certainty is unavailable.

---

## Scenario: Queue Recovery After Crash

### System Under Test

`integrations-real/local-queue-worker/minimal-demo.py` (recovery scenario if available)

### Input

Simulated crash mid-queue; restart worker.

### Expected Behavior

Pending tasks reloaded; no duplicate side effects; audit preserved.

### Expected Event Trace

```
queue_recovered → task_started → ... → task_completed|task_failed
```

Reference: `observability/examples/queue-recovery-trace.txt`

### Expected Failure Mode

Recovery — idempotent re-processing.

### Pass Criteria

- `queue_recovered` in trace
- No lost tasks without audit gap

### Fail Criteria

- Duplicate execution without idempotency
- Silent task drop

### Why This Matters

Durable queue must survive process death without governance loss.
