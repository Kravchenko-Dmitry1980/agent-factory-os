# Memory as Crutch

## Definition

**Memory as crutch** is saving derivable codebase knowledge to long-term memory instead of reading live sources — producing stale parallel state and reduced grounding.

## Key Ideas

- Symptom: architecture decisions saved as memories; model stops reading code.
- Taxonomy excludes code patterns, git history, CLAUDE.md duplicates.
- Push back even when user asks to save raw lists — extract non-obvious insight only.

## Architecture Implications

- Four-type taxonomy as filter, not just label.
- CLAUDE.md for project instructions; MEMORY for non-derivable observations.
- Eval-gate save behavior (0/2 → 3/3 with override instruction).

## Production Implications

- Stale memory contradicts current code → user trust erosion.
- Periodic memory audit via human-readable files.

## Related Concepts

- [[memory-taxonomy]]
- [[long-term-memory]]

## Sources

- `Books/claude/ch11-memory.md`

## My Notes

