# Init Order And Mode Processing Centralization

## Метаданные
- Ассистент: codex
- Тип: task-brief
- Дата: 2026-02-11
- ID (INS-###): N/A

## Diagnosis
Порядок `initialize` был неканонический (по insertion-order словаря), а в `ModeManagementIntegration` были локальные обходы через прямой `set_mode`.

## Root Cause
Разные владельцы порядка инициализации + частичный bypass mode-owner → риск несогласованности startup и второго пути управления режимом.

## Optimal Fix
- `SimpleModuleCoordinator._initialize_integrations()` переведён на `IntegrationFactory.get_startup_order(...)`.
- Добавлен fallback для интеграций, отсутствующих в каноническом списке.
- В `ModeManagementIntegration` убраны direct `set_mode` ветки в `PROCESSING -> PROCESSING`; оставлена синхронизация `session_id` через `update_session_id`.

## Verification
- `PYTHONPATH=. pytest -q tests/test_mode_management_mode_request_dedup.py tests/test_event_ownership_contract.py tests/test_init_order.py`
- Результат: `6 passed, 4 skipped`.

## Запрос/цель
Сделать управление запуском и режимами более централизованным и устойчивым к дублям/гонкам.

## Контекст
- Файлы:
  - `integration/core/simple_module_coordinator.py`
  - `integration/integrations/mode_management_integration.py`

## Решения/выводы
- Single-owner для порядка `initialize/start` выровнен через `IntegrationFactory`.
- Локальные обходы mode transition в active PROCESSING сведены к session sync без второго пути смены режима.

## Открытые вопросы
- Нужно ли дополнительно запретить fallback `AppMode` enum в `base_workflow.py` и `permission_gateways.py` (следующий шаг централизации типов).

## Следующие шаги
- Добавить/обновить тест, который валидирует именно runtime `initialize` order, а не только литерал в коде.
