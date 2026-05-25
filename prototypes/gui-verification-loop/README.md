# GUI Verification Loop

**Purpose:** Validate visual verification, GUI action risks, unverified-click prevention.

**No real ADB/emulator** — mocked screenshots and synthetic states only.

## Flow

```
observe → plan → proposed click → visual verify → execute OR reject
```

## Run

```powershell
python prototypes/gui-verification-loop/minimal-demo.py
python prototypes/gui-verification-loop/minimal-demo.py --scenario outcome-b
python prototypes/gui-verification-loop/minimal-demo.py --scenario outcome-c
```

## Doctrine Links

- `agent-os/00_foundations/visual-verification.md`
- `agent-os/09_antipatterns/unverified-gui-clicks.md`
