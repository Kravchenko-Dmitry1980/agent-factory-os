# Demo Does Not Run

## Symptom

Traceback, import error, or immediate exit non-zero.

## Checklist

- [ ] Running from repo root: `C:\Dima\Projects\CURSOR\AGENT`
- [ ] Correct path in command (`prototypes/...` not `prototype/...`)
- [ ] Valid `--scenario` — open `minimal-demo.py` and read `choices=[...]`
- [ ] No half-edited file if you were changing code

## Common: ModuleNotFoundError: prototypes

**Cause:** Wrong working directory.

```powershell
cd C:\Dima\Projects\CURSOR\AGENT
python prototypes/review-loop-agent/minimal-demo.py --scenario happy
```

## Common: Import error in shared module

**Cause:** Recent change to `prototypes/shared/`.

**Action:** Rollback shared change; run smoke on all demos.

## FastAPI adapter only

```powershell
pip install fastapi uvicorn httpx
```

## What NOT to do

- pip install langchain/langgraph to fix governance demos
- Comment out imports to "make it run"

See [../runbooks/run-prototypes.md](../runbooks/run-prototypes.md)
