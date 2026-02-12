# MCP Actions Duplication/Race/Centralization Audit

## Метаданные
- Ассистент: codex
- Тип: analysis
- Дата: 2026-02-11
- ID (INS-###): INS-N/A

## Diagnosis
MCP pipeline в целом централизован (ingress: `GrpcClientIntegration`, execution owner: `ActionExecutionIntegration`), но есть 2 критичных race/consistency дефекта в runtime cleanup и browser cancel path.

## Root Cause
Неполный lifecycle cleanup и частично session-less terminal events → stale runtime state (`_active_actions`, `_active_browser_sessions`) → ложные блокировки/залипания PROCESSING и конфликтные повторные команды.

## Optimal Fix
Цель: убрать залипание runtime-состояния и сохранить единого владельца MCP execution без новых локальных обходов.

Architecture Fit:
- Логика остаётся в текущих владельцах: `ActionExecutionIntegration` (исполнение/cleanup) и `BrowserUseIntegration` (terminal events).

Where it belongs:
- `integration/integrations/action_execution_integration.py`
- `integration/integrations/browser_use_integration.py`
- точечно `integration/core/integration_factory.py` (gate включения action owner)

Source of Truth:
- Action execution lifecycle: `ActionExecutionIntegration` + `actions.lifecycle.*`
- Browser terminal lifecycle: `BrowserUseIntegration` (`browser.*` с валидным `session_id`)

Breaks architecture: no

Implementation Plan:
1. Добавить единый `finally` cleanup в `_execute_action()` (pop `_active_actions[session_id]`, cleanup `_active_apps` по `close_app`).
2. Убрать дублирующий/неполный cleanup из fallback-веток, чтобы остался один owner cleanup-path.
3. В `BrowserUseIntegration._on_cancel_request` публиковать `browser.cancelled` по активным session_id (или хотя бы с реальным session_id), не с фиктивным `'cancelled'`.
4. В `BrowserUseIntegration._run_process` для exception/cancel включать `session_id` из request в terminal event.
5. В `IntegrationFactory` gate `action_execution` перевести с `open_app.enabled` на агрегированный owner flag (`features.actions` + open/close), чтобы не терять close_app при выключенном open_app.
6. Добавить regression-тесты на cleanup/idempotency и на browser-cancel session ownership.

Code Touchpoints:
- `integration/integrations/action_execution_integration.py`
- `integration/integrations/browser_use_integration.py`
- `integration/core/integration_factory.py`

Concurrency Guard (if needed):
- `state-guard` + `idempotency` через существующий `_actions_lock` и canonical terminal events.

What to remove / merge:
- Убрать разрозненный cleanup в fallback как второй путь; оставить единый cleanup owner в `_execute_action.finally`.

## Verification
- DoD:
  - После успешного open/close нет stale `_active_actions`.
  - Повторный action в новой/той же сессии не блокируется ложным `already running`.
  - После browser cancel ModeManagement получает terminal с корректным `session_id` и не залипает в PROCESSING.
- Шаги:
  1. Unit test: open_app success -> `_active_actions` очищен.
  2. Unit test: close_app MCP success -> `_active_apps` очищен.
  3. Integration test: browser cancel -> публикуется `browser.cancelled` с реальным `session_id`.
  4. Integration test: processing with browser action then cancel -> проходит в SLEEPING.

## Pre-Change Gate Evidence (обязательно)
- Прочитанные документы:
  - `../Docs/DOCS_INDEX.md`
  - `../Docs/PRE_CHANGE_CHECKLIST.md`
  - `../Docs/ASSISTANT_COORDINATION_PROTOCOL.md`
  - `../Docs/PROJECT_REQUIREMENTS.md` (REQ-001/003/006/007/021 релевантные секции)
  - `../Docs/ARCHITECTURE_OVERVIEW.md` (централизация coordinator/event ownership)
  - `../Docs/FEATURE_FLAGS.md`
  - `Docs/DOCS_INDEX.md`
  - `Docs/PRE_CHANGE_CHECKLIST.md`
  - `Docs/PROJECT_REQUIREMENTS.md`
  - `Docs/ARCHITECTURE_OVERVIEW.md`
  - `Docs/FLOW_INTERACTION_SPEC.md`
  - `Docs/STATE_CATALOG.md`
  - `Docs/FEATURE_FLAGS.md`
- Source of Truth:
  - Action ingress: `integration/integrations/grpc_client_integration.py` (`grpc.response.action`)
  - Action execution owner: `integration/integrations/action_execution_integration.py`
  - Mode guard owner: `integration/integrations/mode_management_integration.py`
- Дублирование:
  - Найдено: cleanup active action state частично в fallback-ветках, отсутствует общий cleanup в основном MCP-path.
  - Единый владелец после фикса: `_execute_action.finally`.
- Feature Flags check:
  - Реестр: `Docs/FEATURE_FLAGS.md` (`actions.*`, `features.actions`, `features.browser`, `features.messages`, `features.payment`).
  - Риск: `IntegrationFactory` включает owner по `open_app`-флагу, не по агрегированному actions-owner.
- Race check:
  - Сценарий 1: success path оставляет stale `_active_actions` -> ложный dedupe/already-running.
  - Сценарий 2: browser cancel без валидного `session_id` -> не снимается active browser session в mode guard.
  - Guard: centralized terminal events + cleanup under `_actions_lock`.

## Запрос/цель
Проверить корректность логики получения/обработки MCP действий на дубли, конфликты, гонки и централизацию.

## Контекст
- Файлы:
  - `integration/integrations/grpc_client_integration.py`
  - `integration/integrations/action_execution_integration.py`
  - `integration/integrations/mode_management_integration.py`
  - `integration/integrations/browser_use_integration.py`
  - `integration/core/integration_factory.py`
- Документы:
  - canonical docs из Pre-Change Gate (см. выше)
- Ограничения:
  - Без реархитектуры, внутри текущих owners/слоёв.

## Решения/выводы
- Централизация по MCP в основе корректная.
- Есть 2 существенных runtime дефекта (cleanup + browser cancel session ownership), которые создают риск гонок/залипаний.

## Найденные проблемы (если review)
- P1: stale `_active_actions` в основном MCP execution path.
- P1: session-less browser cancel terminal events.
- P2: gate включения ActionExecutionIntegration привязан только к `open_app`.

## Открытые вопросы
- Нужен ли жёсткий `features.actions` как единственный глобальный gate для action owner?

## Следующие шаги
- Внести точечные фиксы по 3 touchpoints и добавить regression-тесты cleanup/cancel-session.
