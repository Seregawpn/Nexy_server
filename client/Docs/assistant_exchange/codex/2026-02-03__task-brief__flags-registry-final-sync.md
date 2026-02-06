# Task Brief: Flags Registry Final Sync

## Scope
Финальная синхронизация реестра флагов с фактическими env-переменными.

## Changes
- `Docs/FEATURE_FLAGS.md`: убраны ссылки на `NEXY_KS_PERMISSION_RESTART_V2` в колонке kill_switch.
- `Docs/FEATURE_FLAGS.md`: добавлен флаг `NEXY_INIT`.

## Verification
Автосверка показывает:
- MISSING_IN_REGISTRY: none
- IN_REGISTRY_NOT_IN_CODE: остаются общие feature/kill-switch флаги, которые включены в реестр, но не встречаются в коде напрямую (возможны конфиг-флаги без env-упоминания).
