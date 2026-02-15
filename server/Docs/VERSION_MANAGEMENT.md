# Version Management (Canonical)

**Статус:** Active Rulebook  
**Обновлено:** 15 February 2026

## 1) Source of Truth

Единый источник версии:
- `VERSION` (в корне репозитория)

Формат версии:
- `X.Y.Z.W` (пример: `1.6.1.38`)

## 2) Единственный owner-скрипт

Использовать только:
```bash
python3 server/scripts/update_version.py X.Y.Z.W
```

Проверка:
```bash
python3 server/scripts/update_version.py --read
python3 server/scripts/update_version.py X.Y.Z.W --check
```

## 3) Что синхронизирует скрипт

- `VERSION`
- `server/config/unified_config.yaml`
- `server/config/unified_config.py` (fallback)
- `server/config.env.example`
- `server/updates/manifests/manifest.json` (`version`, `build`, `release_date`)
- `server/Docs/SERVER_DEPLOYMENT_GUIDE.md` (doc marker)
- `server/Docs/RELEASE_AND_UPDATE_GUIDE.md` (doc marker)

## 4) Remote sync (Azure)

После push/pull кода на VM:
```bash
bash server/scripts/update_server_version.sh X.Y.Z.W
```

## 5) Запреты

- Нельзя менять версию вручную в нескольких файлах.
- Нельзя использовать legacy-скрипты для версионирования.
- Нельзя использовать `SERVER_VERSION` как primary source.

## 6) DoD

- `VERSION` содержит target-версию.
- `/health` и `/updates/health` возвращают target `latest_version/latest_build`.
- `server/updates/manifests/manifest.json` синхронизирован с `VERSION`.
