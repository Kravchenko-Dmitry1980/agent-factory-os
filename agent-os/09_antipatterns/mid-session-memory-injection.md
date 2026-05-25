# Mid-Session Memory Injection

## Definition

**Mid-session memory injection** is updating curated memory content in the active system prompt after session start — invalidating prefix cache and splitting agent context within one conversation.

## Why It Matters

Persistence and prompt injection are separate concerns. Conflating them increases cost, breaks cache invariants, and creates "saved but not visible" confusion.

## Architecture Implications

**Failure mode:** Memory write triggers system prompt rebuild mid-turn → prefix cache miss → inconsistent reasoning vs tool-reported state.

**Symptoms:**

- Fleet cost spikes after memory feature launch
- Agent cites old memory while tool shows new entries
- Cache analytics show boundary shifts on memory edits

**Why dangerous:** Violates [[prompt-cache-as-constraint]]; masks [[frozen-memory-snapshot]] contract.

**Mitigation:**

- Adopt [[frozen-memory-snapshot]]: write to disk, inject only at bootstrap
- Surface live state via tool results, not prompt mutation
- Cross-ref [[cache-busting-sections]] for non-memory cache breaks

## Production Implications

- Code review gate: no dynamic memory sections after static boundary.
- Document operator expectation for next-session visibility.

## Risks

- "Helpful" real-time memory refresh features reintroduce injection.

## Related Concepts

- [[frozen-memory-snapshot]]
- [[prompt-cache-as-constraint]]
- [[cache-busting-sections]]
- [[memory-char-limits]]

## Related Anti-patterns

- [[cache-busting-sections]]
- [[unbounded-memory-growth]]

## Related Patterns

- [[frozen-memory-snapshot]]
- [[prompt-cache-as-constraint]]

## Upstream Sources

- `experiments/hermes-agent-review/anti-patterns/ANTI_PATTERNS.md` §2
- `experiments/hermes-agent-review/memory/MEMORY_SYSTEM_OVERVIEW.md`
- `Books/claude/ch04-api-layer.md`

## Governance References

- `PROMOTION_REVIEW.md` §3.2
- `governance/PROMOTION_LOG.md`

## Semantic Cluster

memory-governance

## Promotion Metadata

```yaml
maturity: production-relevant
promotion_decision: PROMOTE_NOW
source_tier: research
canonical_status: curated
promotion_rationale: Pairs with frozen snapshot; Hermes-validated cache failure mode.
governance_reference: PROMOTION_REVIEW.md §3.2, governance/CANONICAL_DIRECTION.md Phase 1.2
```
