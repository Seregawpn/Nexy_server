# Task Brief: Tap Recovery + Mic Stuck Failsafe

## Context
- После `CGEventTap` recovery появлялся `pending release Control`, подтверждался и вызывал ложный `RELEASE`.
- В части кейсов `voice.recording_stop` приходил без `session_id`, из-за чего `VoiceRecognition` игнорировал stop и микрофон мог зависать в активном состоянии.

## Root Cause
1. `Quartz` подтверждал `pending release Control` сразу после восстановления tap, когда системные флаги нестабильны.
2. `VoiceRecognitionIntegration._on_recording_stop` требовал строгий `session_id == active_session_id`; при `session_id=None` stop игнорировался.

## Changes
- `/Users/sergiyzasorin/Fix_new/client/modules/input_processing/keyboard/mac/quartz_monitor.py`
  - Добавлен guard после tap recovery (`_tap_recovered_at`, `_tap_recovery_guard_sec=0.8`).
  - В этот guard не ставим и не подтверждаем `pending release Control`.
- `/Users/sergiyzasorin/Fix_new/client/integration/integrations/voice_recognition_integration.py`
  - Для `recording_stop` без `session_id` используется active session, если есть.
  - Добавлен fail-safe: если запись активна, stop выполняется даже при `session_id=None`.

## Expected Effect
- Ложные `DEACTIVATION TRIGGERED` сразу после восстановления tap уменьшаются.
- `recording_stop` больше не теряется при `session_id=None`; микрофон стабильно закрывается.

## Validation
- `python3 -m py_compile` для измененных модулей: OK.
