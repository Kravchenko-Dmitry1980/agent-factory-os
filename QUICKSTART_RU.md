# Быстрый старт (RU)

Одна страница — проверить, что лаборатория работает на вашей машине.

---

## 1. Быстрый запуск

```powershell
cd C:\Dima\Projects\CURSOR\AGENT
python prototypes/review-loop-agent/minimal-demo.py --scenario happy
python evaluation/scripts/run_demo_smoke_checks.py
```

---

## 2. Что должно произойти

| Действие | Ожидание |
|----------|----------|
| Demo `happy` | Безопасный сценарий review: критик → человек → публикация разрешена |
| Smoke | В конце: `PASS=12 FAIL=0` (все проверки демо прошли) |
| Внешние сервисы | **Не нужны** — mock/local по умолчанию |

Дополнительно (2 мин):

```powershell
python prototypes/review-loop-agent/minimal-demo.py --scenario bypass-attempt
```

Должно быть **Published False** — это учебный fail-closed.

---

## 3. Если не работает

| Проверка | Действие |
|----------|----------|
| Python | `python --version` (нужен Python 3.x) |
| Папка | Вы в `C:\Dima\Projects\CURSOR\AGENT` |
| Путь к скрипту | Команды как выше, без сокращений |
| Корень проекта | Не запускайте из `prototypes/` как cwd |

Подробно: [operator-playbooks/ru/ERRORS.md](operator-playbooks/ru/ERRORS.md)

---

## 4. Что читать дальше

| Файл | Тема |
|------|------|
| [curriculum/ru/course-map.md](curriculum/ru/course-map.md) | Уровни 0–10 |
| [operator-playbooks/ru/FIRST_30_MINUTES.md](operator-playbooks/ru/FIRST_30_MINUTES.md) | Первые 30 минут |
| `agent-os/doctrine/system-positioning.md` | Позиционирование системы |
| [governance/phase-2-8/FINAL_PHASE_2_8_REPORT.md](governance/phase-2-8/FINAL_PHASE_2_8_REPORT.md) | Вердикт Phase 2.8 |

---

## 5. Главные правила

1. **AI может ошибаться** — правдоподобно и уверенно.
2. **Вывод LLM ≠ правда** — нужна verification.
3. **Критик ≠ истина** — PASS критика не заменяет факты.
4. **Если сомневаемся — стоп** (fail-closed).
5. **Опасное действие требует человека** (human approval).
6. **Не строим платформу раньше времени** — сначала один безопасный workflow.

Предупреждение Phase 3: [PHASE_3_WARNING_RU.md](PHASE_3_WARNING_RU.md)
