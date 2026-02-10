# Task Brief — remove left_shift hotkey support

## Context
Пользователь попросил полностью убрать `left_shift` из hotkey-поддержки, оставить только актуальные варианты.

## Changes
1. Config validation
- File: `config/unified_config_loader.py`
- `supported_keys` обновлен: удален `left_shift`, оставлены `left_control` и `ctrl_n`.

2. Quartz backend
- File: `modules/input_processing/keyboard/mac/quartz_monitor.py`
- Удалена таблица keycode для `left_shift`.
- Одиночная клавиша в flagsChanged теперь обрабатывается только как `left_control`.
- Переименовано внутреннее состояние `previous_left_shift` -> generic modifier state.
- Сохранен и применен guard против конфликтных модификаторов для `ctrl_n` (Option/Command).

3. pynput fallback backend
- File: `modules/input_processing/keyboard/keyboard_monitor.py`
- Удален путь `left_shift` в `_is_target_key`.
- Одиночный key path оставлен для `left_control`.
- Guard для дополнительных модификаторов (Option/Command) в combo `ctrl_n` сохранен.

## Architecture fit
- Source of truth не менялся: `InputProcessingIntegration` остается владельцем PTT lifecycle.
- Изменения ограничены adapter-слоем keyboard monitor + config validation.

## Verification
- `python3 -m py_compile config/unified_config_loader.py modules/input_processing/keyboard/mac/quartz_monitor.py modules/input_processing/keyboard/keyboard_monitor.py`
- Result: success.

## Expected effect
- `left_shift` больше не является допустимым hotkey и не активирует PTT.
- `ctrl_n` и `left_control` продолжают работать по текущей архитектуре.
- Меньше путаницы и меньше ветвлений в input adapter.
