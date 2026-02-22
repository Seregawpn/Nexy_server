# PTT Press Preempt Armed Race Fix

## Метаданные
- Ассистент: codex
- Тип: analysis
- Дата: 2026-02-20
- ID (INS-###): N/A

## Diagnosis
В логе есть `PRESS_PREEMPT`, но переход `PTT_STATE: idle -> armed` не фиксируется до обработки interrupt pipeline.
При удержании `Ctrl+N` это приводит к длительному `combo_active_hold` без старта записи.

## Root Cause
В `_handle_press` interrupt publish выполнялся до фиксации нового press-cycle (`ARMED`).
Если preempt/cancel ветка занята, long-press может попасть в stale окно и не перевести цикл в `RECORDING`.

## Optimal Fix
Перестроен порядок в owner-path `InputProcessingIntegration._handle_press`:
1. Сразу фиксировать новый цикл (`ARMED`, `active_press_id`, `pending_session_id`, `PTT_PRESSED=True`).
2. После этого выполнять preempt publish (`interrupt.request`) при необходимости.

Дополнительно ранее добавлены fallback-guards: hold watchdog и release fallback для lost long-press.

## Verification
- `python3 -m py_compile client/integration/integrations/input_processing_integration.py` — ok
- `pytest -q tests/test_interrupt_management_preempt_mode_skip.py tests/test_mode_management_mode_request_dedup.py` — 14 passed

## Информация об изменениях
- Что изменено: re-order `_handle_press` (ARMED before preempt await)
- Файлы:
  - `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/integration/integrations/input_processing_integration.py`
- Причина/цель: убрать race "press_preempt без armed" и залипание при hold.
- Проверка: py_compile + targeted pytest.

## Запрос/цель
Устранить залипание при удержании `Ctrl+N` во время активной речи ассистента.

## Контекст
- `client/integration/integrations/input_processing_integration.py`
- Логи runtime `combo_active_hold`, `PRESS_PREEMPT`.

## Решения/выводы
- Race локализован в порядке действий `_handle_press`.
- Исправление выполнено без изменения owner-path архитектуры.

## Открытые вопросы
- Нужен ли отдельный metric по количеству fallback watchdog/release fallback сессий.

## Следующие шаги
- Повторный живой прогон удержания `Ctrl+N` во время playback и проверка `PTT_STATE -> recording`.
