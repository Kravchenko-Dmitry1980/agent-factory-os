# LLM Verification — Failure Modes

## API Timeout

HTTP timeout → deny, escalate, audit.

## Malformed Response

Non-JSON or missing fields → reject (fail-closed).

## Retry Storm

No auto-retry loop — single attempt in demo.

## Corrupted Queue

N/A.

## Audit Failure

Stop before accept if audit append fails.

## Escalation Bypass

Accept on raw LLM text without verify → **blocked**.

## Invalid Approval

N/A — verification gate replaces approval.

## Filesystem Corruption

Audit JSONL issues → fail-closed.

## Network Failure

Connection error → reject + escalate.

## Hidden Autonomy

Treating model output as truth → explicitly forbidden in governance.
