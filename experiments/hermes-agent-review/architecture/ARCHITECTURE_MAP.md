# Architecture Map — Hermes Agent

**Source docs:** `source/hermes-agent/website/docs/developer-guide/architecture.md`  
**Audit date:** 2026-05-25

---

## System Overview

```
┌─────────────────────────────────────────────────────────────────────┐
│                        Entry Points                                  │
│                                                                      │
│  CLI (cli.py)    Gateway (gateway/run.py)    ACP (acp_adapter/)     │
│  Batch Runner    Web Dashboard               Python Library          │
└──────────┬──────────────┬───────────────────────┬───────────────────┘
           │              │                       │
           ▼              ▼                       ▼
┌─────────────────────────────────────────────────────────────────────┐
│                     AIAgent (run_agent.py)                          │
│                                                                     │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐               │
│  │ Prompt       │  │ Provider     │  │ Tool         │               │
│  │ Builder      │  │ Resolution   │  │ Dispatch     │               │
│  └──────┬───────┘  └──────┬───────┘  └──────┬───────┘               │
│         │                 │                 │                       │
│  ┌──────┴───────┐  ┌──────┴───────┐  ┌──────┴───────┐               │
│  │ Memory       │  │ 3 API Modes  │  │ Tool Registry│               │
│  │ Manager      │  │ chat_compl.  │  │ 70+ tools    │               │
│  │ Compression  │  │ codex_resp.  │  │ 28 toolsets  │               │
│  └──────────────┘  │ anthropic    │  └──────────────┘               │
│                    └──────────────┘                                 │
└─────────┴─────────────────┴─────────────────┴───────────────────────┘
           │                                    │
           ▼                                    ▼
┌───────────────────┐              ┌──────────────────────┐
│ Session Storage   │              │ Tool Backends         │
│ SQLite + FTS5     │              │ Terminal (7 backends) │
│ hermes_state.py   │              │ Browser (5 backends)│
└───────────────────┘              │ Web (4 backends)      │
                                   │ MCP (dynamic)         │
                                   └──────────────────────┘
```

---

## Major Subsystems

| Subsystem | Location | Responsibility |
|-----------|----------|----------------|
| Agent Loop | `run_agent.py`, `agent/conversation_loop.py` | Sync orchestration: provider, prompt, tools, retries, compression |
| Prompt System | `agent/prompt_builder.py` | SOUL.md + memory + skills + context files + tool guidance |
| Memory | `agent/memory_manager.py`, `tools/memory_tool.py` | Built-in + one external provider |
| Tools | `tools/registry.py`, `model_tools.py` | 70+ tools, 28 toolsets, dispatch |
| Sessions | `hermes_state.py`, `gateway/session.py` | SQLite + FTS5 persistence |
| Gateway | `gateway/run.py`, `gateway/platforms/` | 20+ messaging adapters |
| CLI | `hermes_cli/main.py`, `cli.py` | All user-facing commands |
| Skills | `skills/`, `tools/skills_*.py`, `agent/curator.py` | Progressive disclosure + self-improvement |
| MCP | `tools/mcp_tool.py` | Client + optional server mode |
| Multi-agent | `tools/delegate_tool.py`, `hermes_cli/kanban*.py` | Subagents + Kanban |
| Cron | `cron/scheduler.py` | Scheduled unattended jobs |
| Profiles | `hermes_constants.py`, `hermes_cli/` | Isolated agent instances |

---

## Data Flow: CLI Session

```
User input
  → HermesCLI.process_input()
    → AIAgent.run_conversation()
      → prompt_builder.build_system_prompt()
        ├── SOUL.md (personality)
        ├── MEMORY.md + USER.md (frozen snapshot)
        ├── skills_list (Level 0)
        ├── AGENTS.md / .hermes.md (context files)
        └── tool guidance
      → memory_manager.prefetch_all(user_message)
      → runtime_provider.resolve_runtime_provider()
      → API call (chat_completions | codex_responses | anthropic_messages)
      → tool_calls?
        → model_tools.handle_function_call()
        → loop until final response
      → memory_manager.sync_all(user, assistant)
      → display → save to SessionDB
```

---

## Data Flow: Gateway Message

```
Platform event (Telegram/Discord/...)
  → Adapter.on_message() → MessageEvent
    → GatewayRunner._handle_message()
      → authorize user (pairing)
      → resolve session key
      → create AIAgent with session history
      → AIAgent.run_conversation()
      → deliver response through adapter
      → optional: mirror to other sessions
```

---

## Data Flow: Subagent Delegation

```
Parent AIAgent
  → delegate_task(goal, context, toolsets)
    → spawn child AIAgent (fresh context)
      → restricted toolset (no delegate, no memory write, no clarify)
      → own terminal session
      → run until completion
    → return summary only to parent
    → memory_manager.on_delegation() hook
```

---

## Data Flow: Kanban Worker

```
Dispatcher loop (every 60s)
  → scan kanban.db for ready tasks
    → atomic claim
    → spawn profile process (HERMES_KANBAN_BOARD env)
      → worker reads task + comment thread
      → uses kanban_* tools + delegate_task internally
      → kanban_complete or kanban_block
    → update task status
```

---

## API Mode Matrix

| Mode | Providers | Notes |
|------|-----------|-------|
| `chat_completions` | OpenRouter, OpenAI, most | Default OpenAI-compatible |
| `codex_responses` | OpenAI Codex | Responses API format |
| `anthropic_messages` | Anthropic, Bedrock | Native Messages API |

Resolution: `hermes_cli/runtime_provider.py` → `agent/runtime_provider.py`

---

## Isolation Boundaries

| Boundary | Mechanism |
|----------|-----------|
| Profile | Separate `~/.hermes/profiles/<name>/` HERMES_HOME |
| Subagent | Fresh conversation, restricted tools, summary return |
| Kanban board | Separate SQLite DB per board slug |
| Kanban tenant | Soft namespace within board |
| Gateway session | Platform + user_id + session key |
| Sandbox | Terminal backend selection (local/docker/ssh/...) |

---

## Recommended Reading Order (from Hermes docs)

1. Architecture (this map)
2. Agent Loop Internals
3. Prompt Assembly
4. Provider Runtime Resolution
5. Tools Runtime
6. Session Storage
7. Gateway Internals
8. Context Compression & Prompt Caching
9. ACP Internals
10. Memory Provider Plugin

**Local paths:** `source/hermes-agent/website/docs/developer-guide/`
