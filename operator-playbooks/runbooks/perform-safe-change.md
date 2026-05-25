# Perform Safe Change

## Purpose

Change workflow behavior without silently breaking governance gates.

## When to Use

Any edit to `prototypes/`, `prototypes/shared/`, `integrations-real/`, or shared gates.

## Commands

### 1. Before change

```powershell
python evaluation/scripts/run_demo_smoke_checks.py
```

Document baseline (optional): copy demo output to local notes.

### 2. Write proposal

Use template: `evolution/change-proposals/change-template.md`

Guide: [../change-guides/how-to-write-change-proposal.md](../change-guides/how-to-write-change-proposal.md)

### 3. Make small change

One invariant at a time. Avoid drive-by refactors.

### 4. After change

```powershell
python evaluation/scripts/run_demo_smoke_checks.py
python evaluation/scripts/check_expected_text_traces.py
```

Run affected scenarios from `evaluation/scenarios/`.

### 5. Quality gates

Checklist: `evaluation/quality-gates/quality-gate-checklist.md`

Operator checklist: [../operator-checklists/after-changing-workflow.md](../operator-checklists/after-changing-workflow.md)

## Expected Result

- Smoke PASS (or explained intentional change to scenarios)
- Trace still shows gate chain
- Change proposal answers "which gate moves?"

## Common Failures

- Smoke FAIL on fail-closed path → likely regression
- Fewer audit events → observability regression

## What to Do If It Fails

[rollback-after-failure.md](rollback-after-failure.md)

## What NOT to Do

- Large refactor + behavior change in one commit
- Skip evaluation "because docs only" when code touched
- Auto-approve to fix failing demo

Full guide: [../change-guides/how-to-change-safely.md](../change-guides/how-to-change-safely.md)
