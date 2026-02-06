# Task Brief

## Context
После проверки основных packaging-документов оставался drift в trace-матрице `Docs/PROJECT_REQUIREMENTS.md` для REQ-015/REQ-018.

## Changes
Обновлены строки таблицы трассировки требований:
- REQ-015:
  - Implementation: `Docs/PACKAGING_FINAL_GUIDE.md`, `packaging/build_final.sh`
  - Verification: `Docs/PRE_PACKAGING_VERIFICATION.md`, `scripts/run_release_suite.py`
- REQ-018:
  - Implementation: `Docs/PRE_PACKAGING_VERIFICATION.md`, `Docs/PACKAGING_READINESS_CHECKLIST.md`
  - Verification: `scripts/problem_scan_gate.sh`, `scripts/run_release_suite.py`, checklist в PR

## Verification
- Проверена обновленная таблица: `Docs/PROJECT_REQUIREMENTS.md` (строки REQ-015/REQ-018).

## Impact
Trace-матрица теперь синхронизирована с текущим release/quality процессом упаковки.
