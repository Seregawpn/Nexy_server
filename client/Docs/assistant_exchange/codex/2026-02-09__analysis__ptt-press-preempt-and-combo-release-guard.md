# PTT press preempt + combo release guard

## Симптомы
1. Во время речи ассистента удержание combo не всегда сразу глушило речь до активации микрофона.  
2. При удержании `Ctrl+N` иногда приходил ложный `n_keyup`, и микрофон выключался, хотя combo еще удерживалась.

## Root Cause
- `InputProcessingIntegration._handle_press()` только armed, без немедленного preempt playback.  
- `QuartzKeyboardMonitor` деактивировал combo сразу на `n_keyup` без подтверждения, что уязвимо к дребезгу/ложным событиям.

## Изменения
- `integration/integrations/input_processing_integration.py`
  - В `_handle_press()` добавлен preempt:
    - если playback активен и есть активная session -> `interrupt.request` + `grpc.request_cancel` публикуются сразу на press.
  - Результат: сначала прерывание речи, затем штатный lifecycle long-press -> recording.

- `modules/input_processing/keyboard/mac/quartz_monitor.py`
  - Добавлен pending-release guard для combo:
    - `n_keyup` при зажатом Control не деактивирует combo мгновенно,
    - сначала ставится pending release с confirm delay (90ms),
    - deactivation происходит только если состояние стабильно подтвердилось.
  - `n_keydown` и `control down` отменяют pending release.

## Verification
- `python3 -m py_compile integration/integrations/input_processing_integration.py modules/input_processing/keyboard/mac/quartz_monitor.py` ✅
- `pytest -q tests/test_processing_workflow_session_guard.py` ✅
- `pytest -q tests/test_welcome_startup_sequence.py` ✅

## Expected Behavior
- При удержании combo во время речи:
  - ассистент сначала прерывается,
  - затем активируется микрофон (после long press порога).
- Ложные краткие `n_keyup` больше не должны сбрасывать удержание combo.
