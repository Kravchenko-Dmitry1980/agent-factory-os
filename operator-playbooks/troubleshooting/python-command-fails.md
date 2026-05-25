# Python Command Fails

## Symptom

`'python' is not recognized` or wrong Python version.

## Fix

```powershell
python --version
# Need 3.10+ (3.12 recommended)

py --version
py -3.12 prototypes/review-loop-agent/minimal-demo.py --scenario happy
```

Install Python 3.12+ from python.org if missing. Check "Add to PATH" on Windows.

## Still fails?

- Restart terminal after install
- Use full path to python.exe
- In VS Code/Cursor: select correct interpreter

## What NOT to do

- Do not rewrite demos for Node.js
- Do not dockerize as first fix
