# Progressive Skill Disclosure

## Definition

**Progressive skill disclosure** is tiered skill loading — catalog metadata first, full procedure on demand, reference files last — minimizing token overhead while preserving access to deep procedural knowledge.

## Why It Matters

Loading entire skill libraries into every turn causes token explosion and cache pressure. Disclosure tiers align skill access with actual task need.

## Architecture Implications

| Level | Content returned | When loaded |
|-------|------------------|-------------|
| L0 | Name, description, category list | Every turn (catalog) |
| L1 | Full skill document | Agent requests specific skill |
| L2 | Attached reference files | Deep procedure requires detail |

- Slash commands or explicit invoke bypass L0 for known workflows.
- Conditional activation metadata (platform, required toolsets) filters catalog without loading bodies.
- Pairs with [[skill-graphs]] and digital-twin procedural memory — curator lifecycle deferred to Phase 1.3.

## Production Implications

- Monitor catalog size; L0 budget is recurring cost.
- Skill authorship standards: concise L1, heavy detail in L2 references.
- Without disclosure, 100+ skills become unusable in production context windows.

## Risks

- L0 catalog still large at 160+ skills — needs category filtering.
- Agent fails to escalate L1 when L0 insufficient.

## Related Concepts

- [[memory-char-limits]]
- [[skill-graphs]]
- [[recursive-self-improvement]]

## Related Anti-patterns

- [[recursive-self-improvement]]

## Related Patterns

- [[memory-char-limits]] (token budget parallel)

## Upstream Sources

- `experiments/hermes-agent-review/skills/SKILLS_SYSTEM_OVERVIEW.md`
- `Books/claude/ch12-extensibility.md` (planned extraction — research catalog)

## Governance References

- `PROMOTION_REVIEW.md` §3.4
- `governance/PROMOTION_LOG.md`
- `governance/SEMANTIC_DRIFT_ANALYSIS.md`

## Semantic Cluster

memory-governance

## Promotion Metadata

```yaml
maturity: reusable-pattern
promotion_decision: PROMOTE_NOW
source_tier: research
canonical_status: curated
promotion_rationale: Addresses ch12 skills gap; no agentskills.io vendor spec as normative contract.
governance_reference: PROMOTION_REVIEW.md §3.4, governance/CANONICAL_DIRECTION.md Phase 1.2
```
