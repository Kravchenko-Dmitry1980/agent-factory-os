# Claude Code vs Hermes Agent

**Comparison date:** 2026-05-25  
**Sources:** Agent-OS Claude Code corpus + Hermes architecture audit

---

## Summary

| Dimension | Claude Code | Hermes Agent |
|-----------|-------------|--------------|
| **Nature** | Production CLI (Anthropic) | Open-source agent (Nous Research) |
| **Language** | TypeScript (~2000 files) | Python (~400 modules) |
| **Primary use** | Developer coding assistant | Self-improving general agent |
| **Distribution** | npm package | pip/uv install |
| **Platforms** | CLI + IDE extensions | CLI + 20+ messaging gateways |

---

## Architecture Comparison

| Abstraction | Claude Code | Hermes |
|-------------|-------------|--------|
| Query Loop | Single `query()` path | `AIAgent.run_conversation()` |
| Tools | Built-in + MCP | 70+ native + MCP client |
| Tasks | Task tool (subagents) | delegate_task + Kanban |
| State | Two-tier state | SQLite + profiles |
| Memory | CLAUDE.md + auto memory | MEMORY.md + USER.md + providers |
| Hooks | Lifecycle hooks | Gateway hooks + curator |

---

## Memory Comparison

| Aspect | Claude Code | Hermes |
|--------|-------------|--------|
| User memory | CLAUDE.md project files | USER.md (1375 chars) |
| Agent memory | Auto memory feature | MEMORY.md (2200 chars) |
| Limits | Project-scoped | Hard char limits |
| Injection | Dynamic | Frozen snapshot at session start |
| External providers | None built-in | 8 providers (Honcho, Mem0, ...) |
| Session search | Limited | FTS5 full-text search |
| User modeling | None | Honcho dialectic |

**Hermes advantage:** Bounded memory forces curation; external provider ecosystem.

**Claude Code advantage:** Deep IDE integration; project file context.

---

## Multi-Agent Comparison

| Aspect | Claude Code | Hermes |
|--------|-------------|--------|
| Subagent spawn | Task tool | delegate_task |
| Parallel | Multiple tasks | Batch mode (max 3 default) |
| Durable queue | None | Kanban SQLite |
| Named workers | None | Profiles |
| Human-in-loop | None | Kanban comments |
| Resumability | None | Kanban block/unblock |

**Hermes advantage:** Kanban for long-running multi-agent workflows.

**Claude Code advantage:** Tighter IDE integration; simpler subagent model.

---

## Skills Comparison

| Aspect | Claude Code | Hermes |
|--------|-------------|--------|
| Skills | Cursor rules/skills | agentskills.io standard |
| Count | User-defined | 88 bundled + 80 optional |
| Loading | Full injection | Progressive disclosure |
| Self-improvement | Manual | Curator auto-maintenance |
| Slash commands | Limited | Every skill → /command |

**Hermes advantage:** Self-improving skill ecosystem; progressive disclosure.

---

## MCP Comparison

| Aspect | Claude Code | Hermes |
|--------|-------------|--------|
| Role | Consumer | Consumer + optional server |
| OAuth | Supported | Full OAuth 2.1 + PKCE |
| Config | MCP settings | mcp_servers in config.yaml |
| Tool filtering | Per-server | Per-tool granularity |

Comparable maturity; Hermes has more config surface.

---

## Runtime Comparison

| Aspect | Claude Code | Hermes |
|--------|-------------|--------|
| Sandbox | Container-based | 7 backends (local→serverless) |
| Providers | Anthropic only | 10+ providers |
| API modes | Messages API | 3 modes (chat/codex/anthropic) |
| Gateway | None | 20+ messaging platforms |
| Cron | None | Built-in scheduler |

**Hermes advantage:** Multi-platform gateway; provider flexibility; cron.

**Claude Code advantage:** Anthropic-optimized; fleet-scale validation.

---

## Patterns Hermes Adds

1. **Frozen memory snapshot** — prompt cache optimization
2. **Progressive skill disclosure** — 3-level loading
3. **Kanban vs delegate matrix** — two multi-agent primitives
4. **Curator pattern** — self-improving skills
5. **Profile isolation** — digital twin instances
6. **One-external-provider rule** — prevent schema bloat
7. **Agent context tagging** — primary/subagent/cron/flush

---

## Patterns Claude Code Adds (not in Hermes)

1. **Prompt cache as constraint** — cache latches
2. **Withholding errors** — error recovery ladder
3. **Bubble permissions** — granular approval
4. **Circuit breakers** — fleet-scale protection
5. **Feature flags** — internal vs npm builds

---

## Integration Recommendation

Extract from Hermes into Agent-OS:
- Memory char limits + frozen snapshot
- Kanban vs delegate decision matrix
- Progressive skill disclosure
- Curator lifecycle pattern

Extract from Claude Code (already in Agent-OS):
- Query loop patterns
- Error recovery ladder
- Prompt cache constraints
