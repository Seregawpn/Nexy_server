# Task Brief: Remove all app browsers (Dev + App)

## Context
Пользователь запросил удалить все браузерные артефакты приложения для Dev и обычного профиля.

## Actions
Удалены каталоги браузеров Playwright:
- `/Users/sergiyzasorin/Library/Application Support/Nexy/ms-playwright`
- `/Users/sergiyzasorin/Library/Application Support/Nexy-Dev/ms-playwright`

Также очищены временные профили browser-use:
- `/var/folders/**/browser-use-user-data-dir-*`

## Verification
- `find` по `ms-playwright`/`chromium-*` в `Nexy` и `Nexy-Dev` не возвращает результатов.
- `find` по `browser-use-user-data-dir-*` в `/var/folders` не возвращает результатов.

## Информация об изменениях
- Что изменено:
  - Удалены все локальные браузерные бинарники/кэши приложения (Dev и App profile).
- Список файлов:
  - `/Users/sergiyzasorin/Library/Application Support/Nexy/ms-playwright` (директория)
  - `/Users/sergiyzasorin/Library/Application Support/Nexy-Dev/ms-playwright` (директория)
  - `/var/folders/**/browser-use-user-data-dir-*` (временные директории)
- Причина/цель изменений:
  - Принудительный чистый re-install браузера при следующем browser task.
- Проверка:
  - Команды `find` после удаления подтвердили отсутствие каталогов.
