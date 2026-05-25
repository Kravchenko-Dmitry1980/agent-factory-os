# FastAPI Review API — Failure Modes

## API Timeout

Client timeout — out of scope for server; demo uses in-process calls.

## Malformed Response

Invalid JSON body → 422 fail-closed.

## Retry Storm

Repeated approve on approved item → 409, no double-write.

## Corrupted Queue

SQLite corruption → demo catches, returns 500, audit failure.

## Audit Failure

If audit insert fails → transition rolled back (transaction).

## Escalation Bypass

Direct SQL approve → prevented by API layer only in demo.

## Invalid Approval

Approve rejected item → 409.

## Filesystem Corruption

SQLite journal issues → fail-closed error.

## Network Failure

N/A for local demo.

## Hidden Autonomy

No cron auto-approve.
