# Frozen Memory Snapshot

## Definition

**Frozen memory snapshot** is the practice of injecting curated memory into the system prompt once at session start and not re-injecting mid-session — persistence and injection timing are deliberately separated.

## Why It Matters

Mid-session prompt mutation invalidates prefix cache, increases cost, and creates inconsistent agent behavior within a single conversation. Frozen injection makes memory a stable architectural input for the loop duration.

## Architecture Implications

- Memory writes persist to durable store immediately but do not alter the active system prompt until the next session.
- Tool responses may surface live memory state to the agent without changing cached prompt prefix.
- Pairs with [[prompt-cache-as-constraint]]: memory sections belong in the static boundary when injected at bootstrap.
- Complements [[memory-char-limits]]: bounded stores make snapshot injection predictable.

## Production Implications

- Agents operating on stale in-session memory views must use explicit recall tools or accept next-session refresh — document this contract for operators.
- Debugging "agent forgot what it just saved" often traces to snapshot semantics, not failed persistence.
- Cost profiles improve when memory blocks remain prefix-stable across turns.

## Risks

- Operators may assume writes are immediately visible in reasoning context.
- Long sessions without refresh can diverge from on-disk truth if tool feedback is ignored.

## Related Concepts

- [[memory-char-limits]]
- [[memory-recall]]
- [[prompt-cache-as-constraint]]
- [[profile-isolation]]
- [[memory-provider-boundaries]]

## Related Anti-patterns

- [[mid-session-memory-injection]]
- [[cache-busting-sections]]
- [[unbounded-memory-growth]]

## Related Patterns

- [[prompt-cache-as-constraint]]
- [[memory-aware-execution]]
- [[verification-before-writeback]]

## Upstream Sources

- `Books/claude/ch04-api-layer.md`
- `experiments/hermes-agent-review/memory/MEMORY_SYSTEM_OVERVIEW.md`

## Governance References

- `PROMOTION_REVIEW.md` §3.1
- `governance/PROMOTION_STRATEGY.md`
- `governance/PROMOTION_LOG.md`
- `governance/SEMANTIC_LINKING_AUDIT.md`

## Semantic Cluster

memory-governance

## Promotion Metadata

```yaml
maturity: production-relevant
promotion_decision: PROMOTE_NOW
source_tier: research
canonical_status: curated
promotion_rationale: Production-validated cache-safe memory injection; complements Claude prompt-cache pattern without runtime port.
governance_reference: PROMOTION_REVIEW.md §3.1, governance/CANONICAL_DIRECTION.md Phase 1.2
```
