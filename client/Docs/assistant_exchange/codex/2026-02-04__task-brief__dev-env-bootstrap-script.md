# Task Brief: dev env bootstrap script

## Goal
Упростить следующий шаг после централизации quality-gate: дать один командный bootstrap dev-зависимостей, включая basedpyright.

## Changes
1. Добавлен `scripts/setup_dev_env.sh`.
- Проверяет наличие `.venv`.
- Устанавливает dev/CI зависимости из `requirements-dev.txt`.

2. Обновлен `scripts/pre_build_gate.sh`.
- Сообщения при отсутствии basedpyright теперь указывают на единый bootstrap:
  - `./scripts/setup_dev_env.sh`

## Verification
- `bash -n scripts/setup_dev_env.sh` -> OK
- `bash -n scripts/pre_build_gate.sh` -> OK
- `scripts/quality_strict.sh --skip-tests --skip-gui` -> FAIL ожидаемо (strict mode), с корректной подсказкой `./scripts/setup_dev_env.sh`.

## Result
- Следующий шаг стал однозначным и централизованным:
  - `./scripts/setup_dev_env.sh`
