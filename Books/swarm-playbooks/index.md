# Swarm Playbooks — Index

## Source

| File | Provenance |
|------|------------|
| [ai-agents-from-scratch.ru.md](source/ai-agents-from-scratch.ru.md) | [provenance](source/ai-agents-from-scratch.ru.provenance.md) |
| [swarm-ai-agents-prompts.ru.md](source/swarm-ai-agents-prompts.ru.md) | [provenance](source/swarm-ai-agents-prompts.ru.provenance.md) |

## Review

| File | Purpose |
|------|---------|
| [source-analysis.md](review/source-analysis.md) | Strengths, weaknesses, gaps |
| [promotion-candidates.md](review/promotion-candidates.md) | SAFE / RESEARCH / NEVER PROMOTE |

## Lifecycle & Orchestration

| File | Purpose |
|------|---------|
| [orchestration-lifecycle.md](lifecycle/orchestration-lifecycle.md) | Goal → publish lifecycle |
| [orchestration/](orchestration/) | Reserved for future orchestration notes |

## Patterns

| Pattern | Classification |
|---------|----------------|
| [human-in-the-loop-approval.md](patterns/human-in-the-loop-approval.md) | reusable-pattern |
| [progressive-autonomy.md](patterns/progressive-autonomy.md) | reusable-pattern |
| [review-gate.md](patterns/review-gate.md) | reusable-pattern |
| [orchestration-lifecycle.md](patterns/orchestration-lifecycle.md) | reusable-pattern |
| [queue-backed-execution.md](patterns/queue-backed-execution.md) | reusable-pattern |
| [critique-before-publish.md](patterns/critique-before-publish.md) | reusable-pattern |
| [staged-agent-evolution.md](patterns/staged-agent-evolution.md) | reusable-pattern |
| [execution-feedback-loop.md](patterns/execution-feedback-loop.md) | reusable-pattern |
| [approval-before-external-action.md](patterns/approval-before-external-action.md) | reusable-pattern |

## Anti-patterns

| Anti-pattern | Classification |
|--------------|----------------|
| [premature-agent-swarm.md](anti-patterns/premature-agent-swarm.md) | non-promotable |
| [critic-as-fake-verification.md](anti-patterns/critic-as-fake-verification.md) | non-promotable |
| [orchestration-without-contracts.md](anti-patterns/orchestration-without-contracts.md) | non-promotable |
| [personality-over-architecture.md](anti-patterns/personality-over-architecture.md) | non-promotable |
| [prompt-chain-fragility.md](anti-patterns/prompt-chain-fragility.md) | non-promotable |
| [unbounded-agent-autonomy.md](anti-patterns/unbounded-agent-autonomy.md) | non-promotable |
| [automation-without-review.md](anti-patterns/automation-without-review.md) | non-promotable |
| [tutorial-driven-architecture.md](anti-patterns/tutorial-driven-architecture.md) | non-promotable |

## Human-in-the-loop

| File | Purpose |
|------|---------|
| [human-approval-boundaries.md](hitl/human-approval-boundaries.md) | Where humans must approve |
| [review-before-publish.md](hitl/review-before-publish.md) | Pre-publish review gate |
| [escalation-to-human.md](hitl/escalation-to-human.md) | When to escalate |
| [safe-autonomy.md](hitl/safe-autonomy.md) | Bounded autonomy |

## Critique

| File | Purpose |
|------|---------|
| [critic-loop.md](critique/critic-loop.md) | Automated critique workflow |
| [critique-vs-verification.md](critique/critique-vs-verification.md) | Critique ≠ verification |
| [critique-limitations.md](critique/critique-limitations.md) | Hard limits of critic agents |

## Budget & Execution

| File | Purpose |
|------|---------|
| [budget-aware-orchestration.md](budget-control/budget-aware-orchestration.md) | Budget limits on runs |
| [execution-cost-visibility.md](budget-control/execution-cost-visibility.md) | Cost/token visibility |
| [retry-cost-awareness.md](budget-control/retry-cost-awareness.md) | Retry and rework costs |

## Diagrams

| Diagram | Topic |
|---------|-------|
| [orchestration-lifecycle.md](diagrams/orchestration-lifecycle.md) | Full lifecycle |
| [review-gates.md](diagrams/review-gates.md) | Human approval points |
| [critique-loop.md](diagrams/critique-loop.md) | Critic rework loop |
| [staged-autonomy.md](diagrams/staged-autonomy.md) | MVP → swarm evolution |
| [queue-backed-execution.md](diagrams/queue-backed-execution.md) | Background queue |

## Glossary

| Term | File |
|------|------|
| [orchestrator.md](glossary/orchestrator.md) | Orchestrator role |
| [critic-agent.md](glossary/critic-agent.md) | Critic agent (limited) |
| [run.md](glossary/run.md) | Swarm run / прогон |
| [review-queue.md](glossary/review-queue.md) | Human review state |

## Governance

| File | Purpose |
|------|---------|
| [corpus-positioning.md](governance/corpus-positioning.md) | Boundaries vs Agent-OS |
