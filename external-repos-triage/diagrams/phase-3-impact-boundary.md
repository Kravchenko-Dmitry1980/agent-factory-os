# Phase 3 Impact Boundary

```mermaid
flowchart TB
    EXT[External repos]
    INSPIRE[Allowed: structure ideas only]
    BLOCK[Forbidden: code install runtime]
    P3[Phase 3.0 Agent Builder Kit MD]
    INT[Internal: review-loop-agent]
    EXT --> INSPIRE --> P3
    EXT --> BLOCK
    INT --> P3
    BLOCK -.->|no path| P3
```
