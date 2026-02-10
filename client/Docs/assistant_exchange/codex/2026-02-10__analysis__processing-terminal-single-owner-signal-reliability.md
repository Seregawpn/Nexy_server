# Analysis: processing-terminal single owner signal reliability

## Context
- Проблема: сигнал при переходе `processing -> sleeping` иногда не воспринимается как корректный (визуально "пропал"), особенно на фоне одновременных `ERROR/DONE` и быстрых событий.

## What was changed
- Введен единый контракт терминала обработки: `processing.terminal`.
- `ProcessingWorkflow` публикует `processing.terminal` с результатом (`success|failed`) перед возвратом в `SLEEPING`.
- `SignalIntegration` переведен на единый источник терминальных cue:
  - слушает `processing.terminal`;
  - `LISTEN_START` оставлен на `app.mode_changed -> LISTENING`;
  - `DONE/ERROR` больше не формируются из разрозненных источников (`voice.recognition_failed`, `grpc.request_failed`, `app.mode_changed -> sleeping`).
- Добавлен dedup по `session_id` в терминальном обработчике сигналов.

## Why this resolves instability
- Убран дубликат владельцев terminal-сигналов.
- Убраны конфликтующие/гоняющиеся источники `ERROR` и `DONE`.
- Сформирован единый Source of Truth по завершению processing-цепочки.

## Verification
- Запуск:
  - `PYTHONPATH=. pytest -q tests/test_signal_integration_cancel_done_suppression.py tests/test_interrupt_playback.py tests/test_processing_workflow_session_guard.py`
- Результат:
  - `22 passed`

## Notes
- Рабочее дерево содержит и другие изменения вне этого фикс-пакета; они не откатывались.
