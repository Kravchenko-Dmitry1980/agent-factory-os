# Brain OS State Machine

## States

```
RECEIVED → CLASSIFIED → ROUTED → MEMORY_READY → EXECUTING → EVALUATING → COMPLETED
```

## Terminal / Exception

- **FAILED**
- **ESCALATED** (human escalation)
- **FALLBACK_EXECUTED**

## Events per Transition

| Transition | Event |
|------------|-------|
| classify | TASK_CLASSIFIED |
| route | ROUTING_DECIDED |
| memory | MEMORY_RETRIEVAL_* |
| policy | POLICY_SELECTED |
| execute | REASONING_* |
| evaluate | EVALUATION_COMPLETED |
| complete | TASK_COMPLETED |

## Maturity

production-relevant

## Provenance

`source/Brain OS.docx` C.§3
