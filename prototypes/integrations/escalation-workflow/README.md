# Escalation Workflow

**Purpose:** Human escalation, fail-closed stop, retry ceiling, uncertainty routing.

## Flow

```
task → execution → uncertainty → retry → escalation → stop
```

## Run

```powershell
python prototypes/integrations/escalation-workflow/minimal-demo.py
python prototypes/integrations/escalation-workflow/minimal-demo.py --scenario retry-storm
python prototypes/integrations/escalation-workflow/minimal-demo.py --scenario immediate-uncertainty
```
