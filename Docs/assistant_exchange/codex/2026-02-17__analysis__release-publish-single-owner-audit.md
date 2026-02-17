# Release Publish Single Owner Audit

## Метаданные
- Ассистент: codex
- Тип: analysis
- Дата: 2026-02-17
- ID (INS-###): N/A

## Diagnosis
Есть конфликт owner-пути публикации: client-документы требуют `Nexy_client_test`, серверные правила и publish-скрипт публикуют DMG/PKG в `Nexy_production` с fixed tags `Update/App`.
Это создает второй путь принятия решения по source-of-truth для артефактов/metadata и допускает рассинхрон.

## Root Cause
Разные регламенты client/server + legacy server publish script (`publish_assets_and_sync.py`) с overwrite-поведением (`gh release upload --clobber`) и без idempotency guard → один и тот же tag может содержать новые бинарники при повторном publish → hash/url в metadata могут расходиться с ожиданиями по версии.

## Optimal Fix
Goal: единый production owner для артефактов и metadata без дублирующих путей.

Architecture Fit:
- Where it belongs: release orchestration (CI/workflow + server metadata publisher).
- Source of Truth: один GitHub Release на один `version/tag`.

Implementation Plan:
1. Зафиксировать единый target repo для production release (убрать конфликт `Nexy_client_test` vs `Nexy_production` в канонических docs).
2. Убрать fixed tags `Update/App`; перейти к version-tag (`vX.Y.Z.W`) и единичному release entry.
3. В publish owner добавить idempotency guard: если version/tag уже опубликован и checksums совпадают, лог `already published, skip`.
4. Запретить серверную повторную загрузку бинарников вне owner-потока; сервер обновляет только metadata (size/sha256/url) из опубликованного release.
5. Оставить обязательные pre-publish проверки подписи/нотаризации только через `scripts/release_build.sh release` + build gates.

## Verification
- Повторный publish того же tag возвращает skip, без перезаписи asset.
- `manifest.json` совпадает с GitHub Release по `artifact.url/size/sha256`.
- В проекте остается один канонический target repo для production artifacts.
- Локальные и CI инструкции не содержат альтернативного publish path.

## Информация об изменениях
- Что изменено:
  - Добавлен аналитический отчет по publish owner и конфликтам source-of-truth.
- Файлы:
  - `Docs/assistant_exchange/codex/2026-02-17__analysis__release-publish-single-owner-audit.md`
- Причина/цель:
  - Зафиксировать текущее состояние, root cause и architecture-compatible plan.
- Проверка:
  - Выполнен audit `client/*`, `server/server/*`, workflow и release scripts.

## Запрос/цель
Проверить, как правильно публиковать приложение в GitHub, и устранить двусмысленность client/server publish flow.

## Контекст
- Файлы:
  - `client/Docs/RELEASE_VERSIONING_AND_PUBLISHING.md`
  - `client/scripts/release_build.sh`
  - `client/packaging/build_final.sh`
  - `server/server/Docs/RELEASE_AND_UPDATE_GUIDE.md`
  - `server/server/scripts/publish_assets_and_sync.py`
  - `server/server/scripts/update_manifest_remote_locked.sh`
  - `server/server/updates/manifests/manifest.json`
- Документы:
  - `Docs/ASSISTANT_COORDINATION_PROTOCOL.md`
  - `Docs/ARCHITECTURE_OVERVIEW.md`
  - `Docs/PROJECT_REQUIREMENTS.md`
- Ограничения:
  - Без реархитектуры; только centralization и удаление дублирующих publish paths.

## Решения/выводы
- Сейчас production artifact owner фактически `server/server/scripts/publish_assets_and_sync.py` (`Nexy_production`, tags `Update/App`).
- Client policy про `Nexy_client_test` применима к client code push, но конфликтует с production release routing и требует явного разграничения в канонических документах.
- Нет release workflow, который централизует публикацию бинарников; есть только quality/deploy workflows.

## Открытые вопросы
- Какой репозиторий фиксируем как production artifact store: `Nexy_production` или `Nexy_client_test`?
- Нужна ли обратная совместимость по старым fixed tags `Update/App` для существующих клиентов?

## Следующие шаги
- Выбрать единый production artifact repo и зафиксировать в root/client/server канонических документах.
- Внедрить idempotency guard в publish owner и убрать overwrite-режим для уже опубликованного version-tag.
- Добавить release workflow owner (manual dispatch) для publish+metadata без второго пути.
