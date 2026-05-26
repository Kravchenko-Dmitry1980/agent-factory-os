# Repository Review: agentic-project-management

## Basic Info

| Field | Value |
|-------|-------|
| **URL** | https://github.com/sdi2200262/agentic-project-management |
| **Local path** | `external-repos-triage/source/agentic-project-management/` |
| **Main purpose** | APM framework: Planner / Manager / Worker multi-agent PM with handoff memory |
| **Claimed capabilities** | Structured Spec/Plan/Rules docs, CLI `apm init`, slash commands, session archive, apm-auto semi variants |
| **Primary audience** | Teams building software with AI agents (Claude Code, Cursor, Codex, etc.) |
| **Main language / stack** | npm CLI `agentic-pm`, markdown templates, skills for customization |
| **Last inspected** | 2026-05-25 |
| **Commit inspected** | `67b954d` |

## What This Repo Is

**Методология управления проектом** через роли агентов и файлы состояния вне контекста чата. Human mediates every agent message — audit trail by design.

## What This Repo Is NOT

- Not fail-closed execution layer
- Not trace-first observability like our demos
- Not replacement for evolution/change-proposals + evaluation

## Most Useful Ideas

- Three planning artifacts: **Spec, Plan, Rules**
- Worker domain boundaries (frontend/backend)
- **Handoff** when context full — structured knowledge transfer
- Human-in-the-loop between all agent hops
- `apm-auto` documented as **different risk model** (autonomous subagents)

## Dangerous Ideas

- `apm-auto` — Manager spawns subagents without user shuttle (conflicts with our governance)
- npm global install mutates workspace
- Could duplicate operator-playbooks + curriculum without safety gates

## Relevance

| Area | Relevance |
|------|-----------|
| Agent-OS | **Low** |
| Agent Builder Kit | **Medium** — project-management agent template later |
| Cursor / Claude Code | **High** — slash command workflow |
| Operator playbooks | **Medium** — complements, not replaces |
| Project-lead curriculum | **Medium** |

## Security / Supply Chain

- CLI installs commands/skills into workspace
- Custom repo fork path (`apm custom`)

## What We Can Learn

- Externalized project state files
- Role separation planner vs executor
- Explicit handoff procedure

## What We Must Not Copy

- APM CLI into our repo
- Autonomous worker dispatch as default
- Overlap with Phase 3.0 scope

## Decision

**STUDY_LATER**

## Rationale

Valuable for **Phase 4+ project-management agent template**, overlaps with existing evolution/operator layers — not Phase 3.0.

## Recommended Future Action

After Review Assistant template: compare APM Spec/Plan/Rules to our change-proposal template; optional playbook addendum for leads.
