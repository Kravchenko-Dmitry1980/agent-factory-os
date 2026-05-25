# Filesystem Audit Log — Failure Modes

## API Timeout

N/A (local FS).

## Malformed Response

Invalid JSON line on read → skip line, record warning event.

## Retry Storm

N/A.

## Corrupted Queue

N/A.

## Audit Failure

Disk full / permission → raise, caller fail-closed.

## Escalation Bypass

Mutation API not exposed — append only.

## Invalid Approval

Approval event without fingerprint → validation warning in demo.

## Filesystem Corruption

Partial write line → reader skips, logs corrupt_line.

## Network Failure

N/A.

## Tamper Attempt

Demo tries rewrite — blocked by API design.
