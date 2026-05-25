# Trace Readability Rules

1. **One event per line** — no JSON blobs in trace body
2. **Canonical event names** — from event taxonomy
3. **Actor always present** — who is responsible
4. **Say what failed in plain language** — `reason=` field
5. **Terminal OUTCOME block** — never infer from last line
6. **No metric lines** — `counter++` forbidden in traces
7. **Timestamps optional** — relative order matters more
8. **≤ 25 lines** per example trace
9. **Escalation visible** — `escalation_triggered` must appear when automation stops
10. **Governance explicit** — `governance_rejection` not `error_code=403`

## Bad Trace (Anti-Example)

```
{"level":"info","msg":"done","t":171666"}
{"level":"debug","step":7,"ok":true}
```

## Good Trace

```
[19:56:59] approval_timeout     actor=gate     reason=deny-by-default
[19:56:59] unsafe_action_blocked actor=gate    action=publish
OUTCOME status=denied
GOVERNANCE gates_failed=1 escalated=yes
```
