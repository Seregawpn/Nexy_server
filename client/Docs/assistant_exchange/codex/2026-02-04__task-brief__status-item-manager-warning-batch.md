# Task Brief

## Context
Следующим top-файлом после short-fix был `modules/tray_controller/macos/status_item_manager.py` (16 warning basedpyright).

## Changes
- Убрано переопределение UPPERCASE class-констант в `__init__`:
  - введены runtime-поля `_circuit_open_threshold`, `_circuit_open_duration_sec`, `_max_attempts_per_series`, `_initial_backoff_ms`, `_max_backoff_ms`, `_backoff_multiplier`, `_jitter_percent`, `_control_center_ready_timeout_sec`, `_first_attempt_delay_ms`, `_final_timeout_ms`, `_background_retry_interval_sec`.
- Конфиг теперь заполняет runtime-поля, а не class-константы.
- Обновлены внутренние расчеты/логи на runtime-поля (`_open_circuit`, `calculate_backoff_ms`, circuit checks).
- Исправлены типы в backoff:
  - `backoff_ms` теперь `int`, совместим с `StatusItemMetrics.backoff_next_ms`.
- Исправлена сигнатура:
  - `wait_for_control_center_ready(self, timeout_sec: float | None = None)`.
- Убраны неизвестные символы `AppKit.NSStatusBar/NSWorkspace`:
  - безопасный доступ через `getattr(..., None)` + guards.

## Verification
- `./.venv/bin/ruff check modules/tray_controller/macos/status_item_manager.py` → OK
- `../server/.venv/bin/basedpyright modules/tray_controller/macos/status_item_manager.py --outputjson` → 0 diagnostics
- `./scripts/problem_scan.sh` → `TOTAL_ISSUES=336`
- `REQUIRE_BASEDPYRIGHT_IN_SCAN=true ./scripts/problem_scan_gate.sh` → PASSED

## Impact
- В `status_item_manager.py`: warning reduced `16 -> 0`.
- Общий backlog reduced: `352 -> 336`.
- Конфиг status-item retry/circuit теперь применяется без нарушения typing-контракта class constants.
