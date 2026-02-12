# Task Brief

- Date: 2026-02-11
- Type: task-brief
- Title: mode-contract-interrupt-source-and-session-id

## Изменения (без дублей)

1. Нормализация interrupt source в `ModeManagementIntegration`:
   - `interrupt_management` -> `interrupt`
   - interrupt-путь теперь проходит через единый guard/priority как один источник.

2. В `InterruptManagementIntegration._handle_recording_stop`:
   - в `mode.request(PROCESSING)` добавлен `session_id` из `interrupt_event.data`.
   - устраняет конфликт с контрактом `PROCESSING requires session_id`.

## Что не менялось

- Не добавлялись новые состояния/флаги.
- Не менялась архитектура владельцев переходов.
- Не добавлялись альтернативные пути `mode.request`.

## Проверка

- `PYTHONPATH=. pytest -q tests/test_mode_management_mode_request_dedup.py tests/test_interrupt_management_contract.py`  
  Result: `5 passed`

- `PYTHONPATH=. pytest -q tests/test_interrupt_playback.py`  
  Result: `19 passed`

