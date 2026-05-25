# Observability Examples

Human-readable trace files derived from repository workflows (Phases 2.0–2.2).

Format: [../workflow-tracing/minimal-trace-format.md](../workflow-tracing/minimal-trace-format.md)

| File | Scenario |
|------|----------|
| [successful-review-trace.txt](successful-review-trace.txt) | Happy path publish |
| [failed-review-trace.txt](failed-review-trace.txt) | Approval denied |
| [escalation-trace.txt](escalation-trace.txt) | Retry exhaustion |
| [malformed-llm-trace.txt](malformed-llm-trace.txt) | LLM parse fail |
| [unsafe-gui-action-trace.txt](unsafe-gui-action-trace.txt) | GUI mismatch block |
| [queue-recovery-trace.txt](queue-recovery-trace.txt) | Crash recovery |

No parser required — read as plain text.
