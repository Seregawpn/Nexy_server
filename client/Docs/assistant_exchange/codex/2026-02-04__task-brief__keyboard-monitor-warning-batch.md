# Task Brief

## Context
После запуска приоритизации (`problem_scan_priority.md`) один из самых шумных файлов был `modules/input_processing/keyboard/keyboard_monitor.py` с 26 warning basedpyright.

## Changes
- Усилена типизация callback-слоя:
  - `event_callbacks: dict[KeyEventType, Callable[[KeyEvent], Any]]`
  - сигнатуры `register_callback`, `_trigger_event`, `_run_callback`.
- Устранен optional-доступ к `self.keyboard`:
  - guard в `_run_keyboard_listener`
  - безопасный доступ в `_is_target_key`.
- Централизована логика распознавания комбинации Control/N:
  - добавлены `_is_control_key` и `_is_n_key`
  - заменены дубли в `_on_key_press`, `_on_key_release`, `_is_target_key`.
- Убран неиспользуемый `press_start_time_backup`.
- Обновлен `_key_to_string` на безопасный `getattr` с проверкой типов.

## Verification
- `./.venv/bin/ruff check modules/input_processing/keyboard/keyboard_monitor.py` → OK
- `../server/.venv/bin/basedpyright modules/input_processing/keyboard/keyboard_monitor.py --outputjson` → 0 diagnostics
- `./scripts/problem_scan.sh` → `TOTAL_ISSUES=441`
- `REQUIRE_BASEDPYRIGHT_IN_SCAN=true ./scripts/problem_scan_gate.sh` → gate PASSED

## Impact
- В этом файле warning reduced: `26 -> 0`.
- Общий warning backlog reduced: `467 -> 441`.
- Логика обработки клавиш стала централизованнее (меньше дублирования и optional-risk).
