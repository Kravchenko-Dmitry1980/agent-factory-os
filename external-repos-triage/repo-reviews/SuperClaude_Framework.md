# Repository Review: SuperClaude_Framework

## Basic Info

| Field | Value |
|-------|-------|
| **URL** | https://github.com/SuperClaude-Org/SuperClaude_Framework |
| **Local path** | `external-repos-triage/source/SuperClaude_Framework/` |
| **Main purpose** | Meta-framework for Claude Code: 30 slash commands, 20 agents, 7 modes, 8 MCP servers |
| **Claimed capabilities** | Behavioral instruction injection, pip/npm install, Smithery distribution |
| **Primary audience** | Claude Code power users wanting structured dev workflows |
| **Main language / stack** | Python package `superclaude`, markdown commands, docs; v4.3 stable, v5 plugin system planned |
| **Last inspected** | 2026-05-25 |
| **Commit inspected** | `226c45c` |

## What This Repo Is

**Надстройка поведения** Claude Code через slash-команды (`/sc:*`), personas, modes — «structured development platform» without being Anthropic official.

## What This Repo Is NOT

- Not governance-first lab
- Not minimal trace-first teaching path
- Not v5 plugin system yet (docs warn TS plugins not available)

## Most Useful Ideas

- **Command taxonomy** by lifecycle (brainstorm → deploy)
- PLANNING.md / TASK.md / KNOWLEDGE.md session files for agents
- Commands reference with decision trees
- Disclaimer: not affiliated with Anthropic

## Dangerous Ideas

- **Persona / mode explosion** — persona-over-architecture
- **8 MCP servers** bundled conceptually
- 30 commands — command explosion for beginners
- pip/npm install modifies global/user config

## Relevance

| Area | Relevance |
|------|-----------|
| Agent Builder Kit | **Low 3.0** — command naming ideas only |
| Cursor operator | **Medium later** |
| Curriculum | **Anti-pattern** persona-over-architecture |

## Security / Supply Chain

- Third-party MCP integrations in docs
- Global install via pipx

## What We Can Learn

- Command naming groups
- Session doc pattern (planning/task/knowledge) — analog to our learning log + runbooks

## What We Must Not Copy

- Wholesale slash command pack
- Personas as gates substitute

## Decision

**STUDY_LATER**

## Rationale

Teaching value for **command taxonomy** after core safety mastered; high confusion risk if adopted early.

## Recommended Future Action

Phase 4: optional «operator command map» doc — 5–10 commands max, not 30.
