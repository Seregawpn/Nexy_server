# Browser Interaction Centralization Audit

## Метаданные
- Ассистент: codex
- Тип: analysis
- Дата: 2026-02-11
- ID (INS-###): N/A

## Diagnosis
В browser interaction есть неконсистентные event-контракты, нецентрализованные точки отмены и конфиг-путь, который фактически отключает BrowserProgressIntegration.

## Root Cause
Разрозненные владельцы cancel/event namespace + частичное расхождение с каноническим FLOW_INTERACTION_SPEC → параллельные пути и неоднозначные terminal-сигналы → риск ложных отмен/дублированных lifecycle событий.

## Optimal Fix
- Цель: оставить один owner для browser cancel/task lifecycle и один контракт событий.
- Где в архитектуре: integration layer (`ActionExecutionIntegration` как ingress, `BrowserUseIntegration` как execution owner, `BrowserProgressIntegration` как progress consumer).
- Source of Truth: `Docs/FLOW_INTERACTION_SPEC.md` + `integration/core/event_types.py`.
- План:
  1. Канонизировать browser request/cancel события (`browser.task_request` + session-scoped cancel), оставить alias только на миграцию.
  2. Убрать прямую подписку `BrowserUseIntegration` на `keyboard.short_press`; принимать cancel только от централизованного interrupt/cancel канала.
  3. Сделать session-scoped cancel в `BrowserUseIntegration` (не global cancel всех задач по умолчанию).
  4. Подключить реальный config для `BrowserProgressIntegrationConfig` из `unified_config.yaml`.
  5. Привести terminal событие к единому имени (`browser.completed` vs `browser.completion`) и payload (обязательный `session_id`, валидный timestamp).

## Verification
- Проверить, что `browser.cancelled` всегда с `session_id` и не отменяет соседние browser-сессии.
- Проверить, что `keyboard.short_press` не обходит owner interrupt-потока.
- Проверить, что BrowserProgressIntegration реально subscribes/обрабатывает `browser.progress` при enabled=true.

## Pre-Change Gate Evidence (обязательно)
- Прочитанные документы:
  - `../AGENTS.md`
  - `Docs/DOCS_INDEX.md`
  - `Docs/PRE_CHANGE_CHECKLIST.md`
  - `Docs/PROJECT_REQUIREMENTS.md` (REQ-006, REQ-007, REQ-009)
  - `Docs/ARCHITECTURE_OVERVIEW.md` (централизация mode/event ownership)
  - `../Docs/ASSISTANT_COORDINATION_PROTOCOL.md`
  - `Docs/FEATURE_FLAGS.md`
  - `Docs/FLOW_INTERACTION_SPEC.md` (3.13, 4.6)
  - `Docs/STATE_CATALOG.md`
  - `../Docs/CODEX_PROMPT.md`, `../Docs/ANTIGRAVITY_PROMPT.md`, `../Docs/assistant_exchange/TEMPLATE.md`
- Source of Truth: Event contract в `Docs/FLOW_INTERACTION_SPEC.md`, константы в `integration/core/event_types.py`, orchestration в `integration/core/integration_factory.py`.
- Дублирование: найдено пересечение cancel-путей (`keyboard.short_press` direct + interrupt chain); единый владелец должен быть interrupt/cancel orchestration.
- Feature Flags check: найдены пересекающиеся browser-флаги (`actions.browser_use`, `features.browser`, `features.browser_use`) — требуется унификация owner-решения.
- Race check: найден сценарий global cancel без session scoping в browser integration.

## Запрос/цель
Проверить browser-interaction файлы на гонки, конфликты и нецентрализацию.

## Контекст
- Файлы:
  - `integration/integrations/browser_use_integration.py`
  - `integration/integrations/browser_progress_integration.py`
  - `integration/integrations/action_execution_integration.py`
  - `integration/core/integration_factory.py`
  - `integration/core/event_types.py`
  - `modules/browser_automation/module.py`
  - `config/unified_config.yaml`
- Ограничения: без изменения архитектуры и без введения новых state-осей.

## Решения/выводы
- Есть критические точки нецентрализации и race-risk в browser cancel path.
- Есть конфигурационный конфликт: BrowserProgressIntegration создается, но по умолчанию disabled и config не пробрасывается.
- Есть контрактный дрейф event names/payload относительно FLOW spec.

## Открытые вопросы
- Каноничное terminal имя для браузера: `browser.completed` или `browser.completion`?
- Должен ли `grpc.request_cancel` отменять только browser task той же session_id или весь browser subsystem при системном interrupt?

## Следующие шаги
- Подготовить патч унификации cancel/event contract и добавить тесты на session-scoped cancel.
