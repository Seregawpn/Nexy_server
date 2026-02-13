# Task Brief: Version-Only Manifest Update Flow

## Context
- Запрос: убрать необходимость ручного указания `artifact.size` при обновлении, оставить фокус на указании версии.
- Область: update subsystem (`server/modules/update`, `server/updates/scripts`).

## Changes
1. `server/modules/update/providers/update_server_provider.py`
- Удалена runtime-мутация манифеста в `download_handler`.
- При несовпадении размера теперь только warning в логах.

2. `server/updates/scripts/generate_manifest.py`
- Переведен на `argparse`.
- Новый контракт CLI: обязательны `artifact_path` и `version`, `--build` опционален (по умолчанию равен `version`).
- Добавлена проверка формата версии `X.Y.Z`.
- Явно зафиксировано в выводе, что `artifact.size` и `artifact.sha256` вычисляются автоматически.

3. `server/Docs/SERVER_DEVELOPMENT_RULES.md`
- Обновлены правила: `artifact.size`/`artifact.sha256` больше не ручной шаг, а результат генератора манифеста.

## Architecture Fit
- Source of Truth для release-метаданных остается манифест.
- Владелец расчета `size/sha256` централизован в release-скрипте генерации.
- Runtime download endpoint больше не меняет release-данные.

## Verification
- `python3 -m py_compile server/updates/scripts/generate_manifest.py` — OK.
- `python3 server/updates/scripts/generate_manifest.py --help` — OK, новый интерфейс доступен.
- Проверка `update_server_provider.py`: вызовов `update_manifest(...)` в `download_handler` больше нет.

## Notes
- Формат версии оставлен `X.Y.Z` по текущему контракту `VersionProvider`.
