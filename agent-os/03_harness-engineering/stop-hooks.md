# Stop Hooks

## Definition

**Stop hooks** are harness interceptors that run when the model completes a turn without requesting tools — challenging whether work is truly done and optionally forcing another loop iteration.

## Key Ideas

- Pipeline: job classification → background tasks → stop hooks → blocking errors → continue.
- `stopHookActive: true` on retry prevents re-running same hooks.
- `preventContinuation` → exit with `stop_hook_prevented`.
- Skipped when last message is API error (prevents hook→error loops).

## Architecture Implications

- Blocking errors appended as messages; loop continues with preserved reactive compact guard.
- Integrates with token budget check after successful stop hook pass.
- Background: prompt suggestion, memory extraction run concurrently.

## Production Implications

- Example: linter finds 3 errors after model declared done → hook forces fix turn.
- Misconfigured aggressive stop hooks burn API budget on low-value retries.
- Must coordinate with SDK consumers that treat any error as fatal.

## Related Concepts

- [[execution-verification]]
- [[verification]]
- [[query-loop]]

## Sources

- `Books/claude/ch05-agent-loop.md`

## My Notes

