# Remove direct state access in permissions v2 integration

## Метаданные
- Ассистент: codex
- Тип: task-brief
- Дата: 2026-02-11
- ID (INS-###): N/A

## Diagnosis
`problem_scan` блокировался в том числе из-за прямого доступа к state: `modules/permissions/v2/integration.py:412`.

## Root Cause
В V2 integration использовался `state_manager.get_state_data(...)` напрямую, что нарушает правило доступа через selectors/gateways.

## Optimal Fix
Заменен direct access на `selectors.get_state_value(...)` в `_publish_ready_to_greet`.

## Verification
- `python3 scripts/verify_no_direct_state_access.py` → `No direct state access violations detected.`
- `python3 -m py_compile modules/permissions/v2/integration.py` → OK
- `./.venv/bin/ruff check modules/permissions/v2/integration.py integration/integrations/payment_integration.py` → OK
- `./scripts/problem_scan_gate.sh` → `TOTAL_ISSUES=410`, `BLOCKING_ISSUES=259` (улучшение на 1)

## Pre-Change Gate Evidence (обязательно)
- Прочитанные документы: `Docs/PROJECT_REQUIREMENTS.md`, `Docs/ARCHITECTURE_OVERVIEW.md`, `Docs/ASSISTANT_COORDINATION_PROTOCOL.md`, `Docs/FEATURE_FLAGS.md`, `Docs/PRE_CHANGE_CHECKLIST.md`, `Docs/DOCS_INDEX.md`.
- Source of Truth: `integration/core/selectors.py` (доступ к state), `ApplicationStateManager`.
- Дублирование: none.
- Feature Flags check: none.
- Race check: none.

## Следующие шаги
- Дальше можно разбирать top rule `I001/F401/UP045` пачками по файлам с максимальным вкладом.
