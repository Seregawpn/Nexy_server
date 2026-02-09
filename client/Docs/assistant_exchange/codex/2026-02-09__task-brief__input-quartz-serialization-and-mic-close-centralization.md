# Input/Quartz stabilization: remove duplicates and race-prone paths

## Что реализовано

1. `InputProcessingIntegration`
- Удалены неиспользуемые sync-wrapper методы `_sync_handle_*`.
- Удалены неиспользуемые импорты (`dataclass`, `EventTypes`, `get_user_data_dir`, `os`).
- Убран дубль публикации `voice.mic_closed` из `_force_reset_mic_state` (теперь fail-safe reset не создаёт второй источник mic_closed).

2. `VoiceRecognitionIntegration`
- Добавлена единая idempotent-публикация `voice.mic_closed`:
  - `_publish_mic_closed(session_id, source=...)`
  - dedup окно: `0.5s` по ключу `(session_id, source)`.
- Все локальные публикации `voice.mic_closed` заменены вызовом `_publish_mic_closed`:
  - `_on_recording_stop`
  - `_publish_v2_completed`
  - `_publish_v2_failed`

3. `QuartzKeyboardMonitor`
- Убран `thread-per-event` dispatch.
- Добавлен последовательный dispatcher callback-ов:
  - `self._callback_queue`
  - `self.callback_dispatch_thread`
  - `_start_callback_dispatcher`, `_stop_callback_dispatcher`, `_run_callback_dispatcher`
- `_trigger_event` теперь кладёт событие в очередь, сохраняя порядок callback-ов.

## Зачем
- Устранить дубли `voice.mic_closed`.
- Снизить out-of-order гонки между `PRESS/LONG/RELEASE` при высокой частоте событий Quartz.
- Упростить слой input, убрать мёртвый/шумный код.

## Проверка
- `python3 -m py_compile integration/integrations/input_processing_integration.py`
- `python3 -m py_compile integration/integrations/voice_recognition_integration.py`
- `python3 -m py_compile modules/input_processing/keyboard/mac/quartz_monitor.py`

