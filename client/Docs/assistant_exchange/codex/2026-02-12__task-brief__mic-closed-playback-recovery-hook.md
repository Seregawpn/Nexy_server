# Task Brief: mic_closed playback recovery hook

## Goal
Снизить риск "audio pipeline ok, но не слышно" после цикла микрофона, не нарушая текущую архитектуру.

## Change
- Реализован owner-совместимый recovery-хук в:
  - `integration/integrations/speech_playback_integration.py`
  - метод: `_on_voice_mic_closed`
- Ранее обработчик был `pass`.
- Теперь при активном playback-контексте (`_playback_active` или `_current_session_id`) выполняется:
  - сериализованный через `_playback_op_lock` вызов `_ensure_player_ready()`
  - лог `AUDIO_MIC_RECOVERY ... before=... after=...`
- Новых источников истины не добавлено, recovery остаётся в playback-owner.

## Architecture
- Owner lifecycle микрофона: `VoiceRecognitionIntegration` (события `voice.mic_opened/closed`)
- Owner output recovery: `SpeechPlaybackIntegration` + `AVFoundationPlayer`
- Централизация сохранена.

## Validation
Команда:
- `PYTHONPATH=. python3 -m pytest -q tests/test_speech_playback_pipeline_diagnostic.py tests/test_microphone_activation.py tests/test_interrupt_playback.py`

Результат:
- `21 passed`

## Notes
Это предварительный безопасный шаг перед полевой проверкой на реальном аудиоустройстве/BT route.
