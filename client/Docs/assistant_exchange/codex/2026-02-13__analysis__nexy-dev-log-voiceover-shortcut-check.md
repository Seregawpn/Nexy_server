# Analysis — nexy-dev.log voiceover/shortcut check

## Checked file
- `/Users/sergiyzasorin/Library/Logs/Nexy/nexy-dev.log`
- Last modified: `2026-02-12 20:17:59 -0500`

## Findings
1. В логе есть многочисленные записи suppression только по strict `Ctrl+N`:
- `combo suppress: reason=strict_ctrl_n ... blocked=False`
- `combo suppress: reason=debounce ...`
- `combo suppress: reason=n_keyup_confirm ...`

2. В тех же сессиях видно, что `keyboard.press` доставлялся в VoiceOver integration:
- `EventBus: dispatch 'keyboard.press' ... VoiceOverDuckingIntegration.handle_keyboard_press`

3. Явных следов `Cmd+Space`/`Spotlight`/`Alfred` в dev-логе нет (по текстовым маркерам).

4. По фокусу:
- в `nexy-dev.log` нет срабатываний `[FOCUS]`/`activateIgnoringOtherApps` из runtime-фазы;
- но это не доказывает отсутствие interception-мисрутинга shortcut.

## Interpretation
- Лог подтверждает, что проблемный период содержал keyboard-path к VoiceOver integration.
- Это ожидаемо для старых сессий до примененного фикса (safe default + opt-in subscribe).
- После текущих правок нужен новый runtime запуск и новый log segment для валидации.

## Next verification
1. Перезапустить Nexy с текущими изменениями.
2. Повторить сценарий VoiceOver + `Cmd+Space`.
3. Проверить в новом хвосте лога:
- отсутствие `dispatch 'keyboard.press' ... VoiceOverDuckingIntegration.handle_keyboard_press` (при default config),
- наличие suppression только для strict `Ctrl+N`.
