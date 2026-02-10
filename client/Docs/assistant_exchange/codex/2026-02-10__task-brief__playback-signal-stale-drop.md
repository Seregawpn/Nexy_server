# Task Brief: stale playback.signal drop

Date: 2026-02-10
Assistant: codex

## Goal
Убрать запоздалые cue-сигналы, которые приходят в новый режим/сессию и вызывают ложное воспроизведение.

## Changes
Files:
- `integration/adapters/signals_event_sink.py`
- `integration/integrations/speech_playback_integration.py`

Implemented:
1. В `playback.signal` добавлен timestamp публикации:
- поле `emitted_at_ms = int(time.monotonic() * 1000)`.

2. В `SpeechPlaybackIntegration._on_playback_signal` добавлен stale-filter:
- `signal_max_age_ms` из конфига (`speech_playback.signal_max_age_ms`, default `1200`).
- если возраст сигнала `age_ms > signal_max_age_ms`, cue пропускается.

3. Существующие guard-ы (shutdown/quit-intent/mode-context/cancel-in-flight) сохранены.

## Architecture fit
- Централизация не нарушена: все решения о проигрывании cue остаются в едином consumer-е `playback.signal`.
- Source of Truth не менялся: `state_manager` + `mode_management`.

## Validation
Command:
- `PYTHONPATH=. pytest -q tests/test_interrupt_playback.py tests/test_signal_integration_cancel_done_suppression.py tests/test_mode_management_mode_request_dedup.py tests/test_speech_playback_session_id.py`

Result:
- `18 passed`

## Expected runtime effect
- Запоздалые сигналы (`error/done/cancel`) не воспроизводятся в новом `LISTENING` контексте.
- Поведение cue более детерминированно под нагрузкой и при быстром переключении режимов.
