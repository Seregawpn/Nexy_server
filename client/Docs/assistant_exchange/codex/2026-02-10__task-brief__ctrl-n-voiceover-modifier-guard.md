# Task Brief — Ctrl+N modifier conflict guard

## Context
Пользователь сообщил, что при включенном Nexy и VoiceOver клавиатура ведет себя некорректно (внешние сочетания работают нестабильно). Требуется убрать конфликт без ломки текущей архитектуры PTT.

## Diagnosis
Root-cause в input layer: combo `ctrl_n` активировался даже когда зажаты дополнительные модификаторы (Option/Command), из-за чего Nexy перехватывал `N` в чужих chord-сценариях (в т.ч. VoiceOver).

## Implemented changes
1. Quartz combo guard against extra modifiers:
- File: `modules/input_processing/keyboard/mac/quartz_monitor.py`
- Added detection of `Option/Command` flags (`kCGEventFlagMaskAlternate`, `kCGEventFlagMaskCommand`).
- `ctrl_n` теперь активируется только если нет дополнительных модификаторов.
- При появлении дополнительных модификаторов активная combo принудительно деактивируется (`blocked_modifiers`).
- В состоянии blocked `N` больше не подавляется, события проходят в систему.
- Added diagnostic status field `combo_blocked_by_modifiers`.

2. Fallback parity for pynput monitor:
- File: `modules/input_processing/keyboard/keyboard_monitor.py`
- Added `_other_modifier_pressed` state.
- Combo `ctrl_n` activates only when other modifiers are not pressed.
- Added helper for Option/Command keys in fallback backend.

3. Config validation sync:
- File: `config/unified_config_loader.py`
- Added `left_control` to supported key list (consistency with keyboard monitor support).

## Architecture fit
- Source of truth сохранен: `integration/integrations/input_processing_integration.py` (PTT lifecycle).
- Изменения ограничены low-level adapter слоем (`modules/input_processing/keyboard/*`).
- Новый параллельный путь управления режимами не добавлен.

## Verification
- `python3 -m py_compile modules/input_processing/keyboard/mac/quartz_monitor.py modules/input_processing/keyboard/keyboard_monitor.py config/unified_config_loader.py`
- Result: success.

## Expected runtime effect
- `Ctrl+N` продолжает работать как PTT.
- Комбинации с доп. модификаторами (например VoiceOver chords с Option/Command) не должны перехватываться Nexy.
- Снижается вероятность «странного» поведения клавиатуры при активном VoiceOver.
