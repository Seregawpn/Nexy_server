# Task Brief

## Context
После централизации финализации режима оставался дубль обработки `playback.completed` в `ModeManagementIntegration`.

## Objective
Убрать остаточный дубль terminal-обработки и оставить единый owner-путь для `playback.completed`.

## Architecture Fit
- Owner оси mode: `ModeManagementIntegration -> ModeController -> ApplicationStateManager`.
- Source of Truth сохранен; второй путь не добавлен.

## Implementation
1. Удалена подписка `playback.completed -> _bridge_playback_done`.
2. Оставлен единственный путь: `playback.completed -> _on_playback_finished`.
3. `playback.failed` bridge сохранен.

## Verification
- `python3 -m py_compile integration/integrations/mode_management_integration.py` — OK.
- `pytest -q tests/test_mode_management_mode_request_dedup.py tests/test_mode_management_sleep_guard_session_scope.py` — 8 passed.
- Проверка подписок: в файле осталась одна подписка на `playback.completed`.

## Информация об изменениях
- Что изменено:
  - Удален дубль подписки на `playback.completed`.
- Список файлов:
  - `integration/integrations/mode_management_integration.py`
  - `Docs/assistant_exchange/codex/2026-02-17__task-brief__mode-remove-playback-completed-duplicate-subscription.md`
- Причина/цель изменений:
  - Снизить риск race/дублирующей финализации и упростить owner-логику.
- Проверка:
  - Синтаксис и профильные тесты режима выполнены успешно.
