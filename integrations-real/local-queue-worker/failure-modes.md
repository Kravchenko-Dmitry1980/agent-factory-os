# Local Queue Worker — Failure Modes

## API Timeout

N/A.

## Malformed Response

Invalid task payload JSON → mark corrupt, skip.

## Retry Storm

Bounded by MAX_RETRIES in code.

## Corrupted Queue

Bad status value → audit + skip row.

## Audit Failure

Worker stops if audit insert fails.

## Escalation Bypass

Mark complete after max retries → prevented.

## Invalid Approval

N/A.

## Filesystem Corruption

SQLite locked/corrupt → fail-closed error message.

## Network Failure

N/A.

## Recovery

`--scenario recovery` enqueues, simulates crash, reopens DB, resumes pending.
