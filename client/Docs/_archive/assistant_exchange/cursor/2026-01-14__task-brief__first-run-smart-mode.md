# Task Brief — First-Run Smart Mode

Дата: 2026-01-14  
Задача: включить smart‑режим в first‑run — пропуск уже выданных разрешений (кроме Input Monitoring).

## Что сделано

- Добавлен `permissions.first_run.mode` (`smart` | `legacy`), по умолчанию `smart`.
- `FirstRunPermissionsIntegration` поддерживает оба режима:
  - smart: пропускает GRANTED (кроме input_monitoring), polling с ранним выходом;
  - legacy: всегда активирует и держит фиксированное время.
- Документация обновлена (`Docs/first_run_flow_spec.md`, `Docs/PROJECT_REQUIREMENTS.md`).
- Обновлён `client/VERSION_INFO.json` через `scripts/update_requirements_snapshot.py --update`.
 - Для `legacy` режима убрана публикация initial-статусов (соответствует старому формату).

## Затронутые файлы

- `integration/integrations/first_run_permissions_integration.py`
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
