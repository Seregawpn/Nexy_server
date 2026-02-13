# Task Brief: gRPC playback inaudible after Input/mic activity

## Context
Поток `grpc.response.audio` стабильно приходит (`peak>0`, `engine=True`, `player=True`), но пользователь не слышит звук.

## Changes
1. `integration/integrations/speech_playback_integration.py`
- Добавлен state-owner маркер `self._active_output_session_id`.
- В `_queue_session_audio(...)` добавлен controlled fresh-start policy:
  - только для `source == "grpc_audio"`
  - только на первом чанке новой gRPC-сессии
  - только если уже была предыдущая активная сессия
  - действие: `self._stop_player_locked()` перед `self._ensure_player_ready()`.
- Добавлен лог-маркер:
  - `AUDIO_FRESH_START session=... prev_session=... reason=grpc_session_first_chunk`.
- Исправлен дефект в `_on_voice_mic_closed(...)`:
  - удалена ссылка на несуществующий `self._playback_active`
  - заменено на runtime-check `self._avf_player.is_playing()`.
- В `_apply_cancel_state(...)` сбрасывается `self._active_output_session_id` при завершении/cancel текущей сессии.

## Why this is architecture-safe
- Владелец воспроизведения не менялся: `SpeechPlaybackIntegration` + `AVFoundationPlayer`.
- Решение централизовано в существующем owner, без нового side-channel.
- Нет нового внешнего стейта/флагов между модулями.

## Verification
Команда:
`PYTHONPATH=. python3 -m pytest -q tests/test_speech_playback_pipeline_diagnostic.py tests/test_microphone_activation.py tests/test_interrupt_playback.py`

Результат:
- `21 passed`

## Runtime DoD markers
На живом прогоне при старте новой gRPC-сессии после предыдущей должно быть:
- `AUDIO_FRESH_START session=... prev_session=...`
- далее обычный pipeline:
  - `AUDIO_PIPELINE phase=before_queue ...`
  - `Scheduled chunk ... engine=True, player=True`

