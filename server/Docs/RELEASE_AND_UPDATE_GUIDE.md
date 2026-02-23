# Server Release & Update Guide

**Статус:** Active Rulebook  
**Обновлено:** 21 February 2026  
**Текущий релиз документации:** `v2.0.0.4`

Канон публикации клиентских артефактов и синхронизации update-канала.

## Canonical Release Target (обязательно)

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

Перед release всегда сверять именно этот блок (без legacy host/RG/VM).

## 0) Separation Rules

- Code deploy path: `Seregawpn/Nexy`.
- Assets path (`Nexy.dmg`, `Nexy.pkg`): `Seregawpn/Nexy_production`.
- Запрещено смешивать code-pipeline и asset-pipeline.

## 1) Version Source of Truth

Единый owner версии: файл `VERSION` в корне workspace.

```bash
python3 scripts/update_version.py X.Y.Z.W
```

Обновляются:
- `VERSION`
- `server/updates/manifests/manifest.json`
- server/client version-linked files

## 2) Pre-Release Checklist

1. `gh auth status` успешно.
2. `release_inbox/` содержит `Nexy.dmg` и/или `Nexy.pkg`.
3. Code deploy сервера уже прошёл (`quick_server_ops.sh check`).
4. На VM есть `GEMINI_API_KEY`:

```bash
az vm run-command invoke \
  --resource-group NexyNewRG \
  --name NexyNew \
  --command-id RunShellScript \
  --scripts "grep -q '^GEMINI_API_KEY=' /home/azureuser/voice-assistant/config.env && echo OK || (echo MISSING && exit 1)"
```

## 3) Publish Assets

```bash
python3 scripts/publish_assets_and_sync.py
```

Ожидание:
- обновлены fixed-каналы:
  - `https://github.com/Seregawpn/Nexy_production/releases/download/Update/Nexy.dmg`
  - `https://github.com/Seregawpn/Nexy_production/releases/download/App/Nexy.pkg`
- `manifest.json` обновлён и синхронизирован

Dry-run:

```bash
python3 scripts/publish_assets_and_sync.py --dry-run
```

## 4) Verify

1. Проверить release URL в `Nexy_production`.
2. Проверить `server/updates/manifests/manifest.json` (`version`, `build`, `artifact.url`, `sha256`, `size`).
3. Проверить endpoint:

```bash
curl -fsS https://nexy-prod-sergiy.canadacentral.cloudapp.azure.com/updates/health
```

## 5) Rollback

- Новые теги создавать запрещено.
- Повторный publish выполняется в те же fixed-каналы (`Update`/`App`) с заменой assets.

## 6) DoD

1. Release assets опубликованы в `Nexy_production`.
2. Manifest указывает на fixed URL `.../download/Update/Nexy.dmg` и валидные checksum/size.
3. `/updates/health` и `/health` согласованы по версии.
