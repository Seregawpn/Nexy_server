# Problem scan blocker reduction pass

## Метаданные
- Ассистент: codex
- Тип: task-brief
- Дата: 2026-02-11
- ID (INS-###): N/A

## Diagnosis
`problem_scan_gate.sh` имел высокий объём ruff-блокеров в top-файлах (`I001/F401/UP045/UP006`).

## Root Cause
Накопленные style/type-modernization нарушения в крупных модулях orchestration/input.

## Optimal Fix
Точечный авто-cleanup ruff для top файлов:
- `integration/core/simple_module_coordinator.py`
- `modules/input_processing/keyboard/mac/quartz_monitor.py`
- `integration/integrations/input_processing_integration.py`

Также закрыт отдельный blocking issue direct state access:
- `modules/permissions/v2/integration.py` (`selectors.get_state_value` вместо `state_manager.get_state_data`).

## Verification
- `ruff check` + `py_compile` по каждому изменённому файлу: OK
- `python3 scripts/verify_no_direct_state_access.py`: OK
- `./scripts/problem_scan_gate.sh` динамика:
  - старт: `TOTAL_ISSUES=411`, `BLOCKING_ISSUES=260`
  - после pass: `TOTAL_ISSUES=301`, `BLOCKING_ISSUES=150`

## Pre-Change Gate Evidence (обязательно)
- Прочитанные документы: `Docs/PROJECT_REQUIREMENTS.md`, `Docs/ARCHITECTURE_OVERVIEW.md`, `Docs/ASSISTANT_COORDINATION_PROTOCOL.md`, `Docs/FEATURE_FLAGS.md`, `Docs/PRE_CHANGE_CHECKLIST.md`, `Docs/DOCS_INDEX.md`.
- Source of Truth: `integration/core/selectors.py` + integration owners.
- Дублирование: не вводилось.
- Feature Flags check: none.
- Race check: none.

## Следующие шаги
- Продолжить cleanup по top files (`modules/tray_controller/macos/menu_handler.py`, `modules/tray_controller/core/tray_controller.py`).
