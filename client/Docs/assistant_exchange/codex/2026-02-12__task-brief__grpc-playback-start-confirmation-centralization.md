# Task Brief

## Context
- Симптом: gRPC audio chunks приходят и планируются, но пользователь слышит тишину.
- Цель: централизовать старт gRPC playback и добавить однозначный маркер подтверждения старта, без дублей/гонок.

## Changes
- `integration/integrations/speech_playback_integration.py`
  - Добавлены структуры контроля старта gRPC:
    - `_grpc_start_confirmed_sessions`
    - `_grpc_start_reasserted_sessions`
    - `_grpc_start_watchdogs`
  - `_queue_session_audio(...)` расширен параметром `source`.
  - Для `source="grpc_audio"` добавлен централизованный confirm:
    - лог `AUDIO_GRPC_START_CONFIRMED session=... route=... engine_running=... player_playing=...`
  - Добавлен watchdog reassert:
    - лог `AUDIO_GRPC_START_REASSERT session=... ready=... timeout_sec=...`
  - Добавлен cleanup tracking на terminal/cancel/fail/completed путях.

- `modules/speech_playback/core/avf_player.py`
  - В no-op ветке `start_playback()` добавлен runtime лог:
    - `AUDIO_SESSION_RUNTIME reason=start_playback_noop snapshot=...`
  - Добавлен публичный runtime snapshot метод:
    - `get_playback_runtime_status()`

## Architecture
- Source of truth сохранен:
  - orchestration: `SpeechPlaybackIntegration`
  - runtime/audio session: `AVFoundationPlayer`
- Новый обходной путь не добавлен, локальные дубли старта не введены.

## Concurrency / Race
- Сериализация операций playback остаётся на `_playback_op_lock`.
- Confirm/reassert реализованы идемпотентно per `session_id`.
- Cleanup watchdog задач исключает утечки состояния между сессиями.

## Validation
- `python3 -m py_compile integration/integrations/speech_playback_integration.py modules/speech_playback/core/avf_player.py`
- `PYTHONPATH=. python3 -m pytest -q tests/test_speech_playback_grpc_audio_format.py` → `2 passed`
- `PYTHONPATH=. python3 -m pytest -q tests/test_interrupt_playback.py -k "playback_started or signal"` → `4 passed, 11 deselected`

## Next Run Log Markers
- Обязательные:
  - `AUDIO_GRPC_START_CONFIRMED ...`
  - при необходимости: `AUDIO_GRPC_START_REASSERT ...`
  - `AUDIO_SESSION_RUNTIME reason=start_playback_noop ...`
