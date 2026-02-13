# Analysis: PTT re-press while previous release still in-flight

## Context
- Симптом: при быстром повторном зажатии `Ctrl+N` после отпускания микрофон иногда не стартует, хотя удержание продолжается.
- Лог-фрагмент: `PTT_STATE: stopping -> armed` (новый press), затем позже `PTT_STATE: armed -> waiting_grpc (reason=release_to_processing, press_id=<новый>)`.

## Root cause
- Owner-модуль: `integration/integrations/input_processing_integration.py`.
- Гонка между двумя press-cycle:
  - `release` первого цикла выполняет async-хвост (`_request_terminal_stop`/ожидания).
  - Пользователь уже начал второй цикл (`_handle_press` -> `ARMED`).
  - Хвост старого `release` продолжает выполнение и перетирает состояние второго цикла (`ARMED -> WAITING_GRPC`) + отправляет `mode.request=PROCESSING`.
- Из-за этого `LONG_PRESS` второго цикла не приводит к `voice.recording_start` (состояние уже не `ARMED/IDLE`).

## Architecture fit
- Логика должна оставаться в `InputProcessingIntegration` (owner PTT lifecycle).
- Нужен ownership-guard по press-cycle в асинхронных хвостах `release/stop`, без новых внешних owners.

## Minimal fix direction
1. В `_handle_release` фиксировать `release_press_id` в начале.
2. После каждого `await` в release-хвосте проверять, что текущий активный цикл все еще тот же (`self._active_press_id == release_press_id`), иначе выходить без `mode.request` и без `WAITING_GRPC`.
3. Аналогично защитить поздние state-трансферы, которые могут срабатывать после нового `press`.
4. Не менять monitor-уровень (`quartz_monitor`): проблема не в генерации long_press, а в stale release tail.

## Expected result
- Быстрый re-press не перетирается старым release.
- Удержание после re-press стабильно приводит к `voice.recording_start`.
- Уходит переход `armed -> waiting_grpc` с чужого (нового) `press_id`.
