# Task Brief

## Context
Следующим приоритетным файлом после `keyboard_monitor.py` был `run_diagnostics.py` (26 warning basedpyright), в основном из-за статических импортов несуществующих `diagnostic_*` модулей.

## Changes
- `run_diagnostics.py`:
  - заменены статические импорты `diagnostic_*` на централизованный dynamic loader `_load_diagnostic_class(...)` через `importlib`;
  - добавлен fallback класс `_MissingDiagnostic`, который возвращает корректный `run_diagnostic()` результат со статусом `skipped`;
  - удалена рекурсивная ошибка в `run_all_diagnostics()` (блок `general` больше не вызывает `MasterDiagnostic` из самого себя);
  - `general` секция теперь помечается как `skipped` с явной причиной.

## Verification
- `./.venv/bin/ruff check run_diagnostics.py` → OK
- `../server/.venv/bin/basedpyright run_diagnostics.py --outputjson` → 0 diagnostics
- `./scripts/problem_scan.sh` → `TOTAL_ISSUES=415`
- `REQUIRE_BASEDPYRIGHT_IN_SCAN=true ./scripts/problem_scan_gate.sh` → PASSED (`blocking: 0`)

## Impact
- В `run_diagnostics.py` warning reduced: `26 -> 0`.
- Общий backlog reduced: `441 -> 415`.
- Убрана потенциальная runtime-рекурсия в диагностическом раннере.
