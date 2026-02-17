# Task Brief

## Context
Оставались остаточные дубли terminal-path:
- `playback.failed` в `ModeManagementIntegration` обрабатывался двумя путями.
- `browser.cancelled` мог дублироваться в окне cancel/cleanup.

## Objective
Убрать остаточные дубли и снизить race-риск без изменения архитектурных owner-границ.

## Architecture Fit
- Mode owner: `ModeManagementIntegration -> ModeController -> ApplicationStateManager`.
- Browser terminal owner: `BrowserUseIntegration`.
- Второй путь принятия mode-решений не добавлялся.

## Implementation
1. `ModeManagementIntegration`:
- Удалена подписка `playback.failed -> _bridge_playback_done`.
- Удалён сам legacy-bridge `_bridge_playback_done`.
- Оставлен единый путь `playback.failed -> _on_playback_finished`.

2. `BrowserUseIntegration`:
- Введен учет активных browser session (`_active_browser_sessions`).
- Усилен dedup terminal events через `_publish_terminal_event_once`.
- Для cancel без `session_id` добавлен fallback: если активна ровно одна browser-сессия, использовать её `session_id`.
- Терминальные публикации (`completed/failed/cancelled`) сведены к единой dedup-точке.

## Verification
- `python3 -m py_compile integration/integrations/mode_management_integration.py integration/integrations/browser_use_integration.py` — OK.
- `pytest -q tests/test_mode_management_mode_request_dedup.py tests/test_mode_management_sleep_guard_session_scope.py` — 8 passed.

## Информация об изменениях
- Что изменено:
  - Удален дубль обработки `playback.failed` в mode-owner.
  - Усилен dedup и session fallback для `browser.cancelled` в browser-owner.
- Список файлов:
  - `integration/integrations/mode_management_integration.py`
  - `integration/integrations/browser_use_integration.py`
  - `Docs/assistant_exchange/codex/2026-02-17__task-brief__remove-residual-terminal-duplicates-mode-browser.md`
- Причина/цель изменений:
  - Снизить остаточные дубли и race-window в terminal событиях.
- Проверка:
  - Синтаксис и профильные mode-тесты пройдены.
