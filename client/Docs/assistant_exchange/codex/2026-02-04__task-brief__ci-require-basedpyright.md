# Task Brief: CI require basedpyright

## Goal
Сделать обязательным type-check (basedpyright) в CI, чтобы PR не проходил без проверки типизации.

## Changes
1. `scripts/pre_build_gate.sh`
- Добавлен env-флаг `REQUIRE_BASEDPYRIGHT` (default: `false`).
- Если `REQUIRE_BASEDPYRIGHT=true` и `basedpyright` не найден:
  - шаг фиксируется как `FAILED`,
  - gate завершается с ошибкой.
- Локально поведение прежнее: при отсутствии basedpyright шаг остается `skipped` (без ломания dev-потока).

2. `.github/workflows/ci.yml`
- В job `pre-build-gate` добавлена установка `basedpyright`:
  - `pip install ruff pytest jsonschema pyyaml basedpyright`
- В шаг `Run pre-build gate` добавлено:
  - `env: REQUIRE_BASEDPYRIGHT: "true"`

## Verification
- `bash -n scripts/pre_build_gate.sh` -> OK
- YAML parse `.github/workflows/ci.yml` -> OK
- `REQUIRE_BASEDPYRIGHT=true scripts/pre_build_gate.sh --skip-tests --skip-gui` -> FAIL (ожидаемо, т.к. basedpyright не установлен локально)

## Result
- В CI type-check стал hard requirement.
- Если basedpyright не установлен/недоступен в CI, PR блокируется.
