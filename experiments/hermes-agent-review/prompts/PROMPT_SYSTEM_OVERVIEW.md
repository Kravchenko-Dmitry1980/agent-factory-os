# Prompt System Overview

**Code:** `agent/prompt_builder.py`  
**Docs:** `website/docs/developer-guide/prompt-assembly.md`

---

## System Prompt Components

Built in order by `prompt_builder.build_system_prompt()`:

| Component | Source | Mutable Mid-Session |
|-----------|--------|---------------------|
| Personality | `SOUL.md` | No (file-based) |
| Memory | MEMORY.md + USER.md | No (frozen snapshot) |
| Memory provider | External provider block | Prefetch only |
| Skills list | Level 0 disclosure | No |
| Context files | AGENTS.md, .hermes.md | No |
| Tool guidance | Built-in instructions | No |
| Model-specific | Provider adapter | No |

---

## SOUL.md — Personality

User-editable personality file at `~/.hermes/SOUL.md`.

Defines agent character, tone, behavior guidelines.

Changed via `/personality` command or direct edit.

---

## Context Files

| File | Scope | Purpose |
|------|-------|---------|
| `AGENTS.md` | Project root | Project-specific agent instructions |
| `.hermes.md` | Project root | Hermes-specific project config |
| Workspace files | Per backend | Backend-specific context |

Auto-discovered and injected into system prompt.

---

## Memory Injection Format

```
══════════════════════════════════════════════
MEMORY (your personal notes) [67% — 1,474/2,200 chars]
══════════════════════════════════════════════
[entries separated by §]

══════════════════════════════════════════════
USER PROFILE [45% — 619/1,375 chars]
══════════════════════════════════════════════
[entries separated by §]
```

Frozen at session start. See `memory/MEMORY.md`.

---

## Skills Injection

Level 0 only in system prompt:

```json
[
  {"name": "plan", "description": "Write implementation plan", "category": "productivity"},
  {"name": "github-pr-workflow", "description": "...", "category": "software-development"}
]
```

Full content loaded on demand via `skill_view()`.

---

## Provider-Specific Instructions

Added by runtime provider resolution:
- Anthropic cache markers
- Model-specific formatting
- Tool call format adaptation

---

## Prompt Caching Strategy

**Code:** `agent/prompt_caching.py`

1. Static prefix (personality, memory snapshot, skills list) → cacheable
2. Dynamic suffix (conversation, prefetched context) → not cached
3. Curator uses auxiliary model to avoid invalidating main cache

**Design principle:** Maximize cacheable prefix stability.

---

## Agent-OS Relevance

Maps to:
- `01_agent-runtime/context-compression.md`
- `08_patterns/prompt-cache-as-constraint.md`
- Separation of static vs dynamic prompt components
