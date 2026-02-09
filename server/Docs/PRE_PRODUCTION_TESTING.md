# Pre-Production Testing (Server)

Этот документ фиксирует обязательный pre-production gate для серверной части.

## Обязательный запуск перед продом

```bash
bash server/scripts/prod_ready_check.sh
```

Скрипт выполняет:
- полный quality gate (`full_quality_scan.sh`: syntax + basedpyright + pytest),
- проверку реестра feature flags (`verify_feature_flags.py`),
- sanity-check `config.env` на пустые/placeholder значения.

## Опциональные smoke-проверки

```bash
RUN_GRPC_SMOKE=true GRPC_HOST=127.0.0.1 GRPC_PORT=50051 bash server/scripts/prod_ready_check.sh
RUN_WEB_SEARCH_SMOKE=true WEB_SEARCH_QUERY="latest news about SpaceX" bash server/scripts/prod_ready_check.sh
```

## Критерий готовности к деплою

- `prod_ready_check.sh` завершился с exit code `0`.
- Нет ошибок в basedpyright.
- Нет падающих тестов.
- Нет ошибок `verify_feature_flags.py`.
