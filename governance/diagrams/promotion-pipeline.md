# Promotion Pipeline

```mermaid
flowchart LR
    S[Source / Experiment] --> E[Extraction note draft]
    E --> R[Promotion scoring]
    R --> G[Governance review]
    G -->|PROMOTE_NOW| C[Curated agent-os/]
    G -->|PROMOTE_LATER| Q[Backlog]
    G -->|RESEARCH_ONLY| X[Stay in Books/experiments]
    G -->|REJECT| Z[Archive / anti-pattern only]
    C --> V[Validate: provenance dedup wikilinks]
```
