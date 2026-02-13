# Hotkey Conflict Guard — Implementation Plan

## 1. Goal

Внедрить hotkey/focus/voiceover логику без конфликтов с системными shortcut:
- Nexy реагирует только на strict `Ctrl+N`;
- `Cmd+Space`/другие нецелевые комбинации не перехватываются;
- после `tray_ready` нет постоянного возврата фокуса;
- long press работает стабильно в фоне.

## 2. Scope

В рамках плана:
- `modules/input_processing/keyboard/mac/quartz_monitor.py`
- `integration/integrations/input_processing_integration.py`
- `integration/integrations/voiceover_ducking_integration.py`
- `main.py`
- `integration/core/simple_module_coordinator.py`
- `tests/test_quartz_monitor_chord_logic.py`

Вне scope:
- реархитектура mode/workflow;
- изменения бизнес-логики PTT вне suppression/focus/voiceover guard.

## 3. Baseline (must keep)

- `integrations.keyboard.key_to_monitor: ctrl_n`
- `integrations.keyboard.backend: auto` (или `quartz` для строгого режима)
- `integrations.input_processing.enable_keyboard_monitoring: true`
- `accessibility.voiceover_control.engage_on_keyboard_events: false`
- `accessibility.voiceover_control.hard_toggle_enabled: false`
- `focus.force_activate_on_startup: false`
- `focus.allow_tray_startup_fallback: true`

## 4. Phase Plan

### Phase 1 — Baseline Freeze
1. Зафиксировать и проверить runtime baseline-флаги.
2. Добавить pre-check список для smoke перед каждым запуском.

### Phase 2 — Focus Safety Hardening
1. Ограничить `activateIgnoringOtherApps` только startup/tray fallback window.
2. После `tray_ready` запретить автоматический фокусный takeover.
3. Добавить лог причины для каждой focus-активации (`reason`, `phase`, `allowed`).

### Phase 3 — Strict Suppression Enforcement
1. Подтвердить suppress только для strict `Ctrl+N`.
2. Ввести единый predicate-подход:
   - target predicate true -> suppress,
   - иначе -> pass-through.
3. Исключить side effects для любого non-target shortcut в hotkey path.

### Phase 4 — Dedup and Race Cleanup
1. Удалить duplicate subscribe на `system.permissions_ready` в VoiceOver integration.
2. Проверить idempotent-подписки и отсутствие второго decision-path.
3. Сохранить pending-release confirm и stale-modifier guards в Quartz path.

### Phase 5 — Observability
1. Нормализовать decision-логи suppression (`target_combo`, `blocked`, `suppressed`).
2. Нормализовать focus-логи (`startup_fallback`, `post_tray_ready`, `skipped`).
3. Добавить диагностику для спорных shortcut (`Cmd+Space`) без перехвата событий.

### Phase 6 — Verification Gate
1. Прогнать матрицу сценариев (см. раздел 7).
2. Подтвердить отсутствие regressions в PTT lifecycle.
3. Зафиксировать результаты в отчете `Docs/assistant_exchange/codex/`.

## 5. Implementation Rules

1. Single suppression owner: только Quartz combo path.
2. Single PTT owner: только InputProcessingIntegration.
3. No runtime focus hijack after `tray_ready`.
4. No keyboard-trigger VoiceOver ducking (по default).
5. No duplicate subscriptions for same event in one integration.

## 6. Risk Controls

### Duplication
- Риск: второй suppression path или повторная подписка.
- Контроль: code-review checklist + grep-проверка owner boundaries.

### Race
- Риск: `flagsChanged`/keyup out-of-order и ложный suppression.
- Контроль: event-flags guard + delayed confirm + stale-state reset.

### Focus Regression
- Риск: hidden forced activation после startup.
- Контроль: phase guard (`tray_ready`) + explicit logging + smoke checks.

## 7. Verification Matrix (DoD)

### Functional
1. `Ctrl+N` short/long/release работает стабильно.
2. любой non-target shortcut не перехватывается, системный маршрут сохраняется.

### Focus
1. До `tray_ready` fallback может сработать one-shot.
2. После `tray_ready` нет автоматического возврата фокуса.

### VoiceOver
1. VoiceOver ON/OFF не ломает pass-through для нецелевых shortcut.
2. Нет keyboard-press ducking side effects при default конфиге.

### Logs
1. `suppressed=true` только для strict `Ctrl+N`.
2. Для `Cmd+Space` фиксируется `suppressed=false`.
3. Нет post-startup focus-takeover log.

## 8. Rollback / Safe Degradation

Если выявлен критический конфликт:
1. Временно выключить `integrations.input_processing.enable_keyboard_monitoring`.
2. Оставить app без global hotkey до фикса.
3. Вернуть monitoring после прохождения verification gate.

## 9. Acceptance Criteria

План считается реализованным, если:
1. Nexy ловит `Ctrl+N` в фоне без foreground takeover.
2. Нецелевые shortcut полностью независимы от Nexy.
3. После `tray_ready` нет постоянного/повторного возврата фокуса.
4. Дубликаты подписок и вторые owner-path отсутствуют.
