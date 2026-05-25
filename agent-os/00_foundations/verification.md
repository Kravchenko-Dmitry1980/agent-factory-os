# Verification

## Definition

**Verification** in agent systems is the practice of checking whether claimed completion matches reality — via hooks, classifiers, linters, tests, or dedicated verification subagents — before accepting loop termination.

## Key Ideas

- Models often declare completion prematurely; harness must **challenge the done state**.
- Stop hooks append blocking errors and force another loop iteration with `stopHookActive: true`.
- Dedicated **verification agent** type runs adversarial checks (tests, lint) in isolation.
- Verification is separated from execution to avoid polluting main conversation context.

## Architecture Implications

- Stop hook pipeline: classify job → background tasks → execute hooks → blocking errors → continue loop.
- `preventContinuation` from stop hooks yields terminal state `stop_hook_prevented`.
- Verification agents get constrained tool pools and permission modes suited to read/test workloads.

## Production Implications

- Re-running stop hooks on retry causes infinite hook→error loops — guard with `stopHookActive`.
- Verification cost is traded against user trust and reduced rework in later sessions.
- Classifier-based auto-approval must not bypass verification-critical mutations.

## Related Concepts

- [[execution-verification]]
- [[visual-verification]]
- [[stop-hooks]]
- [[subagents]]
- [[feedback-loops]]
- [[fail-closed-agent-loop]]

## Related Anti-patterns

- [[unverified-gui-clicks]]
- [[infinite-retry-loops]]

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

- `Books/claude/ch05-agent-loop.md` — stop hooks
- `Books/claude/ch08-sub-agents.md` — verification agent type

## My Notes

