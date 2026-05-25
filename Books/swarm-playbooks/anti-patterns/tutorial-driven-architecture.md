# Tutorial-Driven Architecture

---
classification: non-promotable
source_tier: operational-playbook
promotion_status: unreviewed
canonical_status: non-canonical
origin: swarm-playbooks
---

## Statement

Adopting the **tutorial stack and folder layout** (npm workspaces, Next.js dashboard, Express backend, seed.sql personas) as the system's architecture rather than extracting domain-specific requirements and contracts.

## Symptoms

- Architecture.md equals technology shopping list
- Eight agents because tutorial Prompt 2 says so
- PostgreSQL chosen before data model requirements clear
- CLAUDE.md treated as governance document

## Why It Fails

- Stack fits author’s tutorial path, not operator’s constraints
- Hard to migrate when requirements diverge (e.g. headless API-only)
- Confuses **learning scaffold** with **production topology**

## Corrective Pattern

- [staged-agent-evolution.md](../patterns/staged-agent-evolution.md) — treat tutorial as sequence, not blueprint
- Extract patterns from `patterns/`; leave boilerplate in `source/`

## Sources

- Both source files — extensive install and framework prompts (Prompt 0–1)

## Promotion Potential

**NEVER PROMOTE** tutorial structure to canonical architecture.
