# Server Scripts Canonical Usage

Этот файл — короткий индекс. Каноничные инструкции:
- Release/Update process: `../../Docs/RELEASE_AND_UPDATE_GUIDE.md`
- Azure deploy process: `../Docs/SERVER_DEPLOYMENT_GUIDE.md`

## Mandatory Pipeline Split
- Server code/tag push: только `Seregawpn/Nexy_server`
- Client artifacts (`Nexy.dmg`, `Nexy.pkg`): только `Seregawpn/Nexy_production/releases`

## Mandatory Update Consistency Gate
Перед publish/deploy всегда:

```bash
python3 server/scripts/sync_update_manifests.py
python3 server/scripts/sync_update_manifests.py --check
bash server/scripts/validate_updates.sh nexy-server.canadacentral.cloudapp.azure.com 443
```

## Canonical Commands
Publish artifacts + manifest sync:

```bash
python3 server/scripts/publish_assets_and_sync.py
python3 server/scripts/sync_update_manifests.py
```

Deploy to Azure:

```bash
bash server/scripts/deploy_azure_guarded.sh vX.Y.Z.BUILD
```

## Anti-Drift Rules
- Не использовать version-tag URL для appcast (например `.../download/v1.6.1.34/...`).
- Использовать только fixed tag URL:
  - `https://github.com/Seregawpn/Nexy_production/releases/download/Update/Nexy.dmg`
- Если `sync_update_manifests.py --check` или `validate_updates.sh` падают, деплой блокируется.
