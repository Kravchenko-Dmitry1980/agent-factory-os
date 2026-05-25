# Run Observability Examples

## Purpose

Read human-readable trace files — learn what correct governance looks like in logs.

## When to Use

- After running a demo (compare demo audit to example trace)
- When trace "doesn't look right"
- Teaching event vocabulary

## Commands

No runner — open text files:

```powershell
# PowerShell — open in default editor
notepad observability\examples\successful-review-trace.txt
notepad observability\examples\failed-review-trace.txt
notepad observability\examples\escalation-trace.txt
notepad observability\examples\malformed-llm-trace.txt
notepad observability\examples\unsafe-gui-action-trace.txt
notepad observability\examples\queue-recovery-trace.txt
```

Or read in Cursor/VS Code.

## Expected Result

Each file has:

- `TRACE id=...` header
- Timestamped events
- `OUTCOME status=...`
- `GOVERNANCE gates_passed=... escalated=...`

## Common Failures

| Symptom | Likely cause |
|---------|--------------|
| Demo audit doesn't match example | Different demo — map via canonical events doc |
| Can't find events | Read `observability/event-taxonomy/canonical-events.md` |

## What to Do If It Fails

[../troubleshooting/trace-does-not-match.md](../troubleshooting/trace-does-not-match.md)

## What NOT to Do

- Do not build trace parser platform
- Do not require metrics backend to understand failures

Supporting docs:

- `observability/workflow-tracing/minimal-trace-format.md`
- `observability/event-taxonomy/canonical-events.md`
- `evaluation/trace-comparison/good-trace-vs-bad-trace.md`
