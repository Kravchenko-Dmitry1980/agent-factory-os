# Telegram Review Gate — Failure Modes

## API Timeout

Telegram `getUpdates` exceeds timeout → deny, audit network failure.

## Malformed Response

Invalid JSON from API → deny, no continue.

## Retry Storm

Repeated approve polls without backoff cap → mitigated: max 3 polls in demo.

## Corrupted Queue

Pending file tampered → fingerprint mismatch → deny.

## Audit Failure

If audit append fails → workflow stops (fail-closed).

## Escalation Bypass

Continue without approval record → blocked in gate.

## Invalid Approval

Wrong fingerprint in approve command → deny.

## Filesystem Corruption

Unreadable pending JSON → deny.

## Network Failure

Send message fails → log + deny (real mode).

## Hidden Autonomy

Auto-approve on send success → **not implemented**.
