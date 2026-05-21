# Infinite Retry Loops

## Definition

An **infinite retry loop** anti-pattern occurs when error recovery, compaction, or stop hooks retry without hard limits — burning API budget in sessions stuck at context or permission boundaries.

## Key Ideas

- Observed: 250K API calls/day from auto-compact fail-retry cycles.
- Hook blocking + error injection adds tokens each cycle without progress.
- Resetting reactive compact guard on stop hook retry caused recurrence.

## Architecture Implications

- Circuit breakers required: auto-compact ×3, max-output recovery ×3, reactive compact once.
- Skip stop hooks on API error responses.
- Preserve `hasAttemptedReactiveCompact` across stop hook retries.

## Production Implications

- First production session without limits can exhaust budget overnight.
- Monitor consecutive compaction failures and recovery attempt counters.
- Alert on anomalous turns-per-session metrics.

## Related Concepts

- [[error-recovery-ladder]]
- [[withholding-errors]]
- [[stop-hooks]]

## Sources

- `Books/claude/ch05-agent-loop.md` — death spiral guards

## My Notes

