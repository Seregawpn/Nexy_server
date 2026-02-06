# Task Brief: scanner PYTHONPATH update and rescan

## Goal
Убрать ложный pytest import-blocker в агрегированном скане и перезапустить полный scan.

## Changes
1. `scripts/scan_problem_list.py`
- В subprocess env расширен `PYTHONPATH`:
  - добавлен root проекта
  - добавлен parent root
- Это устраняет конфликт import-layout (`integration.*` и `client.*`) при запуске pytest из сканера.

## Verification
- `scripts/problem_scan.sh` -> OK
- Новый snapshot:
  - `build_logs/problem_scan_latest.json`
  - `build_logs/problem_scan_latest.md`
- `TOTAL_ISSUES=3`

## Current issues (after rescan)
- `pytest` failures:
  - `tests/test_webp_screenshot.py::test_webp_capture`
  - `tests/test_webp_screenshot.py::test_jpeg_fallback`
  - `tests/test_webp_screenshot.py::test_quality_levels`
- Message: `async def functions are not natively supported`.

## Result
- Scanner теперь доходит до реальных тестовых проблем (вместо раннего import error).
