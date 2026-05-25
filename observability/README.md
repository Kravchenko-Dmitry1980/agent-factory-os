# Observability & Failure Intelligence (Phase 2.3)

**Status:** Human-readable diagnostics — not a monitoring platform.

---

## Why Observability Matters

Governed AI workflows can **pass unit logic** and still fail invisibly:

- Critic approves hallucinations
- Queue retries mask root cause
- Memory writes look successful but snapshot is stale
- Approval timeouts feel like "slow UX" not governance events

Without visibility, teams optimize latency while **autonomy leaks**.

---

## Why AI Systems Fail Invisibly

| Invisible failure | What operators see |
|-------------------|-------------------|
| Verification bypass | "It finished" |
| Retry storm | "High activity" |
| Uncertain LLM output accepted | "Model responded" |
| Stale frozen snapshot | "Agent forgot" |
| Escalation never fired | "Stuck task" |

AI failures are often **semantic**, not exceptions. Exceptions are the easy part.

---

## Why Human-Readable Traces Matter

Distributed tracing answers: *where did time go?*

Governed agent observability must answer:

- **Which gate failed?**
- **Was escalation correct?**
- **Was autonomy blocked?**
- **What did the human see?**

Text-first traces in this layer are **explainable in a postmortem** without dashboard access.

---

## Monitoring Platforms Are Intentionally Forbidden

Phase 2.3 does **not** add:

- Prometheus / Grafana
- OpenTelemetry collectors
- Metrics databases
- Event streaming
- Dashboard templates

Those teach **infra**, not **governance visibility**.

See [governance/anti-monitoring-platform-rules.md](governance/anti-monitoring-platform-rules.md).

---

## Governance Visibility Is Critical

Observability must expose:

- Fail-closed denials
- Escalation triggers
- Approval boundaries
- Governance rejections
- Unsafe action blocks

If logs cannot answer "was autonomy prevented?" — observability failed.

---

## Structure

| Module | Purpose |
|--------|---------|
| [event-taxonomy/](event-taxonomy/) | Canonical workflow events |
| [workflow-tracing/](workflow-tracing/) | Readable trace formats |
| [escalation-intelligence/](escalation-intelligence/) | Why escalation happens |
| [verification-failures/](verification-failures/) | Verification & critic limits |
| [memory-failures/](memory-failures/) | Drift, overload, writeback |
| [queue-failures/](queue-failures/) | Retries, dead queues |
| [audit-lineage/](audit-lineage/) | Append-only lineage |
| [human-readable-logs/](human-readable-logs/) | Good vs bad logging |
| [examples/](examples/) | Sample traces |
| [diagrams/](diagrams/) | Mermaid views |
| [governance/](governance/) | Boundaries |

---

## Relation to Repository Layers

```
prototypes/           → demos emit audit events
integrations-real/    → real I/O failures (timeout, malformed)
observability/        → how to READ those failures
agent-os/doctrine/    → why gates exist
governance/           → promotion & policy
```

Optional: read JSONL from `integrations-real/.data/` manually — no parser platform required.

---

## Navigation

1. [event-taxonomy/canonical-events.md](event-taxonomy/canonical-events.md)
2. [workflow-tracing/minimal-trace-format.md](workflow-tracing/minimal-trace-format.md)
3. [examples/](examples/)
4. [governance/observability-boundaries.md](governance/observability-boundaries.md)
