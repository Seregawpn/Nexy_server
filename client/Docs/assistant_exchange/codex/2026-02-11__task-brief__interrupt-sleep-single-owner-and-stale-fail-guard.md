# Task Brief

- Date: 2026-02-11
- Type: task-brief
- Title: interrupt-sleep-single-owner-and-stale-fail-guard

## Что исправлено

1. Убран дублирующий `mode.request(SLEEPING)` из external interrupt path в `InputProcessingIntegration._on_interrupt_request`.
2. Добавлен session-guard в fallback `InputProcessingIntegration._on_recognition_failed`:
   - stale `failed_sid` (mismatch с active sid) теперь игнорируется;
   - в sleep publish добавляется `session_id`.

## Почему это безопасно

- Ownership `interrupt -> sleep` остается у `InterruptManagementIntegration` (single-owner).
- Основная текущая логика цикла PTT не менялась.
- Уменьшен риск out-of-order sleep от старого `recognition_failed`.

## Тесты

- `PYTHONPATH=. pytest -q tests/test_interrupt_playback.py -k "external_interrupt_does_not_publish_sleep_from_input_owner or recognition_failed_fallback_ignores_stale_session or recognition_failed_resets_waiting_grpc_state"`  
  Result: `3 passed, 16 deselected`

- `PYTHONPATH=. pytest -q tests/test_interrupt_playback.py`  
  Result: `19 passed`

