# Task Brief — First-Run Sequence Legacy Alignment

Дата: 2026-01-14  
Задача: привести порядок и способ запроса разрешений к формату старой версии (фиксированное удержание, последовательность, форсированный pre‑status).

## Что сделано

- `FirstRunPermissionsIntegration` переведён на legacy‑сценарий:
  - pre‑activation статус всегда `NOT_DETERMINED`;
  - каждое разрешение активируется независимо от текущего статуса;
  - фиксированное удержание `activation_hold_duration_sec`;
  - пауза между запросами `pause_between_requests_sec`.
- `activator.py` принимает `hold_duration` и держит запросы открытыми заданное время.
- В конфиг добавлены `permissions.first_run.pause_between_requests_sec` и `activation_hold_duration_sec`.
- Документация обновлена (`Docs/first_run_flow_spec.md`, `Docs/PROJECT_REQUIREMENTS.md`).
- Обновлён `client/VERSION_INFO.json` через `scripts/update_requirements_snapshot.py --update`.

## Затронутые файлы

- `integration/integrations/first_run_permissions_integration.py`
- `modules/permissions/first_run/activator.py`
- `config/unified_config.yaml`
- `Docs/first_run_flow_spec.md`
- `Docs/PROJECT_REQUIREMENTS.md`
- `client/VERSION_INFO.json`

## Команды

- `python3 scripts/verify_feature_flags.py --module integration/integrations/first_run_permissions_integration.py`
- `python3 scripts/update_requirements_snapshot.py --check`
- `python3 scripts/update_requirements_snapshot.py --update`
- `python3 scripts/check_requirements_mapping.py` (❌ см. ниже)

## Проверки

- Линтеры: `read_lints` — ошибок нет.
- Автотесты: не запускались.

## Проблемы/заметки

- `scripts/check_requirements_mapping.py` падает из‑за уже существующих несоответствий в `PROJECT_REQUIREMENTS.md` (не связано с текущей правкой).
