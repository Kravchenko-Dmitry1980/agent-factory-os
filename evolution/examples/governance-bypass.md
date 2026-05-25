# Example: Governance Bypass

## Change

Copy experiment pattern directly into `agent-os/08_patterns/` without PROMOTION_REVIEW.

## Intent

"Everyone agrees it's good."

## Risk

Duplicate doctrine; unreviewed claims become canonical; provenance lost.

## Detection

Missing provenance in promoted file; no governance audit event.

## Rollback

Remove from agent-os; keep in experiments; run promotion simulator.

## Lesson

[governance/PROMOTION_STRATEGY.md](../../governance/PROMOTION_STRATEGY.md) — no stage skipping.
