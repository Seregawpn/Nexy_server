# Hotkey Combination Requirements (Ctrl+N)

## 1. Scope

Документ фиксирует обязательные требования к поведению hotkey `Ctrl+N` в клиенте Nexy, чтобы:
- комбинация работала стабильно;
- не ломались системные/пользовательские shortcut-комбинации;
- не было побочных beep/click эффектов;
- сохранялась архитектурная централизация.

## 2. Architecture Ownership

- Source of Truth (PTT lifecycle): `integration/integrations/input_processing_integration.py`
- Source of Truth (keyboard interception policy): `modules/input_processing/keyboard/mac/quartz_monitor.py`
- Fallback parity owner: `modules/input_processing/keyboard/keyboard_monitor.py`
- Запрещено добавлять второй owner hotkey-логики в UI/tray/других интеграциях.

## 3. Functional Requirements (MUST)

### REQ-HK-000 Single Suppression Rule
- В системе допускается только один suppression path: текущая комбинация `Ctrl+N`.
- Любые другие комбинации/клавиши/модификаторы не подавляются, не блокируются и не переназначаются.
- Это правило является абсолютным и имеет приоритет над локальными оптимизациями.

### REQ-HK-001 Strict Chord
- Перехват и подавление разрешены только для строгого `Ctrl+N`.
- Если присутствует любой дополнительный модификатор (`Command`, `Option/Alt`, `Shift`) — событие НЕ перехватывается и проходит в систему.

### REQ-HK-002 Do-No-Harm Suppression
- Нельзя подавлять одиночные модификаторы (`Control`, `Command`, `Option`, `Shift`).
- Подавление разрешено только на `N` внутри валидной активной `Ctrl+N` комбинации.

### REQ-HK-003 System Shortcut Safety
- Любые нецелевые комбинации (`Ctrl+Cmd+N`, `Ctrl+Opt+N`, `Ctrl+Shift+N`, VoiceOver chords и другие системные shortcuts) должны работать как без Nexy.

### REQ-HK-004 Focus Safety
- Приложение не должно форсированно захватывать foreground-фокус в рантайме hotkey-обработки.
- `focus.force_activate_on_startup` по умолчанию должен быть `false`.

### REQ-HK-005 VoiceOver Isolation
- VoiceOver ducking не должен вмешиваться в любой keyboard press path для hotkey-обработки.
- `voiceover_control.engage_on_keyboard_events` по умолчанию должен быть `false`.

### REQ-HK-006 Secure Input Degradation
- При Secure Input hotkey может быть недоступен, но приложение не должно ломать чужие комбинации и не должно залипать в активном состоянии.

## 4. Non-Functional Requirements (MUST)

### REQ-HK-007 Latency
- Детекция `Ctrl+N` должна быть без заметной задержки для пользователя (целевая реакция в пределах текущих порогов клавиатурного конфига).

### REQ-HK-008 Stability
- Не допускаются race-состояния, где stale flags локального состояния приводят к ложному suppression нецелевых событий.

### REQ-HK-009 Backward Compatibility
- Поведение PTT lifecycle (`PRESS -> LONG_PRESS -> RELEASE`) не должно изменяться вне hotkey suppression policy.

## 5. Configuration Contract

Базовые параметры для стабильного поведения:
- `integrations.keyboard.key_to_monitor: ctrl_n`
- `integrations.keyboard.short_press_threshold: 0.08..0.12`
- `integrations.keyboard.long_press_threshold: 0.5..0.7`
- `integrations.keyboard.event_cooldown: 0.08..0.12`
- `integrations.keyboard.hold_check_interval: 0.03..0.06`
- `accessibility.voiceover_control.engage_on_keyboard_events: false`
- `focus.force_activate_on_startup: false`

Примечание: диапазоны выше — эксплуатационные границы для тюнинга без изменения контракта безопасности комбинаций.

## 6. Runtime Backend & Libraries Contract

### REQ-HK-010 Allowed Libraries
- Для production interception на macOS используется `PyObjC Quartz` (`CGEventTap*`, `CGEventGetFlags`).
- `pynput` допускается только как fallback-детектор (без suppression-owner роли).

### REQ-HK-011 Backend Selection
- Поддерживаемые backend значения: `auto`, `quartz`, `pynput`.
- `quartz`: использовать только Quartz; при недоступности Quartz не переключаться молча на другой suppression path.
- `auto`: Quartz как primary, fallback на `pynput` только для детекции событий.
- `pynput`: явный opt-in fallback режим.

### REQ-HK-012 Single Suppression Owner
- Единственный suppression-owner для `Ctrl+N` — Quartz combo path.
- В fallback режиме (`pynput`) suppression-policy не расширяется и не дублируется.

## 7. Prohibited Changes (Hard NO)

- Любой новый suppression path кроме `Ctrl+N`.
- Добавление альтернативных hotkey-путей вне input owner слоя.
- Локальные обходы в tray/UI для consume shortcuts.
- Suppression на основе неактуального локального состояния модификаторов без подтверждения текущими event flags.
- Любые изменения, где нецелевые shortcut-комбинации начинают зависеть от состояния Nexy.

## 8. Acceptance Criteria (DoD)

Система считается корректной только если выполняются все пункты:

1. `Ctrl+N` стабильно активирует PTT.
2. `Ctrl+Cmd+N`, `Ctrl+Opt+N`, `Ctrl+Shift+N` не перехватываются Nexy.
3. VoiceOver/system shortcuts работают без деградации при активном Nexy.
4. Нет beep/click артефактов на целевой комбинации в штатном режиме.
5. При Secure Input отсутствуют залипания состояния и побочные блокировки других комбинаций.
6. Логика централизована: один owner suppression policy + один owner PTT lifecycle.

## 9. Verification Matrix

Минимальный набор проверок:

1. Manual hotkey scenarios:
- `Ctrl+N` (short/long/release)
- `Ctrl+Cmd+N`
- `Ctrl+Opt+N`
- `Ctrl+Shift+N`
- активные VoiceOver chords

2. Runtime logs:
- проверка причин suppression только для strict `Ctrl+N`
- отсутствие suppression причин для нецелевых комбинаций

3. Regression:
- отсутствие изменений в mode/workflow ownership
- отсутствие второго пути принятия решения по hotkey
