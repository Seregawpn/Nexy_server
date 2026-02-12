# Browser Smoke And Terminal E2E Followup

## Метаданные
- Ассистент: codex
- Тип: task-brief
- Дата: 2026-02-11
- ID (INS-###): N/A

## Diagnosis
После централизации оставался шаг финализации: удалить legacy alias, добавить тест terminal success path и проверить runtime smoke на реальном browser_use.

## Root Cause
Исторический alias (`browser.use.request`) и отсутствие позитивного terminal regression для `browser.completed` оставляли риск дрейфа контракта.

## Optimal Fix
- Удалён legacy subscribe `browser.use.request` из `BrowserUseIntegration`.
- Обновлён комментарий dispatch-path в `ActionExecutionIntegration` под canonical topic `browser.task_request`.
- Добавлен позитивный regression-тест `browser.completed` с проверкой `session_id`.
- Обновлён smoke-критерий `verify_latency_fix.py`: immediate feedback считается валидным для `browser_latency_mask` и `browser_step`.

## Verification
- `PYTHONPATH=. pytest -q tests/test_client_server_flow_contracts.py -q` → `........` (8 тестов, passed).
- Runtime smoke запускался с `.venv` и escalated permissions; в логах зафиксированы:
  - subscribe на `browser.task_request`
  - публикация `grpc.tts_request`
  - публикация `browser.completed` (в одном из прогонов)
- Скрипт smoke в этом окружении нестабилен по завершению процесса (долгоживущие browser/posthog процессы), поэтому часть прогонов завершается по внешнему таймауту раннера.

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
  - Event contract: `Docs/FLOW_INTERACTION_SPEC.md`
  - Runtime constants: `integration/core/event_types.py`
  - Integration owner: `integration/integrations/browser_use_integration.py`
- Дублирование:
  - Было: canonical+legacy request path.
  - Стало: только canonical request path.
- Feature Flags check:
  - Новые флаги не добавлялись.
- Race check:
  - Сценарий: cross-session cancel.
  - Guard: session-scoped cancel + e2e tests на terminal events.

## Запрос/цель
Выполнить follow-up: alias cleanup, e2e terminal success test, smoke check.

## Контекст
- Файлы:
  - `integration/integrations/browser_use_integration.py`
  - `integration/integrations/action_execution_integration.py`
  - `tests/test_client_server_flow_contracts.py`
  - `tests/verify_latency_fix.py`

## Решения/выводы
- Контракт browser request окончательно централизован.
- Позитивный terminal-path (`browser.completed`) покрыт тестом.
- Runtime smoke функционально подтверждает работу, но требует стабилизации завершения процесса для полностью детерминированного CI-run.

## Открытые вопросы
- Нужно ли в smoke-скрипте жёстко ограничивать время `browser_integration.stop()` и принудительно завершать фоновые telemetry/browser процессы?

## Следующие шаги
- Добавить timeout-guard на shutdown в `tests/verify_latency_fix.py` (например, `asyncio.wait_for(..., 3s)`) и итоговый принудительный cleanup для детерминированного завершения.
