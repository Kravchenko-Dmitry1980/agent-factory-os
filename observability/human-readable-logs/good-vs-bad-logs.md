# Good vs Bad Logs

## Good

```
[gate] fail-closed: approval timeout — publish denied (fingerprint=5173f3ce)
[supervisor] escalated: high-risk action without human response
```

**Why:** Plain language, actor, reason, governance outcome.

## Bad

```
INFO: handler returned false
DEBUG: state=7 err=0xA3
metric: agent_step_total++ 
```

**Why:** Requires code archaeologist; metrics without story.

## Comparison Table

| Aspect | Good | Bad |
|--------|------|-----|
| Failure | Named gate + reason | Error code only |
| Retry | `retry=2 of 3` | Loop iteration log |
| Success | `task_completed verified=true` | `ok` |
| LLM | `LLM output != truth; format pass only` | Full model dump |
| Volume | ~10 lines per workflow | Thousands of DEBUG |

## Rule

If a new engineer cannot debug from logs alone in 15 minutes — rewrite logs, not add Grafana.
