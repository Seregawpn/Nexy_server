# Task Brief

## Context
По логам `nexy-dev.log` браузерный путь завершался (`browser.completed`), но в части прогонов `MODE_REQUEST` уходил в deferred и не всегда закрывался в `SLEEPING` в том же окне событий.

## Objective
Убрать риск залипания `PROCESSING` из-за out-of-order/без-session terminal событий, сохранив единого owner mode-решений в `ModeManagementIntegration`.

## Architecture Fit
- Owner оси mode: `ModeManagementIntegration -> ModeController -> ApplicationStateManager`.
- Source of Truth: `ModeManagementIntegration` для guard/finalize логики.
- Второй путь принятия решений не добавлялся.

## Implementation
1. Добавлен единый finalize-метод ` _try_finalize_sleep(session_id, source)` с idempotent/session-guard поведением.
2. Добавлен массовый re-check ` _try_finalize_deferred_sessions(source)` для кейсов, где terminal-событие приходит без `session_id`.
3. Добавлен fallback-резолвер ` _resolve_action_finished_session_id(...)`:
   - если `actions.lifecycle.finished` без `session_id`, но активна ровно одна action-сессия, используется она.
4. Обновлены обработчики:
   - `_bridge_playback_done`
   - `_on_playback_finished`
   - `_on_browser_finished`
   - `_on_action_finished`
   чтобы все шли через единый finalize-путь, а не через разрозненные локальные проверки.

## Verification
- `python3 -m py_compile integration/integrations/mode_management_integration.py` — OK.
- Поиск новых точек финализации/фолбеков в файле — OK.

## Информация об изменениях
- Что изменено:
  - Централизован owner-путь финализации `PROCESSING -> SLEEPING`.
  - Добавлены fallback-механизмы для terminal-событий без `session_id`.
  - Убраны дубли локальных условий финализации в трех обработчиках, заменены единым методом.
- Список файлов:
  - `integration/integrations/mode_management_integration.py`
  - `Docs/assistant_exchange/codex/2026-02-17__task-brief__mode-processing-finalize-centralized-fallback.md`
- Причина/цель изменений:
  - Устранить гонки и зависание режима при out-of-order событиях и неполных payload (`session_id=None`).
- Проверка:
  - Синтаксическая валидация модуля выполнена (`py_compile`).
  - Локальная проверка присутствия новых guard/finalize точек выполнена (`rg`).
