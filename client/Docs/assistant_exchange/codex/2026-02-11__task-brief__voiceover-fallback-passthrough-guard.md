# Task Brief: VoiceOver passthrough guard for fallback keyboard path

## Goal
Снизить риск конфликтов с VoiceOver/system shortcuts в fallback keyboard backend и убрать лишний keyboard hook в VoiceOver integration.

## Done
- Добавлен guard в fallback `KeyboardMonitor` (single-key path):
  - non-PTT modifiers (`alt/cmd`) блокируют старт PTT по `left_control`;
  - если modifier появляется во время active press, цикл корректно завершается (short/release path).
- В `VoiceOverDuckingIntegration` подписка на `keyboard.press` теперь создаётся только если `engage_on_keyboard_events=true`.
- Добавлены unit tests для fallback passthrough сценариев.

## Files
- `/Users/sergiyzasorin/Fix_new/client/modules/input_processing/keyboard/keyboard_monitor.py`
- `/Users/sergiyzasorin/Fix_new/client/integration/integrations/voiceover_ducking_integration.py`
- `/Users/sergiyzasorin/Fix_new/client/tests/test_keyboard_monitor_voiceover_passthrough.py`

## Verification
- `pytest -q tests/test_keyboard_monitor_voiceover_passthrough.py tests/test_quartz_voiceover_passthrough.py`
- Result: `5 passed`.

## Architecture fit
- Source of Truth не менялся: lifecycle по-прежнему в `InputProcessingIntegration`.
- Изменения ограничены low-level adapter и условной подпиской интеграции, без второго owner пути.
