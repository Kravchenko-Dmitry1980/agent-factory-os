# Review Assistant Agent — Workflow

## Standard Flow

```
task
  → draft
  → critique (optional, advisory)
  → verification
  → human review
  → approval / rejection
  → output (if approved)
  → trace
```

## Stage Detail

| Stage | Actor | Notes |
|-------|-------|-------|
| task | user / orchestrator | Accept goal and constraints |
| draft | assistant | Mark output unverified |
| critique | critic (optional) | **Advisory only** — not truth |
| verification | validator | Policy, format, fact checks |
| human review | human | Mandatory for delivery |
| approval / rejection | human | Explicit terminal decision |
| output | system | Only if approved |
| trace | audit | Canonical events required |

## Critical Rules

### Critique is useful but not truth

- Critic may pass, fail, or be uncertain
- Uncertain → fail-closed or escalate
- Human may reject even if critic passes

Reference: `prototypes/review-loop-agent/README.md` — "Critic ≠ truth"

### Human review is mandatory

- No final delivery without `approval_requested` → human approve
- Timeout → deny-by-default

## Alignment

Matches [workflow-template-spec.md](../../template-specs/workflow-template-spec.md) and prototype flow:

```
task → draft → critique → human review → approve/reject → publish (or stop)
```

Phase 3.0 spec uses "output" instead of "publish" to emphasize no auto-publish.

## Diagram

[diagrams/review-assistant-workflow.md](../../diagrams/review-assistant-workflow.md)
