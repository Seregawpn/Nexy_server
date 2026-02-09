# Input Architecture Cleanup: stop dedup + release guards

## Контекст
Симптомы: ложные `RELEASE` из Quartz hold monitor/watchdog, дубли `voice.recording_stop`, рассинхрон lifecycle (`_mic_active=True` при `session_id=None`).

## Что сделано
- Добавлен lifecycle Source of Truth и явные переходы (`PTTLifecycleState`), с логированием.
- Добавлен idempotency guard на terminal stop по `press_id`:
  - `self._terminal_stop_press_id`
  - `_try_mark_terminal_stop(...)`
- `PRESS` теперь сбрасывает terminal-stop маркер.
- `reset_session(...)` сбрасывает terminal-stop маркер.
- `RELEASE` для Quartz `ctrl_n` ужесточен:
  - без `press_id` -> игнор
  - без `active_press_id` -> игнор
- В `RELEASE` и `SHORT_PRESS` stop-путь теперь idempotent (один `voice.recording_stop` на press).
- Удален прямой дубль `voice.mic_closed` из ветки release без session_id (оставлен единый stop-путь).
- Удалены debug `print(...)` из async/sync обработчиков.
- Публикация interrupt/cancel централизована через `_publish_interrupt_and_cancel(...)`.

## Файлы
- `/Users/sergiyzasorin/Fix_new/client/integration/integrations/input_processing_integration.py`

## Проверка
- `python3 -m py_compile integration/integrations/input_processing_integration.py`
- `python3 -m py_compile modules/input_processing/keyboard/mac/quartz_monitor.py integration/integrations/voice_recognition_integration.py`

