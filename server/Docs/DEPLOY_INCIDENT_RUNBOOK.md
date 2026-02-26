# Deploy Incident Runbook

**Статус:** Active Runbook  
**Обновлено:** 21 February 2026

Формат: `Symptom -> Check -> Fix -> Verify`.

## 0) Target

- RG: `NexyNewRG`
- VM: `NexyNew`
- Host: `nexy-prod-sergiy.canadacentral.cloudapp.azure.com`

## 1) Azure Access Error

Symptom:
- `ReadOnlyDisabledSubscription` / auth error.

Check:
```bash
az account show
az account list -o table
az vm show --resource-group NexyNewRG --name NexyNew -o table
```

Fix:
- `az login`
- выбрать активную подписку с правами write.

Verify:
- `az vm show` успешен.

## 2) Deploy Failed

Check:
```bash
bash server/scripts/deploy_server_one_click.sh --tag vX.Y.Z.W
```

Fix:
- исправить ошибку из stdout/stderr,
- повторить команду.

Verify:
```bash
bash server/scripts/quick_server_ops.sh check
```

## 3) Service Down After Restart

Check:
```bash
az vm run-command invoke \
  --resource-group NexyNewRG \
  --name NexyNew \
  --command-id RunShellScript \
  --scripts "systemctl status voice-assistant --no-pager -l; journalctl -u voice-assistant -n 200 --no-pager"
```

Fix:
- устранить первую runtime ошибку в журнале.

Verify:
- `systemctl is-active voice-assistant` = `active`
- `quick_server_ops.sh check` = `CHECK_OK`

## 4) API key expired

Symptom:
- `API_KEY_INVALID` / `API key expired`.

Fix:
1. Обновить `GEMINI_API_KEY` в `/home/azureuser/voice-assistant/config.env`.
2. `systemctl restart voice-assistant`.

Verify:
```bash
bash server/scripts/quick_server_ops.sh check
bash server/scripts/quick_server_ops.sh monitor-once
cat monitor_inbox/remote_server_status.json
```

## 5) Monitoring Drift During Deploy

Symptom:
- deploy завершился `ERROR: monitor artifacts changed during deploy`.

Meaning:
- во время deploy был изменён monitoring owner-path.

Fix:
- если изменение не планировалось: вернуть monitor-файлы к канону.
- если планировалось: rerun deploy с флагом:
```bash
bash server/scripts/deploy_server_one_click.sh --tag vX.Y.Z.W --allow-monitor-changes
```

## 6) Incident Inbox First

Всегда сначала смотреть:
- `monitor_inbox/remote_server_status.json`
- последний `monitor_inbox/*__incident__server-monitor*.md`
