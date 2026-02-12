# Task Brief: Route Reconcile Runtime Owner in Voice Integration

Date: 2026-02-11

## Context
`decide_route_manager_reconcile` был описан в gateway/matrix, но не вызывался в runtime.

## Change
Файлы:
- `integration/integrations/voice_recognition_integration.py`
- `tests/test_voice_route_manager_gate.py`

Сделано:
- Добавлен runtime-gate `_allow_route_reconcile_start(session_id)` в integration layer.
- В `_on_recording_start` добавлен вызов gate до активации записи/сессии.
- Поведение:
  - `ABORT` → публикация `voice.mic_closed` + `voice.recognition_failed` и остановка старта.
  - `RETRY` → один короткий retry (100ms), при `ABORT` после retry — такой же terminal fail.
  - `START/DEGRADE` → стандартный путь запуска.

## Verification
- `PYTHONPATH=. pytest -q tests/test_voice_route_manager_gate.py` → `2 passed`
- `PYTHONPATH=. pytest -q tests/test_interrupt_playback.py -k "grpc_cancel or interrupt_idempotently"` → `2 passed, 19 deselected`

## Impact
- Route reconcile policy получил runtime-owner без нарушения границ модулей (решение в integration layer).
- Уменьшен разрыв между `interaction_matrix` и фактическим исполнением.
