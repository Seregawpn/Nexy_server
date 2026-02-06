# Task Brief: CI problem scan artifact

## Goal
Продолжить следующие шаги: закрепить централизованный скан проблем в CI и сохранять отчет как артефакт PR/пайплайна.

## Changes
1. `.github/workflows/ci.yml`
- В `pre-build-gate` job добавлены шаги:
  - `Run consolidated problem scan` (`./scripts/problem_scan.sh`)
  - `Upload problem scan report` (artifact)
- Загружаемые файлы:
  - `build_logs/problem_scan_latest.json`
  - `build_logs/problem_scan_latest.md`

## Verification
- YAML parse `ci.yml` -> OK
- `scripts/problem_scan.sh` -> OK
- `TOTAL_ISSUES=0`

## Result
- В CI теперь всегда формируется и прикладывается единый список проблем.
- Это дает быстрый доступ к actionable issue list прямо из артефактов workflow.
