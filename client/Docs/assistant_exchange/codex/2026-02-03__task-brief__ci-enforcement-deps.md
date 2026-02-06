# Task Brief: CI-only Enforcement for Integration Dependencies

## Scope
Добавлен CI-only enforcement через pre-build gate.

## Changes
- `scripts/pre_build_gate.sh`: добавлена проверка `scripts/check_dependency_violations.py` в секцию линтеров.

## Verification
Не запускалась.
