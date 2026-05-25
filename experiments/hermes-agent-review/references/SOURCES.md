# References

External sources and documentation index for Hermes Agent research.

---

## Primary Source

| Resource | URL |
|----------|-----|
| GitHub Repository | https://github.com/NousResearch/hermes-agent |
| Official Documentation | https://hermes-agent.nousresearch.com/docs/ |
| Nous Research | https://nousresearch.com |
| Nous Portal | https://portal.nousresearch.com |

---

## Local Clone

```
experiments/hermes-agent-review/source/hermes-agent/
```

Shallow clone, v0.14.0, read-only reference.

---

## Key Documentation Paths (in clone)

### Developer Guide

| Doc | Path |
|-----|------|
| Architecture | `website/docs/developer-guide/architecture.md` |
| Agent Loop | `website/docs/developer-guide/agent-loop.md` |
| Prompt Assembly | `website/docs/developer-guide/prompt-assembly.md` |
| Provider Runtime | `website/docs/developer-guide/provider-runtime.md` |
| Tools Runtime | `website/docs/developer-guide/tools-runtime.md` |
| Session Storage | `website/docs/developer-guide/session-storage.md` |
| Gateway Internals | `website/docs/developer-guide/gateway-internals.md` |
| Memory Provider Plugin | `website/docs/developer-guide/memory-provider-plugin.md` |
| Context Compression | `website/docs/developer-guide/context-compression-and-caching.md` |

### User Guide Features

| Doc | Path |
|-----|------|
| Memory | `website/docs/user-guide/features/memory.md` |
| Memory Providers | `website/docs/user-guide/features/memory-providers.md` |
| Skills | `website/docs/user-guide/features/skills.md` |
| MCP | `website/docs/user-guide/features/mcp.md` |
| Delegation | `website/docs/user-guide/features/delegation.md` |
| Kanban | `website/docs/user-guide/features/kanban.md` |
| Profiles | `website/docs/user-guide/profiles.md` |
| Sessions | `website/docs/user-guide/sessions.md` |

### Reference

| Doc | Path |
|-----|------|
| CLI Commands | `website/docs/reference/cli-commands.md` |
| Tools Reference | `website/docs/reference/tools-reference.md` |
| MCP Config | `website/docs/reference/mcp-config-reference.md` |
| Skills Catalog | `website/docs/reference/skills-catalog.md` |

---

## External Standards

| Standard | URL |
|----------|-----|
| agentskills.io | https://agentskills.io/specification |
| Model Context Protocol | https://modelcontextprotocol.io |
| Honcho | https://docs.honcho.dev |

---

## Agent-OS Cross-References

| Agent-OS Resource | Path |
|-------------------|------|
| Claude Code Architecture | `agent-os/10_research/claude-code-architecture.md` |
| Code as Agent Harness | `Books/agents/` |
| Memory Taxonomy | `agent-os/02_memory/memory-taxonomy.md` |
| Subagents | `agent-os/04_multi-agent/subagents.md` |
| MCP Protocol | `agent-os/05_mcp/mcp-protocol.md` |
| Digital Twins | `agent-os/06_digital-twins/` |
| Anti-patterns | `agent-os/09_antipatterns/` |

---

## Key Source Files (in clone)

| Component | File |
|-----------|------|
| Agent core | `run_agent.py` |
| Conversation loop | `agent/conversation_loop.py` |
| Memory manager | `agent/memory_manager.py` |
| Memory provider ABC | `agent/memory_provider.py` |
| Memory tool | `tools/memory_tool.py` |
| Delegate tool | `tools/delegate_tool.py` |
| MCP client | `tools/mcp_tool.py` |
| Curator | `agent/curator.py` |
| Session DB | `hermes_state.py` |
| Kanban DB | `hermes_cli/kanban_db.py` |
| Config | `hermes_cli/config.py` |

---

## Kanban Spec

| Resource | Path |
|----------|------|
| Kanban v1 Spec (PDF) | `docs/hermes-kanban-v1-spec.pdf` |
| Kanban Tutorial | `website/docs/user-guide/features/kanban-tutorial.md` |

---

## Issues & Discussions

For architecture-related discussions, search:
- https://github.com/NousResearch/hermes-agent/issues
- https://discord.gg/NousResearch

Keywords: memory, kanban, subagent, mcp, profile, curator, gateway
