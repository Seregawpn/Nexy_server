# Server Release & Update Guide

**Статус:** Active Rulebook  
**Обновлено:** 25 February 2026  
**Текущий релиз документации:** `v2.0.0.19`

Канон публикации клиентских артефактов и синхронизации update-канала.

Command context (обязательно):
- Выполнять server-команды из директории `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/server`.
- Формат owner-path команд: `server/scripts/*`.

## Canonical Release Target (обязательно)

```yaml
release_target:
  version: "2.0.0.15"
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

Перед release всегда сверять именно этот блок (без legacy host/RG/VM).

## 0) Separation Rules

- Code deploy path: `Seregawpn/Nexy` (push в `Seregawpn/Nexy` запрещен для этого workspace).
- Assets path (`Nexy.dmg`, `Nexy.pkg`): `Seregawpn/Nexy_production`.
- Запрещено смешивать code-pipeline и asset-pipeline.
- GitHub publication control:
  - default: **tag-only** publish;
  - создание branch только после явного согласования;
  - имя branch всегда согласовывается до создания;
  - перед publish обязательная проверка, что API keys/secrets не входят в push.
- Runtime split на одном VM:
  - production: `:443` (`voice-assistant`)
  - staging: `:4443` (`voice-assistant-staging`, on-demand)
- Server-side beta gate:
  - env `UPDATE_BETA_ENABLED=true|false` управляет доступом к `/updates/appcast-beta.xml`.
  - при `false` endpoint beta возвращает `404` (beta updates закрыты).

## 1) Version Source of Truth

Versioning управляется единым owner-скриптом: `server/scripts/update_version.py`.

Разделение Source of Truth по осям:
- Artifact metadata SoT: `server/updates/manifests/manifest.json`
- Staging channel SoT: `server/updates/manifests/manifest_beta.json`
- Runtime update version SoT (для `/updates/health` и `/updates/appcast.xml`):
  `server/config/unified_config.yaml` -> `update.default_version/default_build`
- Runtime versioned manifest: `server/updates/manifests/manifest_<version>.json`

Производные файлы (`VERSION`, `unified_config`, docs markers) обновляются owner-скриптом.

```bash
python3 server/scripts/update_version.py X.Y.Z.W
```

Обновляются:
- `VERSION`
- `server/updates/manifests/manifest.json`
- `server/updates/manifests/manifest_<version>.json` (обязательно создать/обновить в паре с `manifest.json`)
- server/client version-linked files

## 2) Pre-Release Checklist

1. `gh auth status` успешно.
2. Канонический inbox channel-path содержит артефакты:
   - beta: `server/release_inbox/beta/`
   - stable: `server/release_inbox/stable/`
3. Code deploy сервера уже прошёл (`quick_server_ops.sh check`).
4. На VM есть `GEMINI_API_KEY`:
5. Fixed release tags существуют:
   - stable: `Update`, `App`
   - beta: `UpdateBeta`, `AppBeta`
6. Нет конфликта owner-path манифеста:
   - canonical: `server/updates/manifests/manifest.json`
   - legacy (если файл существует): `server/server/updates/manifests/manifest.json` должен быть идентичен canonical

```bash
az vm run-command invoke \
  --resource-group NexyNewRG \
  --name NexyNew \
  --command-id RunShellScript \
  --scripts "grep -q '^GEMINI_API_KEY=' /home/azureuser/voice-assistant/config.env && echo OK || (echo MISSING && exit 1)"
```

## 3) Publish Assets

```bash
python3 server/scripts/publish_assets_and_sync.py publish --channel beta
```

Ожидание:
- для staging (`beta`) обновлены fixed-каналы:
  - `https://github.com/Seregawpn/Nexy_production/releases/download/UpdateBeta/Nexy.dmg`
  - `https://github.com/Seregawpn/Nexy_production/releases/download/AppBeta/Nexy.pkg`
- манифесты:
  - beta: `manifest_beta.json`
- артефакты читаются только из `server/release_inbox/beta/`.

Политика воронки (обязательно):
- Прямой publish в `stable` запрещен (скрипт блокирует `publish --channel stable`).
- Единственный путь в production:
  1) publish в `beta`
  2) validation на staging runtime
  3) `promote --source beta --target stable`

После publish обязательно синхронизировать runtime manifest pair на VM:
- stable flow:
  - `manifest.json`
  - `manifest_<version>.json` (копия актуального `manifest.json`)
- beta flow:
  - `manifest_beta.json`

И обязательно обновить runtime version на VM (иначе appcast/health могут остаться на старой версии):

```bash
bash server/scripts/update_server_version.sh X.Y.Z.W
```

Dry-run:

```bash
python3 server/scripts/publish_assets_and_sync.py --dry-run
python3 server/scripts/publish_assets_and_sync.py publish --channel beta --dry-run
```

## 3.1) Promote beta -> stable (быстрый выпуск после проверки)

```bash
python3 server/scripts/publish_assets_and_sync.py promote --source beta --target stable
```

Что делает promote:
- копирует `Nexy.dmg`, `Nexy.pkg`, `LATEST_CHANGES.md` из `UpdateBeta/AppBeta` в `Update/App`;
- синхронизирует `manifest.json` из проверенного beta-артефакта;
- повторный запуск с тем же fingerprint версии/артефакта обрабатывается идемпотентно (skip);
- не требует пересборки клиента.

## 3.2) Обязательная staged-последовательность (без отклонений)

### Шаг A — публикация только в staging/beta

```bash
cd /Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27
./scripts/release_package_and_publish.sh --channel beta

# staging runtime (same VM) must be running during validation
az vm run-command invoke \
  --resource-group NexyNewRG \
  --name NexyNew \
  --command-id RunShellScript \
  --scripts "sudo sed -i 's/^UPDATE_BETA_ENABLED=.*/UPDATE_BETA_ENABLED=true/' /home/azureuser/voice-assistant/config.env || echo 'UPDATE_BETA_ENABLED=true' | sudo tee -a /home/azureuser/voice-assistant/config.env; sudo systemctl start voice-assistant-staging"
```

Проверка после Шага A:
- `appcast-beta.xml` показывает новую версию.
- `appcast.xml` остаётся на текущем production.
- Обновление доступно только на beta-клиенте (ваш Mac).

### Шаг B — подтверждение корректности на staging

```bash
curl -fsS https://nexy-prod-sergiy.canadacentral.cloudapp.azure.com:4443/health
curl -fsS https://nexy-prod-sergiy.canadacentral.cloudapp.azure.com:4443/updates/health
curl -fsS https://nexy-prod-sergiy.canadacentral.cloudapp.azure.com:4443/updates/appcast-beta.xml | rg -n 'sparkle:version|sparkle:shortVersionString|length'
```

Если `rg` не установлен, использовать fallback:

```bash
curl -fsS https://nexy-prod-sergiy.canadacentral.cloudapp.azure.com:4443/updates/appcast-beta.xml | grep -nE 'sparkle:version|sparkle:shortVersionString|length'
```

Примечание по gRPC smoke:
- `scripts/grpc_smoke.py` сейчас жёстко включает TLS только для `port=443`.
- Для staging `:4443` используйте TLS-ready проверку или обновите smoke-скрипт под secure ports (`443`, `4443`).

Допуск к promote:
- нет ошибок в smoke и health;
- beta-обновление корректно скачивается/устанавливается на вашем устройстве;
- критические проверки подписи/нотаризации уже пройдены packaging owner-скриптом.

### Шаг C — быстрый promote в production/stable

```bash
python3 server/scripts/publish_assets_and_sync.py promote --source beta --target stable
bash server/scripts/update_manifest_remote_locked.sh --channel stable \
  --resource-group NexyNewRG \
  --vm NexyNew \
  --url https://github.com/Seregawpn/Nexy_production/releases/download/Update/Nexy.dmg \
  --size <SIZE_BYTES> \
  --sha256 <SHA256> \
  --version X.Y.Z.W \
  --build X.Y.Z.W
bash server/scripts/update_server_version.sh X.Y.Z.W
```

Проверка после Шага C:
- `appcast.xml` показывает протестированную версию;
- `updates/health.latest_version` = `X.Y.Z.W`;
- stable-клиенты начинают видеть обновление только после promote.

После завершения staged-цикла (чтобы staging не работал постоянно):

```bash
az vm run-command invoke \
  --resource-group NexyNewRG \
  --name NexyNew \
  --command-id RunShellScript \
  --scripts "sudo systemctl stop voice-assistant-staging"
```

Рекомендуется также закрывать beta feed вне окна тестирования:

```bash
az vm run-command invoke \
  --resource-group NexyNewRG \
  --name NexyNew \
  --command-id RunShellScript \
  --scripts "sudo sed -i 's/^UPDATE_BETA_ENABLED=.*/UPDATE_BETA_ENABLED=false/' /home/azureuser/voice-assistant/config.env || echo 'UPDATE_BETA_ENABLED=false' | sudo tee -a /home/azureuser/voice-assistant/config.env; sudo systemctl restart voice-assistant-staging"
```

## 4) Verify

1. Проверить release URL в `Nexy_production`.
2. Проверить `server/updates/manifests/manifest.json` и `manifest_<version>.json` (`version`, `build`, `artifact.url`, `sha256`, `size`).
3. Для staging проверить `server/updates/manifests/manifest_beta.json` и endpoint `/updates/appcast-beta.xml`.
4. Проверить endpoints:

```bash
curl -fsS https://nexy-prod-sergiy.canadacentral.cloudapp.azure.com/updates/health
curl -fsS https://nexy-prod-sergiy.canadacentral.cloudapp.azure.com/updates/appcast.xml | \
  rg -n 'sparkle:version|sparkle:shortVersionString|length'
curl -fsS https://nexy-prod-sergiy.canadacentral.cloudapp.azure.com:4443/updates/appcast-beta.xml | \
  rg -n 'sparkle:version|sparkle:shortVersionString|length'
```

Ожидание:
- `/updates/health`: `latest_version/latest_build = target version`
- `/updates/appcast.xml`: `sparkle:version/sparkle:shortVersionString = target version`

## 5) Rollback

- Новые теги создавать запрещено.
- Повторный publish выполняется в те же fixed-каналы (`Update`/`App`) с заменой assets.
- Для staged rollback использовать те же fixed-каналы (`UpdateBeta`/`AppBeta`) без влияния на stable.

## 6) DoD

1. Release assets опубликованы в `Nexy_production`.
2. Manifest указывает на fixed URL `.../download/Update/Nexy.dmg` и валидные checksum/size.
3. На VM существует пара `manifest.json` + `manifest_<version>.json` с одинаковыми `version/build/url/size/sha256`.
4. `/updates/health`, `/updates/appcast.xml` и `/health` согласованы по версии.
