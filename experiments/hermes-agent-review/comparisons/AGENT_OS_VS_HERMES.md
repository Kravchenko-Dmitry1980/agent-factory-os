# Agent-OS vs Hermes Agent

**Agent-OS path:** `agent-os/`  
**Hermes path:** `experiments/hermes-agent-review/source/hermes-agent/`  
**Comparison date:** 2026-05-25

---

## Nature Difference

| | Agent-OS | Hermes |
|---|----------|--------|
| **Type** | Knowledge operating system (docs) | Runnable agent product |
| **Content** | 153 markdown files | 4000+ files (code + docs) |
| **Purpose** | Extract patterns from sources | Self-improving agent runtime |
| **Execution** | None (knowledge only) | Full runtime stack |

Agent-OS **documents** agent architecture; Hermes **implements** it.

---

## Section Mapping

| Agent-OS Section | Hermes Equivalent | Coverage |
|------------------|-------------------|----------|
| `00_foundations/` | README, architecture.md | Partial |
| `01_agent-runtime/` | run_agent.py, conversation_loop.py | Strong |
| `02_memory/` | memory_tool.py, memory_manager.py | Strong |
| `03_harness-engineering/` | callbacks.py, approval.py | Partial |
| `04_multi-agent/` | delegate_tool.py, kanban*.py | Strong |
| `05_mcp/` | mcp_tool.py | Strong |
| `06_digital-twins/` | profiles, Honcho, Kanban workers | Strong |
| `07_projects/` | User stories, examples | Weak |
| `08_patterns/` | Various implementations | Partial |
| `09_antipatterns/` | Implicit in design decisions | Weak |
| `10_research/` | Claude Code corpus | N/A (different source) |
| `11_glossary/` | website/docs/reference/ | Partial |
| `12_diagrams/` | architecture.md diagrams | Partial |

---

## What Agent-OS Has That Hermes Lacks (Documented)

| Agent-OS Pattern | Hermes Status |
|------------------|---------------|
| Prompt cache as constraint | Has caching, different approach |
| Error recovery ladder | Basic retries, no ladder |
| Withholding errors | Not documented |
| Circuit breakers | Not implemented |
| Bubble permissions | approval.py (simpler) |
| Two-tier state | SQLite (different model) |
| Sticky latch pattern | Not identified |

---

## What Hermes Has That Agent-OS Lacks

| Hermes Feature | Agent-OS Gap |
|----------------|--------------|
| Frozen memory snapshot | Not documented |
| Progressive skill disclosure | Not documented |
| Curator self-improving skills | Not documented |
| Kanban vs delegate matrix | Partial (subagents only) |
| One-external-provider rule | Not documented |
| 8 memory providers | Not documented |
| 20+ gateway platforms | Not documented |
| 7 sandbox backends | Not documented |
| Profile isolation model | Partial (digital twins) |
| Honcho dialectic modeling | Not documented |
| execute_code RPC | Not documented |
| Agent context tagging | Not documented |

---

## Integration Strategy

### Phase 1: Knowledge Extraction (Current)

Extract Hermes patterns into `hermes-agent-review/` without modifying Agent-OS.

### Phase 2: Atomic Notes (Future)

Create Agent-OS atomic notes from extracted patterns:

| New Note | Source |
|----------|--------|
| `02_memory/frozen-memory-snapshot.md` | Hermes MEMORY.md pattern |
| `02_memory/memory-char-limits.md` | Hermes bounded memory |
| `04_multi-agent/kanban-vs-delegate.md` | Hermes decision matrix |
| `04_multi-agent/kanban-orchestration.md` | Hermes Kanban spec |
| `06_digital-twins/profile-isolation.md` | Hermes profiles |
| `06_digital-twins/curator-pattern.md` | Hermes curator |
| `08_patterns/progressive-skill-disclosure.md` | Hermes skills |
| `08_patterns/one-provider-rule.md` | Hermes memory manager |
| `08_patterns/agent-context-tagging.md` | Hermes provider hooks |

### Phase 3: Research Corpus (Future)

Add Hermes as third research corpus alongside Claude Code and Code-as-Agent-Harness:

```
Books/
├── claude/          # Claude Code architecture
├── agents/          # Code as Agent Harness survey
└── hermes/          # Hermes Agent (extracted, not full repo)
```

---

## What NOT to Integrate

| Hermes Component | Reason |
|------------------|--------|
| Full codebase | Too large, product-specific |
| Gateway platforms | Not knowledge, implementation |
| Bundled skills | Product-specific, not patterns |
| Nous Portal coupling | Vendor-specific |
| Install scripts | Deployment, not architecture |

---

## Digital Twin Implications

Agent-OS `06_digital-twins/` can be enriched with Hermes patterns:

| Digital Twin Concept | Hermes Implementation |
|---------------------|----------------------|
| Persistent identity | Profiles |
| Evolving memory | Curator + Honcho |
| Skill graphs | Skills + progressive disclosure |
| Multi-agent coordination | Kanban + profiles |

Hermes is closer to **production digital twin** than Agent-OS currently documents.

---

## Recommended Agent-OS Updates (Knowledge Only)

1. Add Hermes to `10_research/sources.md`
2. Create `10_research/hermes-agent-architecture.md` summary
3. Enrich `02_memory/` with bounded memory patterns
4. Enrich `04_multi-agent/` with Kanban primitive
5. Enrich `06_digital-twins/` with profile + curator patterns
6. Add comparison matrix to `12_diagrams/`

**No runtime integration.** Agent-OS remains knowledge layer.
