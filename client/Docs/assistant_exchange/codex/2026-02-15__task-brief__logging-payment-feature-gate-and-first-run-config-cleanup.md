# Task Brief — logging contract + payment gate + first-run config cleanup

## Done
- `config/unified_config_loader.py`
  - `LoggingConfig` приведён к текущему формату `logging` секции (`console_level/file_level/file_path/...`).
  - Добавлены backward-compatible alias properties (`level/file/max_size/backup_count`).
  - `get_logging_config()` теперь поддерживает новый и legacy форматы без падений.

- `integration/integrations/action_execution_integration.py`
  - Убран silent no-op для `payment` при disabled feature.
  - Теперь disabled feature всегда отдает единый `feature_disabled` failure-path (в т.ч. payment).

- `config/unified_config.yaml`
  - Удалены legacy batching-поля из `permissions.first_run`:
    - `batch_size`
    - `enable_batching`
    - `batch_restart_delay_sec`
  - Оставлен явный комментарий, что owner first-run path — V2 orchestrator.

## Validation
- `python3 scripts/verify_feature_flags.py` → OK
- `python3 scripts/verify_config.py` → OK
- `python3 scripts/verify_imports.py` → OK

## Notes
- В `config/unified_config.yaml` уже был сторонний рабочий diff (`integrations.grpc_client.server: production -> local`) до этой задачи; не изменялся в рамках правок этого пакета.
