# Готовность к полной проверке: First-Run Permissions

## Метаданные
- Ассистент: cursor
- Тип: task-brief
- Дата: 2026-01-13
- Статус: ready for full verification

## Резюме

Подготовлены все инструменты и инструкции для полной проверки first-run логики:
- ✅ Скрипты для автоматической проверки
- ✅ Инструкции для визуальной проверки диалогов
- ✅ Чек-лист полной проверки

## Подготовленные инструменты

### 1. Скрипты для проверки логики/логов ✅

**Очистка флагов:**
- ✅ `scripts/clear_first_run_flags.py` — очистка всех флагов first-run

**Сброс TCC разрешений:**
- ✅ `scripts/reset_tcc_for_first_run.sh` — быстрый сброс всех 4 разрешений
- ✅ Ручной способ: `sudo tccutil reset <permission> com.nexy.assistant`

**Интеграционный тест:**
- ✅ `scripts/test_first_run_integration.sh` — проверка событий и флагов

**Golden logs тест:**
- ✅ `tests/test_golden_first_run_logs.py` — проверка последовательности событий

**Проверка состояния:**
- ✅ `scripts/check_first_run_state.py` — offline проверка (флаг + логи)

### 2. Инструкции для визуальной проверки ✅

**Подготовка:**
1. Очистить флаги: `python3 scripts/clear_first_run_flags.py`
2. Сбросить TCC: `bash scripts/reset_tcc_for_first_run.sh`
3. (Опционально) Перезапустить tccd: `sudo killall tccd`

**Запуск .app:**
- `open dist/Nexy.app` или `./dist/Nexy.app/Contents/MacOS/Nexy`

**Ожидаемый порядок диалогов:**
1. Accessibility (первый)
2. Microphone (второй)
3. Screen Capture (третий)
4. Input Monitoring (четвёртый, последний)

## Чек-лист полной проверки

### Автоматические проверки

- [ ] `clear_first_run_flags.py` — флаги очищены
- [ ] `reset_tcc_for_first_run.sh` — все 4 разрешения сброшены
- [ ] `test_first_run_integration.sh` — события найдены, флаг создан
- [ ] `test_golden_first_run_logs.py` — последовательность соответствует канону
- [ ] `check_first_run_state.py` — флаг и события в логах

### Визуальная проверка диалогов

- [ ] Порядок диалогов: Accessibility → Microphone → Screen Capture → Input Monitoring
- [ ] Диалоги появляются последовательно (не параллельно)
- [ ] Ранний переход при предоставлении разрешения (без ожидания 13s)
- [ ] Fallback диалог появляется только после таймаута всех разрешений
- [ ] Нет прямого открытия Settings из activator

### Проверка логов

- [ ] Событие `permissions.first_run_started` публикуется
- [ ] События `permissions.status_checked` для каждого разрешения
- [ ] События `permissions.changed` при изменении статуса
- [ ] Событие `permissions.first_run_restart_pending` (если нужен рестарт)
- [ ] Событие `permissions.first_run_completed` публикуется
- [ ] Все события содержат `session_id`

## Быстрый старт

### Полная проверка (автоматические + визуальная)

```bash
# 1. Подготовка
python3 scripts/clear_first_run_flags.py
bash scripts/reset_tcc_for_first_run.sh

# 2. Автоматические тесты
bash scripts/test_first_run_integration.sh
python3 -m pytest tests/test_golden_first_run_logs.py -v
python3 scripts/check_first_run_state.py

# 3. Визуальная проверка
open dist/Nexy.app
```

### Только автоматические проверки

```bash
python3 scripts/clear_first_run_flags.py
bash scripts/reset_tcc_for_first_run.sh
bash scripts/test_first_run_integration.sh
python3 -m pytest tests/test_golden_first_run_logs.py -v
python3 scripts/check_first_run_state.py
```

## Ожидаемые результаты

### Логи (канонический порядок)

```
permissions.first_run_started
permissions.status_checked (accessibility)
permissions.status_checked (microphone)
permissions.status_checked (screen_capture)
permissions.status_checked (input_monitoring)
permissions.changed (если статус изменился)
permissions.first_run_restart_pending (если нужен рестарт)
permissions.first_run_completed
```

### Диалоги (канонический порядок)

1. **Accessibility** (системный диалог)
2. **Microphone** (системный диалог)
3. **Screen Capture** (системный диалог)
4. **Input Monitoring** (системный диалог)
5. **Fallback** (in-app dialog, только после таймаута всех разрешений)

## Критерии успеха

- ✅ Логи соответствуют канону (порядок событий)
- ✅ Диалоги отображаются в каноническом порядке
- ✅ Ранний переход при предоставлении разрешения
- ✅ Fallback только после таймаута всех разрешений
- ✅ Нет прямого открытия Settings из activator

## Следующие шаги

1. Запустить автоматические скрипты
2. Выполнить визуальную проверку диалогов
3. Зафиксировать результаты в отчёте
4. Подтвердить соответствие канону

## Документация

- Полное руководство: `Docs/assistant_exchange/cursor/2026-01-13__task-brief__first-run-full-verification-guide.md`
- Скрипт сброса TCC: `scripts/reset_tcc_for_first_run.sh`
- Инструкции по тестированию: `scripts/README_FIRST_RUN_TEST.md`
