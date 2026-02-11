# Payment manage subscription hardware-id alignment

## Метаданные
- Ассистент: codex
- Тип: task-brief
- Дата: 2026-02-11
- ID (INS-###): N/A

## Diagnosis
`open_manage_subscription` использовал отдельный fail-fast путь при отсутствии `hardware_id`, что расходилось с уже унифицированным checkout-путем.

## Root Cause
Дублированная логика потребителя (`PaymentIntegration`) вместо единого event-driven wait контракта через owner `hardware_id_integration`.

## Optimal Fix
- Переиспользован helper `_ensure_hardware_id_ready()` в `open_manage_subscription`.
- Добавлен race-safe fast path после `hardware.id_request` (проверка `_hardware_id` до wait).
- Оба payment-пути (`buy/manage`) теперь используют один механизм ожидания ID без polling.

## Verification
- `python3 -m py_compile integration/integrations/payment_integration.py` ✅
- `python3 integration/scripts/verify_payment_integration.py` ✅
- `python3 integration/scripts/verify_payment_404_fallback.py` ✅
- `./scripts/problem_scan_gate.sh` ❌ (общий backlog: `BLOCKING_ISSUES=260`, не связано точечно с этим изменением)
- `./.venv/bin/ruff check integration/integrations/payment_integration.py` ✅

## Pre-Change Gate Evidence (обязательно)
- Прочитанные документы: `AGENTS.md`, `Docs/DOCS_INDEX.md`, `Docs/PRE_CHANGE_CHECKLIST.md`, `Docs/PROJECT_REQUIREMENTS.md`, `Docs/ARCHITECTURE_OVERVIEW.md`, `Docs/ASSISTANT_COORDINATION_PROTOCOL.md`, `Docs/FEATURE_FLAGS.md`, `Docs/FLOW_INTERACTION_SPEC.md`, `Docs/STATE_CATALOG.md`.
- Source of Truth: `integration/integrations/hardware_id_integration.py`.
- Дублирование: устранен второй path ожидания ID в `open_manage_subscription`.
- Feature Flags check: none.
- Race check: event-driven wait + immediate re-check `_hardware_id` после request.

## Следующие шаги
- При необходимости вынести общий helper ожидания `hardware_id` в shared utility для повторного использования интеграциями.
