# Folder Inventory — Detailed Module Map

**Base:** `source/hermes-agent/`

---

## `agent/` — 107 files

Core agent runtime internals.

```
agent/
├── conversation_loop.py      # Main loop (~4300 lines)
├── prompt_builder.py         # System prompt assembly
├── memory_manager.py         # Provider orchestration
├── memory_provider.py        # ABC for external providers
├── context_engine.py         # Pluggable context ABC
├── context_compressor.py     # Default summarization engine
├── prompt_caching.py         # Anthropic cache markers
├── curator.py                # Skill maintenance orchestrator
├── background_review.py      # Forked review agents
├── skill_commands.py         # Slash command handlers
├── skill_utils.py            # Skill preprocessing
├── skill_bundles.py          # Bundled skill management
├── anthropic_adapter.py      # Messages API conversion
├── runtime_provider.py       # Provider resolution
├── auxiliary_client.py       # Side-task LLM (vision, curator)
├── model_metadata.py         # Context lengths, token estimation
├── models_dev.py             # models.dev registry
├── display.py                # Spinner, tool preview
├── trajectory.py             # Trajectory saving
├── lsp/                      # LSP integration
└── transports/
    └── hermes_tools_mcp_server.py  # MCP server mode
```

---

## `tools/` — 98 files

One file per tool + shared infrastructure.

```
tools/
├── registry.py               # Central tool registry
├── approval.py               # Dangerous command detection
├── terminal_tool.py          # Terminal orchestration
├── process_registry.py       # Background processes
├── file_tools.py             # read/write/patch/search
├── web_tools.py              # web_search, web_extract
├── browser_tool.py           # 10 browser automation tools
├── code_execution_tool.py    # execute_code sandbox
├── delegate_tool.py          # Subagent delegation (~2800 lines)
├── mixture_of_agents_tool.py # Multi-LLM parallel
├── mcp_tool.py               # MCP client (~3600 lines)
├── mcp_oauth.py              # OAuth flow
├── mcp_oauth_manager.py      # Token management
├── memory_tool.py            # MEMORY.md / USER.md
├── session_search_tool.py    # FTS5 cross-session search
├── skills_tool.py            # skills_list, skill_view
├── skills_hub.py             # Remote skill installation
├── skills_guard.py           # Skill safety checks
├── skill_manager_tool.py     # skill_manage (curator)
├── kanban_tools.py           # kanban_* toolset
├── credential_files.py       # File-based credential passthrough
├── env_passthrough.py        # Env var passthrough
├── ansi_strip.py             # ANSI escape stripping
├── computer_use_tool.py      # Computer use MCP
├── environments/             # Terminal backends
│   ├── local.py
│   ├── docker.py
│   ├── ssh.py
│   ├── singularity.py
│   ├── modal.py
│   ├── daytona.py
│   └── vercel.py
└── computer_use/             # Computer use helpers
```

---

## `hermes_cli/` — 101 files

CLI commands, configuration, setup wizards.

```
hermes_cli/
├── main.py                   # Entry point (~14k lines)
├── config.py                 # DEFAULT_CONFIG (~5650 lines)
├── commands.py               # Slash command registry
├── auth.py                   # PROVIDER_REGISTRY
├── runtime_provider.py       # Provider → api_mode
├── models.py                 # Model catalog
├── model_switch.py           # /model command
├── setup.py                  # Interactive wizard
├── skin_engine.py            # CLI theming
├── plugins.py                # PluginManager
├── callbacks.py              # Terminal callbacks
├── memory_setup.py           # Memory provider wizard
├── mcp_config.py             # MCP configuration
├── skills_config.py          # Skills enable/disable
├── skills_hub.py             # /skills command
├── tools_config.py           # Tools enable/disable
├── gateway.py                # Gateway start/stop
├── kanban.py                 # Kanban CLI
├── kanban_swarm.py           # Swarm topology
├── kanban_db.py              # SQLite layer
├── kanban_decompose.py       # Task decomposition
├── kanban_specify.py         # Task specification
├── web_server.py             # Dashboard FastAPI
└── claw.py                   # OpenClaw migration
```

---

## `gateway/` — 62 files

```
gateway/
├── run.py                    # GatewayRunner (~18.5k lines)
├── session.py                # SessionStore
├── delivery.py               # Outbound delivery
├── pairing.py                # DM authorization
├── hooks.py                  # Hook lifecycle
├── mirror.py                 # Cross-session mirroring
├── status.py                 # Token locks, process tracking
├── builtin_hooks/            # Extension point (empty)
└── platforms/                # 20 adapters
    ├── telegram.py
    ├── discord.py
    ├── slack.py
    ├── whatsapp.py
    ├── signal.py
    ├── matrix.py
    ├── mattermost.py
    ├── email.py
    ├── sms.py
    ├── dingtalk.py
    ├── feishu.py
    ├── wecom.py
    ├── webhook.py
    ├── api_server.py
    └── ...
```

---

## `plugins/` — 219 files

```
plugins/
├── memory/
│   ├── honcho/               # Dialectic user modeling
│   ├── hindsight/
│   ├── mem0/
│   ├── supermemory/
│   ├── retaindb/
│   ├── openviking/
│   ├── holographic/
│   └── byterover/
├── context_engine/           # Context engine plugins
├── web/                      # Web search backends
├── tts/                      # Text-to-speech
├── video_gen/                # Video generation
├── spotify/                  # Spotify integration
└── teams_pipeline/           # Teams pipeline
```

---

## `skills/` — 571 files (88 bundled)

Categories include:
- `software-development/` — subagent-driven-development, github-pr-workflow
- `devops/` — kanban-orchestrator, kanban-worker
- `autonomous-ai-agents/` — kanban-codex-lane
- `mcp/` — native-mcp
- `research/`, `security/`, `media/`, `productivity/`

Each skill: `SKILL.md` + optional `scripts/`, `references/`, `assets/`

---

## Config & State Files

| File | Location | Purpose |
|------|----------|---------|
| `config.yaml` | `~/.hermes/` | Main config |
| `SOUL.md` | `~/.hermes/` | Personality |
| `MEMORY.md` | `~/.hermes/memories/` | Agent memory |
| `USER.md` | `~/.hermes/memories/` | User profile |
| `state.db` | `~/.hermes/` | Sessions SQLite |
| `kanban.db` | `~/.hermes/` | Kanban board |
| `.curator_state` | `~/.hermes/skills/` | Curator scheduler |
| `honcho.json` | `$HERMES_HOME/` | Honcho config |
