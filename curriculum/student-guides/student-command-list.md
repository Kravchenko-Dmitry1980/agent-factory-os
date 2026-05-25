# Student Command List

Run from: `C:\Dima\Projects\CURSOR\AGENT`

## First demos

```powershell
python prototypes/review-loop-agent/minimal-demo.py --scenario happy
python prototypes/review-loop-agent/minimal-demo.py --scenario bypass-attempt
python prototypes/fail-closed-external-action/minimal-demo.py --scenario no-approval
python prototypes/bounded-memory-agent/minimal-demo.py --scenario overflow
python prototypes/queue-orchestration/minimal-demo.py --scenario max-retries
python prototypes/gui-verification-loop/minimal-demo.py --scenario outcome-b
python prototypes/promotion-pipeline-simulator/minimal-demo.py --scenario reject
```

## Integrations

```powershell
python prototypes/integrations/escalation-workflow/minimal-demo.py --scenario retry-storm
python prototypes/integrations/review-queue-workflow/minimal-demo.py --scenario approval-denied
```

## Real adapters (mock)

```powershell
python integrations-real/llm-verification-adapter/minimal-demo.py --scenario malformed
python integrations-real/local-queue-worker/minimal-demo.py --scenario recovery
```

## Evaluation

```powershell
python evaluation/scripts/run_demo_smoke_checks.py
python evaluation/scripts/check_expected_text_traces.py
python evaluation/scripts/summarize_evaluation_status.py
```

Full lists: [../operator-playbooks/runbooks/](../operator-playbooks/runbooks/)

## Read traces (no command)

`observability/examples/*.txt`
