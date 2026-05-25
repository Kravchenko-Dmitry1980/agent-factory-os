# Bounded Memory Scenarios

System under test: `prototypes/bounded-memory-agent/`, `prototypes/integrations/bounded-memory-review-workflow/`

Run:

```powershell
python prototypes/bounded-memory-agent/minimal-demo.py --scenario happy
python prototypes/bounded-memory-agent/minimal-demo.py --scenario overflow
python prototypes/bounded-memory-agent/minimal-demo.py --scenario unverified-writeback
python prototypes/integrations/bounded-memory-review-workflow/minimal-demo.py
```

---

## Scenario: Memory Under Limit

### System Under Test

`prototypes/bounded-memory-agent/minimal-demo.py --scenario happy`

### Input

Verified summary within `MAX_MEMORY_CHARS` budget.

### Expected Behavior

Writeback allowed after verification; snapshot updated.

### Expected Event Trace

```
task_started → verification_passed → memory_write (implicit) → task_completed
```

### Expected Failure Mode

None.

### Pass Criteria

- Write succeeds
- Memory size ≤ limit
- Audit shows verification before write

### Fail Criteria

- Write without verification event
- Silent limit bypass

### Why This Matters

Baseline: controlled writeback only when verified and bounded.

---

## Scenario: Memory Over Limit Rejected

### System Under Test

`prototypes/bounded-memory-agent/minimal-demo.py --scenario overflow`

### Input

Content exceeding character budget.

### Expected Behavior

Write rejected; prior snapshot preserved.

### Expected Event Trace

```
task_started → verification_passed → memory_write_rejected → task_failed|blocked
```

### Expected Failure Mode

Reject with overflow reason.

### Pass Criteria

- `memory_write_rejected` in audit or output
- Snapshot unchanged or rollback noted

### Fail Criteria

- Truncation without audit
- Unbounded growth accepted

### Why This Matters

Prevents context drift and unbounded memory creep.

---

## Scenario: Unsafe Writeback Rejected

### System Under Test

`prototypes/bounded-memory-agent/minimal-demo.py --scenario unverified-writeback`

### Input

Write attempt without passing verification gate.

### Expected Behavior

Fail-closed: no writeback.

### Expected Event Trace

```
task_started → verification_failed → memory_write_rejected
```

### Expected Failure Mode

Block — verification-before-writeback invariant.

### Pass Criteria

- No memory mutation
- Explicit rejection reason

### Fail Criteria

- Write despite failed verification
- "Best effort" writeback

### Why This Matters

Core doctrine: verification before writeback.

---

## Scenario: Snapshot Preserved After Rejected Write

### System Under Test

`prototypes/bounded-memory-agent/minimal-demo.py --scenario happy` (then compare after overflow/unverified runs)

### Input

Rejected write attempt must not mutate frozen snapshot.

### Expected Behavior

On happy path: `Snapshot still frozen: True` after verified durable write. On reject paths: snapshot unchanged.

### Expected Event Trace

```
verification_failed|memory_write_rejected → (no durable mutation of snapshot)
```

### Expected Failure Mode

Reject — snapshot anchor preserved.

### Pass Criteria

- Curated snapshot equals original after reject scenarios
- Audit shows reject reason

### Fail Criteria

- Partial write corrupts snapshot
- Silent overwrite without audit

### Why This Matters

Memory must be recoverable; frozen snapshot is safety anchor.
