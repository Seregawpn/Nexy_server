# Task Brief: problem scan hard gate

## Goal
Следующий шаг после публикации scan-отчета: сделать enforcement, чтобы CI падал при ненулевом списке проблем.

## Changes
1. Добавлен `scripts/problem_scan_gate.sh`.
- Запускает `scripts/problem_scan.sh`.
- Читает `build_logs/problem_scan_latest.json`.
- Завершает с ошибкой, если `summary.total_issues > 0`.

2. Обновлен `.github/workflows/ci.yml`.
- Шаг `Run consolidated problem scan` заменен на
  - `Run consolidated problem scan gate`
  - `./scripts/problem_scan_gate.sh`
- Шаг загрузки артефактов остается `if: always()`, поэтому отчеты сохраняются даже при fail gate.

## Verification
- `bash -n scripts/problem_scan_gate.sh` -> OK
- YAML parse `ci.yml` -> OK
- `scripts/problem_scan_gate.sh` -> PASS (`TOTAL_ISSUES=0`)

## Result
- CI теперь не только публикует список проблем, но и блокирует pipeline при наличии issues.
