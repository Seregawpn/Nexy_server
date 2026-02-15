# Task Brief: Auto Version Sync From Config

## Goal
Сделать так, чтобы при обновлении версии в `config/unified_config.yaml` версия синхронизировалась во всех обязательных местах централизованно.

## Changes
1. Добавлен централизованный синк-скрипт:
   - `config/auto_sync.py`
   - Source of Truth: `config/unified_config.yaml -> app.version`
   - Поддерживает:
     - sync mode: записывает изменения
     - check mode: `--check` (дрейф версии без записи)

2. Переведён `set_version` на SoT-подход:
   - `scripts/set_version.py`
   - Теперь: записывает версию в `unified_config.yaml` и вызывает `config/auto_sync.py`

3. Интеграция в релизный pipeline:
   - `packaging/build_final.sh`
   - Вместо локального update модулей теперь запускает:
     - `python config/auto_sync.py --scope version`

4. Обновлён регламент:
   - `Docs/RELEASE_VERSIONING_AND_PUBLISHING.md`
   - В обязательный процесс добавлен шаг запуска `config/auto_sync.py`

## Synced Targets (version)
- `client/VERSION_INFO.json`
- `packaging/distribution.xml`
- `modules/*/macos/info/Info.plist`
- `integration/**/__init__.py` и `modules/**/__init__.py` где есть `__version__`
- `RELEASE_CHECKLIST.md`
- `Docs/RELEASE_VERSIONING_AND_PUBLISHING.md`
- `Docs/PACKAGING_FINAL_GUIDE.md`
- `config/README.md`

## Verification
- `./.venv/bin/python config/auto_sync.py --scope version` -> synced
- `./.venv/bin/python config/auto_sync.py --scope version --check` -> OK
- `bash -n packaging/build_final.sh` -> OK
- `./.venv/bin/python scripts/set_version.py 1.6.1.38` -> OK (idempotent)

## Result
Version-sync централизован и автоматизирован от `unified_config.yaml`; ручной разнобой между runtime/packaging/docs устранён.
