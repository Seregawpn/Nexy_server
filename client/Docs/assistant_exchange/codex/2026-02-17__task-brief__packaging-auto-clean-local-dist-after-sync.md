## Task
Добавить в packaging-скрипт автоматическое удаление локальных финальных артефактов клиента после успешной синхронизации в `server/release_inbox`.

## Actions
- Обновлен `packaging/build_final.sh`:
  - Добавлена финальная очистка `dist` после sync/install/smoke:
    - удаление `dist/Nexy.pkg`
    - удаление `dist/Nexy.dmg`
    - удаление `dist/packaging_verification.log`
  - Добавлен guard `NEXY_KEEP_LOCAL_DIST_ARTIFACTS=1` для отключения этой очистки.
- Обновлен `scripts/release_build.sh`:
  - Для legacy flow установлен `export NEXY_KEEP_LOCAL_DIST_ARTIFACTS=1`, чтобы не ломать `verify_packaging_artifacts.sh` (он читает `dist`).

## Verification
- `bash -n packaging/build_final.sh` — OK
- `bash -n scripts/release_build.sh` — OK
- Проверка вставок через `rg` — новые блоки и переменные на месте.

## Информация об изменениях
- Что изменено:
  - Автоматизирована очистка локальных артефактов после успешной публикации в `release_inbox`.
  - Сохранена совместимость с `release_build.sh`.
- Список файлов:
  - `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/packaging/build_final.sh`
  - `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/scripts/release_build.sh`
  - `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/Docs/assistant_exchange/codex/2026-02-17__task-brief__packaging-auto-clean-local-dist-after-sync.md`
- Причина/цель изменений:
  - По требованию: после упаковки не хранить финальные артефакты в клиентской папке, оставлять их в серверной папке release.
- Проверка:
  - Выполнены синтаксические проверки bash-скриптов и поиск новых блоков в коде.
