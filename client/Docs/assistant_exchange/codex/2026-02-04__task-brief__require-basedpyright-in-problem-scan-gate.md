# Task Brief: require basedpyright in problem scan gate

## Goal
Продолжить следующий шаг: закрыть "слепую зону" type-check в агрегированном scan-gate.

## Changes
1. `scripts/problem_scan_gate.sh`
- Добавлен контроль статуса basedpyright из `build_logs/problem_scan_latest.json`.
- Новый env-флаг:
  - `REQUIRE_BASEDPYRIGHT_IN_SCAN=true`
- Если флаг включен и `basedpyright_status != ok`, gate падает с ошибкой.

2. `.github/workflows/ci.yml`
- Для шага `Run consolidated problem scan gate` добавлен env:
  - `REQUIRE_BASEDPYRIGHT_IN_SCAN: "true"`

## Verification
- `bash -n scripts/problem_scan_gate.sh` -> OK
- YAML parse `ci.yml` -> OK
- `scripts/problem_scan_gate.sh` -> PASS (`TOTAL_ISSUES=0`)
- `REQUIRE_BASEDPYRIGHT_IN_SCAN=true scripts/problem_scan_gate.sh` -> FAIL ожидаемо локально (basedpyright_status=skipped)

## Result
- В CI problem-scan-gate теперь не пройдет, если type-layer не отсканирован.
- Полный quality gate включает и наличие списка проблем, и обязательность basedpyright-скана.
