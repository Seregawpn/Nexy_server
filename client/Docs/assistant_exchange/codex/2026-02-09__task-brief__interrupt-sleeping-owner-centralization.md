# Task Brief: Interrupt->Sleeping owner centralization (race/conflict reduction)

## Goal
Уменьшить гонки и дубли `mode.request(SLEEPING)` в interrupt-ветке, сохранив одного владельца перехода режима.

## Changes
1. `integration/integrations/input_processing_integration.py`
- `_cancel_short_tap`: удалена публикация `mode.request(SLEEPING)`.
  Путь оставлен через `interrupt.request` (owner: InterruptManagementIntegration).
- `_force_stop`: `mode.request(SLEEPING)` публикуется только если `interrupt.request` не отправлялся.

2. `integration/workflows/processing_workflow.py`
- `_on_interrupt_request`:
  - при active workflow — только cleanup, без дополнительного `mode.request`;
  - при inactive workflow — не публикуем `mode.request`, owner остается InterruptManagementIntegration.

## Architecture Fit
- Центр управления режимом сохранён: `ModeManagementIntegration`.
- Owner interrupt->sleeping унифицирован: `InterruptManagementIntegration`.
- Второй путь принятия решений по режиму в interrupt-ветке убран.

## Verification
- `python3 -m py_compile integration/integrations/voice_recognition_integration.py integration/workflows/processing_workflow.py integration/integrations/input_processing_integration.py` — OK.

## Expected result
- Меньше out-of-order `mode.request(SLEEPING)` дублей.
- Ниже риск конфликтов между ProcessingWorkflow/InputProcessing и InterruptManagement в interrupt-цепочке.
