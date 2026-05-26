# Template Specs

Specifications that define **what every future agent template must include**.

| Spec | Purpose |
|------|---------|
| [agent-template-spec.md](agent-template-spec.md) | Master template structure |
| [workflow-template-spec.md](workflow-template-spec.md) | Standard safe workflow |
| [tool-boundary-spec.md](tool-boundary-spec.md) | Tool permissions and limits |
| [memory-boundary-spec.md](memory-boundary-spec.md) | Memory read/write rules |
| [human-approval-spec.md](human-approval-spec.md) | HITL approval policy |
| [observability-trace-spec.md](observability-trace-spec.md) | Required trace events |
| [evaluation-checklist-spec.md](evaluation-checklist-spec.md) | Evaluation requirements |
| [change-proposal-spec.md](change-proposal-spec.md) | Template change process |
| [anti-pattern-checklist-spec.md](anti-pattern-checklist-spec.md) | Pre-acceptance anti-pattern scan |

**Rule:** No agent template is accepted without safety gates, evaluation checklist, failure modes, human approval policy, trace template, and anti-pattern checklist.
