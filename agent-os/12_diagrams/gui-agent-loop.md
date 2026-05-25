# GUI Agent Loop Diagram

Mermaid view of the embodied agent cycle promoted in [[gui-agent-loop]].

```mermaid
flowchart TD
    START([Task start]) --> SCREEN[Screen: capture observation]
    SCREEN --> REASON[Reason: plan next action]
    REASON --> ACTION[Action: execute via adapter]
    ACTION --> FEEDBACK[Feedback: new screen + verify]
    FEEDBACK --> VERIFY{Verification A/B/C?}
    VERIFY -->|A: success| UPDATE[Update: progress + memory]
    VERIFY -->|B: wrong state| REPLAN[Replan / backtrack]
    VERIFY -->|C: no change| RETRY[Retry grounding / action]
    REPLAN --> REASON
    RETRY --> REASON
    UPDATE --> BUDGET{Step budget OK?}
    BUDGET -->|Yes| SCREEN
    BUDGET -->|No| STOP([Terminal: fail or escalate])
    UPDATE --> GOAL{Task complete?}
    GOAL -->|Yes| DONE([Terminal: success])
    GOAL -->|No| BUDGET
```

## Related Concepts

- [[gui-agent-loop]]
- [[visual-verification]]
- [[visual-grounding]]
- [[unverified-gui-clicks]]

## Semantic Cluster

gui-modality · verification

## Upstream Sources

- `experiments/mobile-agent-review/diagrams/gui-agent-loop.md`
- `agent-os/01_agent-runtime/gui-agent-loop.md`

## Governance References

- `governance/PROMOTION_LOG.md`

## Promotion Metadata

```yaml
maturity: reusable-pattern
promotion_decision: PROMOTE_NOW
source_tier: research
canonical_status: curated
```
