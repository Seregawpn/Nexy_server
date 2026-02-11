# Screenshot Cache Eviction (Bounded)

## Метаданные
- Ассистент: codex
- Тип: task-brief
- Дата: 2026-02-11
- ID (INS-###): INS-UNASSIGNED

## Diagnosis
Кэш `screenshot.captured` (`_published_sessions`, `_captured_by_session`) рос без лимита при долгом uptime.

## Root Cause
Отсутствовал bounded eviction в session-scoped screenshot replay/idempotency слое.

## Optimal Fix
- Добавлен bounded cache:
  - `_published_order: deque[str]`
  - `_published_sessions_max: int = 128`
  - `_evict_published_cache_if_needed()`
- Eviction выполняется централизованно в owner-методе `_publish_captured(...)`.
- Старейшие session keys удаляются из `_published_sessions` и `_captured_by_session`.

## Verification
- `PYTHONPATH=. pytest -q tests/test_screenshot_capture_regressions.py tests/test_client_server_flow_contracts.py tests/test_interrupt_management_contract.py -q` ✅
- Добавлен тест: `test_screenshot_publish_cache_eviction_allows_republish`.

## Pre-Change Gate Evidence (обязательно)
- Прочитанные документы: `Docs/PROJECT_REQUIREMENTS.md`, `Docs/ARCHITECTURE_OVERVIEW.md`, `Docs/FLOW_INTERACTION_SPEC.md`, `Docs/STATE_CATALOG.md`, `Docs/PRE_CHANGE_CHECKLIST.md`.
- Source of Truth: `session_id` + owner `ScreenshotCaptureIntegration`.
- Дублирование: не добавлено, логика eviction интегрирована в существующий owner метод.
- Feature Flags check: none.
- Race check: bounded eviction не вводит второй путь публикации; contract `_publish_captured` сохранён как единый.

## Запрос/цель
Сделать bounded eviction для screenshot replay cache и закрепить тестом.

## Контекст
- `/Users/sergiyzasorin/Fix_new/client/integration/integrations/screenshot_capture_integration.py`
- `/Users/sergiyzasorin/Fix_new/client/tests/test_screenshot_capture_regressions.py`

## Решения/выводы
- Рост памяти по этому кэшу ограничен.
- Поведение idempotency/replay сохранено и проверено тестом.

## Открытые вопросы
- Нужен ли runtime-config для `_published_sessions_max` через unified config.

## Следующие шаги
- При необходимости вынести cache-limit в конфиг и добавить тест на override.
