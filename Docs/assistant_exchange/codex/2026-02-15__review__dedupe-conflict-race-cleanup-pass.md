# Review: Dedupe / Conflict / Race Cleanup Pass

## Scope
- Удаление конфликтующих и лишних файлов
- Централизация version/update owner-потоков
- Снижение риска гонок и шумовых конфликтов в git

## Key Fixes
1. Приведен к канону fallback версии в `modules/update/config.py` (убран legacy hardcoded `1.6.0.35`).
2. Активные доки обновлены на `VERSION` (корень workspace), а не `server/VERSION`.
3. `Docs/VERSION_MANAGEMENT.md` переписан как канонический runbook.
4. Legacy-скрипты переведены в блокирующий deprecated-режим:
   - `scripts/deploy.sh`
   - `scripts/sync_manifest.sh`
   - `scripts/update_manifest_with_dmg.sh`
   - `scripts/fix_version_mismatch.sh`
   - `scripts/sync_version_centralization.sh`
5. `scripts/README.md` переведен на каноничные owner-скрипты.
6. Удалены лишние/пустые файлы и backup-хвосты.
7. Добавлены ignore-правила и удалены tracked `__pycache__/*.pyc` из git-индекса.
8. `scripts/update_server_version.sh` обновлен: запись версии на VM в корневой `VERSION`.

## Result
- Один канон для версии и релизного потока.
- Legacy пути заблокированы для предотвращения случайного использования.
- Значительно снижен шум в git и риск конфликтов от pycache.
