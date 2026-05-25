# Runtime Overview

**Core:** `run_agent.py` → `AIAgent`  
**Loop:** `agent/conversation_loop.py` (~4300 lines)  
**State:** `hermes_state.py` (SQLite + FTS5)

---

## Agent Loop

```
AIAgent.run_conversation()
  │
  ├── 1. Build system prompt (prompt_builder)
  │     ├── SOUL.md (personality)
  │     ├── MEMORY.md + USER.md (frozen)
  │     ├── Skills list (Level 0)
  │     ├── Context files (AGENTS.md, .hermes.md)
  │     ├── Memory provider blocks
  │     └── Tool guidance
  │
  ├── 2. Prefetch memory (background)
  │
  ├── 3. Resolve provider (runtime_provider)
  │     └── api_mode: chat_completions | codex_responses | anthropic_messages
  │
  ├── 4. API call loop
  │     ├── Send messages to LLM
  │     ├── Parse response
  │     ├── tool_calls? → handle_function_call → loop
  │     └── final response
  │
  ├── 5. Post-turn
  │     ├── sync_turn to memory providers
  │     ├── queue prefetch for next turn
  │     └── persist to SessionDB
  │
  └── 6. Compression (if needed)
        ├── on_pre_compress hooks
        └── context_compressor
```

---

## Three API Modes

| Mode | Format | Providers |
|------|--------|-----------|
| `chat_completions` | OpenAI-compatible | OpenRouter, OpenAI, most |
| `codex_responses` | OpenAI Responses API | Codex models |
| `anthropic_messages` | Anthropic Messages | Anthropic, Bedrock |

Resolution: `hermes_cli/runtime_provider.py`

---

## Session Persistence

**Database:** `~/.hermes/state.db`

| Table | Content |
|-------|---------|
| sessions | id, platform, user, title, model, timestamps |
| messages | role, content, tool_calls, tool_results |
| FTS5 index | Full-text search across messages |

**Features:**
- Resume conversations (`/resume`)
- Cross-session search (FTS5)
- Parent session ID (compression lineage)
- Platform tagging (cli, telegram, discord, ...)

---

## Profiles (Multi-Agent Runtime)

```bash
hermes profile create coder --description "Code assistant"
coder chat    # Separate HERMES_HOME
```

Each profile gets:
- Own `config.yaml`, `.env`, `SOUL.md`
- Own memories, sessions, skills
- Own gateway state
- Command alias at `~/.local/bin/<name>`

**Isolation:** `~/.hermes/profiles/<name>/`

---

## Sandbox Backends (7)

Terminal execution backends in `tools/environments/`:

| Backend | File | Use Case |
|---------|------|----------|
| **local** | `local.py` | Direct shell on host |
| **docker** | `docker.py` | Container isolation |
| **ssh** | `ssh.py` | Remote machine |
| **singularity** | `singularity.py` | HPC containers |
| **modal** | `modal.py` | Serverless (hibernates idle) |
| **daytona** | `daytona.py` | Serverless dev env |
| **vercel** | `vercel.py` | Vercel Sandbox |

Config via `terminal.backend` in config.yaml.

**Serverless persistence:** Modal and Daytona hibernate when idle, wake on demand.

---

## Cron Scheduler

**Code:** `cron/scheduler.py`, `cron/jobs.py`

```
Scheduler tick
  → load due jobs from jobs.json
  → create fresh AIAgent (no history)
  → inject attached skills
  → run job prompt
  → deliver to target platform
  → update next_run
```

Cron agents tagged `agent_context: cron` — memory providers skip writes.

---

## Context Compression

**Code:** `agent/context_compressor.py`, `agent/context_engine.py`

- Lossy summarization when context exceeds limit
- `on_pre_compress` hook extracts memories before compression
- `/compress` slash command for manual trigger
- Creates new session with parent_session_id lineage

---

## Prompt Caching

**Code:** `agent/prompt_caching.py`

- Anthropic cache markers in system prompt
- Frozen memory snapshot preserves cache
- Curator uses auxiliary model to avoid cache invalidation

---

## Entry Points Matrix

| Entry | File | Context |
|-------|------|---------|
| CLI | `cli.py` | Interactive TUI |
| Gateway | `gateway/run.py` | Messaging platforms |
| ACP | `acp_adapter/entry.py` | IDE integration |
| Cron | `cron/scheduler.py` | Scheduled jobs |
| Kanban | `hermes_cli/kanban.py` | Worker dispatch |
| Batch | `batch_runner.py` | Trajectory generation |
| Library | `run_agent.py` | Programmatic |

---

## Agent-OS Mapping

| Agent-OS | Hermes Runtime |
|----------|----------------|
| `01_agent-runtime/query-loop.md` | conversation_loop.py |
| `01_agent-runtime/terminal-states.md` | Session lifecycle |
| `01_agent-runtime/context-compression.md` | context_compressor.py |
| `01_agent-runtime/concurrency.md` | delegate batch + kanban |
| `00_foundations/stateful-systems.md` | SQLite + profiles |

See also: `runtime/SANDBOX_BACKENDS.md`, `runtime/PERSISTENT_STATE.md`, `runtime/SESSION_RECALL.md`
