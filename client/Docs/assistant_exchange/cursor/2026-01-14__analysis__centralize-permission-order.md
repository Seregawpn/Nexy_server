# Impact Map — Centralized Permission Order

Дата: 2026-01-14  
Контекст: единый источник порядка first-run разрешений и устранение дублирующих списков.

## Impact Map

| Ось или инвариант | Модули/интеграции | EventBus события/контракты | Конфиги/флаги | Тест-планы/скрипты |
| --- | --- | --- | --- | --- |
| permissions.first_run | `integration/integrations/first_run_permissions_integration.py`, `modules/permissions/first_run/activator.py` | `permissions.first_run_started`, `permissions.status_checked` | `config/unified_config.yaml` (`integrations.permissions.required_permissions`) | `scripts/test_first_run_integration.sh` |
| permissions.order | `modules/permissions/first_run/activator.py` | N/A | `config/unified_config.yaml` (`integrations.permissions.required_permissions`) | `scripts/verify_config.py` |
| docs consistency | `Docs/first_run_flow_spec.md`, `Docs/PROJECT_REQUIREMENTS.md` | N/A | N/A | `scripts/update_requirements_snapshot.py --check` |

## План (до изменений)

1. Flags discovery: `python3 scripts/verify_feature_flags.py --module modules/permissions/first_run`
2. Обновить `Docs/PROJECT_REQUIREMENTS.md` (REQ-010: порядок из конфига).
3. Код: убрать локальный список в `activate_all_permissions`, читать порядок из `unified_config.yaml`.
4. Документация: `Docs/first_run_flow_spec.md` → порядок из конфига.
5. Проверки: `scripts/update_requirements_snapshot.py --check` + `scripts/check_requirements_mapping.py`.

## Flags Discovery

- Module: `modules/permissions/first_run`
- Result: no flags found (0)

## Реализация (факт)

- `modules/permissions/first_run/activator.py`: добавлены `hold_duration` параметры; удержание вынесено на конфиг.
- `integration/integrations/first_run_permissions_integration.py`: порядок из `required_permissions`, фиксированное удержание + пауза между запросами.
- `config/unified_config.yaml`: добавлены `pause_between_requests_sec`, `activation_hold_duration_sec`.
- Документация: `Docs/first_run_flow_spec.md`, `Docs/PROJECT_REQUIREMENTS.md`.
