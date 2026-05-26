# Diagram — Demo Runner Boundary

**Phase 3.5.2-Plan**

```mermaid
flowchart TB
  subgraph IN_SCOPE["Demo Runner (future)"]
    MENU[Fixed Russian Menu]
    WRAP[subprocess wrapper]
    PARSE[Parse stdout]
    SUM[Russian Summary]
    WARN[Provider Warning]
    TX[Optional Transcript]
  end

  subgraph FROZEN["Frozen — do not modify"]
    DEMO[minimal_demo.py]
    EVAL[evaluation/scripts/check_*.py]
  end

  subgraph OUT["Out of scope"]
    UI[Web UI]
    RT[Runtime]
    FAC[Factory]
    AGENT[New agent logic]
  end

  OP[Operator] --> MENU
  MENU --> WRAP
  WRAP --> DEMO
  WRAP --> EVAL
  DEMO --> PARSE
  EVAL --> PARSE
  PARSE --> SUM
  MENU --> WARN
  WARN -->|confirm yes| WRAP
  SUM --> TX

  UI -.->|forbidden| OUT
  RT -.->|forbidden| OUT
  FAC -.->|forbidden| OUT
  AGENT -.->|forbidden| OUT
```

## Legend

| Box | Meaning |
|-----|---------|
| Demo Runner | One stdlib script — wrapper only |
| Frozen | Existing behavior unchanged |
| Out of scope | Not in Phase 3.5.2 |
