# Glossary — Extraction Plan

Terminology to extract from `Books/claude/` → `agent-os/11_glossary/`.

Glossary entries are **short pointers** to canonical concept notes — not duplicate definitions.

## Extracted Terms ✅

| Term | Canonical note | Source |
|------|----------------|--------|
| agent | [00_foundations/what-is-an-agent](../../00_foundations/what-is-an-agent.md) | ch01 |
| harness | [00_foundations/harness](../../00_foundations/harness.md) | ch01 |
| mcp | [05_mcp/mcp-protocol](../../05_mcp/mcp-protocol.md) | ch15 |
| query-loop | [01_agent-runtime/query-loop](../../01_agent-runtime/query-loop.md) | ch05 |

## Planned Terms ⬜

Grouped by source chapter. Target file: `11_glossary/<term>.md`.

### ch01 — Architecture

| Term | Canonical target (concept) |
|------|---------------------------|
| query-loop | query-loop (exists) |
| tool-system | tool-runtime |
| tasks | task-state-machine |
| hooks | hooks-lifecycle |
| permission-mode | permission-modes |
| terminal-state | terminal-states |
| bubble-mode | permission-modes |

### ch02 — Bootstrap

| Term | Canonical target |
|------|------------------|
| trust-boundary | trust-boundary (⬜ concept) |
| fast-path | bootstrap-pipeline |
| preaction-hook | bootstrap-pipeline |

### ch03 — State

| Term | Canonical target |
|------|------------------|
| bootstrap-state | stateful-systems |
| app-state | two-tier-state |
| sticky-latch | sticky-latch-pattern |
| on-change-side-effect | two-tier-state |

### ch04 — API

| Term | Canonical target |
|------|------------------|
| dynamic-boundary | prompt-cache-as-constraint |
| prompt-cache | prompt-cache-as-constraint |
| beta-header | sticky-latch-pattern |
| idle-watchdog | api-layer |

### ch05 — Agent loop

| Term | Canonical target |
|------|------------------|
| auto-compact | context-compression |
| reactive-compact | context-compression |
| stop-hook | stop-hooks |
| withholding | withholding-errors |
| query-source | query-loop |

### ch06 — Tools

| Term | Canonical target |
|------|------------------|
| build-tool | fail-closed-defaults |
| tool-use-context | tool-runtime |
| pre-tool-use | harness-mechanisms |
| post-tool-use | harness-mechanisms |
| defer-loading | tool-runtime |
| result-budgeting | tool-runtime |

### ch07 — Concurrency

| Term | Canonical target |
|------|------------------|
| partition-tool-calls | concurrency |
| streaming-tool-executor | streaming-tool-executor |
| context-modifier | concurrency |

### ch08–10 — Multi-agent

| Term | Canonical target |
|------|------------------|
| agent-tool | subagents |
| run-agent | subagents |
| subagent-type | role-systems |
| task-status | task-state-machine |
| send-message | sendmessage-protocol (⬜) |
| coordinator-mode | coordination |
| in-process-teammate | swarms |

### ch09 — Fork

| Term | Canonical target |
|------|------------------|
| fork-agent | fork-agents (⬜) |
| use-exact-tools | byte-identical-prefix (⬜ pattern) |
| fork-boilerplate | fork-agents (⬜) |
| rendered-system-prompt | prompt-cache-sharing (⬜) |

### ch11 — Memory

| Term | Canonical target |
|------|------------------|
| memory-md | long-term-memory |
| claude-md | long-term-memory |
| memory-taxonomy | memory-taxonomy |
| relevance-selector | memory-recall |
| consolidate-lock | memory-compaction |

### ch12 — Extensibility

| Term | Canonical target |
|------|------------------|
| skill | skills-system (⬜) |
| skill-frontmatter | skills-system (⬜) |
| hooks-snapshot | hooks-snapshot-security (⬜) |

### ch13–14 — UI

| Term | Canonical target |
|------|------------------|
| ink-dom | terminal-renderer (⬜) |
| double-buffer | terminal-renderer (⬜) |
| parsed-key | input-system (⬜) |
| chord | keybinding-system (⬜) |
| kitty-keyboard-protocol | input-system (⬜) |

### ch15 — MCP

| Term | Canonical target |
|------|------------------|
| mcp-transport | mcp-transports |
| streamable-http | mcp-transports |
| in-process-transport | runtime-bridges |
| mcp-server-signature | mcp-orchestration |

### ch16 — Remote

| Term | Canonical target |
|------|------------------|
| repl-bridge-transport | remote-execution (⬜) |
| flush-gate | remote-execution (⬜) |
| worker-epoch | remote-execution (⬜) |
| ccr-client | remote-execution (⬜) |

### ch17 — Performance

| Term | Canonical target |
|------|------------------|
| effective-context-window | context-compression |
| profile-checkpoint | performance-engineering (⬜) |
| lazy-schema | performance-engineering (⬜) |

## Glossary Entry Template

```markdown
# Term Name

## Definition
One sentence + link to canonical concept note.

## Related Concepts
- [[canonical-concept]]

## Sources
- Books/claude/chXX-*.md

## My Notes
```

## Up

- [Glossary index](index.md)
- [Master extraction plan](../extraction-plan.md)
