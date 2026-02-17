## Task
Синхронизация packaged артефактов клиента в серверную папку release inbox.

## Actions
- Скопированы файлы:
  - `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.pkg` -> `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/server/release_inbox/Nexy.pkg`
  - `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/dist/Nexy.dmg` -> `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/server/release_inbox/Nexy.dmg`

## Verification
- Проверены размеры и timestamps в `server/release_inbox`.
- Проверены SHA-256 хэши источника и целевых файлов: совпадают для `pkg` и `dmg`.

## Информация об изменениях
- Что изменено:
  - Обновлены артефакты в `server/release_inbox` на актуальные из `client/dist`.
- Список файлов:
  - `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/Docs/assistant_exchange/codex/2026-02-17__task-brief__sync-release-inbox-artifacts.md`
- Причина/цель изменений:
  - Требовалось, чтобы после упаковки серверная папка содержала текущие файлы приложения.
- Проверка:
  - `ls -lhT` и `shasum -a 256` для source/target файлов.
