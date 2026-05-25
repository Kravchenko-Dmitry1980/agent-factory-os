# Repository Inventory — Hermes Agent

**Source:** `source/hermes-agent/`  
**Version:** 0.14.0  
**License:** MIT  
**Python:** ≥3.11  
**Upstream:** https://github.com/NousResearch/hermes-agent

---

## Package Metadata

| Field | Value |
|-------|-------|
| Package name | `hermes-agent` |
| Console scripts | `hermes`, `hermes-agent`, `hermes-acp` |
| Lock file | `uv.lock` |
| Node dep | `agent-browser` (root), Docusaurus (website) |
| Test count | ~3000+ (per architecture docs) |

---

## Top-Level Directory Inventory

| Directory | Files | Role |
|-----------|-------|------|
| `tests/` | 1264 | Pytest suite |
| `website/` | 720 | Docusaurus docs + i18n + generated skill pages |
| `skills/` | 571 | 88 bundled skills (agentskills.io) |
| `ui-tui/` | 339 | React/Ink TUI frontend |
| `optional-skills/` | 285 | ~80 optional skills (explicit install) |
| `plugins/` | 219 | Memory, web search, TTS, video, etc. |
| `web/` | 107 | Dashboard SPA |
| `agent/` | 107 | Core agent internals |
| `hermes_cli/` | 101 | CLI subcommands, config, setup |
| `tools/` | 98 | 70+ tool implementations |
| `gateway/` | 62 | Messaging gateway + 20 platform adapters |
| `scripts/` | 27 | install.sh, install.ps1, CI helpers |
| `acp_adapter/` | 10 | ACP server for IDE integration |
| `tui_gateway/` | 8 | WebSocket TUI gateway |
| `cron/` | 3 | Scheduler |
| `providers/` | 3 | Model provider plugin base |

---

## Root-Level Modules

| File | Purpose |
|------|---------|
| `run_agent.py` | `AIAgent` — core conversation orchestration |
| `cli.py` | `HermesCLI` — interactive TUI (~15k lines) |
| `model_tools.py` | Tool schema collection + dispatch |
| `toolsets.py` | Tool groupings (28 toolsets) |
| `hermes_state.py` | SQLite session DB + FTS5 |
| `hermes_constants.py` | `HERMES_HOME`, profile-aware paths |
| `hermes_bootstrap.py` | Startup initialization |
| `hermes_logging.py` | Logging configuration |
| `batch_runner.py` | Batch trajectory generation |
| `trajectory_compressor.py` | Trajectory compression for training |

---

## Python Packages

### `agent/` — Agent Internals (~107 files)

| Module | Purpose |
|--------|---------|
| `conversation_loop.py` | Main agent loop (~4300 lines) |
| `prompt_builder.py` | System prompt assembly |
| `memory_manager.py` | Memory provider orchestration |
| `memory_provider.py` | MemoryProvider ABC |
| `context_engine.py` | Pluggable context engine ABC |
| `context_compressor.py` | Default lossy summarization |
| `prompt_caching.py` | Anthropic prompt caching |
| `curator.py` | Self-improving skills curator |
| `background_review.py` | Forked review agents |
| `skill_commands.py` | Skill slash commands |
| `skill_utils.py`, `skill_bundles.py` | Skill preprocessing |
| `anthropic_adapter.py` | Anthropic Messages API |
| `runtime_provider.py` | Provider → api_mode resolution |
| `transports/hermes_tools_mcp_server.py` | Hermes as MCP server |

### `tools/` — Tool Implementations (~98 files)

| Category | Key Files |
|----------|-----------|
| Registry | `registry.py` |
| Terminal | `terminal_tool.py`, `environments/` (7 backends) |
| Files | `file_tools.py` |
| Web | `web_tools.py`, `browser_tool.py` |
| Memory | `memory_tool.py`, `session_search_tool.py` |
| Skills | `skills_tool.py`, `skills_hub.py`, `skills_guard.py`, `skill_manager_tool.py` |
| Delegation | `delegate_tool.py`, `mixture_of_agents_tool.py` |
| MCP | `mcp_tool.py`, `mcp_oauth.py`, `mcp_oauth_manager.py` |
| Kanban | `kanban_tools.py` |
| Code | `code_execution_tool.py` |
| Safety | `approval.py` |

### `hermes_cli/` — CLI Layer (~101 files)

| Module | Purpose |
|--------|---------|
| `main.py` | All `hermes` subcommands (~14k lines) |
| `config.py` | DEFAULT_CONFIG, migration (~5650 lines) |
| `setup.py` | Interactive setup wizard |
| `auth.py` | PROVIDER_REGISTRY |
| `plugins.py` | PluginManager |
| `kanban.py`, `kanban_swarm.py`, `kanban_db.py` | Kanban CLI + DB |
| `memory_setup.py` | Memory provider wizard |
| `mcp_config.py` | MCP configuration |
| `skills_config.py`, `skills_hub.py` | Skills management |
| `web_server.py` | Dashboard FastAPI backend |

### `gateway/` — Messaging Gateway (~62 files)

| Component | Purpose |
|-----------|---------|
| `run.py` | GatewayRunner (~18.5k lines) |
| `session.py` | SessionStore |
| `delivery.py` | Outbound message delivery |
| `pairing.py` | DM authorization |
| `hooks.py` | Hook lifecycle |
| `mirror.py` | Cross-session mirroring |
| `platforms/` | 20 adapters (telegram, discord, slack, whatsapp, signal, matrix, email, sms, …) |

### `plugins/` — Plugin Ecosystem (~219 files)

| Plugin | Purpose |
|--------|---------|
| `memory/honcho/` | Honcho dialectic user modeling |
| `memory/hindsight/` | Hindsight memory |
| `memory/mem0/` | Mem0 integration |
| `memory/supermemory/` | Supermemory |
| `memory/retaindb/` | RetainDB |
| `memory/openviking/` | OpenViking |
| `memory/holographic/` | Holographic memory |
| `memory/byterover/` | ByteRover |
| `context_engine/` | Context engine plugins |
| Web, TTS, video_gen, spotify, teams_pipeline | Feature plugins |

---

## Skills Inventory

| Location | Count | Install |
|----------|-------|---------|
| `skills/` (bundled) | 88 SKILL.md | Auto-copied to `~/.hermes/skills/` |
| `optional-skills/` | ~80 SKILL.md | Explicit install |
| User-created | Variable | Agent-managed in `~/.hermes/skills/` |
| Skills Hub | Remote | `/skills` command |

**Notable bundled skills:**
- `subagent-driven-development`
- `hermes-agent-skill-authoring`
- `kanban-orchestrator`, `kanban-worker`
- `native-mcp`

---

## Documentation Locations

| Path | Content |
|------|---------|
| `website/docs/getting-started/` | Quickstart, installation |
| `website/docs/user-guide/` | CLI, TUI, features, profiles |
| `website/docs/developer-guide/` | Architecture, internals (26 files) |
| `website/docs/reference/` | CLI commands, tools, MCP config |
| `README.md` | Project overview |
| `docs/hermes-kanban-v1-spec.pdf` | Kanban design spec |

**Public docs:** https://hermes-agent.nousresearch.com/docs/

---

## Runtime State (not in repo)

| Path | Content |
|------|---------|
| `~/.hermes/config.yaml` | Main configuration |
| `~/.hermes/memories/MEMORY.md` | Agent memory |
| `~/.hermes/memories/USER.md` | User profile |
| `~/.hermes/state.db` | SQLite sessions + FTS5 |
| `~/.hermes/skills/` | Runtime skills |
| `~/.hermes/kanban.db` | Kanban task board |
| `~/.hermes/profiles/<name>/` | Profile isolation |
| `~/.hermes/mcp-tokens/` | OAuth token cache |

---

## Entry Points Summary

```
hermes              → hermes_cli.main:main
hermes-agent        → run_agent:main
hermes-acp          → acp_adapter.entry:main
AIAgent (library)   → from run_agent import AIAgent
```
