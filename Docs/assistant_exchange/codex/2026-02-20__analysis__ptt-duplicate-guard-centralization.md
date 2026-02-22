# Task
Устранить конфликт дублей условий в PTT lifecycle (Ctrl+N hold), который блокировал стабильный переход `armed -> recording`.

## Diagnosis
В `InputProcessingIntegration` owner-path содержал дублированные и местами конфликтующие guard-условия:
- активность input-cycle проверялась разными наборами (`recording/mic/state`) в нескольких местах;
- long-press watchdog требовал слишком строгий набор Quartz-флагов (`combo_active && control_pressed && n_pressed`).

Это создавало окна, когда owner-state был `ARMED`, но синтетический `LONG_PRESS` не запускался.

## Architecture Fit
- Source of Truth: `InputProcessingIntegration` (`PTTState`, `press_id`, `PTT_PRESSED`).
- Quartz monitor оставлен thin-adapter (без owner-логики).
- Второй owner-path не добавлен.

## Changes
Файл: `client/integration/integrations/input_processing_integration.py`

1. Централизация активности input-cycle:
- добавлен helper `_is_input_cycle_active()`;
- на него переведены дублированные проверки в:
  - `_on_interrupt_request`
  - `_request_terminal_stop`
  - `_force_stop`
  - `_on_grpc_completed`
  - `_on_grpc_failed`

2. Централизация hold-сигнала для long-press watchdog:
- добавлен helper `_is_quartz_hold_signal(status, elapsed, threshold)`;
- native путь: `combo_active && control_pressed && n_pressed`;
- degraded fallback: `PTT_PRESSED=True` + частичный физический сигнал (`control_pressed || n_pressed`) + дополнительный margin.

3. Защита health-loop:
- тик Quartz health-check обёрнут в `try/except`, чтобы watchdog не останавливался молча из-за единичного исключения.

## Concurrency / Race Guard
- Сохранён single owner lifecycle через `_lifecycle_lock`.
- Сохранён idempotency/dedup по `press_id` и terminal stop.
- Новые race-path не добавлены.

## Verification
- `python3 -m py_compile client/integration/integrations/input_processing_integration.py`
- `pytest -q tests/test_microphone_activation.py tests/test_interrupt_management_preempt_mode_skip.py tests/test_mode_management_mode_request_dedup.py`

Результат: `20 passed`.

## Gate Check
- Single Owner Gate: pass
- Zero Duplication Gate: pass (дубли активных guard'ов сведены)
- Anti-Race Gate: pass
- Flag Lifecycle Gate: pass (новые runtime flags не добавлялись)
