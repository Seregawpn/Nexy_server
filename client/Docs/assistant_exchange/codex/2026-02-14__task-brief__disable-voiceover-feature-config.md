# Disable VoiceOver Feature via Config

## Change
Отключен VoiceOver функционал в каноническом конфиге:
- `config/unified_config.yaml`
- `accessibility.voiceover_control.enabled: false`

## Why
Пользователь запросил полностью отключить VoiceOver-функционал в приложении.

## Scope
- Только конфиг.
- Код hotkey/voiceover модулей не изменялся.

## Verification
- Проверено, что в `config/unified_config.yaml` установлено `enabled: false` в секции `accessibility.voiceover_control`.

## Runtime Note
- Требуется перезапуск Nexy, чтобы значение из `unified_config.yaml` применилось.
