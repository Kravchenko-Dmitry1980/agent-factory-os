# Memory Character Limits

## Definition

**Memory character limits** are hard upper bounds on curated memory stores that force consolidation, prevent prompt bloat, and make injection cost predictable.

## Why It Matters

Unbounded memory degrades retrieval quality, inflates token cost, and encourages dumping derivable facts instead of distilled insight. Hard limits turn memory curation from optional hygiene into a structural requirement.

## Architecture Implications

- Separate stores may use different limits (e.g., agent notes vs user profile) reflecting distinct curation roles.
- Entries use a delimiter format (e.g., `§`) so agents can replace or merge without full-document rewrite.
- Store headers should expose usage ratio (current/limit) so the agent can consolidate before hard failure.
- Reject-or-consolidate behavior on overflow is preferable to silent truncation.

## Production Implications

- Consolidation workflows (merge related entries, remove ephemera) must be documented for operators.
- Monitor stores approaching ~80% capacity as an operational signal.
- Limits should be chosen relative to model context budget and snapshot injection policy.

## Risks

- Too-small limits cause churn and lost nuance; too-large limits recreate unbounded growth.
- Agents may attempt to bypass limits via external scratch files without governance.

## Related Concepts

- [[frozen-memory-snapshot]]
- [[memory-taxonomy]]
- [[profile-isolation]]
- [[memory-provider-boundaries]]

## Related Anti-patterns

- [[unbounded-memory-growth]]
- [[memory-as-crutch]]
- [[mid-session-memory-injection]]

## Related Patterns

- [[verification-before-writeback]]
- [[memory-aware-execution]]

## Upstream Sources

- `Books/claude/ch11-memory.md`
- `experiments/hermes-agent-review/memory/MEMORY.md`
- `experiments/hermes-agent-review/memory/USER.md`

## Governance References

- `PROMOTION_REVIEW.md` §3.1
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
promotion_rationale: Extends memory taxonomy with enforceable bounds; Hermes evidence only, no provider implementation.
governance_reference: PROMOTION_REVIEW.md §3.1, governance/CANONICAL_DIRECTION.md Phase 1.2
```
