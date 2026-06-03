# Политика сохранения transcript (RU)

**Phase 3.5.2** — когда и что сохраняет Demo Runner.

---

## По умолчанию

**Transcript не сохраняется.** Runner только печатает результат в консоль.

---

## Когда сохраняется

Только при явном флаге:

```powershell
python demos/review-assistant-runner/demo_runner.py --scenario happy --save-transcript
```

Папка: `demos/review-assistant-runner/transcripts/`

Имя файла: `YYYYMMDD_HHMMSS_<scenario>.md`

---

## Что входит в transcript

| Поле | Сохраняется |
|------|-------------|
| Timestamp | да |
| Scenario key и title | да |
| Command (без env) | да |
| Raw stdout | да |
| Parsed decision | да |
| Parsed trace events | да |
| Russian summary | да |
| Safety status | да |

---

## Что НЕ сохраняется

| Данные | Причина |
|--------|---------|
| Environment variables | Могут содержать secrets |
| `RA_LLM_BASE_URL` value | Не логировать endpoint config |
| API keys / tokens | Secret safety |
| Auth headers | Secret safety |
| stderr с secrets | Не включать |

Для real provider scenario сохраняется только ключ сценария (`real_provider_synthetic`), без URL провайдера.

---

## Удаление transcripts

Transcripts — локальные артефакты оператора. Можно удалить папку:

```powershell
Remove-Item -Recurse -Force demos\review-assistant-runner\transcripts
```

Runner создаст папку снова при следующем `--save-transcript`.

---

## Git

Папка `transcripts/` не должна коммититься с секретами. При необходимости добавьте в `.gitignore` локально.
