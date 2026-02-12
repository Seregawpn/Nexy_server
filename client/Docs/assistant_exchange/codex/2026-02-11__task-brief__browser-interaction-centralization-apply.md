# Browser Interaction Centralization Apply

## Метаданные
- Ассистент: codex
- Тип: task-brief
- Дата: 2026-02-11
- ID (INS-###): N/A

## Diagnosis
Browser interaction имел нецентрализованный cancel-path и дрейф event-контракта (`browser.use.request` vs `browser.task_request`, `browser.completion` vs `browser.completed`).

## Root Cause
Несколько параллельных точек отмены и частично устаревший namespace событий → риск кросс-сессионной отмены, дублей terminal-событий и выключенного progress-consumer из-за default config.

## Optimal Fix
- Централизован cancel через session-scoped обработку в `BrowserUseIntegration`.
- Убрана прямая подписка на `keyboard.short_press` в browser integration (нет обхода interrupt-owner).
- Канонизирован dispatch события browser-задачи на `browser.task_request` (alias оставлен в подписках для обратной совместимости).
- Подключен реальный конфиг `browser_use` в `BrowserProgressIntegrationConfig` при создании интеграций.
- Выравнен docs-контракт на `browser.completed`.

## Verification
- `PYTHONPATH=. pytest -q tests/test_client_server_flow_contracts.py -q` → passed.
- Добавлен regression test: session cancel не отменяет соседние browser-сессии.
- `PYTHONPATH=. python3 tests/verify_latency_fix.py` запускается, но сценарий завершается `TEST FAILED: No immediate feedback detected` из-за локально отсутствующего `browser_use` пакета (ожидаемо для окружения без browser-use).

## Pre-Change Gate Evidence (обязательно)
- Прочитанные документы:
  - `../AGENTS.md`
  - `Docs/DOCS_INDEX.md`
  - `Docs/PRE_CHANGE_CHECKLIST.md`
  - `Docs/PROJECT_REQUIREMENTS.md` (REQ-006, REQ-007, REQ-009)
  - `Docs/ARCHITECTURE_OVERVIEW.md`
  - `../Docs/ASSISTANT_COORDINATION_PROTOCOL.md`
  - `Docs/FEATURE_FLAGS.md`
  - `Docs/FLOW_INTERACTION_SPEC.md`
  - `Docs/STATE_CATALOG.md`
- Source of Truth:
  - Event contracts: `Docs/FLOW_INTERACTION_SPEC.md`
  - Runtime константы: `integration/core/event_types.py`
  - Интеграционный owner: `integration/integrations/browser_use_integration.py`
- Дублирование:
  - Было: параллельные request/cancel path (`browser.use.request` + direct keyboard path).
  - Стало: canonical `browser.task_request`, direct keyboard bypass removed.
- Feature Flags check:
  - Без добавления новых флагов.
  - Использован текущий owner path `features.browser` + `browser_use` config section.
- Race check:
  - Сценарий: cancel одной browser-сессии может затронуть другие.
  - Guard: session-scoped task selection + idempotent manual cancel suppression.

## Запрос/цель
Настроить browser interaction: убрать конфликты/гонки и усилить централизацию.

## Контекст
- Файлы:
  - `integration/integrations/browser_use_integration.py`
  - `integration/integrations/action_execution_integration.py`
  - `integration/core/integration_factory.py`
  - `integration/core/event_types.py`
  - `Docs/FLOW_INTERACTION_SPEC.md`
  - `tests/test_client_server_flow_contracts.py`
  - `tests/verify_latency_fix.py`

## Решения/выводы
- Session-scoped cancel внедрен.
- Browser request event канонизирован.
- BrowserProgressIntegration теперь реально активируется по конфигу.

## Открытые вопросы
- После окончания миграции удалить legacy alias `browser.use.request`.

## Следующие шаги
- Добавить e2e тест, где одновременно выполняются 2 browser task и подтверждается отсутствие cross-session cancel в полном runtime.
