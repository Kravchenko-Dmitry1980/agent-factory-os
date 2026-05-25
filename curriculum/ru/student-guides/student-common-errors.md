# Типичные ошибки студента

| Симптом | Частая причина | Что сделать |
|---------|----------------|-------------|
| python не найден | PATH / venv | Проверить `python --version` |
| ModuleNotFoundError | Не тот каталог | `cd C:\Dima\Projects\CURSOR\AGENT` |
| «Всё прошло» но Published False | Fail-closed | Прочитать audit, не exit code |
| Smoke FAIL | Регрессия или окружение | Текст FAIL; наставник |
| Не вижу trace | Смотрите audit section / examples | exercise-read-trace |
| Хочу --real | Рано | mock по policy |

## Ошибки мышления

- Доверие критику
- Пропуск human «внутри компании»
- Объединение всех демо в один скрипт

## Куда за помощью

1. [student-glossary.md](student-glossary.md)
2. [../../operator-playbooks/troubleshooting/common-errors.md](../../operator-playbooks/troubleshooting/common-errors.md)
3. Наставнику — с выводом команды и 5 строками audit
