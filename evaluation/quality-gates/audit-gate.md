# Audit Gate

**Question:** Did audit log still record why decisions happened?

---

## Checks

- [ ] Every gate produces auditable event
- [ ] Deny paths have reason strings
- [ ] Actor attribution present (human, critic, gate)
- [ ] OUTCOME/GOVERNANCE summary readable
- [ ] Append-only — no event deletion in code path
- [ ] Trace compare script passes on examples

## Commands

```powershell
python evaluation/scripts/check_expected_text_traces.py
python integrations-real/filesystem-audit-log/minimal-demo.py
```

## Pass

- Example traces contain required events
- Demo audit dumps ≥ prior event count for same scenario
- filesystem audit appends without overwrite

## Fail

- Generic "error" replaces gate events
- Missing actor on critical decisions
- Audit thinned after refactor

## Cross-check

`observability/human-readable-logs/good-vs-bad-logs.md`
