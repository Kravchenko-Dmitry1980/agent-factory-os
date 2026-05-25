# MCP Integration Overview

**Code:** `tools/mcp_tool.py` (~3600 lines), `hermes_cli/mcp_config.py`  
**Server mode:** `agent/transports/hermes_tools_mcp_server.py`  
**Docs:** `website/docs/user-guide/features/mcp.md`

---

## Architecture

```
┌─────────────────────────────────────────────────────────┐
│                    Hermes Agent                          │
│                                                          │
│  ┌─────────────────────────────────────────────────┐    │
│  │ MCP Client (tools/mcp_tool.py)                   │    │
│  │                                                  │    │
│  │  config.yaml → mcp_servers                       │    │
│  │       │                                          │    │
│  │       ├── stdio servers (local subprocess)       │    │
│  │       ├── HTTP servers (remote endpoints)        │    │
│  │       └── OAuth servers (PKCE, token cache)    │    │
│  │                                                  │    │
│  │  Startup: discover tools → register in registry  │    │
│  │  Runtime: tool calls → MCP protocol              │    │
│  └─────────────────────────────────────────────────┘    │
│                                                          │
│  ┌─────────────────────────────────────────────────┐    │
│  │ MCP Server Mode (optional)                       │    │
│  │ agent/transports/hermes_tools_mcp_server.py      │    │
│  │ Exposes Hermes tools to external MCP clients     │    │
│  └─────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────┘
```

---

## Client Mode (Primary)

Hermes connects TO external MCP servers.

### Server Types

| Type | Config | Use Case |
|------|--------|----------|
| **Stdio** | `command` + `args` + `env` | Local npx servers, CLI tools |
| **HTTP** | `url` + `headers` | Remote hosted endpoints |
| **OAuth HTTP** | `url` + `auth: oauth` | Linear, Sentry, Atlassian, etc. |

### Configuration

```yaml
# ~/.hermes/config.yaml
mcp_servers:
  filesystem:
    command: "npx"
    args: ["-y", "@modelcontextprotocol/server-filesystem", "/home/user/projects"]
  
  linear:
    url: "https://mcp.linear.app/mcp"
    auth: oauth
  
  company_api:
    url: "https://mcp.internal.example.com"
    headers:
      Authorization: "Bearer ***"
    tools:
      search_issues:
        enabled: true
      create_issue:
        enabled: false
```

### Key Config Options

| Key | Purpose |
|-----|---------|
| `enabled` | Skip server entirely if false |
| `timeout` | Tool call timeout |
| `connect_timeout` | Initial connection timeout |
| `supports_parallel_tool_calls` | Allow concurrent MCP tool calls |
| `tools` | Per-tool filtering and policy |

### OAuth Flow

1. First connect → authorize URL printed
2. Browser opens (or paste-back for headless)
3. Tokens cached at `~/.hermes/mcp-tokens/<server>.json` (0o600)
4. Auto-refresh until failure
5. Re-auth: `hermes mcp login <server>`

**Headless:** SSH port forward or paste redirect URL.

---

## Tool Discovery & Registration

```
Startup
  → Read mcp_servers from config
  → For each enabled server:
      → Connect (stdio spawn or HTTP)
      → list_tools()
      → Apply per-tool filtering
      → Register in tools/registry.py
  → Tools available like native Hermes tools
```

Dynamic tool names: `mcp_<server>_<tool>`

---

## Utility Wrappers

When MCP server supports resources/prompts:
- Resource access wrappers
- Prompt template wrappers

---

## Server Mode (Secondary)

Hermes exposes its own tools as MCP server for external clients.

**Use case:** IDE integration, external orchestrators calling Hermes tools.

**Code:** `agent/transports/hermes_tools_mcp_server.py`

---

## Skills for MCP

| Skill | Purpose |
|-------|---------|
| `skills/mcp/native-mcp/` | MCP integration guidance |
| `optional-skills/mcp/fastmcp/` | FastMCP patterns |
| `optional-skills/mcp/mcporter/` | MCP porting |

---

## Subagent Restrictions

Subagents can use MCP tools if in their toolset, but:
- No recursive MCP server spawning
- OAuth tokens shared from parent config

---

## Dangerous Complexity

| Risk | Mitigation |
|------|------------|
| OAuth config race (30s auto-reload) | Use `hermes mcp login` separately |
| Tool schema bloat (many servers) | Per-tool filtering |
| Token expiry mid-session | Auto-refresh + re-auth command |
| Remote headless OAuth | Paste-back or SSH forward |
| 3600-line mcp_tool.py | Well-tested but hard to modify |

---

## Comparison with Agent-OS MCP Docs

| Agent-OS | Hermes |
|----------|--------|
| `05_mcp/mcp-protocol.md` | MCP client implementation |
| `05_mcp/tool-servers.md` | mcp_servers config |
| `05_mcp/mcp-transports.md` | stdio + HTTP + OAuth |
| `05_mcp/runtime-bridges.md` | Dynamic tool registration |

Hermes is **MCP consumer first**, server mode secondary.

---

## Agent-OS Integration Candidates

- Per-tool filtering pattern
- OAuth token cache location/conventions
- Dynamic tool registration at startup
- MCP + subagent toolset interaction rules
