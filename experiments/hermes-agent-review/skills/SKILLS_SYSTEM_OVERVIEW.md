# Skills System Overview

**Standard:** [agentskills.io](https://agentskills.io/specification)  
**Runtime:** `~/.hermes/skills/`  
**Code:** `tools/skills_*.py`, `agent/skill_*.py`, `agent/curator.py`

---

## Architecture

```
┌─────────────────────────────────────────────────────────┐
│                    Skills Ecosystem                      │
│                                                          │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────────┐  │
│  │ Bundled     │  │ Optional    │  │ User/Agent      │  │
│  │ 88 skills   │  │ ~80 skills  │  │ Created         │  │
│  │ (auto-copy) │  │ (explicit)  │  │ (runtime)       │  │
│  └──────┬──────┘  └──────┬──────┘  └────────┬────────┘  │
│         └────────────────┼───────────────────┘          │
│                          ▼                               │
│              ~/.hermes/skills/ (source of truth)         │
│                          │                               │
│         ┌────────────────┼────────────────┐             │
│         ▼                ▼                ▼             │
│   skills_list()    skill_view()     /skill-name         │
│   (Level 0)        (Level 1/2)      slash command       │
│                          │                               │
│                          ▼                               │
│              ┌───────────────────────┐                  │
│              │ Curator (inactivity)  │                  │
│              │ pin/archive/consolidate│                  │
│              └───────────────────────┘                  │
└─────────────────────────────────────────────────────────┘
```

---

## Progressive Disclosure

Three-level loading minimizes token overhead:

| Level | Call | Returns | Token Cost |
|-------|------|---------|------------|
| 0 | `skills_list()` | `[{name, description, category}, ...]` | ~3k tokens |
| 1 | `skill_view(name)` | Full SKILL.md content | Varies |
| 2 | `skill_view(name, path)` | Specific reference file | Varies |

Agent loads full content only when needed.

---

## SKILL.md Format

```markdown
---
name: my-skill
description: Brief description
version: 1.0.0
platforms: [macos, linux]     # Optional OS restriction
metadata:
  hermes:
    tags: [python, automation]
    category: devops
    fallback_for_toolsets: [web]    # Conditional activation
    requires_toolsets: [terminal]   # Conditional activation
---

# Skill Title

## When to Use
Trigger conditions.

## Procedure
1. Step one
2. Step two

## Pitfalls
Known failure modes.

## Verification
How to confirm success.
```

---

## Skill Sources

| Source | Location | Count | Install |
|--------|----------|-------|---------|
| Bundled | `skills/` in repo | 88 | Auto on fresh install |
| Optional | `optional-skills/` | ~80 | `hermes skills install <name>` |
| Skills Hub | Remote registry | Variable | `/skills` command |
| Agent-created | `~/.hermes/skills/` | Variable | Agent via skill_manage |

---

## Slash Commands

Every installed skill → slash command:

```
/gif-search funny cats
/plan design a rollout for auth migration
/subagent-driven-development implement feature X
```

Running `/skill-name` alone loads skill and prompts for input.

---

## Self-Improving Skills (Curator)

**Code:** `agent/curator.py`

Inactivity-triggered auxiliary agent that:
- Reviews agent-created skills only
- Auto-transitions lifecycle states (stale → archive)
- Can pin, archive, consolidate, patch via `skill_manage`
- Never auto-deletes (archive is recoverable)
- Uses auxiliary model (not main session cache)

**Scheduler state:** `~/.hermes/skills/.curator_state`

| Config | Default |
|--------|---------|
| `interval_hours` | 168 (7 days) |
| `min_idle_hours` | 2 |
| `stale_after_days` | 30 |
| `archive_after_days` | 90 |

**Invariants:**
- Only touches agent-created skills
- Pinned skills bypass all auto-transitions
- Never auto-deletes

---

## Notable Bundled Skills

| Skill | Category | Purpose |
|-------|----------|---------|
| `subagent-driven-development` | software-development | Subagent workflow methodology |
| `hermes-agent-skill-authoring` | meta | How to create skills |
| `kanban-orchestrator` | devops | Kanban routing patterns |
| `kanban-worker` | devops | Kanban worker patterns |
| `native-mcp` | mcp | MCP integration guidance |
| `plan` | productivity | Write plan, don't execute |

---

## Platform Restrictions

```yaml
platforms: [macos]            # macOS only
platforms: [macos, linux]     # macOS and Linux
# omitted = all platforms
```

Hidden from system prompt, skills_list(), slash commands on incompatible platforms.

---

## Agent-OS Relevance

| Pattern | Agent-OS Target |
|---------|-----------------|
| Progressive disclosure | New pattern candidate |
| agentskills.io standard | Skill format reference |
| Curator lifecycle | `06_digital-twins/evolving-memory.md` |
| Conditional activation | Toolset fallback pattern |
| Platform restrictions | Environment-aware skills |

See also: `skills/SELF_IMPROVING_SKILLS.md`
