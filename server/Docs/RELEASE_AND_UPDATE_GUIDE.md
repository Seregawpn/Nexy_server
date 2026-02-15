# Server Release & Update Guide

**Статус:** Active Rulebook  
**Обновлено:** 15 February 2026
**Текущий релиз документации:** `v1.6.1.38`

Канон публикации клиентских артефактов и синхронизации update-канала.

---

## 0) Repo Responsibilities (Mandatory)

1. `Seregawpn/Nexy`  
Назначение: корневой workspace (общий код/документация).

2. `Seregawpn/Nexy_server`  
Назначение: серверный код и deploy pipeline на Azure VM.

3. `Seregawpn/Nexy_production/releases`  
Назначение: публикация `Nexy.dmg` и `Nexy.pkg` для клиентских обновлений.

Правила:
- Asset pipeline не смешивать с code pipeline.
- DMG/PKG публиковать только в `Nexy_production`.
- `Nexy_server` не использовать как хранилище клиентских артефактов.

---

## 1) Release Infrastructure Rules

- `release_inbox` должен существовать в корне репозитория.
- Каноничный скрипт публикации: `scripts/publish_assets_and_sync.py`.
- Манифест update-канала: `server/updates/manifests/manifest.json`.
- Fixed tags в `Nexy_production`:
  - `Nexy.dmg` -> `Update`
  - `Nexy.pkg` -> `App`

---

## 2) Version Source of Truth

Единый Source of Truth:
1. `VERSION` (в корне workspace)

Автосинхронизация всех версионных точек:
```bash
python3 scripts/update_version.py X.Y.Z.W
```

Скрипт обновляет:
- `VERSION`
- `server/config/unified_config.yaml`
- `server/config/unified_config.py` (env fallback)
- `server/config.env.example`
- `server/updates/manifests/manifest.json` (`version`, `build`)
- `server/Docs/SERVER_DEPLOYMENT_GUIDE.md` и `server/Docs/RELEASE_AND_UPDATE_GUIDE.md` (marker)
- `client/config/unified_config.yaml` + производные client-файлы через `client/config/auto_sync.py` (если доступен client workspace)

Update metadata:
1. `server/updates/manifests/manifest.json` (`version`, `build`, `artifact.*`)

Правило:
- `server/VERSION` и `manifest.json` должны быть синхронизированы при релизе.
- Обновление `manifest.json` выполнять только через owner-скрипты (`publish_assets_and_sync.py` или `update_manifest_remote_locked.sh`), без ручного inline-редактирования.

---

## 3) Artifact Publication (Nexy_production)

### 3.1 Pre-check

```bash
test -d release_inbox && echo "OK: release_inbox exists" || echo "MISSING: release_inbox"
ls -la release_inbox
gh auth status
```

Ожидания:
- В `release_inbox` есть `Nexy.dmg` и/или `Nexy.pkg`.
- `gh auth status` успешен.

### 3.2 Publish

```bash
python3 scripts/publish_assets_and_sync.py
```

Ожидаемые лог-маркеры:
- `Current Version: ...`
- `Target Repo: Seregawpn/Nexy_production`
- `Uploaded. URL: .../releases/download/Update/Nexy.dmg`
- `RELEASE COMPLETE`

Dry-run:
```bash
python3 scripts/publish_assets_and_sync.py --dry-run
```

### 3.3 Verify

- `https://github.com/Seregawpn/Nexy_production/releases/tag/Update`
- `https://github.com/Seregawpn/Nexy_production/releases/tag/App`
- `https://github.com/Seregawpn/Nexy_production/releases/download/Update/Nexy.dmg`
- Проверить `server/updates/manifests/manifest.json`:
  - `version`, `build`
  - `artifact.url`, `artifact.size`, `artifact.sha256`

---

## 4) Troubleshooting

### 4.1 Inbox not found
```bash
mkdir -p release_inbox
ls -la release_inbox
```

### 4.2 Script not found
Корректно:
```bash
python3 scripts/publish_assets_and_sync.py
```

### 4.3 GH CLI auth issues
```bash
gh --version
gh auth status
gh auth login
```

### 4.4 Wrong target repo/tags
Проверить в `scripts/publish_assets_and_sync.py`:
- `TARGET_REPO = "Seregawpn/Nexy_production"`
- `DMG_TAG = "Update"`
- `PKG_TAG = "App"`

---

## 5) Search / Logs (Поиск)

- Артефакты: `release_inbox/`
- Манифест: `server/updates/manifests/manifest.json`
- Логи публикации: stdout/stderr `python3 scripts/publish_assets_and_sync.py`
- Remote check: release URLs `Update` и `App`

---

## 6) DoD

1. `release_inbox` существует и содержит артефакты.
2. Публикация завершилась без ошибок.
3. DMG/PKG доступны в `Nexy_production`.
4. `manifest.json` обновлён и синхронизирован.
5. После code deploy `/health` и `/updates/health` показывают нужную версию.
