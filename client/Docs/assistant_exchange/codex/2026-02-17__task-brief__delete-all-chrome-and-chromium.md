## Task
Удалить все Chrome/Chromium и связанные браузерные артефакты на машине для чистой проверки поведения приложения.

## Actions
- Остановлены процессы, связанные с Google Chrome/Chromium/browser-use user data.
- Удалены app bundles:
  - `/Applications/Google Chrome.app`
  - `/Applications/Chromium.app`
  - `~/Applications/Google Chrome.app`
  - `~/Applications/Chromium.app`
  - `Google Chrome Canary.app` (если присутствовал)
- Удалены пользовательские данные и кэши:
  - `~/Library/Application Support/Google`
  - `~/Library/Application Support/Chromium`
  - `~/Library/Caches/Google`
  - `~/.config/browseruse`
  - `ms-playwright/ms-playwright-go` в Nexy/Nexy-Dev/cache
- Удалены временные каталоги в `/var/folders`:
  - `browser-use-user-data-dir-*`
  - `com.google.Chrome*`

## Verification
- Повторный поиск app bundles не возвращает Chrome/Chromium.
- Все указанные каталоги данных/кэшей отсутствуют.
- Временные папки `browser-use-user-data-dir-*` отсутствуют.
- Процессы Chrome/Chromium/browser-use не запущены.

## Информация об изменениях
- Что изменено:
  - Полностью удалены Chrome/Chromium и все найденные связанные данные.
- Список файлов:
  - `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/Docs/assistant_exchange/codex/2026-02-17__task-brief__delete-all-chrome-and-chromium.md`
- Причина/цель изменений:
  - Нужен полностью чистый браузерный контур для диагностики проблем автоматизации.
- Проверка:
  - Выполнены пост-проверки по наличию app/data/temp/processes.
