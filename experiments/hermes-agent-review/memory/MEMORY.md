# MEMORY.md — Concept Documentation

**Runtime path:** `~/.hermes/memories/MEMORY.md`  
**Code:** `tools/memory_tool.py`  
**Char limit:** 2,200 (~800 tokens)

---

## Definition

MEMORY.md is the agent's **personal notebook** — bounded, curated facts the agent needs to remember about the environment, workflows, and lessons learned across sessions.

---

## What Goes in MEMORY.md

| Category | Examples |
|----------|----------|
| Environment facts | OS, installed tools, project structure |
| Project conventions | Code style, naming, config patterns |
| Tool quirks | Workarounds discovered during use |
| Completed work diary | "Migrated DB from MySQL to PostgreSQL on 2026-01-15" |
| Skills that worked | Techniques worth reusing |

---

## What NOT to Save

- Trivial/obvious info ("User asked about Python")
- Easily re-discovered facts (web-searchable)
- Raw data dumps (logs, code blocks, tables)
- Session-specific ephemera (temp paths, debug context)
- Content already in SOUL.md or AGENTS.md

---

## Format in System Prompt

```
══════════════════════════════════════════════
MEMORY (your personal notes) [67% — 1,474/2,200 chars]
══════════════════════════════════════════════
User's project is a Rust web service at ~/code/myapi using Axum + SQLx
§
This machine runs Ubuntu 22.04, has Docker and Podman installed
§
User prefers concise responses, dislikes verbose explanations
```

Header shows:
- Store name
- Usage percentage
- Character count (current/limit)

---

## Capacity Management

When full, `memory` tool returns error with current entries:

```json
{
  "success": false,
  "error": "Memory at 2,100/2,200 chars. Adding this entry (250 chars) would exceed the limit.",
  "current_entries": ["..."],
  "usage": "2,100/2,200"
}
```

Agent should:
1. Identify consolidatable entries
2. Use `replace` to merge related facts
3. Then `add` new entry

**Best practice:** Consolidate when above 80% capacity.

---

## Good Entry Examples

```
# Good: Information-dense, multi-fact
Project myapi: Rust/Axum/SQLx at ~/code/myapi, uses tabs/120cols, CI on GitHub Actions

# Good: Actionable convention
Never use sudo for Docker — user is in docker group

# Bad: Too vague
User likes coding

# Bad: Too large (use file reference instead)
[entire API schema pasted here]
```

---

## Frozen Snapshot Implications

- Agent sees memory at session start only
- Mid-session `memory add` → saved to disk, not in prompt
- Next session → new snapshot includes changes
- Tool responses always show live state

**Design rationale:** Preserves LLM prefix cache. Memory changes are relatively rare compared to conversation turns.

---

## Mirror to External Providers

When external memory provider active, built-in writes are mirrored via `on_memory_write()` hook. External provider may enrich, not replace, built-in memory.

---

## Agent-OS Relevance

Candidate pattern for `02_memory/`:
- Hard char limits force curation
- § delimiter enables structured entries
- Frozen snapshot = prompt cache optimization
- Substring matching for replace/remove (no full-text required)
