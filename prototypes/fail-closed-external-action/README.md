# Fail-Closed External Action

**Purpose:** Validate approval-before-action, external action governance, uncertainty handling.

## Flow

```
proposed action → verify → approval gate → execute OR deny
```

## Run

```powershell
python prototypes/fail-closed-external-action/minimal-demo.py
python prototypes/fail-closed-external-action/minimal-demo.py --scenario no-approval
python prototypes/fail-closed-external-action/minimal-demo.py --scenario uncertain
```

## Doctrine Links

- `Books/swarm-playbooks/patterns/approval-before-external-action.md`
- `agent-os/08_patterns/fail-closed-defaults.md`
