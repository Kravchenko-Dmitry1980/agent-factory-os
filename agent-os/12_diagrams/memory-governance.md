# Memory Governance Diagram

Mermaid view of bounded memory layers and injection policy.

```mermaid
flowchart TB
    subgraph bootstrap [Session bootstrap]
        SNAP[Frozen memory snapshot]
        SNAP --> PROMPT[System prompt static boundary]
    end

    subgraph stores [Curated stores per profile]
        MEM[Agent notes - char limited]
        USER[User profile - char limited]
    end

    subgraph external [External layer - max one]
        EXT[External provider recall]
    end

    PROFILE[[profile-isolation]] --> stores
    stores --> SNAP
    EXT -. optional augment .-> SNAP

    WRITE[Memory tool write] --> stores
    WRITE -. no mid-session inject .-> PROMPT

    subgraph contexts [Write gates]
        PRIMARY[Primary agent - writes allowed]
        SUB[Subagent - writes blocked]
        CRON[Scheduled job - writes blocked]
    end

    contexts --> WRITE

    VERIFY[[verification-before-writeback]] --> WRITE
```

## Related Concepts

- [[frozen-memory-snapshot]]
- [[memory-char-limits]]
- [[memory-provider-boundaries]]
- [[profile-isolation]]
- [[mid-session-memory-injection]]

## Semantic Cluster

memory-governance

## Upstream Sources

- `experiments/hermes-agent-review/memory/MEMORY_SYSTEM_OVERVIEW.md`
- `agent-os/02_memory/frozen-memory-snapshot.md`

## Governance References

- `governance/PROMOTION_LOG.md`

## Promotion Metadata

```yaml
maturity: reusable-pattern
promotion_decision: PROMOTE_NOW
source_tier: research
canonical_status: curated
```
