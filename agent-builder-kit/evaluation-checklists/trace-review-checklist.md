# Trace Review Checklist

Use when reviewing expected or example traces.

## Completeness

- [ ] `task_started` with task id / goal
- [ ] All gates emit pass or fail
- [ ] `approval_requested` before publish (if applicable)
- [ ] Terminal: `task_completed` or `task_failed`
- [ ] OUTCOME summary present

## Semantics

- [ ] Critic marked `advisory=true` if used
- [ ] Human decision explicit
- [ ] Block events have reasons
- [ ] No publish event before approval

## Operability

- [ ] Readable in under 2 minutes
- [ ] Actor names consistent
- [ ] Timestamps optional but ordered
- [ ] Gate pass/fail counts in summary

## Anti-patterns in trace

- [ ] No "Done." only traces
- [ ] No missing human gate on happy path
- [ ] No critic pass without advisory flag

Reference: [observability-trace-spec.md](../template-specs/observability-trace-spec.md)
