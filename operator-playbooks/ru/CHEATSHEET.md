# Шпаргалка оператора (RU)

Одна страница. Команды — из корня `C:\Dima\Projects\CURSOR\AGENT`.

---

## Главные команды

```powershell
cd C:\Dima\Projects\CURSOR\AGENT

# Первое демо
python prototypes/review-loop-agent/minimal-demo.py --scenario happy
python prototypes/review-loop-agent/minimal-demo.py --scenario bypass-attempt

# Evaluation
python evaluation/scripts/run_demo_smoke_checks.py
python evaluation/scripts/check_expected_text_traces.py
python evaluation/scripts/summarize_evaluation_status.py
```

---

## Что смотреть в выводе

| Сигнал | Значение |
|--------|----------|
| **PASS / FAIL** | Результат smoke или trace check |
| **Published True/False** | Разрешена ли публикация |
| **Human decision** | Решение человека |
| **Critic** | Оценка черновика — **не факты** |
| **Audit** | След решений (lineage) |
| **approval / deny** | Gate одобрения |
| **escalation** | Передача человеку после retry |
| **fail-closed** | Сомнение → стоп |

---

## Что делать при FAIL

1. **Стоп** — не «чинить» снятием approval.
2. Прочитать **trace** / audit в выводе.
3. Сравнить с `evaluation/expected-outcomes/`.
4. Если после изменения — **rollback**, не слепой patch.
5. Записать в learning log (curriculum RU).

Подробно: [ERRORS.md](ERRORS.md)

---

## Что нельзя делать

- auto-approve по таймауту
- убрать human review «для скорости»
- игнорировать evaluation FAIL
- объединить демо в **shared runtime**
- объявить Phase 3 / фабрику без [PHASE_3_START_CONDITIONS.md](../../governance/PHASE_3_START_CONDITIONS.md)
