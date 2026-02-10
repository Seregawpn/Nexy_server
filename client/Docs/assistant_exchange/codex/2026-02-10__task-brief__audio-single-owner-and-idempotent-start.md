# Task brief: audio single-owner + idempotent start/resume

Date: 2026-02-10
Assistant: Codex
Type: task-brief

## Goal
Убрать дублирующие пути управления аудио start/stop и исключить повторный start при уже активном listening.

## Minimal architecture-compatible changes
1. `voice_recognition_integration.py`
   - Добавить async single-flight lock для start/stop переходов.
   - В `_on_recording_start` сделать idempotent guard:
     - если уже активна та же сессия и `_recording_active=True`, skip;
     - если контроллер уже слушает, skip повторного `start_listening`.

2. `input_processing_integration.py`
   - Оставить единственным владельцем публикации terminal `voice.recording_start/stop`.
   - Сохранять reason/source в одном месте.

3. `listening_workflow.py`
   - Убрать прямой `event_bus.publish("voice.recording_stop", ...)` из timeout ветки.
   - Вместо этого публиковать request в owner (interrupt/stop-request), чтобы owner выпустил terminal stop.

## Expected result
- Один путь принятия решения по recording lifecycle.
- Нет дублей `start_listening` в соседних событиях.
- Снижение `StartIO error 35` и `already is a thread` в runtime-логах.
