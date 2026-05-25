# Early Warning Signals

Human-readable — no dashboard required.

## Code Signals

- [ ] New file in `*/shared/` beyond path helper
- [ ] Abstract base class across workflows
- [ ] `import` between `minimal-demo.py` files
- [ ] Third-party orchestration lib in requirements
- [ ] `MAX_RETRIES` constant changed without doc
- [ ] `failure-modes.md` deleted or emptied

## Doc Signals

- [ ] README says "production-ready"
- [ ] "Temporary" bypass documented > 30 days
- [ ] Observability event renamed without mapping

## Trace Signals

- [ ] `task_completed` without verification event
- [ ] Shrinking audit JSONL for "noise reduction"
- [ ] Missing `escalation_triggered` at ceiling

## Social Signals

- "We'll add governance later"
- "Only internal users"
- "Metrics look fine"

## Action

Fill [change-proposals/change-template.md](../change-proposals/change-template.md) or rollback.
