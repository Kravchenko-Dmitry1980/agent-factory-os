# Research Status — Hermes Agent

**Дата:** 2026-05-25  
**Фаза:** Architecture audit (read-only)  
**Clone:** `source/hermes-agent/` (shallow, v0.14.0)  
**Hermes запущен:** нет  
**Интеграция в Agent-OS:** нет

---

## Current Understanding

Hermes Agent — self-improving AI agent от Nous Research. Это **runnable product**, не knowledge corpus. ~400 Python modules, 3000+ tests, Docusaurus docs site.

**Центральная идея:** closed learning loop — агент сам создаёт skills, улучшает их, сохраняет память, ищет прошлые сессии, моделирует пользователя между сессиями.

**Entry points:**
- CLI/TUI (`cli.py`, `hermes_cli/main.py`)
- Gateway (`gateway/run.py`) — 20+ messaging platforms
- ACP adapter — IDE integration (VS Code, Zed, JetBrains)
- Cron scheduler — unattended automations
- Python library (`from run_agent import AIAgent`)

**Core loop:** `AIAgent.run_conversation()` → prompt_builder → provider resolution → API call → tool dispatch → persist to SQLite+FTTS5.

---

## Key Architectural Insights

### 1. Frozen Memory Snapshot Pattern
MEMORY.md и USER.md инжектируются в system prompt **один раз** при старте сессии. Изменения через `memory` tool пишутся на диск сразу, но не попадают в prompt до следующей сессии. Это сохраняет prefix cache LLM.

### 2. Progressive Skill Disclosure
Skills загружаются трёхуровнево: list (~3k tokens) → full content → reference file. Минимизирует token overhead при 88+ bundled skills.

### 3. Dual Multi-Agent Model
- **`delegate_task`** — RPC fork-join, anonymous subagents, parent blocks
- **Kanban** — durable SQLite queue, named profiles, fire-and-forget, human-in-loop

Это принципиально разные примитивы, не взаимозаменяемые.

### 4. One External Memory Provider Rule
`MemoryManager` разрешает только один external provider (Honcho, Mem0, etc.) одновременно. Built-in MEMORY/USER всегда активны. Предотвращает tool schema bloat.

### 5. Profile = Isolated HERMES_HOME
Каждый profile — отдельный agent instance: config, memory, sessions, skills, gateway state. Kanban workers — это profiles, не subagents.

### 6. Curator = Self-Improving Skills
Inactivity-triggered auxiliary agent review agent-created skills: pin, archive, consolidate, patch. Never auto-deletes. Uses auxiliary model, not main session cache.

### 7. Three API Modes
`chat_completions`, `codex_responses`, `anthropic_messages` — unified через `runtime_provider.py`.

---

## Valuable Patterns

| Pattern | Hermes Implementation | Agent-OS Relevance |
|---------|----------------------|-------------------|
| Bounded curated memory | MEMORY.md (2200 chars) + USER.md (1375 chars) | `02_memory/` — explicit limits vs unbounded |
| Frozen prompt injection | Session-start snapshot | `08_patterns/prompt-cache-as-constraint` |
| Progressive disclosure | skills_list → skill_view → skill_view(path) | Skill loading strategy |
| Context fencing | `<memory-context>` tags + scrubber | Prevent memory leak to UI |
| Subagent isolation | Fresh context, restricted toolsets, summary-only return | `04_multi-agent/subagents` |
| Durable work queue | Kanban SQLite + comment protocol | Digital twin persistence |
| Prefetch-before-turn | MemoryProvider.prefetch() background | Proactive recall |
| on_pre_compress hook | Extract memories before compression | Memory preservation |
| Agent context tagging | primary/subagent/cron/flush | Prevent cron corruption |
| Toolset restriction | Subagents can't delegate, write memory, clarify | Safety boundaries |

---

## Dangerous Complexity

| Area | Risk | Why |
|------|------|-----|
| `hermes_cli/main.py` | ~14k lines | God entry point |
| `gateway/run.py` | ~18.5k lines | Platform matrix explosion |
| `tools/mcp_tool.py` | ~3600 lines | OAuth, reconnect, sampling |
| `tools/delegate_tool.py` | ~2800 lines | Subagent lifecycle |
| 20+ gateway platforms | Maintenance burden | Each adapter = edge cases |
| 8 memory providers | Plugin matrix | One-at-a-time rule helps, but config complexity |
| 88 bundled + 80 optional skills | Discovery noise | Progressive disclosure mitigates |
| Kanban + delegate coexistence | Conceptual overlap | Easy to misuse wrong primitive |
| Honcho dialectic config | 15+ knobs | contextCadence, dialecticDepth, etc. |
| Profile × Gateway × Kanban | State explosion | Multi-dimensional isolation |

---

## Reusable Components

**High confidence (concept extraction):**
- Memory char limits + § delimiter format
- Frozen snapshot injection pattern
- MemoryProvider ABC lifecycle hooks
- Progressive skill disclosure levels
- Subagent toolset restrictions list
- Kanban vs delegate decision matrix
- Profile isolation model
- Session FTS5 search architecture
- Curator inactivity-trigger pattern
- Context fencing for provider output

**Medium confidence (needs deeper read):**
- `execute_code` RPC tool collapsing
- Trajectory compression for training
- Mixture of Agents parallel aggregation
- Gateway session mirroring
- Skin engine / personality system

**Low confidence (defer):**
- Full gateway platform adapter patterns
- Individual memory provider implementations
- Browser backend matrix (5 backends)
- Voice mode pipeline

---

## Integration Candidates

**For Agent-OS knowledge layer (not runtime):**

1. **MEMORY.md / USER.md taxonomy** → enrich `02_memory/memory-taxonomy.md`
2. **Kanban vs delegate matrix** → new note in `04_multi-agent/`
3. **Progressive skill disclosure** → `08_patterns/` candidate
4. **Frozen memory snapshot** → link to existing `prompt-cache-as-constraint`
5. **MemoryProvider hook lifecycle** → `02_memory/` provider abstraction doc
6. **Profile = digital twin instance** → `06_digital-twins/persistent-identity.md`
7. **Curator pattern** → `06_digital-twins/evolving-memory.md`
8. **One-external-provider rule** → anti-pattern prevention doc

**NOT recommended for integration:**
- Full gateway codebase
- Hermes CLI monolith structure
- Bundled skills catalog (too product-specific)
- Nous Portal / Tool Gateway coupling

---

## Open Questions

1. Как Hermes решает conflict между curator и user-edited skills?
2. Какова точная схема SQLite session DB (parent_session_id lineage)?
3. Как `execute_code` RPC сравнивается с Claude Code's code execution?
4. Какие gateway platforms production-ready vs experimental?
5. Как Honcho sessionStrategy `per-directory` vs `per-repo` влияет на digital twin?
6. Есть ли formal spec для Kanban comment protocol?
7. Как trajectory compression используется для model training?
8. Как profiles interact с gateway DM pairing authorization?
9. Какой overhead progressive disclosure при 160+ skills?
10. Совместимость agentskills.io spec — полная или partial?

---

## Recommended Next Steps

### Phase 2 — Deep Dives (read-only)
- [ ] `agent/conversation_loop.py` — full loop state machine
- [ ] `hermes_state.py` — SQLite schema documentation
- [ ] `tools/delegate_tool.py` — subagent restrictions exhaustive list
- [ ] `website/docs/developer-guide/agent-loop.md` — canonical loop docs
- [ ] `plugins/memory/honcho/` — dialectic architecture deep dive

### Phase 3 — Comparison Enrichment
- [ ] Map Hermes concepts to each Claude Code chapter
- [ ] Cross-reference Code-as-Agent-Harness §2-§4 with Hermes primitives
- [ ] Identify Agent-OS gaps Hermes fills

### Phase 4 — Pattern Extraction
- [ ] Draft Agent-OS atomic notes from extracted patterns
- [ ] Create integration proposal (knowledge-only, no code)
- [ ] Digital twin implications document

### Phase 5 — Optional Experiments (isolated)
- [ ] MEMORY.md format prototype in `experiments/`
- [ ] Progressive disclosure mock in `experiments/`
- [ ] Kanban decision tree interactive canvas

**Не делать без явного запроса:**
- Install Hermes globally
- Connect to Cursor MCP
- Modify Agent-OS structure
- Run gateway or cron
