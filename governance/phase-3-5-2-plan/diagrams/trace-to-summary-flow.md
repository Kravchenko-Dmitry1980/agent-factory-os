# Diagram — Trace to Summary Flow

**Phase 3.5.2-Plan**

```mermaid
flowchart LR
  subgraph DEMO_OUT["minimal_demo.py stdout"]
    D[decision=...]
    DEL[delivered=...]
    TR[TRACE lines]
  end

  subgraph RUNNER["demo_runner.py"]
    P1[Parse decision]
    P2[Parse delivered]
    P3[Extract key trace events]
    M[Lookup TRACE_EXPLANATION_MAPPING_RU]
    F[Format OPERATOR_OUTPUT_FORMAT_RU]
  end

  subgraph OP_VIEW["Operator sees"]
    RU[Russian summary block]
    RAW[Optional full raw output]
  end

  D --> P1
  DEL --> P2
  TR --> P3
  P3 --> M
  P1 --> F
  P2 --> F
  M --> F
  F --> RU
  TR --> RAW
```

## Safety checks in summary step

```mermaid
flowchart TD
  F[Format summary] --> C1{DELIVERED?}
  C1 -->|yes| C2{approval_granted in trace?}
  C2 -->|no| W[WARNING in summary]
  C2 -->|yes| OK[OK status]
  C1 -->|no| C3{unsafe_action_blocked?}
  C3 -->|yes| OK2[OK fail-closed noted]
  C3 -->|no| OK3[OK or context message]
```

## Principle

Parse does **not** reinterpret agent decisions — only **explains** what demo already decided.
