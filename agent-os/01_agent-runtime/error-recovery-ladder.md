# Error Recovery Ladder

## Definition

The **error recovery ladder** is the escalating sequence of interventions when API or context errors occur — withhold, collapse, reactive compact, output token escalation, multi-turn recovery — each with explicit limits.

## Key Ideas

- **Withhold** recoverable errors from yield stream until recovery fails.
- Prompt too long: context collapse drain → reactive compact → surface error.
- Max output tokens: 8K → 64K escalation → multi-turn recovery (max 3).
- Media size errors: reactive compact path.

## Architecture Implications

- Stop hooks skipped on error responses to prevent hook→retry→error loops.
- `hasAttemptedReactiveCompact` preserved across stop hook retries.
- Model fallback strips thinking signatures (model-bound) and tombstones failed messages.

## Production Implications

- SDK consumers disconnect on any error field — withholding is mandatory for recovery UX.
- Each guard added after production incident (documented in source comments).
- Orphan tool_result safety net in three code paths: crash, fallback, abort.

## Related Concepts

- [[withholding-errors]]
- [[infinite-retry-loops]]
- [[query-loop]]
- [[context-compression]]

## Sources

- `Books/claude/ch05-agent-loop.md`

## My Notes

