# Review Assistant Workflow

```mermaid
flowchart LR
  T[task] --> D[draft]
  D --> C{critique optional}
  C --> V[verification]
  V -->|pass| H[human review]
  V -->|fail| X[stop / escalate]
  C -->|uncertain| X
  H --> A{approval?}
  A -->|approve| O[output]
  A -->|deny| F[task_failed]
  A -->|timeout| F
  O --> TR[trace / audit]
  X --> TR
  F --> TR
```

## Rules

- Critique is **advisory** — dashed mentally, not a gate replacement
- Human review **mandatory** before output
- No output on reject or timeout (deny-by-default)

Reference: [templates/review-assistant-agent/workflow.md](../templates/review-assistant-agent/workflow.md)
