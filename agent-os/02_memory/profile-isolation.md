# Profile Isolation

## Definition

**Profile isolation** is the architectural boundary that gives each persistent agent instance its own memory stores, skills, task history, and configuration — preventing cross-contamination between twin instances or deployment roles.

## Why It Matters

Digital twins and specialized agents require stable, scoped identity. Shared default stores collapse distinct roles into one polluted user model and procedural memory.

## Architecture Implications

- Each profile owns isolated curated memory paths (agent notes, user model) — not shared with sibling profiles.
- Ephemeral subagents remain separate: they do not write to parent or profile stores.
- Profile selection is an environment boundary, not a prompt tweak — equivalent to distinct home roots or namespace prefixes.
- Cross-ref [[persistent-identity]] for session-scoped IDs; profile isolation adds instance-scoped persistence.

## Production Implications

- Fleet deployments (triage bot, coding bot, research bot) require explicit profile provisioning.
- Backup, migration, and audit scope per profile — not whole-system dumps.
- Profile deletion must define archive policy for memory and skills.

## Risks

- Operators may reuse default profile for all workloads, negating isolation benefits.
- Copy-paste configuration between profiles can leak secrets or wrong user models.

## Related Concepts

- [[memory-char-limits]]
- [[frozen-memory-snapshot]]
- [[memory-provider-boundaries]]
- [[persistent-identity]]
- [[subagent-tool-restrictions]]

## Related Anti-patterns

- [[unbounded-memory-growth]]
- [[mid-session-memory-injection]]

## Related Patterns

- [[memory-aware-execution]]
- [[verification-before-writeback]]

## Upstream Sources

- `experiments/hermes-agent-review/notes/DIGITAL_TWIN_IMPLICATIONS.md`
- `experiments/hermes-agent-review/runtime/RUNTIME_OVERVIEW.md`

## Governance References

- `PROMOTION_REVIEW.md` §3.6
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
promotion_rationale: Twin instance boundary promoted as memory governance concept; placed in 02_memory per Phase 1.2 scope (bounded stores per instance).
governance_reference: PROMOTION_REVIEW.md §3.6, governance/CANONICAL_DIRECTION.md Phase 1.2
```
