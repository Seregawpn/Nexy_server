# Server Deployment Guide (Azure)

**Статус:** Active Rulebook  
**Обновлено:** 21 February 2026  
**Текущий релиз документации:** `v2.0.0.8`

Канонический деплой серверной части в Azure.

## 0) Runtime Target (Single Source)

- Resource Group: `NexyNewRG`
- VM: `NexyNew`
- Public host: `nexy-prod-sergiy.canadacentral.cloudapp.azure.com`
- Internal services (VM localhost only):
  - gRPC: `127.0.0.1:50051`
  - API health/status: `127.0.0.1:8080`
  - update server: `127.0.0.1:8081`

Запрет:
- Не использовать старые цели `NetworkWatcherRG/Nexy` для production deploy.

### Canonical Target Block (обязательно использовать в таком формате)

```yaml
release_target:
  version: "2.0.0.4"
  azure:
    resource_group: "NexyNewRG"
    vm_name: "NexyNew"
  server:
    host: "nexy-prod-sergiy.canadacentral.cloudapp.azure.com"
  grpc:
    endpoint: "nexy-prod-sergiy.canadacentral.cloudapp.azure.com:443"
    tls: true
  update:
    dmg_url: "https://github.com/Seregawpn/Nexy_production/releases/download/Update/Nexy.dmg"
    pkg_url: "https://github.com/Seregawpn/Nexy_production/releases/download/App/Nexy.pkg"
```

### Preflight (перед любыми настройками/деплоем)

```bash
dig +short nexy-prod-sergiy.canadacentral.cloudapp.azure.com
az vm show --resource-group NexyNewRG --name NexyNew -o table
curl -fsS https://nexy-prod-sergiy.canadacentral.cloudapp.azure.com/health >/dev/null
```

## 1) Repo Responsibilities

1. `Seregawpn/Nexy` — root workspace, документация, общий код.
2. `Seregawpn/Nexy` — единственный source code path для server deploy.
3. `Seregawpn/Nexy_production` — только клиентские release assets.

## 2) Mandatory Preconditions

1. `az login` выполнен.
2. `az vm show --resource-group NexyNewRG --name NexyNew -o table` успешен.
3. На VM есть валидный `/home/azureuser/voice-assistant/config.env`.
4. Есть `GEMINI_API_KEY` (не пустой, не placeholder).
5. Нет параллельного `az vm run-command invoke`.

## 3) Standard Deploy (One Command)

```bash
bash server/scripts/deploy_server_one_click.sh --tag vX.Y.Z.W
```

Опционально:

```bash
bash server/scripts/deploy_server_one_click.sh \
  --tag vX.Y.Z.W \
  --resource-group NexyNewRG \
  --vm NexyNew \
  --host nexy-prod-sergiy.canadacentral.cloudapp.azure.com
```

Важно:
- По умолчанию deploy использует guard неизменности мониторинга.
- Если во время deploy изменились `/usr/local/bin/nexy-monitor-snapshot.sh` или `/etc/cron.d/nexy-monitor-snapshot`, deploy падает с ошибкой.
- Обход guard разрешён только при осознанном изменении мониторинга:

```bash
bash server/scripts/deploy_server_one_click.sh --tag vX.Y.Z.W --allow-monitor-changes
```

## 4) Quick Ops (Canonical)

```bash
bash server/scripts/quick_server_ops.sh check
bash server/scripts/quick_server_ops.sh monitor-once
bash server/scripts/quick_server_ops.sh monitor-start
bash server/scripts/quick_server_ops.sh monitor-stop
bash server/scripts/quick_server_ops.sh monitor-bridge-setup
```

## 5) Post-Deploy Verification (DoD)

1. `bash server/scripts/quick_server_ops.sh check` -> `CHECK_OK`.
2. `https://nexy-prod-sergiy.canadacentral.cloudapp.azure.com/health` -> 200.
3. `https://nexy-prod-sergiy.canadacentral.cloudapp.azure.com/status` -> 200.
4. `https://nexy-prod-sergiy.canadacentral.cloudapp.azure.com/updates/health` -> 200.
5. `monitor_inbox/remote_server_status.json` содержит валидный JSON (не `{}` при реальном статусе).

## 6) Monitoring Rules

- Primary owner мониторинга: VM (`/usr/local/bin/nexy-monitor-snapshot.sh` + `/etc/cron.d/nexy-monitor-snapshot`).
- Schedule: `0 * * * *` (каждый час).
- Local mirror:
  - `monitor_inbox/remote_server_status.json`
  - `monitor_inbox/*__incident__server-monitor.remote.md`
- Локальный watcher (`start_local_server_monitor.sh`) — дополнительный сигнал, не owner runtime.

## 7) Hard Troubleshooting

1. `API_KEY_INVALID` / `API key expired`:
- Обновить `GEMINI_API_KEY` в VM `config.env`.
- `systemctl restart voice-assistant`.
- Повторить `quick_server_ops.sh check` и `monitor-once`.

2. `Run command extension execution is in progress`:
- Дождаться завершения предыдущего `az vm run-command`.
- Не запускать команды параллельно.

3. `PermissionError ... config.env`:

```bash
sudo chown root:azureuser /home/azureuser/voice-assistant/config.env
sudo chmod 640 /home/azureuser/voice-assistant/config.env
sudo systemctl restart voice-assistant
```

## 8) Non-Canonical / Deprecated

Ссылки с `NetworkWatcherRG`, `Nexy` и прямым прод-доступом к портам `50051/8080/8081` считать устаревшими для production.
