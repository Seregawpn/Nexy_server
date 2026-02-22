# Task
Сделать PTT поведение детерминированным: при зажатии `Ctrl+N` во время playback старая сессия должна отменяться и новая должна гарантированно стартовать (без зависания в `armed`).

## Diagnosis
Логи подтверждали отмену предыдущей сессии (`interrupt.request` -> `grpc.request_cancel` -> `Audio queue cleared`), но не происходил устойчивый переход `armed -> recording`.

## Root Cause
Owner lifecycle новой сессии зависел от доставки Quartz `LONG_PRESS`/watchdog-сигнала. При его потере цикл оставался в `PTTState.ARMED`.

## Fix (Primary)
Файл: `client/integration/integrations/input_processing_integration.py`

1. Добавлен owner long-press timer:
- поля:
  - `_long_press_timer_task`
  - `_long_press_timer_press_id`
- методы:
  - `_arm_long_press_timer(...)`
  - `_cancel_long_press_timer(...)`
  - `_run_long_press_timer(...)`

2. Таймер стартует на `PRESS`:
- в `_handle_press(...)` сразу после `PTT_STATE: ARMED`.

3. Таймер синтетически запускает `LONG_PRESS`:
- если к моменту threshold цикл всё ещё валиден (`ARMED`, `PTT_PRESSED=True`, тот же `press_id`, без active start).

4. Таймер корректно отменяется:
- на `LONG_PRESS`, `RELEASE`, `reset`, `grpc_failed`, `stop`.

## Architecture Fit
- Source of Truth сохранён: `InputProcessingIntegration`.
- Quartz остаётся low-level adapter, не owner lifecycle.
- Второй owner-path не добавлен.

## Concurrency / Race
- Использован текущий owner guard: `_lifecycle_lock`, `press_id`-dedup, state-guards.
- Таймер привязан к одному press-cycle через `_long_press_timer_press_id`.

## Verification
- `python3 -m py_compile client/integration/integrations/input_processing_integration.py`
- `pytest -q tests/test_microphone_activation.py tests/test_interrupt_management_preempt_mode_skip.py tests/test_mode_management_mode_request_dedup.py`

Результат: `20 passed`.

## Gate Check
- Single Owner Gate: pass
- Zero Duplication Gate: pass
- Anti-Race Gate: pass
- Flag Lifecycle Gate: pass
