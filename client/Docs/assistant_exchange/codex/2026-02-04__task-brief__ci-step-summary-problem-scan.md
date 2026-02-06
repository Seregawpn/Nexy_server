# Task Brief: CI step summary for problem scan

## Goal
Следующий шаг после hard-gate: сделать результаты scan видимыми прямо в UI workflow без скачивания артефактов.

## Changes
1. `.github/workflows/ci.yml`
- Добавлен шаг `Publish problem scan summary` (if: always).
- Шаг публикует `build_logs/problem_scan_latest.md` в `$GITHUB_STEP_SUMMARY`.
- Если отчет не найден, пишет fallback сообщение.

## Verification
- YAML parse `ci.yml` -> OK
- `scripts/problem_scan_gate.sh` -> PASS (`TOTAL_ISSUES=0`)

## Result
- В каждом CI run проблема/статусы видны сразу на странице job.
- Артефакты остаются для детального анализа, summary — для быстрого просмотра.
