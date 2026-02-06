# Task Brief: offline basedpyright fallback

## Goal
Убрать инфраструктурный тупик strict-gate в условиях закрытой сети: дать рабочий offline путь установки basedpyright.

## Changes
1. `scripts/setup_dev_env.sh`
- Добавлен fallback сценарий, если `pip install -r requirements-dev.txt` не может установить basedpyright из сети.
- Поддержка установки через переменную:
  - `BASEDPYRIGHT_WHEEL=/abs/path/basedpyright-*.whl ./scripts/setup_dev_env.sh`
- Явные сообщения об ошибке и инструкциях.

2. `scripts/pre_build_gate.sh`
- В strict-ошибке добавлена подсказка про offline fallback (wheel path).

## Verification
- `bash -n scripts/setup_dev_env.sh` -> OK
- `bash -n scripts/pre_build_gate.sh` -> OK
- `scripts/quality_strict.sh --skip-tests --skip-gui` -> FAIL ожидаемо, но теперь с подсказкой offline fallback.

## Result
- Есть практический путь разблокировки strict-gate без доступа к PyPI.
