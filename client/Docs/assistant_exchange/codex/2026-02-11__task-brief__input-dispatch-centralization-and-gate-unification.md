# Input Dispatch Centralization and Gate Unification

## Метаданные
- Ассистент: codex
- Тип: task-brief
- Дата: 2026-02-11
- ID (INS-###): N/A

## Diagnosis
- В fallback `KeyboardMonitor` callback'и отправлялись через thread-per-event, что создавало риск out-of-order delivery.
- В `InputProcessingIntegration` admission gate (`ptt_available`) был продублирован в нескольких обработчиках.

## Root Cause
- Дубли dispatch-путей и дубли gate-проверок повышали риск race/рассинхрона между backend и lifecycle.

## Optimal Fix
- Централизован dispatch в fallback backend:
  - добавлен единый queue-based dispatcher thread (ordered delivery).
  - удален thread-per-event callback запуск.
- Централизован gate для нового PTT-входа:
  - добавлен `_can_accept_new_ptt_input(source)` в `InputProcessingIntegration`.
  - `press/long_press` используют единый gate.

## Verification
- `pytest -q tests/test_keyboard_monitor_dispatch_order.py tests/test_keyboard_monitor_stale_timeout.py tests/test_quartz_stale_state_timeout.py tests/test_quartz_voiceover_passthrough.py tests/test_tray_quit_dispatch.py tests/test_user_quit_ack.py`
- Результат: `14 passed`.

## Запрос/цель
- Привести input/quit path к более чистой архитектуре с меньшим риском конфликтов и гонок.

## Контекст
- Файлы:
  - `modules/input_processing/keyboard/keyboard_monitor.py`
  - `integration/integrations/input_processing_integration.py`
  - `tests/test_keyboard_monitor_dispatch_order.py`
- Ограничения: без реархитектуры и без новых источников истины.

## Решения/выводы
- Ordering контракт callback-доставки унифицирован и предсказуем.
- Admission gate для PTT-входа централизован в одном методе.

## Открытые вопросы
- Для полного backend parity можно дополнительно вынести общий helper для callback-dispatch между Quartz/fallback (опционально).

## Следующие шаги
- Ручной прогон пользовательского сценария (VO + Safari/YouTube + Spotlight) для финального UX подтверждения.
