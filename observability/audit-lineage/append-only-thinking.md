# Append-Only Thinking

## Rule

Audit records are **never updated or deleted** in governed demos.

## Why

- Tamper-evident postmortems
- Promotion provenance (`governance/PROMOTION_LOG.md` style)
- Trust: "what did the system know at decision time?"

## Implementation (Local)

- JSONL append (`filesystem-audit-log`)
- SQLite INSERT-only audit table (no UPDATE on audit rows)

## Observable Violation

If postmortem finds missing intermediate decisions — audit was bypassed, not corrupted.

## Not Required

Cryptographic hash chains — educational layer stays simple.

Optional: note `event_id` + `parent_id` for logical chain.
