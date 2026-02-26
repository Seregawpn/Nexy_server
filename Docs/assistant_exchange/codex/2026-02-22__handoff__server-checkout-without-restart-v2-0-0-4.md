# Handoff — Server checkout `v2.0.0.4` without runtime restart

## Goal
Залить текущую версию на удалённый сервер, не запускать новый релиз (без restart сервиса).

## Actions
1. Выполнен remote command на VM `NexyNew` (RG `NexyNewRG`) через `az vm run-command invoke`.
2. В `/home/azureuser/voice-assistant` выполнено:
   - `git fetch origin --tags --force`
   - `git checkout -f v2.0.0.4`
3. Зафиксирована проверка до/после:
   - `systemctl is-active voice-assistant`
   - `systemctl show -p MainPID --value voice-assistant`

## Verification
- `after_head=0ba120c1` (workspace на VM переключён на `v2.0.0.4`).
- `before_pid=8145` и `after_pid=8145`.
- `service_restart=no`.

## Result
Код текущей версии залит на удалённый сервер (checkout выполнен), активный процесс сервиса не перезапускался.
