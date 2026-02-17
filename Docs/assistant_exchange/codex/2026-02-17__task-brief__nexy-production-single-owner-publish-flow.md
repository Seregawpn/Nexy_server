# Nexy Production Single Owner Publish Flow

## Метаданные
- Ассистент: codex
- Тип: task-brief
- Дата: 2026-02-17
- ID (INS-###): N/A

## Diagnosis
Публикация release-артефактов была неидемпотентной (перезапись под тем же tag через `--clobber`) и допускала вторичный metadata-path в runtime.
Это нарушало single-owner принцип и повышало риск рассинхрона `url/size/sha256`.

## Root Cause
Fixed-tag publish + overwrite behavior + runtime manifest mutation → один tag мог содержать разные бинарники в разное время → metadata drift.

## Optimal Fix
- Закрепить production owner: `Seregawpn/Nexy_production`.
- Перейти на единый version-tag `vX.Y.Z.W` для `Nexy.dmg`, `Nexy.pkg`, `LATEST_CHANGES.md`.
- Добавить idempotency guard: если asset уже опубликован и совпадает по размеру+sha256, publish skip.
- Запретить overwrite для уже опубликованного version-tag (вместо `--clobber` блокировка на mismatch).
- Убрать runtime обновление `manifest` при download: metadata меняется только в publish flow.

## Verification
- `python3 -m py_compile server/server/scripts/publish_assets_and_sync.py server/server/modules/update/providers/update_server_provider.py` → OK.
- Проверен diff:
  - version-tag publish flow;
  - `already published, skip` path;
  - no runtime manifest mutation;
  - docs aligned on `Nexy_production` + version-tag.

## Информация об изменениях
- Что изменено:
  - Внедрен idempotent publish flow с единым version-tag.
  - Удалена перезапись release assets при повторном publish.
  - Убрана runtime-мутация metadata в update download handler.
  - Обновлена каноническая документация release-потока.
- Файлы:
  - `server/server/scripts/publish_assets_and_sync.py`
  - `server/server/modules/update/providers/update_server_provider.py`
  - `server/server/Docs/RELEASE_AND_UPDATE_GUIDE.md`
  - `client/Docs/RELEASE_VERSIONING_AND_PUBLISHING.md`
- Причина/цель:
  - Централизация owner-пути публикации и исключение рассинхрона артефактов/metadata.
- Проверка:
  - Компиляция Python-файлов и review diff по ключевым сценариям.

## Запрос/цель
Зафиксировать единый production поток публикации в GitHub для клиента и исключить дубли/гонки публикации.

## Контекст
- `Seregawpn/Nexy_production` выбран пользователем как единственный production owner.

## Решения/выводы
- Publish owner централизован в `publish_assets_and_sync.py`.
- Version-tag выбран единственным контейнером release assets.
- Runtime update-server больше не правит manifest в download path.

## Открытые вопросы
- Нужен ли отдельный migration шаг для legacy клиентов, ожидающих fixed tag `Update`.

## Следующие шаги
- Запустить dry-run и реальный publish для следующей версии.
- Проверить клиентский update path на новой версии с version-tag URL.
