# Deploy Incident Runbook

**Статус:** Active Runbook  
**Обновлено:** 15 February 2026

Формат: `Symptom -> Check -> Fix -> Verify`

---

## 0) Scope

- Code deploy pipeline: `Seregawpn/Nexy_server`
- Artifact release pipeline: `Seregawpn/Nexy_production/releases`

Каноны:
- `Docs/SERVER_DEPLOYMENT_GUIDE.md`
- `Docs/RELEASE_AND_UPDATE_GUIDE.md`

---

## 0.1 Incident Guardrails (Mandatory)

- `az vm run-command invoke` выполнять последовательно (без параллельных запусков).
- Для `RunShellScript` использовать POSIX-режим (`set -eu`), либо явно `bash -lc`.
- Любой restart сервиса разрешён только после preflight:
  - `/home/azureuser/voice-assistant/config.env` существует;
  - `GEMINI_API_KEY` присутствует и не placeholder;
  - `config.env` доступен для чтения пользователем `azureuser`;
  - `ExecStart` указывает на `server/main.py`.

---

## 1) Azure Auth / Access

### Symptom
- `az vm run-command invoke` returns auth/subscription error.

### Check
```bash
az account show
az account list -o table
az vm show --resource-group NetworkWatcherRG --name Nexy -o table
```

### Fix
```bash
az login
az account set --subscription <SUBSCRIPTION_ID>
```

### Verify
- `az vm show` successful.

---

## 2) GitHub Actions Deploy Not Triggered

### Symptom
- Push exists, deploy workflow not started.

### Check
- `https://github.com/Seregawpn/Nexy_server/actions`
- Verify trigger config in workflow.

### Fix
- Push changes to target branch/path.
- Verify `AZURE_CREDENTIALS` secret.

### Verify
- Workflow goes to `in_progress/success`.

---

## 3) Dependency Mismatch After Deploy

### Symptom
- Import/runtime errors after deploy.

### Check
```bash
az vm run-command invoke \
  --resource-group NetworkWatcherRG \
  --name Nexy \
  --command-id RunShellScript \
  --scripts "cd /home/azureuser/voice-assistant && . venv/bin/activate && python -V && pip freeze | head -100"
```

### Fix
```bash
az vm run-command invoke \
  --resource-group NetworkWatcherRG \
  --name Nexy \
  --command-id RunShellScript \
  --scripts "cd /home/azureuser/voice-assistant && . venv/bin/activate && pip install --upgrade -r server/requirements.txt && pip install --upgrade 'protobuf>=6.31.1,<7' 'grpcio>=1.75.1,<2' 'grpcio-tools>=1.75.1,<2' 'grpcio-status>=1.75.1,<2'"
```

### Verify
- Service starts and remains `active`.

---

## 4) Wrong Runtime Version In /health

### Symptom
- `/health` returns old `latest_version/latest_build`.

### Check
```bash
az vm run-command invoke \
  --resource-group NetworkWatcherRG \
  --name Nexy \
  --command-id RunShellScript \
  --scripts "cd /home/azureuser/voice-assistant && cat VERSION && cat server/updates/manifests/manifest.json"
```

### Fix
```bash
bash scripts/update_server_version.sh X.Y.Z.Build
```

### Verify
- `/health` and `/updates/health` match expected version/build.

---

## 5) Service Restart / systemd Failure

### Symptom
- `voice-assistant` not active after deploy.

### Check
```bash
az vm run-command invoke \
  --resource-group NetworkWatcherRG \
  --name Nexy \
  --command-id RunShellScript \
  --scripts "systemctl status voice-assistant --no-pager -l; journalctl -u voice-assistant -n 200 --no-pager"
```

### Fix
- Resolve primary error from journal.
- Restart service.

### Verify
- `systemctl is-active voice-assistant` -> `active`.

### Fast Branching
- Если `PermissionError` по `config.env` -> перейти в раздел 6.1.
- Если `can't open file ...` -> перейти в раздел 6.2.
- Если `TextProcessor` initialization failed -> перейти в раздел 6.3.

---

## 6) Gemini API Key Expired

### Symptom
- Logs contain `API_KEY_INVALID` / `API key expired`.

### Check
```bash
az vm run-command invoke \
  --resource-group NetworkWatcherRG \
  --name Nexy \
  --command-id RunShellScript \
  --scripts "journalctl -u voice-assistant -n 200 --no-pager | grep -E 'API_KEY_INVALID|API key expired|google.genai.errors' || true"
```

### Fix
- Update `GEMINI_API_KEY` in `/home/azureuser/voice-assistant/config.env`.
- `systemctl restart voice-assistant`.

Mandatory preflight:
```bash
grep -q '^GEMINI_API_KEY=' /home/azureuser/voice-assistant/config.env
```

### Verify
- No API key errors in new logs.
- Health endpoints are stable.

### 6.1 Config Permission Denied

#### Symptom
- `PermissionError: [Errno 13] Permission denied: '/home/azureuser/voice-assistant/config.env'`

#### Fix
```bash
sudo chown root:azureuser /home/azureuser/voice-assistant/config.env
sudo chmod 640 /home/azureuser/voice-assistant/config.env
sudo systemctl restart voice-assistant
```

#### Verify
```bash
systemctl is-active voice-assistant
curl -fsS http://127.0.0.1:8080/health
```

### 6.2 ExecStart Path Drift

#### Symptom
- `can't open file '/home/azureuser/voice-assistant/server/server/main.py'`
- `can't open file '/home/azureuser/voice-assistant/main.py'`

#### Check
```bash
systemctl cat voice-assistant | grep '^ExecStart='
```

#### Fix
```bash
sudo sed -i 's|^ExecStart=.*|ExecStart=/home/azureuser/voice-assistant/venv/bin/python3 server/main.py|' /etc/systemd/system/voice-assistant.service
sudo systemctl daemon-reload
sudo systemctl restart voice-assistant
```

#### Verify
```bash
systemctl is-active voice-assistant
curl -fsS http://127.0.0.1:8080/health
```

### 6.3 TextProcessor Init Failure (LLM Startup)

#### Symptom
- `Не удалось инициализировать TextProcessor`
- gRPC service initialization failed right after startup.

#### Check
```bash
journalctl -u voice-assistant -n 200 --no-pager | grep -E 'TextProcessor|LangChain|google.genai|API_KEY_INVALID|expired|invalid' || true
```

#### Fix
1. Обновить `GEMINI_API_KEY` в `/home/azureuser/voice-assistant/config.env`.
2. Проверить минимальный Gemini smoke (до restart).
3. Перезапустить сервис.

#### Verify
- Нет ошибок `google.genai` в новых логах.
- `8080/8081` health стабильно отвечают.

### 6.4 Run Command Conflict

#### Symptom
- `Run command extension execution is in progress`

#### Fix
- Дождаться завершения активной команды.
- Повторить команду после освобождения run-command канала.

---

## 7) release_inbox Missing / Artifact Missing

### Symptom
- Publish flow fails: inbox/artifact not found.

### Check
```bash
test -d release_inbox && ls -la release_inbox
```

### Fix
```bash
mkdir -p release_inbox
# put Nexy.dmg and/or Nexy.pkg
```

### Verify
```bash
python3 scripts/publish_assets_and_sync.py --dry-run
```

---

## 8) GH CLI Auth / Upload Failure

### Symptom
- `gh auth required`, `401/403`, upload failed.

### Check
```bash
gh --version
gh auth status
```

### Fix
```bash
gh auth login
```

### Verify
```bash
gh release view Update -R Seregawpn/Nexy_production
```

---

## 9) Manifest/Appcast Mismatch

### Symptom
- Release uploaded, but appcast/manifest mismatch.

### Check
```bash
cat server/updates/manifests/manifest.json
```

### Fix
```bash
python3 scripts/publish_assets_and_sync.py
```

### Verify
- `artifact.url/version/build` in manifest match release assets.

---

## 10) Final Checklist (Any Incident)

1. Root cause fixed (not only symptom).
2. Minimal architecture-compatible fix applied.
3. Post-fix verify completed (`health`, `status`, `updates/health`).
4. Rulebook updated if new edge-case found.
5. Added/updated prevention gate to avoid recurrence.
