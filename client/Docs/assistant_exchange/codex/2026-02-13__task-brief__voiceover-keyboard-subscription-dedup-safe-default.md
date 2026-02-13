# Task Brief — voiceover keyboard subscription dedup + safe default

## Context
В рамках реализации плана по устранению shortcut interception конфликтов нужно было убрать лишние side-effect пути в VoiceOver keyboard-интеграции и закрыть риск дублирования подписок.

## Deliverable
Изменены файлы:
- `integration/integrations/voiceover_ducking_integration.py`
- `modules/voiceover_control/core/controller.py`

## Что сделано
1. Safe default:
- В `VoiceOverControlSettings` default для `engage_on_keyboard_events` изменен на `False`.

2. Dedup:
- В `VoiceOverDuckingIntegration` удалена повторная подписка на `system.permissions_ready`.

3. Centralization/opt-in:
- Подписка на `keyboard.press` теперь выполняется только при явном `engage_on_keyboard_events=true`.
- Добавлен idempotent helper `_ensure_keyboard_press_subscription()` и флаг `_keyboard_press_subscribed`, чтобы исключить дубли и корректно обрабатывать deferred first-run инициализацию.

## Verification
- `PYTHONPATH=. pytest -q tests/test_quartz_monitor_chord_logic.py` → `2 passed`
- `python3 -m py_compile integration/integrations/voiceover_ducking_integration.py modules/voiceover_control/core/controller.py` → success

## Architecture fit
- Suppression owner и PTT owner не изменялись.
- Изменения ограничены VoiceOver integration path и безопасными defaults.
