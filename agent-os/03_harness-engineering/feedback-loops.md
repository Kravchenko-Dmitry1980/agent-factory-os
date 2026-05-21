# Feedback Loops

## Definition

**Feedback loops** in harness engineering are cycles where execution outcomes inform subsequent behavior — stop hook retries, memory writes, classifier training signals, and episodic feedback memories.

## Key Ideas

- Stop hook blocking errors = immediate in-session feedback to model.
- Feedback memories capture validated rules with Why/How structure.
- Auto-mode classifier uses transcript + tool input compact representation.
- Cost/token histograms (reservoir sampling) feed operational feedback.

## Architecture Implications

- Centralized `onChangeAppState` syncs permission mode across 8+ mutation paths.
- Memory write uses same File tools — feedback loop through standard harness.
- Diminishing returns detection on token budget continuations.

## Production Implications

- Recording only corrections (not confirmations) causes behavioral drift.
- Scattered permission sync broke 6 of 8 paths before centralization.
- Telemetry on tool errors must avoid logging secrets or raw adversarial input.

## Related Concepts

- [[execution-verification]]
- [[episodic-memory]]
- [[adaptive-harness]]

## Sources

- `Books/claude/ch03-state.md`
- `Books/claude/ch05-agent-loop.md`
- `Books/claude/ch11-memory.md`

## My Notes

