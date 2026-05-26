# Diagram — Operator Flow

**Phase 3.5.2-Plan**

```mermaid
flowchart TD
  START([Operator starts demo_runner.py]) --> SHOW[Show menu Groups 1-4]
  SHOW --> CHOICE{Select item}

  CHOICE -->|1.x-2.x demo| RUN_DEMO[subprocess minimal_demo.py]
  CHOICE -->|3.1 real provider| WARN[Show LM Studio warning]
  CHOICE -->|4.x eval| RUN_EVAL[subprocess check_*.py]
  CHOICE -->|0| EXIT([Exit])

  WARN --> CONFIRM{Continue y/N?}
  CONFIRM -->|N default| SHOW
  CONFIRM -->|y + env OK| RUN_PROVIDER[subprocess --real-provider]
  CONFIRM -->|env missing| ABORT[Print abort message]
  ABORT --> SHOW

  RUN_DEMO --> PARSE[Parse decision + trace]
  RUN_PROVIDER --> PARSE
  RUN_EVAL --> EVAL_SUM[Print PASS/FAIL summary RU]

  PARSE --> SUMMARY[Print Russian operator block]
  SUMMARY --> SAVE{--save-transcript?}
  SAVE -->|yes| WRITE[Write transcript.md]
  SAVE -->|no| SHOW
  WRITE --> SHOW
  EVAL_SUM --> SHOW
```

## Notes

- Default path is no-network (groups 1, 2, 4).
- Group 3 never runs without explicit confirmation.
- Loop returns to menu until operator exits.
