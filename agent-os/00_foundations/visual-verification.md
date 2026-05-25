# Visual Verification

## Definition

**Visual verification** is post-action confirmation that the UI transitioned as expected — using structured outcome taxonomy before advancing plan or declaring progress.

## Why It Matters

GUI tool execution lacks structured stderr. Visual delta is the primary feedback channel; without explicit verification, agents assume clicks succeeded.

## Architecture Implications

**A/B/C outcome taxonomy** (post-operation reflect):

| Outcome | Meaning | Typical agent response |
|---------|---------|------------------------|
| A | Expected UI transition observed | Advance subgoal |
| B | Wrong screen or unexpected state | Backtrack, replan |
| C | No meaningful change | Retry with revised grounding |

Distinctions:

- **Action succeeded** — tap executed, no transport error.
- **Task succeeded** — user goal advanced; requires A outcome chain, not C tolerance.

- Extends [[verification]] into visual modality; code hooks and GUI reflect serve different harness layers.
- Typed verification records in message history improve replay and debugging.
- Pre-operation critic (research-only upstream) is optional layer — not required for curated baseline.

## Production Implications

- Circuit breaker after repeated C outcomes on same subgoal.
- Never ship with verification disabled for latency without benchmark proof.
- Second-check harness for high-risk actions (payments, deletes) even after A.

## Risks

- Reflector false-A — premature success classification.
- v3.5-style monolithic loops without structured verification records.

## Related Concepts

- [[gui-agent-loop]]
- [[visual-grounding]]
- [[verification]]
- [[verification-before-writeback]]
- [[fail-closed-agent-loop]]
- [[execution-feedback]]

## Related Anti-patterns

- [[unverified-gui-clicks]]
- [[brittle-gui-automation]]

## Related Patterns

- [[verification-before-writeback]]
- [[fail-closed-agent-loop]]

## Upstream Sources

- `experiments/mobile-agent-review/extracted-patterns/action-verification-pattern.md`
- `experiments/mobile-agent-review/action-runtime/action-verification.md`
- `Books/claude/ch05-agent-loop.md` (code verification parallel)

## Governance References

- `PROMOTION_REVIEW.md` §4.4
- `governance/PROMOTION_LOG.md`
- `governance/SEMANTIC_LINKING_AUDIT.md`

## Semantic Cluster

verification

## Promotion Metadata

```yaml
maturity: production-relevant
promotion_decision: PROMOTE_NOW
source_tier: research
canonical_status: curated
promotion_rationale: A/B/C taxonomy extends foundations verification; no GUI-Critic integration claims.
governance_reference: PROMOTION_REVIEW.md §4.4, governance/CANONICAL_DIRECTION.md Phase 1.2
```
