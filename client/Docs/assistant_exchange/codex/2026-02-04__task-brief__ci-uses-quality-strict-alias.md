# Task Brief: CI uses quality_strict alias

## Goal
Продолжить централизацию проверки: убрать дублирование strict-флагов в CI и запускать единый strict entrypoint.

## Changes
1. `.github/workflows/ci.yml`
- В job `pre-build-gate` запуск заменен на:
  - `./scripts/quality_strict.sh --verbose`
- Ранее было:
  - `./scripts/pre_build_gate.sh --verbose --require-basedpyright`

## Verification
- YAML parse `ci.yml` -> OK
- `scripts/quality_strict.sh --skip-tests --skip-gui` -> FAIL ожидаемо (strict mode, basedpyright отсутствует локально)

## Result
- CI и локальный строгий запуск теперь используют один и тот же entrypoint (`quality_strict.sh`).
- Меньше риска рассинхрона параметров strict-режима между CI и ручными запусками.
