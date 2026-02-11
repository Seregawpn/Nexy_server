# Session Contract Hardening: Cancel + Tests

## Метаданные
- Ассистент: codex
- Тип: task-brief
- Дата: 2026-02-11
- ID (INS-###): INS-UNASSIGNED

## Diagnosis
После удаления fallback в gRPC оставался publisher `grpc.request_cancel` с `session_id=None` в interrupt-owner path.

## Root Cause
Смешанный legacy-контракт (допуск sessionless cancel) конфликтовал с новым строгим session-scoped behavior.

## Optimal Fix
- `InterruptManagementIntegration`: не публиковать `grpc.request_cancel`, если `session_id` отсутствует.
- Тесты: обновлен контрактный тест gRPC cancel (без fallback), добавлены проверки screenshot idempotency/replay и новый тест на reject sessionless cancel.

## Verification
- `PYTHONPATH=. pytest -q tests/test_screenshot_capture_regressions.py tests/test_client_server_flow_contracts.py tests/test_interrupt_management_contract.py -q` ✅

## Pre-Change Gate Evidence (обязательно)
- Прочитанные документы: `Docs/FLOW_INTERACTION_SPEC.md`, `Docs/STATE_CATALOG.md`, `Docs/ARCHITECTURE_OVERVIEW.md`, `Docs/PRE_CHANGE_CHECKLIST.md`, `Docs/PROJECT_REQUIREMENTS.md`.
- Source of Truth: session-scoped EventBus payload + `ApplicationStateManager`.
- Дублирование: убран скрытый sessionless publish-путь для cancel.
- Feature Flags check: none.
- Race check: межсессионная отмена без `session_id` исключена.

## Запрос/цель
Продолжить: “что далее” → закрепить контракт тестами и проверить publisher’ы.

## Контекст
- `/Users/sergiyzasorin/Fix_new/client/integration/integrations/interrupt_management_integration.py`
- `/Users/sergiyzasorin/Fix_new/client/tests/test_client_server_flow_contracts.py`
- `/Users/sergiyzasorin/Fix_new/client/tests/test_screenshot_capture_regressions.py`
- `/Users/sergiyzasorin/Fix_new/client/tests/test_interrupt_management_contract.py`

## Решения/выводы
- Cancel path стал полностью session-scoped.
- Screenshot replay теперь только controlled replay с reason.

## Открытые вопросы
- Нужен ли лимит на хранение `_captured_by_session` (TTL/size bound).

## Следующие шаги
- Добавить bounded eviction для `_captured_by_session` при долгом uptime.
