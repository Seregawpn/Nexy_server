# Task Brief: Browser Terminal Single-Owner Dedup

## Context
В browser-потоке оставался риск конкурирующих terminal-событий для одной `session_id` (например, `browser.completed` и поздний `browser.failed/cancelled`).

## Goal
Закрепить правило `one browser session -> one terminal event` и убрать terminal-публикацию без `session_id` при cancel.

## Changes
- Добавлен session-level dedup guard для terminal-событий в `BrowserUseIntegration`.
- Усилен cancel-path: при отсутствии `session_id` публикуем `browser.cancelled` по каждой активной browser-сессии.
- Добавлен cleanup для новых dedup-структур.

## Verification
- `python3 -m py_compile integration/integrations/browser_use_integration.py integration/integrations/mode_management_integration.py`
- Проверка наличия guard-логов через `rg`.

## Информация об изменениях
- Что изменено:
  - Введён session-level terminal dedup (`_terminal_by_session_ts`, `_terminal_by_session_event`).
  - В `_publish_terminal_event_once(...)` добавлен single-owner guard для terminal event per session.
  - В `_on_cancel_request(...)` добавлена публикация `browser.cancelled` для каждой активной сессии при отсутствии входного `session_id`.
- Список файлов:
  - `integration/integrations/browser_use_integration.py`
- Причина/цель изменений:
  - Убрать дубли/гонки terminal-событий browser и исключить неоднозначность завершения сессии.
- Проверка:
  - Компиляция модулей успешна, патч применён, логические точки guard подтверждены поиском.
