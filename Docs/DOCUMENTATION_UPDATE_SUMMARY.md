# Documentation Update Summary

**Дата:** 21 February 2026  
**Статус:** canonical sync complete

## Что синхронизировано

1. Обновлены канонические документы деплоя и релиза:
- `server/Docs/SERVER_DEPLOYMENT_GUIDE.md`
- `server/Docs/RELEASE_AND_UPDATE_GUIDE.md`
- `server/Docs/DEPLOY_INCIDENT_RUNBOOK.md`

2. Обновлены runtime-документы подключения и конфигурации:
- `Docs/REMOTE_SERVER_CONFIG.md`
- `Docs/CLIENT_CONNECTION_GUIDE.md`
- `Docs/CLIENT_QUICK_REFERENCE.md`

3. Зафиксирован production target:
- RG: `NexyNewRG`
- VM: `NexyNew`
- Host: `nexy-prod-sergiy.canadacentral.cloudapp.azure.com`

4. Зафиксированы operational owner-команды:
- deploy: `server/scripts/deploy_server_one_click.sh`
- check/monitor: `server/scripts/quick_server_ops.sh`

5. Зафиксировано правило безопасности deploy:
- мониторинг не должен изменяться при обычном deploy;
- при дрейфе monitor-артефактов deploy блокируется;
- явный override только через `--allow-monitor-changes`.

## Deprecated References

Все упоминания `NetworkWatcherRG/Nexy` и production `insecure_channel` считать устаревшими и не использовать для новых действий.
