# Fail-Closed Agent Loop

## Definition

**Fail-closed agent loop** is the invariant that verification failure, permission denial, or ambiguous terminal state keeps the agent in a non-success path — retry, escalate, or halt — rather than defaulting to completion or unchecked writeback.

## Why It Matters

Models declare done prematurely. Harness must treat unresolved verification as blocking, analogous to [[fail-closed-defaults]] at tool level but applied to loop termination and side effects.

## Architecture Implications

- Stop hooks, verification subagents, and GUI A/B/C reflectors append blocking errors — loop continues with `stopHookActive` or equivalent guard.
- Terminal states reached only after explicit pass gate — not model self-report alone.
- Parse failures in tool batching fail-closed to serial/safe path (tool layer); loop layer fails closed on unverified outcomes.
- Pairs with [[verification-before-writeback]]: no durable writes on fail-closed iteration.
- Distinct from [[fail-closed-defaults]]: that pattern covers tool metadata defaults; this covers loop lifecycle.

## Production Implications

- Guard infinite hook loops when `stopHookActive` re-triggers same failure.
- User-visible stall preferred over silent wrong completion.
- GUI: repeated C outcomes trigger circuit breaker, not infinite retry.

## Risks

- Over-aggressive fail-closed without retry budget frustrates users.
- Under-aggressive fail-closed ships wrong GUI clicks and bad memory.

## Related Concepts

- [[fail-closed-defaults]]
- [[verification]]
- [[visual-verification]]
- [[verification-before-writeback]]
- [[terminal-states]]
- [[execution-verification]]
- [[durable-task-coordination]]

## Related Anti-patterns

- [[unverified-gui-clicks]]
- [[infinite-retry-loops]]

## Related Patterns

- [[verification-before-writeback]]
- [[withholding-errors]]

## Upstream Sources

- `Books/claude/ch05-agent-loop.md`
- `Books/claude/ch06-tools.md` (fail-closed tool defaults, cross-layer analogy)
- `experiments/mobile-agent-review/extracted-patterns/action-verification-pattern.md`

## Governance References

- `PROMOTION_REVIEW.md` §5.5
- `governance/SEMANTIC_LINKING_AUDIT.md`

## Semantic Cluster

verification

## Promotion Metadata

```yaml
maturity: reusable-pattern
promotion_decision: PROMOTE_NOW
source_tier: research
canonical_status: curated
promotion_rationale: Loop-level fail-closed distinct from tool defaults; Claude + MobileAgent verification evidence.
governance_reference: governance/PROMOTION_STRATEGY.md Patterns criteria, governance/CANONICAL_DIRECTION.md
```
