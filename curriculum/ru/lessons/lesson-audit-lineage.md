# Урок: Аудит и lineage

## Что это?

**Audit lineage** — дополняемая история решений: кто, какой gate, исход, почему (append-only по смыслу).

## Почему это важно?

Без lineage нельзя разбор инцидента, compliance и доверие к deny.

## Что может пойти не так?

- Тонкий лог «error occurred»
- Удаление событий после рефакторинга
- Нет атрибуции актора

## Как это проверить?

Каждый deny path имеет именованный gate + reason. Сравните good vs bad trace.

`evaluation/trace-comparison/good-trace-vs-bad-trace.md`

```powershell
python integrations-real/filesystem-audit-log/minimal-demo.py --scenario happy
```

## Какое демо это показывает?

- Все prototypes (секция Audit)
- filesystem-audit-log adapter
- `observability/examples/*.txt`
