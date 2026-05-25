# Future Integration Candidates

Patterns ready for Agent-OS knowledge layer integration (not runtime).

---

## High Confidence — Ready for Atomic Notes

| Pattern | Target Section | Effort |
|---------|---------------|--------|
| Frozen memory snapshot | `02_memory/` | Low |
| Memory char limits | `02_memory/memory-taxonomy.md` | Low |
| Kanban vs delegate matrix | `04_multi-agent/` | Medium |
| Progressive skill disclosure | `08_patterns/` | Low |
| Profile isolation | `06_digital-twins/persistent-identity.md` | Medium |
| One-provider rule | `02_memory/` or `09_antipatterns/` | Low |
| Subagent tool restrictions | `04_multi-agent/subagents.md` | Low |
| Agent context tagging | `02_memory/` | Low |

---

## Medium Confidence — Needs Deep Dive

| Pattern | Target Section | Blocker |
|---------|---------------|---------|
| Curator lifecycle | `06_digital-twins/evolving-memory.md` | Need curator source read |
| Honcho dialectic | `06_digital-twins/` | Complex config |
| on_pre_compress hook | `02_memory/memory-compaction.md` | Hook semantics |
| execute_code RPC | `01_agent-runtime/` | RPC implementation |
| Kanban comment protocol | `04_multi-agent/coordination.md` | Full spec read |
| Context fencing | `08_patterns/` | Streaming scrubber |

---

## Low Confidence — Defer

| Pattern | Reason |
|---------|--------|
| Gateway platform adapters | Implementation, not pattern |
| Browser backend matrix | Product-specific |
| Nous Portal integration | Vendor lock-in |
| Voice mode pipeline | Feature, not architecture |
| Skin engine | UI theming, not agent pattern |
| Batch trajectory generation | Research feature |

---

## Integration Workflow

```
1. Pattern identified in hermes-agent-review/
2. Draft atomic note in agent-os/templates/
3. Cross-reference with existing notes
4. Add to section index.md
5. Update 12_diagrams/ if needed
6. Add to 10_research/sources.md
```

**No code changes to Agent-OS runtime.** Knowledge layer only.

---

## Proposed New Agent-OS Files

```
agent-os/
├── 02_memory/
│   ├── frozen-memory-snapshot.md      # NEW
│   └── memory-char-limits.md          # NEW
├── 04_multi-agent/
│   ├── kanban-vs-delegate.md          # NEW
│   └── kanban-orchestration.md        # NEW
├── 06_digital-twins/
│   ├── profile-isolation.md           # NEW
│   └── curator-pattern.md             # NEW
├── 08_patterns/
│   ├── progressive-skill-disclosure.md # NEW
│   ├── one-provider-rule.md           # NEW
│   └── agent-context-tagging.md       # NEW
└── 10_research/
    └── hermes-agent-architecture.md   # NEW (summary)
```

---

## Not Recommended for Integration

| Component | Reason |
|-----------|--------|
| Hermes codebase | Product, not knowledge |
| Bundled skills | Too specific |
| Gateway implementation | 20 platforms = maintenance |
| Install/deployment | Not architecture |
| MCP OAuth implementation | Use MCP docs instead |

---

## Digital Twin Integration Path

Most valuable for `06_digital-twins/`:

1. **Profile isolation** — twin instance model
2. **Curator pattern** — evolving procedural memory
3. **Honcho dialectic** — user modeling depth
4. **Kanban workers** — persistent task-oriented twins

These transform Agent-OS digital twin docs from concept to production patterns.
