# Terminal States

## Definition

**Terminal states** are the typed reasons the query loop exits — a discriminated union returned from the async generator, not an implicit "done" event.

## Key Ideas

| Reason | Trigger |
|--------|---------|
| `completed` | Normal finish, budget exhausted, or API error surfaced |
| `aborted_streaming` | User abort during model stream |
| `aborted_tools` | User abort during tool execution |
| `blocking_limit` | Hard token limit, auto-compact off |
| `prompt_too_long` | 413 after recovery exhausted |
| `max_turns` | Turn limit hit |
| `stop_hook_prevented` | Stop hook blocked continuation |
| `hook_stopped` | PreToolUse stopped execution |
| `model_error` | Unrecoverable API failure |
| `image_error` | Unrecoverable media error |

## Architecture Implications

- Continue reasons (`next_turn`, `reactive_compact_retry`, etc.) separate from terminals.
- Generator return value gives callers typed termination without event subscription.
- Tests assert on `transition.reason` at continue sites.

## Production Implications

- Telemetry and UX depend on precise terminal reason — not generic "error".
- Subagents always stop on token budget (no continuation nudge).

## Related Concepts

- [[query-loop]]
- [[execution-loops]]
- [[stop-hooks]]

## Sources

- `Books/claude/ch05-agent-loop.md`

## My Notes

