# Readability-First Policy

## Priority Order

1. Can a human read the trace?
2. Does it answer which gate failed?
3. Is escalation visible?
4. Is governance rejection explicit?
5. (Last) Is it machine-parseable?

## Format Choices

- Plain text traces over JSON logs for examples
- Canonical event names over vendor codes
- `reason=` in prose over errno
- Terminal `OUTCOME` block mandatory in examples

## Volume

One workflow run ≈ one screen of logs (≤ 25 lines in examples).

## Anti-Noise

Drop DEBUG from default educational traces. Demos may verbose-print audit — label as demo mode in postmortem docs.

## Review Question

> Would an auditor understand this without training on our metrics system?

Must be yes.
