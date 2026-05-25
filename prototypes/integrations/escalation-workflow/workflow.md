# Escalation — Workflow

1. **Task received**
2. **Execute** — mock worker produces result + confidence
3. **Uncertainty check** — low confidence → uncertain path
4. **Retry** — bounded attempts on recoverable failure
5. **Escalation** — human/supervisor when threshold hit
6. **Stop** — fail-closed terminal; no hidden continue

Escalation is success at governance, not demo failure.
