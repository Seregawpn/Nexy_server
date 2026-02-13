# Analysis — VoiceOver + Cmd+Space Spotlight conflict

## Context
Пользователь сообщает: при установленном Nexy и активном VoiceOver нажатие Cmd+Space (Spotlight/Alfred) открывает launcher на секунду и затем окно пропадает, фокус возвращается в Finder. После удаления Nexy проблема исчезает.

## Diagnosis
Вероятный источник — keyboard interception path в старом релизе (до strict Ctrl+N policy), который перехватывает/подавляет нецелевые комбинации (включая Cmd+Space) или вызывает фокусный побочный эффект.

## Architecture fit
- Source of Truth hotkey suppression: `modules/input_processing/keyboard/mac/quartz_monitor.py`
- Source of Truth PTT lifecycle: `integration/integrations/input_processing_integration.py`
- VoiceOver path должен быть изолирован от keyboard press path (`accessibility.voiceover_control.engage_on_keyboard_events=false`)

## Evidence from current tree
- В текущем конфиге уже зафиксировано безопасное значение:
  - `config/unified_config.yaml`: `accessibility.voiceover_control.engage_on_keyboard_events: false`
  - `config/unified_config.yaml`: `focus.force_activate_on_startup: false`
  - `integrations.keyboard.key_to_monitor: ctrl_n`
- Требования Do-No-Harm документированы:
  - `Docs/HOTKEY_COMBINATION_REQUIREMENTS.md` (strict `Ctrl+N`, pass-through для других сочетаний, Focus/VoiceOver isolation).

## Primary fix
1. Не использовать legacy hotkey suppression path из ранних релизов (space/нестрогий перехват).
2. Оставить единственный suppression-owner: Quartz strict `Ctrl+N` policy.
3. Гарантировать pass-through для любых комбинаций с `Command/Option/Shift`.
4. Не активировать NSApp в runtime hotkey-пути (только startup/tray-gate по условиям).

## Quick verification (5–15 min)
1. Запустить сборку с текущим hotkey policy.
2. Включить VoiceOver.
3. Проверить `Cmd+Space` и `Cmd+Shift+A` в фокусе Finder и в фоне Nexy.
4. В логах не должно быть suppression для нецелевых комбинаций; Spotlight/Alfred не должен закрываться сам.

## User-facing conclusion
Проблема вероятнее всего на стороне Nexy (legacy keyboard interception/focus side-effect), а не в системных permissions.
