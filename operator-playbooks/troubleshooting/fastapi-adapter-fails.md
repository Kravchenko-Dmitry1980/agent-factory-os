# FastAPI Adapter Fails

## Symptom

Errors from `integrations-real/fastapi-review-api/minimal-demo.py`.

## Dependencies

```powershell
pip install fastapi uvicorn httpx
```

## Run

```powershell
python integrations-real/fastapi-review-api/minimal-demo.py --scenario happy
```

Demo may start local server briefly — read script output for port.

## Common issues

| Issue | Action |
|-------|--------|
| Port in use | Close other uvicorn; re-run |
| Module not found | Install deps above |
| SQLite path | Uses `.data/` — ensure writable |

## Fail scenarios

```powershell
python integrations-real/fastapi-review-api/minimal-demo.py --scenario reject
python integrations-real/fastapi-review-api/minimal-demo.py --scenario invalid-transition
```

## What NOT to do

- Deploy to cloud as "fix"
- Disable validation to pass demo

Reference: `integrations-real/fastapi-review-api/README.md`
