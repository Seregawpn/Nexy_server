# Startup Control Robustness Audit

## Метаданные
- Ассистент: codex
- Тип: analysis
- Дата: 2026-02-11
- ID (INS-###): N/A

## Diagnosis
Система в целом централизована (EventBus + Coordinator + ModeManagementIntegration), но есть локальные обходы центра управления в режиме инициализации и режима `PROCESSING`.

## Root Cause
Неполная централизация (два пути применения mode/state и fail-open на first-run) → возможны out-of-order переходы и рассинхронизация ожиданий REQ-006/REQ-003 → нестабильное поведение старта в крайних сценариях.

## Optimal Fix
Цель: оставить один путь принятия решений на старте и в mode pipeline, убрать дубли ownership.

Место в архитектуре:
- `integration/core/integration_factory.py` как единственный владелец порядка `initialize/start`.
- `integration/integrations/mode_management_integration.py` как единственный владелец применения переходов.
- `modules/permissions/v2` + `first_run_permissions_integration.py` как единственный владелец decision по first-run.

Source of Truth:
- Порядок: `IntegrationFactory.STARTUP_ORDER`.
- Режимы: `ModeController` + callback bridge в `state_manager.set_mode`.
- First-run: ledger (`permission_ledger.json`) + V2 orchestrator.

План внедрения:
1. Синхронизировать `initialize`-порядок с `IntegrationFactory.get_startup_order(...)`, убрать итерацию `dict.items()`.
2. В `ModeManagementIntegration` убрать прямые вызовы `state_manager.set_mode(...)` из `_on_mode_request`, оставить только `_apply_mode(...)` через `ModeController`.
3. В `BaseWorkflow` и `permission_gateways` убрать локальные fallback-Enum `AppMode`; при невозможности импорта — fail-fast с явной ошибкой конфигурации.
4. Явно зафиксировать policy fail-open/fail-closed для `FirstRunPermissionsIntegration.start()` (сейчас on-exception = forced startup).
5. Привести проверки `StateManager` в интеграциях к selectors/gateways (минимум для USER_QUIT_INTENT/FIRST_RUN_RESTART_SCHEDULED).

## Verification
- `PYTHONPATH=. pytest -q tests/test_init_order.py tests/test_centralization_regressions.py tests/test_event_ownership_contract.py`
- `PYTHONPATH=. pytest -q tests/test_mode_management_mode_request_dedup.py tests/test_welcome_startup_sequence.py tests/test_processing_workflow_session_guard.py`
- Проверка логов:
  - один источник mode transition (`mode.request` -> `ModeController` -> `app.mode_changed`);
  - отсутствие прямых `state_manager.set_mode` вне bridge/callback;
  - предсказуемый startup-лог по REQ-006.

## Запрос/цель
Проверить крепкость управления клиентом при запуске, как работает поток, есть ли дубли, конфликты, гонки и места для централизации.

## Контекст
- Файлы:
  - `main.py`
  - `integration/core/simple_module_coordinator.py`
  - `integration/core/integration_factory.py`
  - `integration/integrations/mode_management_integration.py`
  - `integration/workflows/base_workflow.py`
  - `integration/integrations/first_run_permissions_integration.py`
  - `integration/core/event_bus.py`
  - `integration/core/gateways/permission_gateways.py`
- Документы:
  - `AGENTS.md`
  - `Docs/PROJECT_REQUIREMENTS.md`
  - `Docs/ARCHITECTURE_OVERVIEW.md`
  - `../Docs/_archive/ASSISTANT_COORDINATION_PROTOCOL.md`
  - `../Docs/_archive/CODEX_PROMPT.md`
  - `../Docs/_archive/ANTIGRAVITY_PROMPT.md`
  - `../Docs/_archive/assistant_exchange/TEMPLATE.md`

## Решения/выводы
- Архитектурный каркас устойчивый: coordinator + event bus + mode controller + gateways.
- Найдены 4 критичных точки централизации: initialize-order, direct set_mode bypass, AppMode fallback duplication, first-run fail-open policy ambiguity.
- Базовые архитектурные тесты проходят, но часть проверок по init-order фактически пропущена (`skipped`) и не закрывает реальный риск.

## Открытые вопросы
- Должен ли first-run при ошибке V2 всегда продолжать startup (`fail-open`) или блокировать (`fail-closed`) в production?

## Следующие шаги
- Внести точечные правки по 5 шагам из раздела Optimal Fix и добавить отдельный тест на одинаковый порядок `initialize/start`.
