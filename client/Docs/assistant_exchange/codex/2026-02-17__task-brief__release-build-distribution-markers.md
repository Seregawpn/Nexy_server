# Task Brief: release/local distribution markers in release_build

## Context
Пользователь запросил исключить ситуацию, когда приложение продолжает открываться с Gatekeeper-warning из-за публикации неподходящего артефакта.

## Decision
Усилен существующий owner-поток `scripts/release_build.sh` без реархитектуры:
- release-режим явно маркируется как готовый к дистрибуции;
- local-режим явно маркируется как запрещенный для внешней публикации.

## Verification
- `bash -n scripts/release_build.sh` → OK
- Проверено наличие новых маркеров/проверок через `rg`.

## Информация об изменениях
- Что изменено:
  - Добавлены маркеры результата сборки в `dist/`:
    - `RELEASE_NOTARIZED_READY.txt` для validated release;
    - `NOT_FOR_DISTRIBUTION_LOCAL_BUILD.txt` для local-сборки.
  - Добавлена финальная проверка notarization для `dist/Nexy.dmg` в release-режиме (если DMG присутствует).
  - Исключено одновременное существование конфликтующих маркеров (cleanup обоих перед выставлением актуального).
- Список файлов:
  - `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/scripts/release_build.sh`
  - `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/Docs/assistant_exchange/codex/2026-02-17__task-brief__release-build-distribution-markers.md`
- Причина/цель изменений:
  - Снизить риск публикации non-release/non-notarized артефакта и последующего Gatekeeper prompt у конечного пользователя.
- Проверка (что выполнено для валидации):
  - Синтаксическая проверка bash-скрипта;
  - Проверка присутствия новых guard/maker строк.
