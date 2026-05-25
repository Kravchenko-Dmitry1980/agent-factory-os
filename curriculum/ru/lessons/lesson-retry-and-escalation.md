# Урок: Повторы и эскалация

## Что это?

**Bounded retry** — ограниченное число повторов; при исчерпании — **escalation** (передача человеку или отдельному пути), с записью в trace.

## Почему это важно?

Бесконечные retry маскируют баги, жгут бюджет и скрывают нужду в человеке.

## Что может пойти не так?

- Retry storm без эскалации
- Увеличение MAX_RETRIES без proposal
- Эскалация без события в trace

## Как это проверить?

Прочитайте `observability/examples/escalation-trace.txt`, затем запустите retry-storm.

```powershell
python prototypes/integrations/escalation-workflow/minimal-demo.py --scenario retry-storm
python prototypes/queue-orchestration/minimal-demo.py --scenario max-retries
```

## Какое демо это показывает?

- escalation-workflow
- queue-orchestration
