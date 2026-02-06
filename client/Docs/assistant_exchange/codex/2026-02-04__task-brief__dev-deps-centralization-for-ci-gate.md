# Task Brief: dev deps centralization for CI gate

## Goal
Продолжить усиление quality-gate: централизовать dev-зависимости и сделать strict mode basedpyright явным через CLI-флаг.

## Changes
1. `scripts/pre_build_gate.sh`
- Добавлен явный флаг запуска `--require-basedpyright`.
- Обновлен usage в help.
- Флаг включает strict-режим обязательности basedpyright (эквивалентно env `REQUIRE_BASEDPYRIGHT=true`).

2. `requirements-dev.txt` (новый файл)
- Добавлен единый список dev/CI зависимостей:
  - `ruff`
  - `pytest`
  - `jsonschema`
  - `pyyaml`
  - `basedpyright`

3. `.github/workflows/ci.yml`
- Переведен install step на `pip install -r requirements-dev.txt` (в релевантных job).
- Запуск pre-build gate в CI теперь использует явный контракт:
  - `./scripts/pre_build_gate.sh --verbose --require-basedpyright`

## Verification
- `bash -n scripts/pre_build_gate.sh` -> OK
- YAML parse `.github/workflows/ci.yml` -> OK
- `scripts/pre_build_gate.sh --skip-tests --skip-gui --require-basedpyright` -> FAIL (ожидаемо, basedpyright отсутствует локально)
- `scripts/pre_build_gate.sh --skip-tests --skip-gui` -> PASS

## Result
- В CI и локально есть единый явный strict-mode контракт для type-check.
- Dev/CI зависимости централизованы в одном файле, уменьшен риск расхождения install команд.
