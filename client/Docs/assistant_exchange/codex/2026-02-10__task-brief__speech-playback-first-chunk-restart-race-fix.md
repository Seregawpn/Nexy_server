# Task Brief: speech playback first-chunk restart race fix

## Problem
В боевом логе наблюдался паттерн `Playback started -> Playback stopped -> Playback started` на первом `grpc.response.audio` чанке новой сессии.

## Root cause
В `SpeechPlaybackIntegration._on_audio_chunk` был принудительный restart на первом чанке сессии:
- `stop_playback()`
- `start_playback()`

Этот блок запускался поверх уже выполненного `_ensure_player_ready()`, что создавало гонку/дребезг старта.

## Changes
### 1) Удален принудительный restart на первом audio chunk
- Файл: `integration/integrations/speech_playback_integration.py`
- Удален блок `stop_playback()+start_playback()` для `is_first_session_chunk`.
- Оставлен единый источник старта: `_ensure_player_ready()`.

### 2) Добавлен регрессионный тест
- Файл: `tests/test_interrupt_playback.py`
- Новый тест: `test_first_grpc_audio_chunk_does_not_force_stop_start_restart`
- Проверяет, что при первом grpc audio chunk:
  - `stop_playback` не вызывается
  - `start_playback` не вызывается
  - `add_audio_data` вызывается

## Validation
Команда:
`PYTHONPATH=. pytest -q tests/test_interrupt_playback.py tests/test_signal_integration_cancel_done_suppression.py tests/test_mode_management_mode_request_dedup.py tests/test_speech_playback_session_id.py`

Результат:
- `24 passed`

## Risk
Низкий. Изменена только локальная ветка restart в интеграции playback, без изменения маршрутизации событий и контрактов EventBus.
