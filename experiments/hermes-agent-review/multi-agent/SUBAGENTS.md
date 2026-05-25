# Subagents — Detailed Reference

**Code:** `tools/delegate_tool.py` (~2800 lines)  
**Docs:** `website/docs/user-guide/features/delegation.md`

---

## Subagent Model

Each subagent is a **full AIAgent instance** with:
- Fresh conversation (zero parent history)
- Focused system prompt from goal + context
- Restricted toolset
- Own terminal session
- Own session ID (linked to parent)
- Summary-only return to parent

---

## Blocked in Subagents

| Tool/Action | Reason |
|-------------|--------|
| `delegate_task` | No recursive delegation |
| `memory` write | Prevent memory corruption |
| `clarify` | Must work with given context |
| `send_message` | No gateway side effects |

Parent sees only final summary — not intermediate tool calls.

---

## Context Passing

```python
# BAD — subagent has no context
delegate_task(goal="Fix the error")

# GOOD — complete context
delegate_task(
    goal="Fix TypeError in api/handlers.py",
    context="""File: api/handlers.py line 47
    Error: 'NoneType' object has no attribute 'get'
    Function process_request() receives dict from parse_body()
    parse_body() returns None when Content-Type missing
    Project: /home/user/myproject, Python 3.11"""
)
```

---

## Toolset Selection

| Pattern | Use Case |
|---------|----------|
| `["web"]` | Research, no local access |
| `["terminal", "file"]` | Code changes, local ops |
| `["file"]` | Read-only analysis |
| `["terminal"]` | Command execution only |

Subagents inherit parent's terminal backend unless overridden.

---

## Parallel Execution

```yaml
delegation:
  max_concurrent_children: 3  # Default, configurable
```

- ThreadPoolExecutor with configured limit
- Batches > limit return error (not silently truncated)
- CLI: tree-view progress display
- Gateway: batched progress relay
- Interrupt parent → interrupts all children

---

## Memory Integration

```python
# MemoryProvider.on_delegation(task, result)
# Parent-side observation of subagent work
# External providers may extract learnings
```

Subagents tagged `agent_context: subagent` — providers skip writes.

---

## Comparison with Claude Code Subagents

| Aspect | Claude Code | Hermes |
|--------|-------------|--------|
| Spawn | Task tool | delegate_task |
| Context | Fresh + task description | Fresh + goal + context |
| Return | Result message | Structured summary |
| Parallel | Multiple tasks | Batch mode (max 3 default) |
| Model | Same as parent | Configurable override |
| Restrictions | Tool allowlist | Blocked tools list |

---

## Agent-OS Relevance

Maps to `04_multi-agent/subagents.md`:
- Fresh context invariant
- Summary-only return
- Tool restrictions for safety
- Parallel batch with concurrency limit
