# Review Loop — Governance

## Principles

| Principle | Implementation |
|-----------|----------------|
| Critique before publish | Critic runs before human queue |
| Critic ≠ verification | Verdict is advisory only |
| Human-in-the-loop | Mandatory approve for publish |
| Fail-closed | Uncertain → block, not proceed |
| Audit | All transitions logged |

## HITL Boundaries

- **Human required:** external publish, approval after critique
- **Human optional:** none in this prototype (by design)
- **Human override:** can approve despite critic fail (logged disagreement)

## Alignment

- `Books/swarm-playbooks/hitl/review-before-publish.md`
- `agent-os/08_patterns/verification-before-writeback.md`
- `prototypes/governance/failure-first-thinking.md`

## Forbidden

- Treating critic as ground truth
- Removing human gate "for speed"
- Publishing on `uncertain` without explicit human waiver (not implemented — would be high-risk)
