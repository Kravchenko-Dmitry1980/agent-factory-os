# Research Repository

Normalized research layer for the Claude Code architecture book corpus. This tree ** catalogs, plans, and navigates** — it does not replace or rewrite source chapters.

## Purpose

1. Preserve original chapters in `Books/claude/` (unchanged)
2. Provide a dedicated research hierarchy for decomposition work
3. Plan extraction into Agent-OS atomic notes (concepts, patterns, anti-patterns, glossary)
4. Track extraction status chapter-by-chapter

## Structure

```
10_research/
├── README.md                 ← you are here
├── sources.md                ← preservation policy
├── extraction-plan.md        ← master decomposition plan
├── chapters/                 ← index stubs → Books/claude/
│   └── index.md
├── concepts/                 ← atomic concept extraction plan
│   ├── index.md
│   └── extraction-plan.md
├── patterns/                 ← architecture pattern extraction plan
│   ├── index.md
│   └── extraction-plan.md
└── glossary/                 ← terminology extraction plan
    ├── index.md
    └── extraction-plan.md
```

## Workflow (Research Phase)

```mermaid
flowchart LR
    A[Read chapter in Books/claude] --> B[Update chapter index stub status]
    B --> C[Extract atomic note per plan]
    C --> D[Place in agent-os/00–09]
    D --> E[Link bidirectionally]
    E --> F[Mark plan row extracted]
```

**Current phase:** repository architecture + decomposition planning only. No semantic rewrites.

## Quick Navigation

| Need | Go to |
|------|-------|
| Read original chapter | [sources.md](sources.md) → `Books/claude/` |
| Chapter catalog | [chapters/index.md](chapters/index.md) |
| What to extract next | [extraction-plan.md](extraction-plan.md) |
| Concept targets | [concepts/extraction-plan.md](concepts/extraction-plan.md) |
| Pattern targets | [patterns/extraction-plan.md](patterns/extraction-plan.md) |
| Glossary targets | [glossary/extraction-plan.md](glossary/extraction-plan.md) |
| Already extracted notes | [Agent-OS README](../README.md) |

## Extraction Status Summary

| Status | Chapters |
|--------|----------|
| **Planned, partially extracted** | ch01–08, ch10–11, ch15 |
| **Planned, not yet extracted** | ch09, ch12–14, ch16–18 |
| **Meta / synthesis** | ch18 (maps to foundations + patterns) |

See [extraction-plan.md](extraction-plan.md) for per-chapter row-level status.

## Up

- [Agent-OS README](../README.md)
- [Research index (legacy entry)](index.md)
