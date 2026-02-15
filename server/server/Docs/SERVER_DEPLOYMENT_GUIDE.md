# Server Deployment Guide (Azure)

**Статус:** Active Rulebook  
**Обновлено:** 15 February 2026

Канон деплоя серверного кода на Azure VM.

---

## 0) Repo Responsibilities (Mandatory)

1. `Seregawpn/Nexy`  
Назначение: корневой workspace (общий код и документация).

2. `Seregawpn/Nexy_server`  
Назначение: единственный source для server deploy на Azure VM.

3. `Seregawpn/Nexy_production/releases`  
Назначение: клиентские артефакты (DMG/PKG) и update download URLs.

Правила:
- Code deploy на Azure выполняется только из `Nexy_server`.
- `Nexy_server` обновляется только server-subtree из корневого репозитория:
  - `git subtree push --prefix=server server_repo <branch>`
- Для клиентских артефактов использовать: `server/Docs/RELEASE_AND_UPDATE_GUIDE.md`.

---

## 1) Preconditions

- Azure CLI авторизован: `az login`
- Проверен target VM:
  - `az vm show --resource-group NetworkWatcherRG --name Nexy -o table`
- Перед прод-деплоем пройден pre-production gate:

```bash
bash server/scripts/prod_ready_check.sh
```

---

## 2) Standard Deploy Flow (GitHub Actions)

1. Изменения в `Nexy_server`.
2. Commit + push.
3. Проверка workflow: `https://github.com/Seregawpn/Nexy_server/actions`

Запрет:
- `git push --force` не использовать в стандартном деплое.

---

## 3) Controlled Deploy Flow (Azure CLI, Manual)

Использовать для выкатки по тегу с ручным контролем.

```bash
TAG_NAME="vX.Y.Z.Build"

az vm run-command invoke \
  --resource-group "NetworkWatcherRG" \
  --name "Nexy" \
  --command-id RunShellScript \
  --scripts "
    set -e
    export HOME=/home/azureuser
    cd /home/azureuser/voice-assistant

    git config --global --add safe.directory /home/azureuser/voice-assistant
    git fetch origin --tags --force
    git checkout -f $TAG_NAME

    . venv/bin/activate
    if [ -f server/requirements.txt ]; then
      pip install --upgrade -r server/requirements.txt
    else
      echo 'server/requirements.txt not found' >&2
      exit 1
    fi

    # protobuf/grpc must be compatible with generated stubs
    pip install --upgrade 'protobuf>=6.31.1,<7' 'grpcio>=1.75.1,<2' 'grpcio-tools>=1.75.1,<2' 'grpcio-status>=1.75.1,<2'

    systemctl restart voice-assistant
    sleep 6
    systemctl is-active voice-assistant
  "

# Centralized owner for runtime version + manifest sync:
VERSION="${TAG_NAME#v}"
bash server/scripts/update_server_version.sh "$VERSION"
```

---

## 4) Post-Deploy Verification

### 4.1 Mandatory (on VM)

```bash
curl -fsS http://127.0.0.1:8080/health
curl -fsS http://127.0.0.1:8080/status
curl -fsS http://127.0.0.1:8081/health
systemctl is-active voice-assistant
```

Проверить:
- `latest_version == latest_build == target tag without "v"`
- `voice-assistant` в `active`

### 4.2 Optional Public Check

Публичный DNS может меняться. Если есть актуальный публичный endpoint:

```bash
curl -sk https://<PUBLIC_HOST>/health
curl -sk https://<PUBLIC_HOST>/status
curl -sk https://<PUBLIC_HOST>/updates/health
```

---

## 5) Troubleshooting

### 5.1 VM deploy command failed
- Проверить `resource-group` / `vm name`.
- Проверить `az account show`.
- Проверить run-command output.

### 5.2 Service not active after restart
- Проверить:
  - `systemctl status voice-assistant --no-pager -l`
  - `journalctl -u voice-assistant -n 200 --no-pager`

### 5.3 API key expired (Gemini)
Симптом:
- `google.genai.errors.ClientError: API key expired` в journal.

Fix:
- Обновить `GEMINI_API_KEY` в `server/config.env` на VM.
- `systemctl restart voice-assistant`.

### 5.4 Wrong runtime version in `/health`
- Primary source: `server/VERSION` (не `SERVER_VERSION` в env).
- Синхронизировать `server/VERSION` и `server/updates/manifests/manifest.json`.

Полный runbook:
- `server/Docs/DEPLOY_INCIDENT_RUNBOOK.md`

---

## 6) DoD

1. Код выкачан на VM из `Nexy_server`.
2. Зависимости установлены без конфликтов.
3. `voice-assistant` активен.
4. `/health`, `/status`, `/updates/health` отдают target version/build.
5. Pipeline кода не смешан с pipeline клиентских артефактов.
