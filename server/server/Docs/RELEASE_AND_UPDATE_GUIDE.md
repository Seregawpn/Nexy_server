# Server Release & Update Guide

**Статус:** Active Rulebook  
**Обновлено:** 15 February 2026
**Текущий релиз документации:** `v1.6.1.43`

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
- `release_inbox/.gitkeep` хранится в git и не удаляется.
- Даже при ручном удалении папка автоматически пересоздаётся в `scripts/publish_assets_and_sync.py`.
- Каноничный скрипт публикации: `scripts/publish_assets_and_sync.py`.
- Манифест update-канала: `server/updates/manifests/manifest.json`.
- Единый release-tag в `Nexy_production`: `vX.Y.Z.W` (например `v1.6.1.40`).
- Все release assets (`Nexy.dmg`, `Nexy.pkg`, `LATEST_CHANGES.md`) публикуются в этот один tag.

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
- `Docs/SERVER_DEPLOYMENT_GUIDE.md` и `Docs/RELEASE_AND_UPDATE_GUIDE.md` (marker)
- `client/config/unified_config.yaml` + производные client-файлы через `client/config/auto_sync.py` (если доступен client workspace)

Update metadata:
1. `server/updates/manifests/manifest.json` (`version`, `build`, `artifact.*`)

Правило:
- `VERSION` (корень workspace) и `manifest.json` должны быть синхронизированы при релизе.
- Обновление `manifest.json` выполнять только через owner-скрипты (`publish_assets_and_sync.py` или `update_manifest_remote_locked.sh`), без ручного inline-редактирования.

---

## 3) Artifact Publication (Nexy_production)

### 3.1 Pre-check

```bash
test -d release_inbox && echo "OK: release_inbox exists" || echo "MISSING: release_inbox"
ls -la release_inbox
gh auth status
az vm run-command invoke \
  --resource-group NetworkWatcherRG \
  --name Nexy \
  --command-id RunShellScript \
  --scripts "grep -q '^GEMINI_API_KEY=' /home/azureuser/voice-assistant/config.env && echo 'OK: GEMINI_API_KEY present' || (echo 'MISSING: GEMINI_API_KEY' && exit 1)"
```

Ожидания:
- В `release_inbox` есть `Nexy.dmg` и/или `Nexy.pkg`.
- `gh auth status` успешен.
- На VM в `/home/azureuser/voice-assistant/config.env` присутствует `GEMINI_API_KEY`.
- Нет активного конкурирующего `az vm run-command` (исполнять команды последовательно).

### 3.2 Publish

```bash
python3 scripts/publish_assets_and_sync.py
```

Ожидаемые лог-маркеры:
- `Current Version: ...`
- `Release Tag: v...`
- `Target Repo: Seregawpn/Nexy_production`
- `Uploaded. URL: .../releases/download/vX.Y.Z.W/Nexy.dmg`
- `RELEASE COMPLETE`
- При повторном publish того же tag и тех же файлов: `already published, skip (tag=vX.Y.Z.W)`.

Dry-run:
```bash
python3 scripts/publish_assets_and_sync.py --dry-run
```

### 3.3 Verify

- `https://github.com/Seregawpn/Nexy_production/releases/tag/vX.Y.Z.W`
- `https://github.com/Seregawpn/Nexy_production/releases/download/vX.Y.Z.W/Nexy.dmg`
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

### 4.4 Wrong target repo/tag
Проверить в `scripts/publish_assets_and_sync.py`:
- `TARGET_REPO = "Seregawpn/Nexy_production"`
- Release tag формируется как `vX.Y.Z.W` из `VERSION`
- Для уже опубликованного tag перезапись запрещена (идемпотентный skip/блокировка)

---

## 5) Search / Logs (Поиск)

- Артефакты: `release_inbox/`
- Манифест: `server/updates/manifests/manifest.json`
- Логи публикации: stdout/stderr `python3 scripts/publish_assets_and_sync.py`
- Remote check: release URL version-tag `vX.Y.Z.W`

---

## 6) DoD

1. `release_inbox` существует и содержит артефакты.
2. Публикация завершилась без ошибок.
3. DMG/PKG доступны в `Nexy_production` в одном version-tag.
4. `manifest.json` обновлён и синхронизирован.
5. После code deploy `/health` и `/updates/health` показывают нужную версию.
