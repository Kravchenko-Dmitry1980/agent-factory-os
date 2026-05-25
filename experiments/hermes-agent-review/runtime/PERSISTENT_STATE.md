# Persistent State & Session Recall

**Code:** `hermes_state.py`, `gateway/session.py`, `tools/session_search_tool.py`

---

## State Storage Layers

| Layer | Storage | Persistence |
|-------|---------|-------------|
| Working memory | Current conversation | Session-scoped |
| Session DB | SQLite + FTS5 | Cross-session |
| MEMORY.md / USER.md | File | Cross-session, bounded |
| External provider | Honcho/Mem0/etc. | Cross-session, unbounded |
| Skills | `~/.hermes/skills/` | Cross-session, evolving |
| Kanban | `kanban.db` | Durable, multi-agent |
| Profiles | `profiles/<name>/` | Isolated instances |

---

## SQLite Session Schema

**Path:** `~/.hermes/state.db`

### Sessions Table

| Field | Purpose |
|-------|---------|
| session_id | Unique identifier |
| source | Platform (cli, telegram, ...) |
| user_id | Platform user |
| title | Human-readable name |
| model | Model used |
| system_prompt_snapshot | Prompt at session start |
| started_at, ended_at | Timestamps |
| parent_session_id | Compression lineage |
| token_counts | Input/output tracking |

### Messages Table

| Field | Purpose |
|-------|---------|
| role | user/assistant/system/tool |
| content | Message text |
| tool_calls | JSON tool invocations |
| tool_results | JSON tool outputs |

### FTS5 Index

Full-text search across message content for cross-session recall.

---

## Session Recall Flow

```
Agent needs past context
  → session_search_tool(query)
    → FTS5 match against all sessions
    → Rank by relevance
    → LLM summarization of matches
    → Inject as <memory-context> fenced block
    → Agent uses as background (not user input)
```

---

## Session Lifecycle

```
/new → fresh session
/resume <name> → continue existing
/compress → summarize + split (parent_session_id)
/sessions → list available
hermes sessions prune → delete old ended sessions
```

---

## Cross-Platform Continuity

Gateway maintains session per:
- Platform (telegram, discord, ...)
- User ID
- Session key (conversation thread)

Same user can have separate sessions per platform or unified via config.

---

## Media Handling

Media attachments are turn-scoped:
- Images: native vision or pre-analyzed text
- Audio: transcribed to text
- Documents: extracted text or path reference
- Raw bytes NOT repeated in future prompts

**Common context growth cause:** verbose text (logs, diffs), not media files.

---

## Profile State Isolation

```
~/.hermes/                    # Default profile
~/.hermes/profiles/coder/     # Coder profile
~/.hermes/profiles/researcher/ # Researcher profile
```

Each profile: own state.db, memories, skills, config, gateway state.

Kanban workers are profiles — persistent identity across tasks.

---

## Digital Twin State Model

For persistent digital twin:

| Component | Hermes Implementation |
|-----------|----------------------|
| Identity | Profile + SOUL.md |
| User model | USER.md + Honcho |
| Episodic memory | Session DB + FTS5 |
| Procedural memory | Skills + Curator |
| Task state | Kanban DB |
| Working context | Current session |

---

## Agent-OS Mapping

| Agent-OS | Hermes |
|----------|--------|
| `02_memory/episodic-memory.md` | Session DB + FTS5 |
| `02_memory/memory-compaction.md` | /compress + on_pre_compress |
| `00_foundations/stateful-systems.md` | Multi-layer state |
| `06_digital-twins/persistent-identity.md` | Profiles |
