# Remove Conflicting Release Build Script

## Метаданные
- Ассистент: codex
- Тип: task-brief
- Дата: 2026-02-17
- ID (INS-###): N/A

## Diagnosis
В проекте оставался альтернативный packaging entrypoint `scripts/release_build.sh`, который конфликтовал с каноническим правилом единственного пути `packaging/build_final.sh`.

## Root Cause
Legacy wrapper для сборки сохранился после централизации packaging owner.

## Optimal Fix
Удален конфликтный скрипт:
- `client/scripts/release_build.sh`

Синхронизирована активная документация:
- `client/Docs/RELEASE_VERSIONING_AND_PUBLISHING.md`
  - ссылка обновлена на `./packaging/build_final.sh`.

## Verification
- Проверка активных ссылок на `release_build.sh` (без archive/assistant_exchange) → отсутствуют.

## Информация об изменениях
- Что изменено:
  - Удален конфликтный packaging скрипт.
  - Обновлена каноническая release-документация.
- Файлы:
  - `client/scripts/release_build.sh` (deleted)
  - `client/Docs/RELEASE_VERSIONING_AND_PUBLISHING.md`
- Причина/цель:
  - Исключить второй путь сборки и снизить риск конфликтов release-процесса.
- Проверка:
  - grep-проверка активных ссылок на удаленный скрипт.

## Запрос/цель
Удалить неиспользуемый packaging путь, который может вызывать конфликты.

## Контекст
- Packaging owner: `client/packaging/build_final.sh`.

## Решения/выводы
- В активном контуре остался один packaging entrypoint.

## Открытые вопросы
- Нет.

## Следующие шаги
- Использовать только:
  - `./client/packaging/build_final.sh`
  - либо `./scripts/release_package_and_publish.sh` для end-to-end flow.
