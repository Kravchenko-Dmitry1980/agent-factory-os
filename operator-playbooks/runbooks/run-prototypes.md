# Run Prototypes

## Purpose

Run core reference demos (Phase 2.0) that teach governance in ~200 lines each.

## When to Use

- First day onboarding
- After changing any file under `prototypes/`
- Before explaining a pattern to a teammate

## Commands

From repository root (`C:\Dima\Projects\CURSOR\AGENT`):

```powershell
python prototypes/review-loop-agent/minimal-demo.py --scenario happy
python prototypes/bounded-memory-agent/minimal-demo.py --scenario happy
python prototypes/queue-orchestration/minimal-demo.py --scenario happy
python prototypes/fail-closed-external-action/minimal-demo.py --scenario approved
python prototypes/gui-verification-loop/minimal-demo.py --scenario happy
python prototypes/promotion-pipeline-simulator/minimal-demo.py --scenario promote
```

Fail-path spot checks:

```powershell
python prototypes/review-loop-agent/minimal-demo.py --scenario bypass-attempt
python prototypes/fail-closed-external-action/minimal-demo.py --scenario no-approval
python prototypes/bounded-memory-agent/minimal-demo.py --scenario overflow
python prototypes/queue-orchestration/minimal-demo.py --scenario max-retries
python prototypes/gui-verification-loop/minimal-demo.py --scenario outcome-b
python prototypes/promotion-pipeline-simulator/minimal-demo.py --scenario reject
```

## Expected Result

- Exit code 0
- Printed audit section at end
- Fail scenarios show block/deny (not crash)

## Common Failures

| Symptom | Likely cause |
|---------|--------------|
| `python` not found | Python not installed or not on PATH |
| `ModuleNotFoundError: prototypes` | Not running from repo root |
| Wrong scenario | Check `--scenario` choices in demo's `minimal-demo.py` |

## What to Do If It Fails

1. [../troubleshooting/python-command-fails.md](../troubleshooting/python-command-fails.md)
2. [../troubleshooting/demo-does-not-run.md](../troubleshooting/demo-does-not-run.md)
3. Do not patch shared code until cause is understood

## What NOT to Do

- Do not pip-install heavy frameworks to "fix" demos
- Do not skip audit reading
- Do not merge demos into one runner script

Reference: [../../prototypes/README.md](../../prototypes/README.md)
