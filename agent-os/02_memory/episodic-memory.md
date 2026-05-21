# Episodic Memory

## Definition

**Episodic memory** captures session-specific events and corrections — especially **feedback** memories recording validated approaches and past incidents that shaped rules.

## Key Ideas

- Feedback type structure: rule + **Why** + **How to apply**.
- Record both corrections AND confirmations to avoid drift from validated approaches.
- KAIROS daily logs (`logs/YYYY/MM/`) as optional episodic trail when feature enabled.
- Session transcripts are ephemeral; episodic memory extracts durable observations.

## Architecture Implications

- Write path: create `.md` file → update `MEMORY.md` index pointer.
- Updates use FileEdit on existing file — no internal versioning.
- `.consolidate-lock` mtime tracks last consolidation.

## Production Implications

- Without episodic feedback capture, same mistakes repeat every Monday.
- Ephemeral task details explicitly excluded from memory taxonomy.
- Consolidation prevents unbounded file proliferation.

## Related Concepts

- [[semantic-memory]]
- [[feedback-loops]]
- [[long-term-memory]]

## Sources

- `Books/claude/ch11-memory.md`

## My Notes

