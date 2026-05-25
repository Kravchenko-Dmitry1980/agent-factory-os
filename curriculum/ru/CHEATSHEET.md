# Шпаргалка студента (RU)

Одна страница. Полный курс: [README.md](README.md)

---

## Первый маршрут

1. [../../START_HERE_RU.md](../../START_HERE_RU.md)
2. [student-guides/student-start-here.md](student-guides/student-start-here.md)
3. [../../QUICKSTART_RU.md](../../QUICKSTART_RU.md)
4. [course-map.md](course-map.md) — уровень 0

---

## Ключевые термины

| Термин | Коротко |
|--------|---------|
| fail-closed | Сомнение → стоп |
| trace | След решений в логе |
| critic | Не проверка фактов |
| verification | Проверка до доверия |
| human approval | Явное «да» человека |
| platform drift | «Платформа» вместо уроков |
| rollback | Откат изменения |

Глоссарий: [student-guides/student-glossary.md](student-guides/student-glossary.md)

---

## Первые команды

```powershell
cd C:\Dima\Projects\CURSOR\AGENT
python prototypes/review-loop-agent/minimal-demo.py --scenario happy
python evaluation/scripts/run_demo_smoke_checks.py
```

---

## Навыки до Phase 3

- [ ] happy + bypass demos
- [ ] read one trace
- [ ] smoke PASS
- [ ] объяснить fail-closed, critic, LLM (своими словами)
- [ ] прочитать [../../PHASE_3_WARNING_RU.md](../../PHASE_3_WARNING_RU.md)

Критерии: [methodology/phase-3-entry-criteria.md](methodology/phase-3-entry-criteria.md)

---

## Опасные признаки

- «Критик сказал OK — публикуем»
- «LLM вернул JSON — значит верно»
- «Уберём человека — быстрее»
- «Соберём все демо в один runtime»
- «Phase 3 = фабрика готова»

Оператор: [../../operator-playbooks/ru/CHEATSHEET.md](../../operator-playbooks/ru/CHEATSHEET.md)
