# Safe Degradation

When components fail, system degrades to **safer** mode.

| Component fail | Safe degradation |
|----------------|------------------|
| Telegram API down | Mock deny / escalate |
| LLM timeout | Reject + escalate, no cache guess |
| SQLite locked | Fail-closed, no partial queue |
| FastAPI down | Store logic still valid offline |
| Human unavailable | Timeout deny |

## Not Degradation

Auto-approve when adapter unavailable — **autonomy drift**.

## Observability

Degradation events must be readable:

```
network failure → approval_timeout → unsafe_action_blocked
```
