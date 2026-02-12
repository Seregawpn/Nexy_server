# Task Brief: remove unused voice.mic_opened signal handler

## Context
После проверки централизации сигналов найден неактивный обработчик `_on_voice_mic_opened` в `SignalIntegration`, который не подписан и создаёт риск будущего дублирования `listen_start` при случайном подключении.

## Change
- `integration/integrations/signal_integration.py`
  - Удалён неиспользуемый метод `_on_voice_mic_opened`.

## Why
- Устраняет потенциальный второй путь эмита `listen_start`.
- Сохраняет единого владельца сигналов: `app.mode_changed` (для listen_start) и `processing.terminal` (для terminal cues).

## Validation
- `PYTHONPATH=. pytest -q tests/test_signal_integration_cancel_done_suppression.py tests/test_interrupt_playback.py`
- Result: `22 passed`.
