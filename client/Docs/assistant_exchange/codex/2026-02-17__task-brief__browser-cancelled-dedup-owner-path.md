# Task Brief

## Context
В `nexy-dev.log` наблюдался дубль `browser.cancelled` для одной сессии в окне cancel/cleanup.

## Objective
Убрать дубль terminal browser-событий в owner-слое браузера без изменения mode-owner архитектуры.

## Architecture Fit
- Owner terminal browser events: `BrowserUseIntegration`.
- Owner mode decisions сохранён: `ModeManagementIntegration -> ModeController -> ApplicationStateManager`.

## Implementation
1. В `BrowserUseIntegration` добавлен централизованный publisher terminal-событий:
   - `_publish_terminal_event_once(event_name, payload)`.
2. Добавлен dedup по ключу `(event_name, session_id)` с коротким окном `2.0s`.
3. Все terminal публикации переведены на этот путь:
   - `browser.completed`
   - `browser.failed`
   - `browser.cancelled`
4. `_on_cancel_request` теперь публикует `browser.cancelled` через dedup-owner путь.

## Verification
- `python3 -m py_compile integration/integrations/browser_use_integration.py` — OK.
- Попытка запуска `pytest tests/test_browser_module_ready_bypass.py` в текущем окружении зависала без вывода; процессы остановлены вручную.

## Информация об изменениях
- Что изменено:
  - Введен idempotent/dedup publisher для terminal browser событий.
  - Устранен риск двойного dispatch `browser.cancelled` в коротком окне cancel.
- Список файлов:
  - `integration/integrations/browser_use_integration.py`
  - `Docs/assistant_exchange/codex/2026-02-17__task-brief__browser-cancelled-dedup-owner-path.md`
- Причина/цель изменений:
  - Снизить дубли/гонки terminal событий, сохранив централизованную архитектуру.
- Проверка:
  - Синтаксическая проверка выполнена.
  - Нужен runtime recheck в `nexy-dev.log` после нового browser cancel-прогона.
