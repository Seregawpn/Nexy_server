# Task
Проверить, остались ли в PTT owner-path конфликты условий, дубли и мертвый код после серии фиксов.

## Findings
1. Конфликт guard-условий в `_handle_long_press`:
- было: входной guard допускал `PTTState.IDLE`, но ниже тот же метод отбрасывал всё кроме `PTTState.ARMED`.
- эффект: stale long-press мог преждевременно отменить owner timer и ломать новый press-cycle.

2. Мертвое поле `_last_interrupt_event_id`:
- записывалось в `_publish_interrupt_and_cancel`, но нигде не читалось.

3. Мелкий мертвый хвост:
- `_preempt_reason` в `_handle_long_press` не использовалась.

## Changes Applied
Файл: `client/integration/integrations/input_processing_integration.py`
- Удалён `_last_interrupt_event_id` и запись в него.
- Ужесточён guard `_handle_long_press`: теперь только `PTTState.ARMED`.
- Убран неиспользуемый `_preempt_reason`.

## Verification
- `python3 -m py_compile client/integration/integrations/input_processing_integration.py`
- `pytest -q tests/test_microphone_activation.py tests/test_interrupt_management_preempt_mode_skip.py tests/test_mode_management_mode_request_dedup.py`
- Результат: `20 passed`.

## Gate Check
- Single Owner Gate: pass
- Zero Duplication Gate: pass
- Anti-Race Gate: pass
- Flag Lifecycle Gate: pass
