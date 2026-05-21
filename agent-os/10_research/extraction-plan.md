# Master Extraction Plan

Knowledge decomposition roadmap: **Books/claude/** → **agent-os/** atomic notes.

**Phase:** planning only — no semantic rewrites of source chapters.

## Target Taxonomy

| Extract type | Agent-OS destination | Contract |
|--------------|---------------------|----------|
| Atomic concept | `00–06/` numbered dirs | [concept-note-template](../../templates/concept-note-template.md) |
| Architecture pattern | `08_patterns/` | Same contract |
| Anti-pattern | `09_antipatterns/` | Same contract |
| Glossary term | `11_glossary/` | Short entry → link to canonical concept |
| Diagram | `12_diagrams/` | Mermaid + Related Concepts |

## Status Legend

| Symbol | Meaning |
|--------|---------|
| ✅ | Extracted (note exists in agent-os) |
| 🟡 | Partially extracted |
| ⬜ | Planned, not extracted |
| 🔗 | Covered by existing note (verify depth) |

---

## Chapter → Extraction Matrix

| Ch | Concepts | Patterns | Anti-patterns | Glossary | Status |
|----|----------|----------|---------------|----------|--------|
| 1 | six-abstractions, golden-path, agent-vs-cli | generator-loop, self-describing-tools, two-tier-state (refs) | — | agent, query-loop, harness | 🟡 |
| 2 | bootstrap-pipeline | fast-path-dispatch, module-level-io-parallelism | lazy-init-bootstrap | — | 🟡 |
| 3 | stateful-systems, shared-state | two-tier-state, sticky-latch, centralized-onchange | ungoverned-global-state | AppState, bootstrap-state | 🟡 |
| 4 | api-layer | prompt-cache-as-constraint, DANGEROUS-sections, streaming-watchdog | cache-busting-sections | prompt-cache, dynamic-boundary | 🟡 |
| 5 | query-loop, execution-loops | generator-loop, withholding-errors, immutable-transitions | infinite-retry-loops | terminal-states, continue-states | 🟡 |
| 6 | tool-runtime, harness (refs) | self-describing-tools, fail-closed-defaults | central-orchestrator-god-object | ToolUseContext, buildTool | 🟡 |
| 7 | concurrency, streaming-tool-executor | input-dependent-concurrency, speculative-execution | — | partition-algorithm | 🟡 |
| 8 | subagents, role-systems | dynamic-tool-schema, attachment-not-description | — | AgentTool, runAgent | 🟡 |
| 9 | fork-agents, prompt-cache-sharing | byte-identical-prefix, rendered-system-prompt-threading | cache-divergence-recompute | fork-agent, useExactTools | ⬜ |
| 10 | coordination, task-state-machine, swarms | task-output-file-ipc, sendmessage-queue | flat-task-no-tree | Task, SendMessage | 🟡 |
| 11 | long-term-memory, memory-taxonomy, memory-recall | file-memory-llm-recall, two-step-write | memory-as-crutch | MEMORY.md, frontmatter | 🟡 |
| 12 | skills-system, hooks-extensibility | two-phase-skill-loading, hooks-snapshot-freeze | post-start-hook-tampering | skill, PreToolUse | ⬜ |
| 13 | terminal-renderer | double-buffer-rendering, pool-interning, cell-diff | object-per-cell-gc | ink-dom, ConcurrentRoot | ⬜ |
| 14 | input-system, keybinding-system | progressive-enhancement-input, discreteUpdates-batch | raw-mode-refcount-leak | ParsedKey, chord | ⬜ |
| 15 | mcp-protocol, tool-servers | mcp-tool-wrapping, transport-stack | malicious-readonly-hint | MCP, stdio | 🟡 |
| 16 | remote-execution | asymmetric-read-write, FlushGate, bridge-v2-sse | jwt-session-leak | CCR, ReplBridgeTransport | ⬜ |
| 17 | performance-engineering | slot-reservation-8k, api-preconnect, bitmap-search-prefilter | over-reserved-output-tokens | effectiveContextWindow | ⬜ |
| 18 | architectural-bets (meta) | — (synthesizes prior patterns) | — | — | ⬜ |

---

## Priority Queue (Recommended Order)

### Wave 1 — Close gaps in core runtime (already partial)
1. ch09 → fork / cache exploitation concepts
2. ch12 → skills + hooks extensibility
3. ch17 → performance cross-cutting (validates ch02, ch04, ch09)

### Wave 2 — UI + remote (new domains)
4. ch13 → terminal renderer
5. ch14 → input / keybindings
6. ch16 → remote execution bridges

### Wave 3 — Synthesis
7. ch18 → meta note linking five bets to existing patterns
8. Reconcile duplicates between early agent-os extractions and research plan

---

## Decomposition Rules

1. **One concept per file** — split ch05 into query-loop, context-compression, error-recovery-ladder (✅ done)
2. **Patterns ≠ concepts** — "async generator" is pattern; "query loop" is concept
3. **Anti-patterns from failure modes** — name the failure, link to fix pattern
4. **No duplication** — glossary links to canonical concept; no second definition
5. **Sources preserved** — every extraction cites `Books/claude/chXX-*.md` section
6. **Chapter untouched** — edit only `agent-os/` targets

---

## Cross-Reference: Existing Agent-OS Notes

Early extractions (verify against source before expanding):

| Note | Source chapters |
|------|-----------------|
| [00_foundations/*](../../00_foundations/index.md) | ch01, ch18 |
| [01_agent-runtime/*](../../01_agent-runtime/index.md) | ch02, ch04, ch05, ch07 |
| [02_memory/*](../../02_memory/index.md) | ch11 |
| [03_harness-engineering/*](../../03_harness-engineering/index.md) | ch01, ch05, ch06, ch12 (pending) |
| [04_multi-agent/*](../../04_multi-agent/index.md) | ch08, ch10, ch09 (pending) |
| [05_mcp/*](../../05_mcp/index.md) | ch15, ch16 (partial) |
| [08_patterns/*](../../08_patterns/index.md) | ch01–07, ch04 |
| [09_antipatterns/*](../../09_antipatterns/index.md) | ch03, ch04, ch05, ch11 |

---

## Domain Plans

- [Concepts extraction plan](concepts/extraction-plan.md)
- [Patterns extraction plan](patterns/extraction-plan.md)
- [Glossary extraction plan](glossary/extraction-plan.md)

---

## Anti-Patterns Extraction Plan

Target: `agent-os/09_antipatterns/` · Pair each with fix pattern in `08_patterns/`

| Anti-pattern file | Source | Fix pattern | Status |
|-------------------|--------|-------------|--------|
| infinite-retry-loops | ch05 | circuit-breaker-retries | ✅ |
| central-orchestrator-god-object | ch06 | self-describing-tools | ✅ |
| cache-busting-sections | ch04 | prompt-cache-as-constraint | ✅ |
| scattered-permission-sync | ch03 | centralized-onchange-side-effects | ✅ |
| memory-as-crutch | ch11 | file-memory-llm-recall | ✅ |
| cache-divergence-recompute | ch09 | byte-identical-prefix | ⬜ |
| ungoverned-global-state | ch03 | two-tier-state | ⬜ |
| lazy-init-bootstrap | ch02 | fast-path-dispatch | ⬜ |
| post-start-hook-tampering | ch12 | hooks-snapshot-freeze | ⬜ |
| object-per-cell-gc | ch13 | pool-based-string-interning | ⬜ |
| raw-mode-refcount-leak | ch14 | raw-mode-reference-counting | ⬜ |
| jwt-session-leak | ch16 | bridge-v2-epoch-registration | ⬜ |
| over-reserved-output-tokens | ch17 | slot-reservation-8k-64k | ⬜ |
| malicious-readonly-hint | ch15 | (document trust boundary) | ⬜ |

## Up

- [Research README](README.md)
- [Chapters index](chapters/index.md)
