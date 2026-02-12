# Restart Pending SoT and Autostart Config Dedupe

## Метаданные
- Ассистент: codex
- Тип: task-brief
- Дата: 2026-02-11

## Diagnosis
Ось `restart_pending` в Snapshot была нецентрализована (константа `False`), а в autostart-модуле существовал дублирующий конфиг-класс.

## Root Cause
1) Источник `restart_pending` не был подключен к V2 ledger.
2) В `modules/autostart_manager` остались два определения `AutostartConfig`.

## Changes
- В `integration/core/selectors.py` добавлен selector `is_restart_pending(...)` c чтением `permission_ledger.json` (SoT).
- `create_snapshot_from_state(...)` теперь заполняет `restart_pending` через selector (вместо hardcoded `False`).
- Удален дублирующий `modules/autostart_manager/core/config.py`.
- В `modules/autostart_manager/__init__.py` alias `Config` теперь указывает на `AutostartConfig` из `core/types.py`.

## Verification
- `python3 -m py_compile` для затронутых модулей — ok.
- Поиск по коду подтверждает: `restart_pending` больше не hardcoded в Snapshot.
- Импортов удаленного `autostart_manager/core/config.py` не осталось.
