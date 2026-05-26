# Repository Review: ruflo

## Basic Info

| Field | Value |
|-------|-------|
| **URL** | https://github.com/ruvnet/ruflo |
| **Local path** | `external-repos-triage/source/ruflo/` |
| **Main purpose** | «Multi-agent orchestration for Claude Code» — swarms, MCP, RAG memory, federation, 33+ plugins |
| **Claimed capabilities** | 100+ agents, self-learning memory, RuVector/Graph RAG, autopilot, enterprise security, npm `npx ruflo init` |
| **Primary audience** | Power users wanting agent platforms on Claude Code |
| **Main language / stack** | TypeScript/Rust ecosystem, large monorepo, plugins, MCP server, hooks, daemon |
| **Last inspected** | 2026-05-25 |
| **Commit inspected** | `60f37f2` |

## What This Repo Is

**Платформа оркестрации** поверх Claude Code: устанавливает `.claude/`, `.claude-flow/`, MCP, hooks, swarm commands. Marketing emphasizes scale (22M+ downloads, 100+ agents).

## What This Repo Is NOT

- Not aligned with Agent-OS «small demos, visible gates»
- Not Phase 3.0 material
- Not safe default for learners

## Most Useful Ideas

- Clear doc that **plugin path ≠ full CLI path** (different surface area)
- Warning that lite plugin lacks MCP tools — honest comparison table
- Federation / memory as **future research topics** only

## Dangerous Ideas

- **Swarm / autopilot / self-learning memory** — direct conflict with bounded-memory doctrine
- **RAG + graph + vector DB plugins** — frozen in our Phase 3
- `npx ruvflo init` — massive workspace mutation
- Platform drift exemplar (`evolution/examples/unsafe-shared-runtime.md` archetype)
- Hype metrics (downloads, clones) as social proof

## Relevance

| Area | Relevance |
|------|-----------|
| Agent-OS | **Reject for promotion** |
| Agent Builder Kit | **NONE for 3.0** |
| Phase 3 | **Must not influence** |
| Long-term | **Negative reference** for drift training |

## Security / Supply Chain

- MCP server with broad tool surface
- Many plugins = large trust boundary
- Autonomous loops

## What We Can Learn

- Anti-pattern case study for curriculum «platform drift»
- Plugin-vs-full-install distinction (teaching clarity)

## What We Must Not Copy

- Anything — no code, no commands, no init

## Decision

**FREEZE** (research-only as cautionary tale; **REJECT** for adoption)

## Rationale

Highest **platform drift** and **runtime-before-specs** risk in the set.

## Recommended Future Action

Use in teacher notes: «what happens if Phase 3 becomes ruflo». Revisit only if explicit multi-year platform phase with new governance — not planned.
