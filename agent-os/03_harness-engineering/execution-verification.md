# Execution Verification

## Definition

**Execution verification** is harness-level checking that tool outcomes and claimed task completion satisfy constraints — via stop hooks, verification agents, linters, and classifiers — before accepting loop termination.

## Key Ideas

- Stop hooks evaluate "done" claims when model emits no further tool_use.
- Blocking errors appended to history force another loop iteration.
- Verification agent: adversarial read/test focused subagent type.
- Template job classification runs before stop hook execution.

## Architecture Implications

- `stopHookActive` prevents re-entry to stop hooks on forced retry.
- `preventContinuation` → terminal `stop_hook_prevented`.
- Background tasks (prompt suggestion, memory extraction) fire alongside stop hooks.

## Production Implications

- Hook blocking + error injection can inflate tokens each cycle — guard against loops.
- Verification agent cost traded for correctness on high-stakes tasks.
- Auto mode must not auto-approve operations that bypass verification intent.

## Related Concepts

- [[verification]]
- [[stop-hooks]]
- [[feedback-loops]]
- [[subagents]]
- [[visual-verification]]
- [[fail-closed-agent-loop]]

## Related Anti-patterns

- [[infinite-retry-loops]]
- [[unverified-gui-clicks]]

## Related Patterns

- [[fail-closed-agent-loop]]
- [[verification-before-writeback]]

## Upstream Sources

- `Books/claude/ch05-agent-loop.md`
- `Books/claude/ch08-sub-agents.md`

## Governance References

- `governance/SEMANTIC_LINKING_AUDIT.md`

## Semantic Cluster

verification

## Sources

- `Books/claude/ch05-agent-loop.md`
- `Books/claude/ch08-sub-agents.md`

## My Notes

