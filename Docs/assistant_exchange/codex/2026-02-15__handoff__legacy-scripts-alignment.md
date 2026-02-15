# Handoff: Legacy Scripts Alignment (Azure defaults)

## Метаданные
- Ассистент: codex
- Тип: handoff
- Дата: 2026-02-15
- ID (INS-###): N/A

## Diagnosis
В `server/scripts` оставались legacy-дефолты для старой VM/IP (`Nexy/nexy-regular`, `20.151.51.172`), что создавало риск запуска скриптов против неверной инфраструктуры.

## Root Cause
Исторические утилиты и README развивались отдельно от каноничных deploy-docs -> накопились stale defaults/примерные команды -> операторский риск ошибок.

## Optimal Fix
Сделан массовый выравнивающий проход по utility-скриптам и script-docs в `server/scripts`:
- IP: `20.151.51.172` -> `20.63.24.187`
- `AZURE_RESOURCE_GROUP="Nexy"` -> `AZURE_RESOURCE_GROUP="NetworkWatcherRG"`
- `AZURE_VM_NAME="nexy-regular"` / `VM_NAME="nexy-regular"` -> `...="Nexy"`

## Verification
- `rg`-поиск старых значений в `server/scripts`: не найдено.
- Синтакс-проверка изменённых скриптов:
  - `bash -n` для `.sh` — ok
  - `python3 -m py_compile` для `.py` — ok

## Контекст
- Файлы: набор utility-скриптов и `README`/`SYNC_MANIFEST_README` в `server/scripts`
- Ограничения: без реархитектуры, только приведение к текущему прод-контуру.

## Следующие шаги
- При желании: вынести IP/RG/VM в единый shared `.env` для всех utility-скриптов, чтобы убрать будущий drift.
