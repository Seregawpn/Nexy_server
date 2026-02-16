# Task Brief: packaging auto-sync to server release_inbox

## Метаданные
- Ассистент: codex
- Тип: task-brief
- Дата: 2026-02-16
- ID (INS-###): N/A

## Diagnosis
Синхронизация артефактов в `server/release_inbox` была привязана к `scripts/release_build.sh`, но упаковка запускалась через `packaging/build_final.sh`, из-за чего owner-сценарий не всегда выполнялся.

## Root Cause
Разделение entrypoint'ов упаковки → sync был не в каноническом owner-скрипте упаковки → после успешной упаковки артефакты могли не попадать в `server/release_inbox`.

## Optimal Fix
Цель: гарантировать единый и обязательный путь доставки `Nexy.dmg`/`Nexy.pkg`/`LATEST_CHANGES.md` в `server/release_inbox` после любой успешной упаковки.

- Source of Truth: `packaging/build_final.sh` (канонический owner потока упаковки).
- Реализация:
  - Добавлен обязательный шаг `Шаг 12: Синхронизация release_inbox` в `packaging/build_final.sh`.
  - Подключен существующий `scripts/sync_release_inbox.sh` (без дублирования логики копирования).
  - Из `scripts/release_build.sh` удалён дублирующий прямой вызов sync (остался единый owner через `build_final.sh`).

## Verification
- `bash -n packaging/build_final.sh` -> OK
- `bash -n scripts/release_build.sh` -> OK
- `./scripts/sync_release_inbox.sh` -> OK (файлы обновлены в `../server/release_inbox`)
- Проверено наличие в inbox:
  - `Nexy.dmg`
  - `Nexy.pkg`
  - `LATEST_CHANGES.md`

## Информация об изменениях
- Что изменено:
  - В `packaging/build_final.sh` добавлен обязательный post-packaging sync в `release_inbox`.
  - В `scripts/release_build.sh` удалён дублирующий sync-вызов.
- Файлы:
  - `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/packaging/build_final.sh`
  - `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/scripts/release_build.sh`
- Причина/цель:
  - Сделать перенос артефактов с клиентской части в серверный inbox обязательным и централизованным.
- Проверка:
  - Синтаксическая проверка shell-скриптов + фактический запуск sync с подтверждением файлов в inbox.

## Следующие шаги
- Для релизов запускать `packaging/build_final.sh` или `scripts/release_build.sh`; в обоих случаях sync теперь проходит через единый owner `build_final.sh`.
