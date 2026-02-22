# Task Brief: Replace client from release/v1.6.1.43

## Context
Пользователь запросил полностью заменить текущее содержимое клиентской части на состояние `client` из `https://github.com/Seregawpn/Nexy/tree/release/v1.6.1.43/client`.

## Actions
- Подтвержден доступ к ветке: `origin/release/v1.6.1.43`.
- Выполнен fetch целевой ветки: `git fetch --depth 1 origin release/v1.6.1.43`.
- Выполнена замена клиентской директории из fetched commit: `git checkout FETCH_HEAD -- client`.
- Выполнена очистка лишних файлов в `client`: `git clean -fd client`.

## Verification
- Проверен статус рабочей копии в `client`.
- Внутри `client` нет unstaged-расхождений после замены.
- Текущее отличие в клиентской части: staged добавление `tests/test_atomic_replace_app.py`.

## Информация об изменениях
- Что изменено:
  - Содержимое директории `client` синхронизировано с `origin/release/v1.6.1.43`.
- Список файлов:
  - `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/tests/test_atomic_replace_app.py` (staged add)
- Причина/цель изменений:
  - Выполнить прямую замену текущей клиентской части на целевой релизный источник пользователя.
- Проверка (что выполнено для валидации):
  - `git ls-remote --heads origin release/v1.6.1.43`
  - `git fetch --depth 1 origin release/v1.6.1.43`
  - `git checkout FETCH_HEAD -- client`
  - `git clean -fd client`
  - `git status --short .`
