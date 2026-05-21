# Self-Revision

## Definition

**Self-revision** is an agent's ability to update its own persistent state — memories, preferences, and behavioral rules — through harness-approved writes without external retraining.

## Key Ideas

- Model writes memories via standard file tools under system prompt protocol.
- Feedback memories capture corrected and confirmed behavioral rules.
- Memory taxonomy prevents saving derivable code knowledge as false permanence.
- Stop hooks and verification agents provide external correction loop.

## Architecture Implications

- No separate memory API — self-revision emerges from tool + instruction design.
- Consolidation pass merges redundant self-written files.
- User override always possible via direct file edit.

## Production Implications

- Ungoverned self-revision → stale or adversarial memory pollution.
- Eval-gated pushback on bad save requests reduces noise.
- Pair self-revision with human-readable storage for auditability.

## Related Concepts

- [[evolving-memory]]
- [[feedback-loops]]
- [[episodic-memory]]

## Sources

- `Books/claude/ch11-memory.md`

## My Notes

