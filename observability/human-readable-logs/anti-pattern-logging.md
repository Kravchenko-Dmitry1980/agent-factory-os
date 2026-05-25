# Anti-Pattern Logging

| Anti-pattern | Symptom | Fix |
|--------------|---------|-----|
| **Metric obsession** | Dashboards green, users blocked | Add canonical events |
| **Telemetry spam** | Cannot find escalation in 10MB | Filter + severity |
| **Hidden states** | Internal enum not logged | Log transitions |
| **JSON soup** | One giant line per step | One fact per line |
| **Success-only logging** | Failures invisible | Log denies explicitly |
| **Critic silence** | No advisory flag | `advisory=true` |
| **LLM worship** | Log "model said X" as fact | Prefix untrusted |

## Stop Signal

Adding log aggregation pipeline before fixing log content — **platform drift**.

Fix messages first in prototypes/adapters.
