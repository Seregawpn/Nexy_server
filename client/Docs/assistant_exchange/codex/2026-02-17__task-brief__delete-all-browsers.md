## Task
Удаление всех браузерных артефактов приложения (Dev + App), включая временные user-data директории.

## Actions
- Выполнено удаление:
  - `/Users/sergiyzasorin/Library/Application Support/Nexy/ms-playwright`
  - `/Users/sergiyzasorin/Library/Application Support/Nexy-Dev/ms-playwright`
  - `/Users/sergiyzasorin/Library/Caches/ms-playwright`
  - `/Users/sergiyzasorin/.cache/ms-playwright`
  - `/var/folders/.../T/browser-use-user-data-dir-*`

## Verification
- Проверено существование директорий после удаления.
- Текущий результат:
  - все `ms-playwright` директории отсутствуют;
  - временные `browser-use-user-data-dir-*` отсутствуют.

## Информация об изменениях
- Что изменено:
  - Удалены все обнаруженные браузерные артефакты Nexy (dev/prod/cache/temp).
- Список файлов:
  - `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/Docs/assistant_exchange/codex/2026-02-17__task-brief__delete-all-browsers.md`
- Причина/цель изменений:
  - Принудительно сбросить локальные браузеры и user-data, чтобы приложение выполнило чистую переустановку браузера при следующем запуске задачи.
- Проверка:
  - Выполнены post-check команды на отсутствие директорий.
