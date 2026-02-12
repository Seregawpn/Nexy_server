# Task Brief: Route Reconcile Retry Exhaustion Guard

Date: 2026-02-11

## Context
После внедрения runtime-gate оставался edge-case: при `RETRY -> RETRY` запись ошибочно продолжалась, хотя правило матрицы требует backoff/блокировку.

## Change
Файлы:
- `integration/integrations/voice_recognition_integration.py`
- `tests/test_voice_route_manager_gate.py`
- `Docs/FLOW_INTERACTION_SPEC.md`

Сделано:
- В `_allow_route_reconcile_start` добавлен блок `RETRY -> RETRY` как terminal fail (`route_reconcile_retry_exhausted`).
- `RETRY -> ABORT` сохранён как terminal fail (`route_reconcile_retry_abort`).
- Добавлен тест `test_route_reconcile_retry_retry_blocks_recording_start`.
- Обновлена flow-документация: `abort/retry->abort/retry->retry` не продолжают старт записи.

## Verification
- `PYTHONPATH=. pytest -q tests/test_voice_route_manager_gate.py tests/test_unified_config_avfoundation_flags.py tests/test_interrupt_playback.py -k "grpc_cancel_publishes_playback_cancelled_with_source_payload or handles_interrupt_idempotently or route_reconcile"` → `5 passed, 22 deselected`

## Impact
- Убран race/конфликт: старт микрофона больше не проходит при неразрешённом `device.busy` после retry.
- Runtime поведение приведено в соответствие с interaction matrix без добавления новых owner/state-осей.
