# Analysis — Ctrl/Command/VoiceOver shortcut block points

## Scope
- User issue: при активном окне Nexy ломаются сочетания с `Control`/`Command`, включая VoiceOver-чорды.
- Goal: pinpoint блокирующие точки без изменения архитектуры.

## Architecture fit
- Source of Truth input lifecycle: `integration/integrations/input_processing_integration.py`.
- Keyboard suppression owner: `modules/input_processing/keyboard/mac/quartz_monitor.py`.
- VoiceOver ducking owner: `integration/integrations/voiceover_ducking_integration.py` + `modules/voiceover_control/core/controller.py`.

## Key findings
1. Global interception действительно есть и может потреблять события:
   - `QuartzKeyboardMonitor` создаёт active tap (`kCGEventTapOptionDefault`) для combo hotkey режима.
   - File: `modules/input_processing/keyboard/mac/quartz_monitor.py` lines ~138-163.
   - Это единственная точка, где Nexy может реально "съесть" системный key event.

2. Текущее подавление ограничено в основном `Ctrl+N` веткой:
   - Подавление происходит только на `N keyDown/keyUp` при активной combo.
   - File: `modules/input_processing/keyboard/mac/quartz_monitor.py` lines ~354-391.
   - Комментарий и логика явно не блокируют `Control` отдельно (`return event` в flagsChanged).

3. Guard для конфликтов с доп. модификаторами уже внедрён:
   - Если зажат `Option`/`Command`, combo помечается blocked и не активируется.
   - File: `modules/input_processing/keyboard/mac/quartz_monitor.py` lines ~315, ~339-351, ~378-382.

4. Конфиг сейчас снижает риск VoiceOver-побочек:
   - `voiceover_control.engage_on_keyboard_events: false`.
   - File: `config/unified_config.yaml` line ~20.
   - Значит `keyboard.press` не запускает ducking-путь при каждом хоткее.

5. VoiceOver fallback потенциально может инжектить `Control`, но только при не-default режиме:
   - В `mode=stop` fallback-нажатие Control не используется.
   - File: `modules/voiceover_control/core/controller.py` lines ~357-360.
   - Текущий config: `mode: stop`, `hard_toggle_enabled: false`.

## Most probable remaining failure mechanism
- При активном global tap и edge-кейсах `flagsChanged` (пропуски/рассинхрон состояния модификаторов) `N` может быть кратковременно подавлен в неожиданный момент, что пользователь воспринимает как "сломанные сочетания".
- Это локализуется в `QuartzKeyboardMonitor._handle_combo_event`.

## Missing context
- В этой копии не найден файл `Docs/ASSISTANT_COORDINATION_PROTOCOL.md`.
- Также отсутствуют `Docs/CODEX_PROMPT.md` и `Docs/ANTIGRAVITY_PROMPT.md` (вероятно вынесены/переименованы).
