# Task Brief

- Date: 2026-02-11
- Type: task-brief
- Title: mode-management-dead-bridge-cleanup

## Что очищено

В `ModeManagementIntegration` удалены неиспользуемые legacy-части:

1. Поле `_priorities` (использовалось только удаленным bridge).
2. Подписка на `voice.recording_start` и пустой handler `_on_voice_recording_start`.
3. Неиспользуемые bridge-методы:
   - `_bridge_keyboard_long`
   - `_bridge_keyboard_release`
   - `_bridge_keyboard_short`
   - `_bridge_grpc_done`
   - `_bridge_interrupt`

## Почему это безопасно

- Эти методы не были подключены к EventBus и не участвовали в runtime-flow.
- Активные владельцы режима (`input_processing`, `interrupt_management`, workflow finalize) не изменялись.
- Централизация сохранена: все переходы остаются через `mode.request` -> `ModeManagementIntegration`.

## Проверка

- `PYTHONPATH=. pytest -q tests/test_mode_management_mode_request_dedup.py tests/test_interrupt_management_contract.py tests/test_interrupt_playback.py`
- Result: `24 passed`

