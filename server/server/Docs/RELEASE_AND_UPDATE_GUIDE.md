# Server Release & Update Guide

**Статус:** Active Rulebook  
**Обновлено:** 21 February 2026  
**Текущий релиз документации:** `v1.6.1.43`

Канон публикации клиентских артефактов и синхронизации update-канала.

## 0) Separation Rules

- Code deploy path: `Seregawpn/Nexy_server`.
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
- релиз в `Seregawpn/Nexy_production/releases/tag/vX.Y.Z.W`
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

- Не перезаписывать assets в уже существующем tag.
- Делать новый tag `vX.Y.Z.W+1` и повторный publish.

## 6) DoD

1. Release assets опубликованы в `Nexy_production`.
2. Manifest указывает на новый tag и валидные checksum/size.
3. `/updates/health` и `/health` согласованы по версии.
