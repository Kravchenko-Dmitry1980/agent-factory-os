# Diagram — Free-Form CLI Boundary

**Phase 3.5.3-Plan**

```mermaid
flowchart TB
  subgraph IN_SCOPE["Free-Form CLI (future)"]
    INPUT[Operator Task Text]
    VALID[Input Validation]
    MODE[Mode Select mock/default]
    FLOW[Review-like Flow]
    GATES[Safety Gates]
    SUM[Russian Summary]
    TRACE[TRACE Output]
    TX[Optional Transcript]
  end

  subgraph FROZEN["Frozen — do not modify in 3.5.3"]
    RUNNER[demo_runner.py v0.1]
    DEMO[minimal_demo.py]
    EVAL[evaluation/scripts]
  end

  subgraph OUT["Out of scope"]
    UI[Web UI]
    RT[Runtime]
    FAC[Factory]
    MEM[Memory/DB]
    CHAT[Multi-turn Chat]
    EXEC[External Execution]
  end

  OP[Operator] --> INPUT
  INPUT --> VALID
  VALID --> MODE
  MODE --> FLOW
  FLOW --> GATES
  GATES --> SUM
  GATES --> TRACE
  SUM --> TX

  RUNNER -.->|separate entry| OP
  DEMO -.->|no modify| FROZEN
  EVAL -.->|no modify| FROZEN

  UI -.->|forbidden| OUT
  RT -.->|forbidden| OUT
  FAC -.->|forbidden| OUT
  MEM -.->|forbidden| OUT
  CHAT -.->|forbidden| OUT
  EXEC -.->|forbidden| OUT
```

## Legend

| Box | Meaning |
|-----|---------|
| Free-Form CLI | Future `free_form_cli.py` — controlled input mode |
| Frozen | Unchanged in this track |
| Out of scope | Not Phase 3.5.3 |
