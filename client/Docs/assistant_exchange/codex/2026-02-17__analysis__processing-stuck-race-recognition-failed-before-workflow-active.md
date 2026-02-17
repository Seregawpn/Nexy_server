# Analysis: processing stuck due out-of-order recognition_failed

## Context
По логу наблюдалось залипание `PROCESSING` при no-speech сценарии после `voice.recording_stop`.

## Diagnosis
`voice.recognition_failed` мог приходить до того, как `ProcessingWorkflow` входил в ACTIVE для той же `session_id`. Событие отбрасывалось как нерелевантное, затем workflow оставался в `sending_grpc` без terminal пути.

## Root Cause
Race (out-of-order events):
- `voice.recognition_failed` (fallback_no_speech) публикуется раньше `app.mode_changed -> processing` для session.
- `_is_relevant_event` возвращает false (workflow ещё не активен), событие теряется.
- После старта цепочки нет признака failed, возможен stuck до общего timeout.

## Architecture Fit
- Owner решения: `ProcessingWorkflow` (owner цепочки PROCESSING).
- Source of truth не менялся, workaround в других интеграциях не добавлялся.

## Changes
Файл: `integration/workflows/processing_workflow.py`

1. Добавлен буфер ранних STT-fail событий:
- `_pending_recognition_failed_by_session: dict[str, dict[str, Any]]`

2. В `_on_recognition_failed`:
- если событие нерелевантно, но содержит `session_id` — буферизуется (error+timestamp), а не теряется.

3. В `_start_processing_chain`:
- перед переходом в `CAPTURING` проверяется buffered fail для текущей session.
- если найден — помечаем `recognition_failed=True` и завершаем цепочку сразу через `_complete_processing_chain()`.

## Concurrency / Race Guard
Использован idempotent session-scoped state-guard:
- буфер keyed by `session_id`
- consume-on-start (`pop`) для единственного применения.

## Verification
- `python3 -m py_compile integration/workflows/processing_workflow.py` — OK.
- Проверка кода: есть buffer/write/apply ветки по session.

## Информация об изменениях
- Что изменено:
  - Исправлена гонка out-of-order между `voice.recognition_failed` и стартом processing workflow.
  - Добавлен deterministic terminal path для no-speech even if fail event arrived early.
- Список файлов:
  - `integration/workflows/processing_workflow.py`
- Причина/цель изменений:
  - Убрать залипание режима `PROCESSING` и задержки завершения при no-speech сценариях.
- Проверка:
  - Синтаксическая проверка `py_compile` выполнена успешно.
