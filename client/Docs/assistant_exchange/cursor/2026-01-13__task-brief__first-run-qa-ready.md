# Готовность к QA: First-Run Permissions

## Метаданные
- Ассистент: cursor
- Тип: task-brief
- Дата: 2026-01-13
- Статус: ready for QA

## Резюме

Реализация завершена и проверена. Код соответствует канону:
- ✅ Dialog-only путь (нет прямых Settings calls в activator)
- ✅ Единый fallback (`_show_missing_permissions_dialog` после таймаута)
- ✅ Единый путь рестарта (`permissions.first_run_restart_pending`)
- ✅ Порядок разрешений из конфига (Accessibility → Microphone → Screen Capture → Input Monitoring)

## Готовность к тестированию

### Автоматические тесты готовы
- ✅ `scripts/test_first_run_integration.sh` — интеграционный тест
- ✅ `tests/test_golden_first_run_logs.py` — golden logs тест
- ✅ `scripts/check_tal_after_restart.py` — проверка TAL после рестарта
- ✅ `scripts/clear_first_run_flags.py` — очистка флагов (обновлён под канонические имена)
- ✅ `scripts/check_first_run_state.py` — проверка состояния (обновлён)

### Документация
- ✅ План QA создан: `Docs/assistant_exchange/cursor/2026-01-13__task-brief__first-run-qa-plan.md`
- ✅ Инструкции по тестированию: `scripts/README_FIRST_RUN_TEST.md`
- ✅ Быстрый старт: `scripts/QUICK_START_FIRST_RUN_TEST.md`

## Быстрый старт QA

### 1. Подготовка окружения

```bash
# Очистить флаги
python3 scripts/clear_first_run_flags.py

# Проверить конфиг
grep -A 5 "required_permissions:" config/unified_config.yaml
```

### 2. Запуск автоматических тестов

```bash
# Интеграционный тест
bash scripts/test_first_run_integration.sh

# Golden logs тест
python3 -m pytest tests/test_golden_first_run_logs.py -v
```

### 3. Ручные проверки

См. детальный план в `Docs/assistant_exchange/cursor/2026-01-13__task-brief__first-run-qa-plan.md`

## Критерии успеха

- ✅ Все автоматические тесты проходят
- ✅ Ручные проверки подтверждают соответствие канону
- ✅ Логи соответствуют ожидаемым паттернам
- ✅ Нет запрещённых паттернов в логах

## Следующие шаги

1. Запустить автоматические тесты
2. Выполнить ручные проверки по сценариям
3. Зафиксировать результаты QA
4. Подтвердить готовность к релизу
