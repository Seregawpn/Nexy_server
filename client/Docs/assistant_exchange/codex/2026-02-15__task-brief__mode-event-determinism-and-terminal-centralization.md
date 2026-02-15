# Task Brief: mode event determinism + terminal centralization

Дата: 2026-02-15

## Что изменено
1. EventBus
- `integration/core/event_bus.py`
- Убран `app.mode_changed` из fast-path (`_fast_events`), оставлен только `app.state_changed`.
- Цель: предсказуемая последовательность обработки критичных mode subscribers.

2. ModeManagementIntegration
- `integration/integrations/mode_management_integration.py`
- Добавлена подписка на `processing.terminal`.
- Добавлен bridge `_on_processing_terminal()` -> публикация `mode.request(SLEEPING)` через центральный owner.
- Guard для `SLEEPING` расширен: обрабатывает весь префикс `ProcessingWorkflow.processing_*`, а не только `processing_completed`.

3. ProcessingWorkflow
- `integration/workflows/processing_workflow.py`
- Удален прямой terminal publish `mode.request(SLEEPING)`.
- Оставлен terminal сигнал `processing.terminal`, cleanup остается в workflow.
- Цель: убрать дублирующий путь mode-решений из workflow.

4. Тесты
- `tests/test_mode_management_mode_request_dedup.py`
- Добавлены тесты:
  - terminal bridge вызывает централизованный sleep path;
  - terminal без `session_id` игнорируется.

## Проверка
Команда:
- `PYTHONPATH=. pytest -q tests/test_mode_management_mode_request_dedup.py tests/test_event_bus_subscription_dedup.py`

Результат:
- `8 passed`

## Риски/заметки
- Legacy/fallback ветки не удалялись в этой задаче (осознанно, чтобы не ломать совместимость).
- В `ModeManagementIntegration` при `priority >= 90` текущая логика нормализует source в `interrupt` (историческое поведение, не менялось этой задачей).
