# Interrupt Centralization Audit

Дата: 2026-02-11
Область: client interrupt flow (`interrupt.request` → `grpc.request_cancel` → `playback.cancelled`)

## Summary
- Канонический поток прерывания в целом работает и подтвержден тестами (`22 passed`).
- Найдены архитектурные дубли и один race-risk в `InterruptCoordinator`.

## Findings

1. Дублирующий путь mode-transition на interrupt
- `/Users/sergiyzasorin/Fix_new/client/integration/integrations/interrupt_management_integration.py:450`
- `/Users/sergiyzasorin/Fix_new/client/integration/workflows/listening_workflow.py:173`
- `ListeningWorkflow` на `interrupt.request` сам публикует `mode.request(SLEEPING)`, при этом `InterruptManagementIntegration` делает то же через `_handle_speech_stop`.

2. Потенциальная гонка при очистке active_interrupts
- `/Users/sergiyzasorin/Fix_new/client/modules/interrupt_management/core/interrupt_coordinator.py:113`
- `/Users/sergiyzasorin/Fix_new/client/integration/integrations/interrupt_management_integration.py:604`
- `trigger_interrupt()` удаляет `event` из `active_interrupts`, а `_cancel_all_interrupts()` может параллельно очистить список вручную; это риск `ValueError`/неконсистентной истории.

3. Неиспользуемые/нецентрализованные ветки interrupt API
- `/Users/sergiyzasorin/Fix_new/client/integration/integrations/interrupt_management_integration.py:493`
- `/Users/sergiyzasorin/Fix_new/client/integration/integrations/interrupt_management_integration.py:536`
- `recording.stop_requested`/`session.clear_requested` публикуются, но подписчиков нет; это шум и второй контур ответственности без владельца.

4. Drift контракта payload
- `/Users/sergiyzasorin/Fix_new/client/Docs/FLOW_INTERACTION_SPEC.md:25`
- `/Users/sergiyzasorin/Fix_new/client/integration/integrations/interrupt_management_integration.py:320`
- Канон требует payload в `event.data`; в обработчике есть fallback на верхний уровень (`event.get("type")`), что поддерживает legacy-формат и размывает контракт.

## Recommended Centralization
- Единственный владелец mode-transition при interrupt: `InterruptManagementIntegration`.
- Единственный владелец terminal input stop: `InputProcessingIntegration` (через `interrupt.request` owner path).
- Единственный владелец аудио cancel события: `SpeechPlaybackIntegration` (`playback.cancelled`).
- В `InterruptCoordinator` убрать внешнюю manual-clear ветку и ввести lock-safe cancel API.

## Verification
- Команда: `PYTHONPATH=. pytest -q tests/test_interrupt_management_contract.py tests/test_interrupt_playback.py`
- Результат: `22 passed in 0.85s`
