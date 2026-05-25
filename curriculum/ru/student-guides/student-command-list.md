# Список команд студента

Базовый каталог: `C:\Dima\Projects\CURSOR\AGENT`

## Первые демо

```powershell
cd C:\Dima\Projects\CURSOR\AGENT
python prototypes/review-loop-agent/minimal-demo.py --scenario happy
python prototypes/review-loop-agent/minimal-demo.py --scenario bypass-attempt
python prototypes/review-loop-agent/minimal-demo.py --scenario uncertain-critic
```

## Fail-closed и approval

```powershell
python prototypes/fail-closed-external-action/minimal-demo.py --scenario no-approval
python prototypes/fail-closed-external-action/minimal-demo.py --scenario approved
python prototypes/fail-closed-external-action/minimal-demo.py --scenario rejected
```

## Память и очередь

```powershell
python prototypes/bounded-memory-agent/minimal-demo.py --scenario overflow
python prototypes/queue-orchestration/minimal-demo.py --scenario max-retries
python prototypes/integrations/escalation-workflow/minimal-demo.py --scenario retry-storm
```

## Интеграции (mock)

```powershell
python integrations-real/llm-verification-adapter/minimal-demo.py --scenario malformed
python integrations-real/llm-verification-adapter/minimal-demo.py --scenario happy
python integrations-real/filesystem-audit-log/minimal-demo.py --scenario happy
```

## Evaluation

```powershell
python evaluation/scripts/run_demo_smoke_checks.py
python evaluation/scripts/check_expected_text_traces.py
python evaluation/scripts/summarize_evaluation_status.py
```

Полный runbook: [../../operator-playbooks/runbooks/run-prototypes.md](../../operator-playbooks/runbooks/run-prototypes.md)
