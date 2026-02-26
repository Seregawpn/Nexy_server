# Remote Server Config (Production)

**Обновлено:** 21 February 2026  
**Версия канона:** `v1.6.1.43`

## 1) Production Runtime

- Cloud: Azure
- Resource Group: `NexyNewRG`
- VM: `NexyNew`
- Region: `canadacentral`
- Public host: `nexy-prod-sergiy.canadacentral.cloudapp.azure.com`
- TLS: Let’s Encrypt (Nginx ingress)

## 2) Network Contract

External (public):
- `https://nexy-prod-sergiy.canadacentral.cloudapp.azure.com/health`
- `https://nexy-prod-sergiy.canadacentral.cloudapp.azure.com/status`
- `https://nexy-prod-sergiy.canadacentral.cloudapp.azure.com/updates/health`
- gRPC endpoint: `nexy-prod-sergiy.canadacentral.cloudapp.azure.com:443`

Internal (VM localhost only):
- `127.0.0.1:50051` (gRPC)
- `127.0.0.1:8080` (API health/status)
- `127.0.0.1:8081` (updates)

Правило:
- Не открывать 50051/8080/8081 наружу.

## 3) Operational Commands

Deploy:
```bash
bash server/scripts/deploy_server_one_click.sh --tag vX.Y.Z.W
```

Health/check:
```bash
bash server/scripts/quick_server_ops.sh check
```

Monitoring:
```bash
bash server/scripts/quick_server_ops.sh monitor-bridge-setup
bash server/scripts/quick_server_ops.sh monitor-start
bash server/scripts/quick_server_ops.sh monitor-once
```

## 4) Monitoring Model

Primary owner on VM:
- `/usr/local/bin/nexy-monitor-snapshot.sh`
- `/etc/cron.d/nexy-monitor-snapshot` (`0 * * * *`)
- `/home/azureuser/voice-assistant/monitoring/latest_status.json`
- `/home/azureuser/voice-assistant/monitoring/incidents/`

Local mirror:
- `monitor_inbox/remote_server_status.json`
- `monitor_inbox/*__incident__server-monitor.remote.md`

## 5) Deployment Safety Rules

- Deploy lock enabled.
- No parallel `az vm run-command`.
- Monitor immutability guard enabled by default.
- Use `--allow-monitor-changes` only when intentionally changing monitoring config.

## 6) Known Critical Alert Class

Если в инцидентах есть `API_KEY_INVALID`/`API key expired`:
- обновить `GEMINI_API_KEY` на VM,
- перезапустить сервис,
- повторить check + monitor-once.
