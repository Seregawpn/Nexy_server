# Task Brief: PTT stale release tail owner-guard

## Goal
Убрать race, где старый `release` перетирает новый `press` и блокирует повторный старт микрофона при быстром re-press.

## Architecture fit
- Owner сохранен: `InputProcessingIntegration` управляет PTT lifecycle.
- Source of Truth: state/press lifecycle внутри `InputProcessingIntegration` + `ApplicationStateManager`.
- Новые owner/state machine не добавлялись.

## Changes
1. Добавлен owner-guard `release`-цикла:
   - `integration/integrations/input_processing_integration.py`
   - новый метод `_is_stale_release_cycle(release_press_id)`.
2. В `_handle_release`:
   - фиксируется `release_press_id`;
   - после async-точек (`_request_terminal_stop`, `mode.request`) добавлен guard stale-tail;
   - `self._active_press_id` очищается только если цикл все еще текущий.
3. Добавлен регрессионный тест:
   - `tests/test_microphone_activation.py`
   - `test_stale_release_does_not_override_new_press_cycle`.

## Race/Dedup status
- Duplication: не добавлена новая ветка управления; использован текущий owner.
- Race: stale release tail больше не может перевести новый цикл в `WAITING_GRPC`.
- Centralization: сохранена, обходов coordinator/state-owner нет.

## Verification
- `PYTHONPATH=. pytest -q tests/test_microphone_activation.py` → `6 passed`.
- `PYTHONPATH=. pytest -q tests/test_interrupt_playback.py` → `15 passed`.
