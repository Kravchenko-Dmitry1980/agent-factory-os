# Bounded Memory — Failure Modes

## Hallucination

Unverified fact written to durable store. **Gate:** reject unless `verified=True`.

## Retry Loops

Agent retries write with slightly different text to bypass limit. **Gate:** total size check, audit each attempt.

## Missing Verification

Writeback without evaluation. **Gate:** fail-closed on `verified=False`.

## Memory Drift

Session snapshot diverges from durable store mid-session. **By design** — document snapshot semantics; use explicit recall.

## Unsafe Autonomy

Agent auto-expands memory budget. **Gate:** hard `MAX_MEMORY_CHARS`.

## Missing Escalation

Silent truncation without operator notice. **Gate:** log overflow rejection with reason.

## Governance Bypass

Direct store mutation skipping API. **Demo:** only `MemoryAgent.write()` mutates store.
