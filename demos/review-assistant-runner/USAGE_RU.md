# Использование Demo Runner (RU)

**Phase 3.5.2** — пошаговая инструкция для оператора.

---

## 1. Перейти в корень репозитория

```powershell
cd C:\Dima\Projects\CURSOR\AGENT
```

Если запустить из другой папки — runner покажет ошибку с требованием корня репозитория.

---

## 2. Интерактивное меню

```powershell
python demos/review-assistant-runner/demo_runner.py
```

1. Выберите номер сценария (1–15)
2. Дождитесь raw output команды
3. Прочитайте блок **РЕЗУЛЬТАТ ДЕМО** или **РЕЗУЛЬТАТ ПРОВЕРКИ**
4. Для выхода — `0`

---

## 3. Прямой запуск сценария

```powershell
python demos/review-assistant-runner/demo_runner.py --scenario happy
python demos/review-assistant-runner/demo_runner.py --scenario missing_approval
python demos/review-assistant-runner/demo_runner.py --scenario provider_safety_harness
```

Список всех ключей:

```powershell
python demos/review-assistant-runner/demo_runner.py --list
```

---

## 4. Сохранение transcript (только явный флаг)

```powershell
python demos/review-assistant-runner/demo_runner.py --scenario happy --save-transcript
```

Файл: `demos/review-assistant-runner/transcripts/YYYYMMDD_HHMMSS_<scenario>.md`

**По умолчанию transcript не сохраняется.**

---

## 5. Real provider (только вручную)

Сценарий `real_provider_synthetic` **не запускается по умолчанию**.

Перед запуском runner покажет предупреждение и спросит `yes/no`.

Подготовка (PowerShell):

```powershell
$env:RA_LLM_BASE_URL = "http://127.0.0.1:1234"
$env:RA_LLM_MODEL = "qwen2.5-7b-instruct-1m"
```

Запуск:

```powershell
python demos/review-assistant-runner/demo_runner.py --scenario real_provider_synthetic
```

Если нажать Enter или anything кроме `yes` — сценарий отменён.

---

## 6. Проверки baseline (группа 4)

Пункты 10–15 меню — это evaluation scripts, не agent demo:

```powershell
python demos/review-assistant-runner/demo_runner.py --scenario thin_baseline
python demos/review-assistant-runner/demo_runner.py --scenario smoke_checks
```

Ожидаемый формат итога: `PASS=N FAIL=0`.

---

## 7. Отладка

```powershell
python demos/review-assistant-runner/demo_runner.py --scenario happy --debug
```

Показывает traceback при неожиданных ошибках runner.

---

## 8. Что читать после запуска

| Документ | Зачем |
|----------|-------|
| [SCENARIO_GUIDE_RU.md](SCENARIO_GUIDE_RU.md) | Все 15 пунктов меню |
| [TRACE_SUMMARY_MAPPING_RU.md](TRACE_SUMMARY_MAPPING_RU.md) | Расшифровка TRACE |
| [../review-assistant-hands-on/SCENARIO_RESULTS.md](../review-assistant-hands-on/SCENARIO_RESULTS.md) | Hands-on таблица результатов |
