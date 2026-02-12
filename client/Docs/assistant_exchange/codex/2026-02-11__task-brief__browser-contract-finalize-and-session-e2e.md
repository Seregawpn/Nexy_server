# Browser Contract Finalize And Session E2E

## Метаданные
- Ассистент: codex
- Тип: task-brief
- Дата: 2026-02-11
- ID (INS-###): N/A

## Diagnosis
Оставался legacy alias `browser.use.request` и отсутствовала e2e-проверка terminal-изоляции между параллельными browser-сессиями.

## Root Cause
Неполная миграция на канонический topic + недостаточная regression-проверка параллельного cancel → риск возврата к нецентрализованному route.

## Optimal Fix
- Удален legacy subscribe `browser.use.request` из `BrowserUseIntegration`.
- Оставлен только canonical `browser.task_request` во входном path.
- Усилен e2e-regression: проверка, что cancel `sid-a` не эмитит `browser.cancelled` для `sid-b`.
- Синхронизирован `Docs/ARCHITECTURE_OVERVIEW.md` с фактическими подписками browser integration.

## Verification
- `PYTHONPATH=. pytest -q tests/test_client_server_flow_contracts.py -q` → passed (7 tests).
- `PYTHONPATH=. python3 tests/verify_latency_fix.py` → запускается, но fail по ожидаемой причине среды: `browser_use` не установлен (`No module named 'browser_use'`).

## Pre-Change Gate Evidence (обязательно)
- Прочитанные документы:
  - `../AGENTS.md`
  - `Docs/DOCS_INDEX.md`
  - `Docs/PRE_CHANGE_CHECKLIST.md`
  - `Docs/PROJECT_REQUIREMENTS.md`
  - `Docs/ARCHITECTURE_OVERVIEW.md`
  - `../Docs/ASSISTANT_COORDINATION_PROTOCOL.md`
  - `Docs/FEATURE_FLAGS.md`
  - `Docs/FLOW_INTERACTION_SPEC.md`
- Source of Truth:
  - `Docs/FLOW_INTERACTION_SPEC.md` (browser contract)
  - `integration/core/event_types.py` (runtime constants)
  - `integration/integrations/browser_use_integration.py` (execution owner)
- Дублирование:
  - Было: `browser.task_request` + legacy `browser.use.request`.
  - Стало: единый owner path `browser.task_request`.
- Feature Flags check: новых флагов не добавлено.
- Race check:
  - Сценарий: cancel одной session может затронуть вторую.
  - Guard: session-scoped cancel + e2e test на изоляцию terminal-событий.

## Запрос/цель
Выполнить дальнейшие шаги: убрать alias, добавить e2e и досинхронизировать docs.

## Контекст
- Файлы:
  - `integration/integrations/browser_use_integration.py`
  - `integration/integrations/action_execution_integration.py`
  - `Docs/FLOW_INTERACTION_SPEC.md`
  - `Docs/ARCHITECTURE_OVERVIEW.md`
  - `tests/test_client_server_flow_contracts.py`

## Решения/выводы
- Browser request contract окончательно централизован.
- Cross-session cancel regression зафиксирован тестом.

## Открытые вопросы
- Для runtime smoke нужен установленный пакет `browser_use` в окружении проверки.

## Следующие шаги
- Прогнать `tests/verify_latency_fix.py` на стенде с установленным `browser_use` и Gemini credentials.
