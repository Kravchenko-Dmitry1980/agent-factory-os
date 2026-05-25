# Queue Orchestration — Failure Modes

## Hallucination

Worker returns plausible but wrong result. **Mitigation:** verification step before complete.

## Retry Loops

Infinite retry on same failure. **Mitigation:** `max_retries` + fail-closed stop.

## Missing Verification

Mark complete on worker exit code alone. **Mitigation:** explicit verify function.

## Memory Drift

Queue state lost on restart. **Note:** in-memory only in prototype; production would need durable queue — out of scope.

## Unsafe Autonomy

Worker self-escalates away failures. **Mitigation:** supervisor role sets escalated flag.

## Missing Escalation

Silent drop after max retries. **Mitigation:** audit + ESCALATED status.

## Governance Bypass

Skip queue, run worker directly. **Documented anti-pattern** — demo always enqueues.
