# Task Brief: EventBus audio debug sampling

## Context
Во время стриминга `grpc.response.audio` EventBus логировал по нескольку debug-строк на каждый chunk (`dispatch/await/published`), что создавало сильный лог-флуд и мешало диагностике сигналов/состояний.

## Goal
Снизить шум логов для high-frequency событий без изменения семантики доставки событий.

## Changes
- Файл: `integration/core/event_bus.py`
- Добавлено:
  - `self._debug_sample_events = {"grpc.response.audio"}`
  - `self._debug_sample_interval_sec = 1.0`
  - `self._debug_sample_state` для счётчика подавленных сообщений
  - метод `_debug_log_event(...)` с sampling и `suppressed=N`
- Заменены прямые `logger.debug(...)` в `publish(...)` на `_debug_log_event(...)` для:
  - `dispatch`
  - `schedule/create_task/await/call_sync`
  - `published`

## Architecture/Behavior
- Логика публикации и вызова подписчиков НЕ изменена.
- Изменён только уровень детализации debug-логов для `grpc.response.audio`.
- Остальные события логируются как раньше.

## Verification
Команда:
`PYTHONPATH=. pytest -q tests/test_interrupt_playback.py tests/test_signal_integration_cancel_done_suppression.py tests/test_mode_management_mode_request_dedup.py tests/test_speech_playback_session_id.py`

Результат:
- `23 passed`

## Risks
- Минимальный риск: возможна меньшая granular-видимость по каждому audio chunk в debug.
- Компенсация: sampled-лог включает `suppressed=N`, поэтому объём потока всё равно наблюдаем.
