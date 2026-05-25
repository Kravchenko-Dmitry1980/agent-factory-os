# Первые 30 минут (RU)

Точный маршрут для новичка или Дмитрия при первом входе.

**Время:** ~30 минут  
**Нужно:** PowerShell, Python 3, корень репозитория

---

## Минуты 0–5 — Контекст

1. Откройте [START_HERE_RU.md](../../START_HERE_RU.md)
2. Прочитайте [QUICKSTART_RU.md](../../QUICKSTART_RU.md) (разделы 1–2)
3. Запомните: **лаборатория, не фабрика**

---

## Минуты 5–15 — Первое демо

```powershell
cd C:\Dima\Projects\CURSOR\AGENT
python prototypes/review-loop-agent/minimal-demo.py --scenario happy
```

**Найдите в выводе:** Task, Critic, Human decision, Published, Audit.

Затем:

```powershell
python prototypes/review-loop-agent/minimal-demo.py --scenario bypass-attempt
```

**Убедитесь:** Published **False**.

---

## Минуты 15–22 — Evaluation

```powershell
python evaluation/scripts/run_demo_smoke_checks.py
```

Ожидание: `PASS=12 FAIL=0`.

---

## Минуты 22–27 — Один trace

Откройте файл:

`observability/examples/successful-review-trace.txt`

Прочитайте 5–7 строк: кто принял решение о публикации?

---

## Минуты 27–30 — Phase 3

Прочитайте [PHASE_3_WARNING_RU.md](../../PHASE_3_WARNING_RU.md) — что **нельзя** ожидать от следующей фазы.

---

## После 30 минут

| Дальше | Файл |
|--------|------|
| Курс | [curriculum/ru/course-map.md](../../curriculum/ru/course-map.md) |
| Шпаргалка | [CHEATSHEET.md](CHEATSHEET.md) |
| Упражнение | [curriculum/ru/exercises/exercise-run-first-demo.md](../../curriculum/ru/exercises/exercise-run-first-demo.md) |

EN полный маршрут (опционально): [../start-here/first-30-minutes.md](../start-here/first-30-minutes.md)
