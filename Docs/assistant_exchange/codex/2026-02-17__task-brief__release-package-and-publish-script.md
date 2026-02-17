# Release Package And Publish Script

## Метаданные
- Ассистент: codex
- Тип: task-brief
- Дата: 2026-02-17
- ID (INS-###): N/A

## Diagnosis
Релизный процесс состоял из нескольких ручных команд (packaging, publish, remote manifest sync), из-за чего его было сложно повторять без ошибок.

## Root Cause
Отсутствовал единый entrypoint-скрипт для последовательного выполнения production release flow.

## Optimal Fix
Добавлен единый orchestration script:
- `scripts/release_package_and_publish.sh`

Он выполняет:
1. Packaging: `client/scripts/release_build.sh release`
2. GitHub publish: `server/server/scripts/publish_assets_and_sync.py`
3. Remote manifest sync (без server deploy): `server/server/scripts/update_manifest_remote_locked.sh`

Поддерживает флаги:
- `--skip-build`
- `--skip-publish`
- `--skip-remote-manifest`
- `--dry-run`

## Verification
- `bash -n scripts/release_package_and_publish.sh` → OK
- Скрипт executable (`chmod +x`) применен.

## Информация об изменениях
- Что изменено:
  - Добавлен единый script для packaging + publish + remote-manifest-sync.
- Файлы:
  - `scripts/release_package_and_publish.sh`
- Причина/цель:
  - Упростить и централизовать production release flow одной командой.
- Проверка:
  - Синтаксическая проверка bash.

## Запрос/цель
Сделать один скрипт, который можно использовать для этапов packaging и публикации.

## Контекст
- Production artifacts owner: `Seregawpn/Nexy_production`.
- Server code deploy не требуется для обычного artifact release.

## Решения/выводы
- Flow централизован, ручные переходы между командами минимизированы.

## Открытые вопросы
- Нет.

## Следующие шаги
- Запустить:
  - `./scripts/release_package_and_publish.sh`
  - или dry-run: `./scripts/release_package_and_publish.sh --skip-build --dry-run`
