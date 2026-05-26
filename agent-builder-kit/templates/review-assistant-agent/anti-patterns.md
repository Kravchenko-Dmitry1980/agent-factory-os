# Review Assistant Agent — Anti-Patterns

Block these before accepting or implementing this template.

| Anti-pattern | Why blocked |
|--------------|-------------|
| Critic treated as judge | Critic is advisory; human final |
| Approval skipped | No delivery without human gate |
| Draft auto-published | Violates core purpose |
| Memory grows silently | v0.1 task-scoped only |
| Template becomes product | Kit stays spec layer |
| Review assistant becomes autonomous agent | Governance-before-autonomy |
| LLM output treated as truth | Verification required |
| Bypass path for "speed" | Fail-closed on bypass |
| External repo template dump | phase-2-10 research-only |
| Framework extraction from kit | No runtime in v0.1 |

## Checklist

Complete [anti-pattern-checklist-spec.md](../../template-specs/anti-pattern-checklist-spec.md) before acceptance.

## Doctrine Links

- `Books/swarm-playbooks/anti-patterns/critic-as-fake-verification.md`
- `agent-os/08_patterns/verification-before-writeback.md`
