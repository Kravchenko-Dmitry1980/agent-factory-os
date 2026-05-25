# Architecture Diagrams

Mermaid diagrams for Hermes Agent architecture understanding.

---

## System Overview

```mermaid
flowchart TB
    subgraph Entry["Entry Points"]
        CLI["CLI (cli.py)"]
        GW["Gateway (gateway/run.py)"]
        ACP["ACP Adapter"]
        CRON["Cron Scheduler"]
        LIB["Python Library"]
    end

    subgraph Core["AIAgent Core"]
        PB["Prompt Builder"]
        MM["Memory Manager"]
        PR["Provider Resolution"]
        TD["Tool Dispatch"]
    end

    subgraph Storage["Persistence"]
        SDB["SQLite + FTS5"]
        MEM["MEMORY.md / USER.md"]
        SK["Skills"]
        KB["Kanban DB"]
    end

    subgraph Backends["Tool Backends"]
        TERM["Terminal (7 backends)"]
        BR["Browser (5 backends)"]
        MCP["MCP Client"]
        WEB["Web Tools"]
    end

    CLI --> Core
    GW --> Core
    ACP --> Core
    CRON --> Core
    LIB --> Core

    Core --> Storage
    Core --> Backends
```

---

## Memory System

```mermaid
flowchart LR
    subgraph BuiltIn["Built-in (always active)"]
        M["MEMORY.md<br/>2200 chars"]
        U["USER.md<br/>1375 chars"]
    end

    subgraph External["External (one only)"]
        H["Honcho"]
        M0["Mem0"]
        HS["Hindsight"]
        OV["OpenViking"]
    end

    MM["MemoryManager"] --> BuiltIn
    MM --> External

    MM --> SP["System Prompt<br/>(frozen snapshot)"]
    MM --> PF["Prefetch<br/>(background)"]
    MM --> SY["Sync Turn<br/>(post-response)"]
```

---

## Multi-Agent Models

```mermaid
flowchart TB
    subgraph Delegate["delegate_task (RPC)"]
        P1["Parent Agent"] -->|"goal + context"| S1["Subagent"]
        S1 -->|"summary only"| P1
    end

    subgraph Kanban["Kanban (Durable Queue)"]
        D["Dispatcher"] -->|"spawn"| W1["Worker Profile"]
        D -->|"spawn"| W2["Worker Profile"]
        W1 --> DB["kanban.db"]
        W2 --> DB
        H["Human"] -->|"comment/unblock"| DB
    end
```

---

## Skill Progressive Disclosure

```mermaid
flowchart LR
    L0["Level 0<br/>skills_list()<br/>~3k tokens"] --> L1["Level 1<br/>skill_view(name)<br/>full content"]
    L1 --> L2["Level 2<br/>skill_view(name, path)<br/>reference file"]
    
    L0 -.->|"agent decides needed"| L1
    L1 -.->|"needs reference"| L2
```

---

## Profile Isolation

```mermaid
flowchart TB
    subgraph Default["~/.hermes/ (default)"]
        DC["config.yaml"]
        DM["memories/"]
        DS["state.db"]
        DSK["skills/"]
    end

    subgraph Coder["~/.hermes/profiles/coder/"]
        CC["config.yaml"]
        CM["memories/"]
        CS["state.db"]
        CSK["skills/"]
    end

    subgraph Researcher["~/.hermes/profiles/researcher/"]
        RC["config.yaml"]
        RM["memories/"]
        RS["state.db"]
        RSK["skills/"]
    end

    KB["kanban.db<br/>(shared board)"] --> Coder
    KB --> Researcher
```

---

## Agent Loop Sequence

```mermaid
sequenceDiagram
    participant U as User
    participant A as AIAgent
    participant P as Prompt Builder
    participant M as Memory Manager
    participant L as LLM Provider
    participant T as Tools

    U->>A: message
    A->>P: build_system_prompt()
    P-->>A: SOUL + memory + skills
    A->>M: prefetch_all()
    M-->>A: recalled context
    A->>L: API call
    L-->>A: response / tool_calls
    loop tool execution
        A->>T: handle_function_call()
        T-->>A: result
        A->>L: continue
    end
    A->>M: sync_all()
    A->>A: persist session
    A-->>U: final response
```

---

## Kanban vs Delegate Decision

```mermaid
flowchart TD
    Q{"Need multi-agent?"}
    Q -->|No| SOLO["Single agent"]
    Q -->|Yes| DUR{"Work duration?"}
    
    DUR -->|"Short, parent waits"| DEL["delegate_task"]
    DUR -->|"Long, survives restarts"| KAN["Kanban"]
    
    DEL --> PAR{"Parallel?"}
    PAR -->|Yes| BATCH["delegate_task(tasks=[...])"]
    PAR -->|No| SINGLE["delegate_task(goal, context)"]
    
    KAN --> HIL{"Human in loop?"}
    HIL -->|Yes| KAN
    HIL -->|No| KAN
    
    KAN --> MULTI{"Multiple roles?"}
    MULTI -->|Yes| SWARM["Kanban Swarm"]
    MULTI -->|No| WORKER["Single worker profile"]
```

---

## Curator Lifecycle

```mermaid
stateDiagram-v2
    [*] --> Active: skill created
    Active --> Pinned: pin (manual/curator)
    Active --> Stale: 30+ days unused
    Stale --> Active: used again
    Stale --> Archived: 90+ days unused
    Archived --> Active: manual restore
    Pinned --> Active: unpin
    
    note right of Archived: Never auto-deleted
    note right of Pinned: Bypass all auto-transitions
```
