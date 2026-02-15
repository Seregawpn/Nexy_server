# Hotkey Conflict Guard Requirements (Preliminary)

## 1. Purpose

Документ фиксирует предварительные требования к реализации hotkey/focus/voiceover логики, чтобы:
- Nexy перехватывал только целевую комбинацию;
- системные и сторонние shortcut не ломались;
- не возникали дубли логики и гонки состояний;
- сохранялась архитектурная централизация.

## 2. Architecture Fit (mandatory)

- Source of Truth (suppression policy):
  - `modules/input_processing/keyboard/mac/quartz_monitor.py`
- Source of Truth (PTT lifecycle):
  - `integration/integrations/input_processing_integration.py`
- Source of Truth (focus startup policy):
  - `main.py`
  - `integration/core/simple_module_coordinator.py`
- Source of Truth (VoiceOver control):
  - `integration/integrations/voiceover_ducking_integration.py`
  - `modules/voiceover_control/core/controller.py`

Запрещено добавлять второй owner suppression/decision логики в tray/UI/других интеграциях.

## 3. What We Can / Cannot

### 3.1 We can

1. Перехватывать только strict `Ctrl+N`.
2. Публиковать `keyboard.press`/PTT события только для целевого hotkey-пути.
3. Деградировать hotkey при Secure Input без влияния на системные shortcut.
4. Использовать startup-only focus fallback для поднятия tray.

### 3.2 We cannot

1. Перехватывать `Cmd+Space` и любые нецелевые комбинации.
2. Подавлять одиночные модификаторы (`Control`, `Command`, `Option`, `Shift`).
3. Делать runtime forced-focus takeover из hotkey-path.
4. Дублировать подписки/обработчики, которые создают второй путь принятия решения.

## 4. Hard Runtime Invariants (MUST)

1. `suppress=true` только при условии:
   - `Control` down
   - `N` key event
   - `Command/Option/Shift` not pressed
2. Для всех остальных комбинаций: `pass-through` без side effects.
   - Политика не основана на списке "разрешенных" комбинаций.
   - Используется inverse-rule: если событие не удовлетворяет strict target predicate, оно не перехватывается.
3. VoiceOver keyboard path isolation:
   - `accessibility.voiceover_control.engage_on_keyboard_events=false` (default).
4. Focus isolation:
   - `focus.force_activate_on_startup=false` (default),
   - `activateIgnoringOtherApps` разрешен только в startup/tray fallback path.
5. No persistent focus return:
   - после `tray_ready` запрещен любой автоматический возврат фокуса на Nexy/Finder,
   - Nexy не должен закрывать Spotlight/Alfred через фокусный side effect.
6. Single suppression owner:
   - только Quartz combo path.
7. Single subscription rule:
   - одна подписка на конкретное событие на интеграцию.
8. Focus-independent command capture:
   - обработка целевой команды (`Ctrl+N`) не должна требовать foreground-фокуса Nexy,
   - global hotkey работает в фоне без forced activation.

## 5. Config Baseline (required)

- `integrations.keyboard.key_to_monitor: ctrl_n`
- `integrations.keyboard.backend: auto|quartz`
- `integrations.input_processing.enable_keyboard_monitoring: true` (или controlled off как workaround)
- `accessibility.voiceover_control.engage_on_keyboard_events: false`
- `accessibility.voiceover_control.hard_toggle_enabled: false`
- `focus.force_activate_on_startup: false`
- `focus.allow_tray_startup_fallback: true`

Любые отклонения фиксируются как explicit override и проходят отдельную проверку регрессий.

## 6. Anti-Race Requirements

Race:
- scenario: `flagsChanged`/key edge приходят out-of-order или теряются при suppression/Secure Input.
- fix (architecture-compatible):
  - решения suppression принимаются по текущим `event flags`,
  - pending release подтверждается с delayed-check,
  - stale local modifier state не может активировать suppression.

Race:
- scenario: duplicate event subscriptions вызывают повторные side effects.
- fix (architecture-compatible):
  - idempotent subscribe policy,
  - единая точка регистрации подписок в интеграции.

## 7. Zero Duplication Rule

Если suppression/shortcut guard уже реализован в Quartz owner:
- не создавать второй guard в InputProcessing, tray, voiceover или UI.
- дубли удалять, owner оставлять один.

## 8. Verification Matrix (DoD)

1. Functional:
- target-combo (`Ctrl+N`) short/long/release работает стабильно.
- любой non-target shortcut проходит без вмешательства.

2. VoiceOver:
- VoiceOver ON/OFF не меняет pass-through для нецелевых shortcut.
- Нет keyboard-trigger ducking side effects при `engage_on_keyboard_events=false`.

3. Focus:
- Нет runtime фокус-перехвата на hotkey события.
- Startup fallback срабатывает только в пределах tray-startup window.
- После `tray_ready` отсутствует постоянный/повторный возврат фокуса, влияющий на Spotlight/Alfred.
- `Ctrl+N` срабатывает при фокусе в сторонних приложениях (без перевода фокуса на Nexy).

4. Logs:
- Decision logs показывают suppression только для strict `Ctrl+N`.
- Для `Cmd+Space` фиксируется `suppressed=false`.

## 9. Change Boundaries

Разрешены изменения:
- в owner-слоях (Quartz/InputProcessing/focus startup/voiceover init),
- в тестах и requirements-документации.

Запрещены изменения:
- с созданием новых state-owner для hotkey,
- с расширением suppression на любые комбинации кроме strict `Ctrl+N`,
- с обходом централизованного пути mode/PTT решений.
