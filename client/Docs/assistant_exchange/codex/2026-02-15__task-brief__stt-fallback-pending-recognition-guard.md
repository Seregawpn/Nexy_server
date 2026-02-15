# Task Brief — STT fallback pending-recognition guard

## Goal
Устранить гонку, где fallback `no_speech_after_release` публикуется раньше позднего `recognition_completed` и преждевременно переводит систему в `SLEEPING`.

## Changes
- `modules/voice_recognition/core/google_sr_controller.py`
  - Добавлен счетчик in-flight распознаваний (`_pending_recognitions`) с lock.
  - Добавлен публичный read-only метод `has_pending_recognition()`.
  - Старт потоков распознавания централизован через `_start_recognition_thread(...)` с корректным increment/decrement.
- `integration/integrations/voice_recognition_integration.py`
  - В fallback после `recording_stop` добавлено ожидание завершения in-flight распознавания перед публикацией terminal `no_speech`.
  - Добавлен guard `_has_pending_stop_recognition()`.
  - Добавлены параметры окна ожидания: poll `0.15s`, max extra wait `1.8s`.

## Architecture
- Source of truth terminal STT остался в `VoiceRecognitionIntegration`.
- Централизованный путь mode transition не изменен (`processing.terminal` -> `ModeManagementIntegration`).

## Validation
- `python3 -m py_compile integration/integrations/voice_recognition_integration.py modules/voice_recognition/core/google_sr_controller.py` — OK.
