# Task Brief — Ruff Phase 2 (E501 config subset)

## Goal
Снять E501 в конфигурационных файлах без изменения логики.

## Changes
- Разбил длинные строки и параметры в `config/unified_config_loader.py`.
- Вынес `allowed_keys` в набор в `config/server_manager.py`.
- Переформатировал `yaml.dump` в `config/updater_manager.py`.

## Files
- `config/unified_config_loader.py`
- `config/server_manager.py`
- `config/updater_manager.py`

## Verification
- `./.venv/bin/ruff check config --select E501`

## Result
All checks passed for config E501.
