# Memory System Overview

**Sources:** `website/docs/user-guide/features/memory.md`, `memory-providers.md`  
**Code:** `tools/memory_tool.py`, `agent/memory_manager.py`, `agent/memory_provider.py`

---

## Architecture

```
┌─────────────────────────────────────────────────────────┐
│                    MemoryManager                         │
│              (agent/memory_manager.py)                   │
│                                                          │
│  ┌─────────────────┐    ┌─────────────────────────┐   │
│  │ Built-in        │    │ External Provider (ONE)  │   │
│  │ MEMORY.md       │    │ Honcho | Mem0 | Hindsight│   │
│  │ USER.md         │    │ OpenViking | Supermemory  │   │
│  │ (always active) │    │ RetainDB | Holographic    │   │
│  └────────┬────────┘    │ ByteRover                 │   │
│           │             └────────────┬──────────────┘   │
│           └──────────┬───────────────┘                  │
│                      ▼                                   │
│           build_system_prompt()                          │
│           prefetch_all() → background recall             │
│           sync_all() → post-turn write                   │
│           on_pre_compress() → extract before compression │
│           on_delegation() → observe subagent results     │
└─────────────────────────────────────────────────────────┘
```

---

## Built-in Memory: MEMORY.md + USER.md

| Store | Path | Limit | Purpose |
|-------|------|-------|---------|
| MEMORY.md | `~/.hermes/memories/MEMORY.md` | 2,200 chars (~800 tokens) | Agent's personal notes |
| USER.md | `~/.hermes/memories/USER.md` | 1,375 chars (~500 tokens) | User profile |

### Format

Entries separated by `§` (section sign) delimiter:

```
User's project is a Rust web service at ~/code/myapi using Axum + SQLx
§
This machine runs Ubuntu 22.04, has Docker and Podman installed
§
User prefers concise responses, dislikes verbose explanations
```

### Frozen Snapshot Pattern

**Critical design decision:** Memory is injected into system prompt **once at session start** and never changes mid-session.

- Changes via `memory` tool → persisted to disk immediately
- NOT reflected in system prompt until next session
- Preserves LLM prefix cache for performance
- Tool responses show live state

### Memory Tool Actions

| Action | Target | Description |
|--------|--------|-------------|
| `add` | memory / user | Add new entry |
| `replace` | memory / user | Replace via `old_text` substring match |
| `remove` | memory / user | Remove via `old_text` substring match |

No `read` action — content auto-injected at session start.

---

## External Memory Providers

Only **one** external provider active at a time. Built-in always runs alongside.

| Provider | Best For | Tools |
|----------|----------|-------|
| **Honcho** | Dialectic user modeling, multi-agent | 5 tools (profile, search, context, reasoning, conclude) |
| **Hindsight** | Long-term recall | Provider-specific |
| **Mem0** | Semantic memory | Provider-specific |
| **OpenViking** | Vector memory | Provider-specific |
| **Supermemory** | Cloud memory | Provider-specific |
| **RetainDB** | Structured retention | Provider-specific |
| **Holographic** | Holographic encoding | Provider-specific |
| **ByteRover** | Byte-level memory | Provider-specific |

### MemoryProvider Lifecycle

```python
initialize(session_id)           # Connect, warm up
system_prompt_block()            # Static text for prompt
prefetch(query)                  # Background recall before turn
sync_turn(user, assistant)       # Async write after turn
get_tool_schemas()               # Tools to expose
handle_tool_call()               # Dispatch tool calls
shutdown()                       # Clean exit

# Optional hooks:
on_turn_start(turn, message)
on_session_end(messages)
on_session_switch(new_session_id)
on_pre_compress(messages) -> str
on_memory_write(action, target, content)
on_delegation(task, result)
```

### Agent Context Tagging

Providers receive `agent_context`:
- `primary` — normal agent session
- `subagent` — delegated child
- `cron` — scheduled job (skip writes to prevent corruption)
- `flush` — session end extraction

Non-primary contexts should skip writes to prevent user representation corruption.

---

## Session Recall (FTS5)

Cross-session search via SQLite FTS5 full-text search.

**Code:** `tools/session_search_tool.py`, `hermes_state.py`

**Storage:** `~/.hermes/state.db`
- Session metadata (id, platform, user, title, model)
- Full message history (role, content, tool calls)
- Token counts, timestamps
- Parent session ID (compression lineage)

**Search flow:**
1. Agent calls session search tool with query
2. FTS5 matches against message content
3. LLM summarization of relevant sessions
4. Results injected as recalled context (fenced with `<memory-context>` tags)

---

## Context Fencing

Provider output is fenced to prevent UI leakage:

```python
# MemoryManager sanitizes:
# - <memory-context>...</memory-context> blocks
# - [System note: The following is recalled memory context...]
# - StreamingContextScrubber for chunk boundaries
```

---

## Honcho Deep Dive (Primary External Provider)

Two-layer context injection:
1. **Base layer:** session summary + user representation + peer card
2. **Dialectic supplement:** LLM-synthesized reasoning

Config knobs (orthogonal):
- `contextCadence` — base layer refresh frequency
- `dialecticCadence` — dialectic LLM call frequency
- `dialecticDepth` — reasoning passes (1-3)

Session strategies: `per-directory`, `per-repo`, `per-session`, `global`

---

## Comparison with Agent-OS Memory Taxonomy

| Agent-OS Concept | Hermes Implementation |
|------------------|----------------------|
| Episodic memory | Session DB + FTS5 search |
| Semantic memory | External providers (Honcho, Mem0) |
| Working memory | Current conversation window |
| Procedural memory | Skills (SKILL.md) |
| User model | USER.md + Honcho peer card |
| Memory compaction | `on_pre_compress` hook + `/compress` |
| Memory limits | Hard char limits (2200/1375) |

See also: `memory/MEMORY.md`, `memory/USER.md`, `memory/MEMORY_PROVIDERS.md`
