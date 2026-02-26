# Version Management (Canonical)

**Статус:** Active Rulebook  
**Обновлено:** 15 February 2026

## 1) Source of Truth

Единый owner изменения версии: `scripts/update_version.py`.

Source of Truth по осям:
- Artifact metadata SoT:
  - `server/updates/manifests/manifest.json`
- Runtime update version SoT (используется `/updates/health` и `/updates/appcast.xml`):
  - `server/config/unified_config.yaml` -> `update.default_version/default_build`
- Runtime versioned manifest:
  - `server/updates/manifests/manifest_<version>.json`

Производные (синхронизируются owner-скриптом):
- `VERSION` (в корне server workspace)
- `server/config/unified_config.yaml`

Формат версии:
- `X.Y.Z.W` (пример: `1.6.1.38`)

## 2) Единственный owner-скрипт

Использовать только:
```bash
python3 scripts/update_version.py X.Y.Z.W
```

Проверка:
```bash
python3 scripts/update_version.py --read
python3 scripts/update_version.py X.Y.Z.W --check
```

## 3) Что синхронизирует скрипт

- `VERSION`
- `server/config/unified_config.yaml`
- `server/config/unified_config.py` (fallback)
- `server/config.env.example`
- `server/updates/manifests/manifest.json` (`version`, `build`, `release_date`)
- `server/updates/manifests/manifest_<version>.json` (runtime versioned copy)
- `server/Docs/SERVER_DEPLOYMENT_GUIDE.md` (doc marker)
- `server/Docs/RELEASE_AND_UPDATE_GUIDE.md` (doc marker)
- `client/config/unified_config.yaml` + client-производные файлы через `client/config/auto_sync.py` (если client доступен)

## 4) Remote sync (Azure)

После push/pull кода на VM:
```bash
bash scripts/update_server_version.sh X.Y.Z.W
```

После publish assets дополнительно обязателен runtime-metadata sync:
- `update_manifest_remote_locked.sh` для `manifest.json` (url/size/sha256)
- создание/обновление `manifest_<version>.json` на VM из актуального `manifest.json`

## 5) Запреты

- Нельзя менять версию вручную в нескольких файлах.
- Нельзя менять `VERSION`/`unified_config` напрямую (они производные от manifest owner path).
- Нельзя использовать legacy-скрипты для версионирования.
- Нельзя использовать `SERVER_VERSION` как primary source.
- Нельзя обновлять только `manifest.json` без `manifest_<version>.json`.
- Нельзя завершать release, если `/updates/appcast.xml` и `/updates/health` не показывают target version.

## 6) DoD

- `manifest.json` содержит target `version/build`.
- `manifest_<version>.json` существует и совпадает по `version/build/url/size/sha256`.
- `VERSION` содержит ту же target-версию.
- `/health` и `/updates/health` возвращают target `latest_version/latest_build`.
- `/updates/appcast.xml` содержит target `sparkle:version` и `sparkle:shortVersionString`.
- `unified_config` синхронизирован с target-version.
