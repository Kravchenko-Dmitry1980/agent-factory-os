# Repository Review: claude-code-templates

## Basic Info

| Field | Value |
|-------|-------|
| **URL** | https://github.com/davila7/claude-code-templates |
| **Local path** | `external-repos-triage/source/claude-code-templates/` |
| **Main purpose** | Marketplace/catalog of Claude Code agents, commands, settings, hooks, MCPs, skills via `npx claude-code-templates` |
| **Claimed capabilities** | 100+ components, web dashboard aitmpl.com, analytics, health-check, plugin dashboard |
| **Primary audience** | Claude Code users wanting quick component installs |
| **Main language / stack** | Node CLI, large template tree, docs site, optional dashboard/cloudflare workers |
| **Last inspected** | 2026-05-25 |
| **Commit inspected** | `a8f3752` |

## What This Repo Is

**Каталог переиспользуемых компонентов** Claude Code с CLI установкой (`--agent`, `--command`, `--hook`, `--mcp`, `--setting`). Taxonomy by category (development-team, testing, performance, etc.).

## What This Repo Is NOT

- Not a governed learning lab
- Not minimal safety-first curriculum
- Not Agent Builder Kit v0.1 (too broad, too many MCPs)

## Most Useful Ideas

- **Component taxonomy**: agents / commands / settings / hooks / MCPs / skills
- Hierarchical paths: `category/subcategory/name`
- `npx ... --yes` non-interactive install pattern (for study only)
- Separation of concerns per component type

## Dangerous Ideas

- **Template dumping** via one-liner stacks
- MCP integrations (GitHub, Postgres, Stripe, AWS) — permission sprawl
- Hooks automation without human gates
- Analytics/chats/tunnel — extra runtime surface
- Marketplace growth = unreviewed community components

## Relevance

| Area | Relevance |
|------|-----------|
| Agent-OS | **None** — do not merge |
| Agent Builder Kit | **High** — template folder taxonomy, metadata |
| Cursor / Claude Code | **High** — operator layer patterns |
| Skills | **Medium** — skills as first-class component |
| Digital twins / CV | **Low in 3.0** |

## Security / Supply Chain

- Third-party MCP servers and hooks = high risk
- `--yes` bypasses interactive review
- Large attack surface (7000+ files in clone)

## What We Can Learn

- Folder naming for template types
- README tables mapping component → description → examples
- Progressive install (single component vs stack)

## What We Must Not Copy

- Bulk `npx claude-code-templates` into AGENT repo
- Default MCP pack
- Cloud analytics/tunnel features
- Marketplace as Phase 3 deliverable

## Decision

**STUDY_NOW** (structure and taxonomy only)

## Rationale

Closest analog to «Builder Kit components» layout — but our kit must stay **one Review Assistant spec**, not marketplace.

## Recommended Future Action

Phase 3.0: mirror **taxonomy ideas** in `agent-builder-kit/template-specs/` (empty categories), not import files. Phase 4+: controlled template registry with provenance.
