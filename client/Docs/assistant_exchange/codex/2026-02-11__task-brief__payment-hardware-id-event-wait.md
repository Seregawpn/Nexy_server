# Payment Hardware ID Event Wait

## Метаданные
- Ассистент: codex
- Тип: task-brief
- Дата: 2026-02-11
- ID (INS-###): N/A

## Diagnosis
В `PaymentIntegration` использовался локальный polling-loop (`sleep`) для ожидания `hardware_id`, что дублировало event-driven подход owner-интеграции.

## Root Cause
Потребитель реализовал собственный wait path вместо единого event-контракта `hardware.id_request`/`hardware.id_obtained`.

## Optimal Fix
Переведен checkout path на event-driven ожидание через `asyncio.Event` и helper `_ensure_hardware_id_ready()` без polling.

## Verification
- `python3 -m py_compile integration/integrations/payment_integration.py`
- `python3 integration/scripts/verify_payment_integration.py`
- `python3 integration/scripts/verify_payment_404_fallback.py`

## Pre-Change Gate Evidence (обязательно)
- Прочитанные документы: `AGENTS.md`, `Docs/DOCS_INDEX.md`, `Docs/PRE_CHANGE_CHECKLIST.md`, `Docs/PROJECT_REQUIREMENTS.md`, `Docs/ARCHITECTURE_OVERVIEW.md`, `Docs/ASSISTANT_COORDINATION_PROTOCOL.md`, `Docs/FEATURE_FLAGS.md`, `Docs/FLOW_INTERACTION_SPEC.md`, `Docs/STATE_CATALOG.md`.
- Source of Truth: `integration/integrations/hardware_id_integration.py`.
- Дублирование: removed local polling wait in `integration/integrations/payment_integration.py`.
- Feature Flags check: none.
- Race check: replaced polling with event wait to reduce concurrent wait races.

## Следующие шаги
- При необходимости вынести общий helper ожидания `hardware_id` в shared integration utility и переиспользовать между интеграциями.
