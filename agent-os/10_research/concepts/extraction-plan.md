# Concepts — Extraction Plan

Atomic concepts to extract from `Books/claude/` into `agent-os/00–06/`.

**Do not rewrite source chapters.** Extract into new files using [concept-note-template](../../templates/concept-note-template.md).

## Index of Planned Concepts

Legend: ✅ extracted · ⬜ planned · 🟡 partial

### 00_foundations

| Concept file | Source | Status |
|--------------|--------|--------|
| what-is-an-agent | ch01 | ✅ |
| agent-vs-cli | ch01 | ✅ |
| stateful-systems | ch03 | ✅ |
| harness | ch01, ch06, ch12 | 🟡 (extend with ch12 skills/hooks) |
| execution-loops | ch05 | ✅ |
| verification | ch05, ch08 | ✅ |
| planning | ch01, ch06 | ✅ |
| orchestration | ch10 | ✅ |
| six-abstractions | ch01 | ✅ |
| golden-path | ch01 | ✅ |
| architectural-bets | ch18 | ⬜ |
| what-transfers | ch18 | ⬜ |

### 01_agent-runtime

| Concept file | Source | Status |
|--------------|--------|--------|
| query-loop / agent-loop | ch05 | ✅ |
| tool-runtime | ch06 | ✅ |
| concurrency | ch07 | ✅ |
| streaming-tool-executor | ch07 | ✅ |
| bootstrap-pipeline | ch02 | ✅ |
| context-compression | ch05 | ✅ |
| error-recovery-ladder | ch05 | ✅ |
| terminal-states | ch05 | ✅ |
| api-layer | ch04 | ✅ |
| multi-provider-client | ch01, ch04 | ⬜ |
| terminal-renderer | ch13 | ⬜ |
| input-system | ch14 | ⬜ |
| remote-execution | ch16 | ⬜ |
| performance-engineering | ch17 | ⬜ |
| build-system-feature-flags | ch01 | ⬜ |

### 02_memory

| Concept file | Source | Status |
|--------------|--------|--------|
| long-term-memory | ch11 | ✅ |
| semantic-memory | ch11 | ✅ |
| episodic-memory | ch11 | ✅ |
| shared-memory / shared-state | ch11, ch03 | ✅ |
| memory-compaction | ch05, ch11 | ✅ |
| memory-taxonomy | ch11 | ✅ |
| memory-recall | ch11 | ✅ |
| team-memory | ch11 | ⬜ |
| kairos-daily-logs | ch11 | ⬜ |
| memory-staleness | ch11 | ⬜ |
| background-memory-extraction | ch11, ch09 | ⬜ |

### 03_harness-engineering

| Concept file | Source | Status |
|--------------|--------|--------|
| harness-interface | ch06, ch12 | 🟡 |
| harness-mechanisms | ch06 | ✅ |
| execution-verification | ch05 | ✅ |
| execution-feedback | ch05, ch06 | ✅ |
| feedback-loops | ch03, ch05 | ✅ |
| adaptive-harness | ch01, ch06 | ✅ |
| permission-modes | ch01, ch06 | ✅ |
| hooks-lifecycle | ch01, ch12 | 🟡 |
| stop-hooks | ch05 | ✅ |
| skills-system | ch12 | ⬜ |
| hooks-snapshot-security | ch12 | ⬜ |
| keybinding-system | ch14 | ⬜ |
| trust-boundary | ch02 | ⬜ |

### 04_multi-agent

| Concept file | Source | Status |
|--------------|--------|--------|
| subagents | ch08 | ✅ |
| task-state-machine | ch10 | ✅ |
| coordination | ch10 | ✅ |
| swarms | ch10 | ✅ |
| synchronization | ch07, ch10 | ✅ |
| role-systems | ch08 | ✅ |
| fork-agents | ch09 | ⬜ |
| prompt-cache-sharing | ch09 | ⬜ |
| coordinator-mode | ch10 | ⬜ (partial in coordination) |
| sendmessage-protocol | ch10 | ⬜ |
| dream-tasks | ch10 | ⬜ |

### 05_mcp

| Concept file | Source | Status |
|--------------|--------|--------|
| mcp-protocol | ch15 | ✅ |
| tool-servers | ch15 | ✅ |
| mcp-transports | ch15 | ✅ |
| mcp-orchestration | ch15, ch02 | ✅ |
| mcp-integrations | ch15 | ✅ |
| runtime-bridges | ch15, ch16 | 🟡 |
| oauth-mcp-discovery | ch15 | ⬜ |
| claudeai-proxy-transport | ch15 | ⬜ |

### 06_digital-twins

| Concept file | Source | Status |
|--------------|--------|--------|
| persistent-identity | ch03, ch10, ch11 | ✅ |
| evolving-memory | ch11 | ✅ |
| skill-graphs | ch12, ch08 | 🟡 |
| self-revision | ch11 | ✅ |
| agent-personas | ch08 | ✅ |

---

## Extraction Procedure (per concept)

1. Read source chapter section in `Books/claude/`
2. Create `agent-os/<dir>/<kebab-name>.md` from template
3. Fill Definition + Key Ideas from source (paraphrase, don't paste wholesale yet if avoiding rewrite phase)
4. Add Architecture / Production implications
5. Link Related Concepts (bidirectional)
6. Set `## Sources` to chapter + section
7. Update this table status → ✅
8. Add link in section `index.md`

## Up

- [Concepts index](index.md)
- [Master extraction plan](../extraction-plan.md)
