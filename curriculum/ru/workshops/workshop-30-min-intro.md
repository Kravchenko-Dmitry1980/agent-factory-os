# Воркшоп: ввод за 30 минут

## Аудитория

Новички, стейкхолдеры, первый день в репозитории.

## Длительность

30 минут

## Цель

Понять «лаборатория, не платформа» и увидеть один gate в действии.

## План

| Мин | Действие |
|-----|----------|
| 0–5 | [../README.md](../README.md) — что НЕ изучаем |
| 5–15 | Первое демо + bypass |
| 15–22 | Один файл из observability/examples |
| 22–28 | Smoke (кратко) |
| 28–30 | what-not-to-touch |

## Какие файлы открыть

- [../student-guides/student-start-here.md](../student-guides/student-start-here.md)
- [../../operator-playbooks/start-here/what-not-to-touch.md](../../operator-playbooks/start-here/what-not-to-touch.md)

## Какие команды запустить

```powershell
cd C:\Dima\Projects\CURSOR\AGENT
python prototypes/review-loop-agent/minimal-demo.py --scenario happy
python prototypes/review-loop-agent/minimal-demo.py --scenario bypass-attempt
python evaluation/scripts/run_demo_smoke_checks.py
```

## Вопросы для обсуждения

1. Где в выводе решение человека?
2. Почему bypass не опубликовал?
3. Чем это отличается от «чата с GPT»?

## Ожидаемый результат обучения

Участник называет 2 вещи, которыми проект не является, и один gate из trace.
