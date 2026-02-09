# Input V2: grpc_failed terminal path isolation

## Context
- Симптом: после long-press release состояние быстро сбрасывалось в `sleeping` и шли дублирующие interrupt/cancel/mode-переходы.
- Логи показывали, что `grpc.request_failed` в `InputProcessingIntegration` уходил в `_force_stop("grpc_failed")`.

## Diagnosis
- `_force_stop` архитектурно предназначен для `secure_input` аварийного пути.
- Использование `_force_stop` для `grpc_failed` смешивало два разных источника терминализации:
  - secure-input watchdog path
  - grpc terminal result path

## Change
- В `integration/integrations/input_processing_integration.py`:
  - добавлен `_finalize_grpc_failed(session_id)`:
    - завершает только input/PTT state machine;
    - очищает `PTT_PRESSED`, `WAITING_GRPC`, session linkage и внутренние флаги;
    - не публикует `interrupt.request`, `grpc.request_cancel`, `mode.request`.
  - `_on_grpc_failed` переключен с `_force_stop("grpc_failed")` на `_finalize_grpc_failed(sid)`.

## Architecture fit
- Source of Truth для lifecycle ввода остается в `InputProcessingIntegration`.
- Mode/interrupt orchestration остается у workflow/integration-слоя, без дублирующего локального канала из input при `grpc_failed`.
- Устранено смешение secure-input и grpc terminal путей.

## Verification
- `python3 -m py_compile integration/integrations/input_processing_integration.py` ✅
- `pytest -q tests/test_processing_workflow_session_guard.py` ✅ (2 passed)
- `pytest -q tests/test_welcome_startup_sequence.py` ✅ (2 passed)
- `pytest -q tests/test_ctrl_n_combo.py` ⚠️ не коллекционируется (класс с `__init__`)

## Expected runtime effect
- После `release -> processing` при `grpc_failed` больше нет повторного secure-input force-stop канала.
- Меньше дубликатов `interrupt/cancel/mode.request`, меньше гонок и конфликтов состояний.
