# Phase 3 Boundary

```mermaid
flowchart TB
  subgraph allowed [Phase 3.0 ALLOWED]
    MD[Markdown specs]
    TM[Templates docs]
    CL[Checklists]
    DG[Mermaid diagrams]
    RA[Review Assistant template]
  end

  subgraph forbidden [Phase 3.0 FORBIDDEN]
    RT[Runtime code]
    GEN[Generator]
    FAC[Factory]
    CV[CV builder]
    DT[Digital twin]
    RAG[RAG platform]
    MCP[MCP runtime]
    SW[Swarm]
  end

  P2[Phase 2 prototypes eval observability] --> allowed
  allowed -.reference.-> P2
  forbidden --> BLOCK[governance FAIL]
```

## Verdict label

**Agent Builder Kit v0.1** — specs only

Not: Agent Factory, Production Platform

Reference: [governance/phase-3-0-scope-lock.md](../governance/phase-3-0-scope-lock.md)
