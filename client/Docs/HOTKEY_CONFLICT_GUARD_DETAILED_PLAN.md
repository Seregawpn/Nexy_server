# Hotkey Conflict Guard — Detailed Implementation Plan

## 1. Objective

Реализовать строгую модель перехвата:
- перехват только target combo (`Ctrl+N`);
- любой non-target input всегда pass-through;
- отсутствие runtime focus takeover;
- отсутствие дублирования/гонок в keyboard/voiceover path.

## 2. Architecture Boundaries

### 2.1 Owners (must keep)
- Suppression policy owner:
  - `modules/input_processing/keyboard/mac/quartz_monitor.py`
- PTT lifecycle owner:
  - `integration/integrations/input_processing_integration.py`
- Focus startup owner:
  - `main.py`
  - `integration/core/simple_module_coordinator.py`
- VoiceOver owner:
  - `integration/integrations/voiceover_ducking_integration.py`
  - `modules/voiceover_control/core/controller.py`

### 2.2 Hard constraints
- No second suppression owner.
- No allowlist/denylist policy for non-target shortcuts.
- No runtime forced focus after `tray_ready`.
- No duplicate event subscriptions in one integration.

## 3. Target Predicate Contract

`is_target_combo == true` только когда:
1. `Control` зажат.
2. Текущий key event = `N`.
3. `Command`, `Option`, `Shift` не зажаты.
4. Состояние подтверждено актуальными event flags (не stale локальным состоянием).

Decision contract:
- `is_target_combo=true` -> interception/suppression разрешен.
- `is_target_combo=false` -> обязательный pass-through без side effects.

## 4. Detailed Phases

### Phase 0 — Prep and Baseline Lock
1. Зафиксировать baseline config (документально):
   - `key_to_monitor=ctrl_n`
   - `backend=auto|quartz`
   - `enable_keyboard_monitoring=true`
   - `engage_on_keyboard_events=false`
   - `hard_toggle_enabled=false`
   - `force_activate_on_startup=false`
2. Зафиксировать контрольный тест-набор и smoke-сценарии.
3. Создать рабочий changelog-файл по фазам.

Exit criteria:
- baseline подтвержден и не меняется в ходе реализации.

### Phase 1 — Suppression Core Refactor (Quartz Owner)
1. В `quartz_monitor.py` выделить единый helper `is_target_combo(...)`.
2. Привязать suppression-решения только к этому helper.
3. Сделать early pass-through для всех non-target событий.
4. Сохранить текущие anti-race guards:
   - pending release confirm,
   - stale-modifier heal,
   - debounce без расширения зоны suppress.

Exit criteria:
- В коде нет второго пути decision для suppression.

### Phase 2 — Event Flow Hardening (Input Owner)
1. Проверить, что `keyboard.press` публикуется только для target combo cycle.
2. Убедиться, что non-target события не инициируют PTT lifecycle.
3. Сверить, что mode/request side effects не происходят для non-target input.

Exit criteria:
- PTT стартует только от target combo.

### Phase 3 — Focus Policy Hardening
1. Проверить `main.py`: forced activation только startup control path.
2. Проверить `simple_module_coordinator.py`: one-shot fallback до `tray_ready`.
3. Добавить явный guard:
   - если `tray_ready=true`, forced focus path недоступен.

Exit criteria:
- Нет runtime focus takeover после startup phase.

### Phase 4 — VoiceOver Isolation and Dedup
1. Подтвердить safe defaults:
   - `engage_on_keyboard_events=false`
   - `hard_toggle_enabled=false`
2. Подтвердить отсутствие duplicate subscriptions (`system.permissions_ready` и др.).
3. Подписка `keyboard.press` только explicit opt-in + idempotent guard.

Exit criteria:
- VoiceOver path изолирован от generic keyboard path по default.

### Phase 5 — Observability
1. Добавить каноничный decision-log в suppression owner:
   - `target_combo=<bool>`
   - `intercepted=<bool>`
   - `reason=<...>`
2. Добавить каноничный focus-log:
   - `phase=<startup|runtime>`
   - `forced_activation=<bool>`
   - `allowed=<bool>`
3. Убрать noisy дубли, мешающие диагностике.

Exit criteria:
- По логам за 1 проход понятно, кто и почему перехватил событие.

### Phase 6 — Tests and Regression Gates
1. Unit tests:
   - strict target interception.
   - non-target pass-through (property-based стиль по группам модификаторов).
2. Integration tests:
   - нет side effects для non-target input.
   - нет duplicate subscription effects.
3. Manual smoke:
   - VoiceOver ON/OFF
   - `Ctrl+N` short/long/release
   - произвольные non-target shortcuts
4. Log validation:
   - `intercepted=true` только при `target_combo=true`.

Exit criteria:
- все тесты green, smoke подтвержден.

## 5. Test Strategy (explicit)

### 5.1 Automated
- `tests/test_quartz_monitor_chord_logic.py`
- новые/обновленные тесты target/non-target contract.
- подписки coordinator/integration (dedup regressions).

### 5.2 Manual
1. Запустить Nexy.
2. Проверить target combo в фоне.
3. Проверить произвольные non-target shortcuts (без привязки к списку).
4. Повторить с VoiceOver ON.

### 5.3 Log checks
- suppression logs только для target combo.
- отсутствие runtime focus takeover.
- отсутствие keyboard-path side effects в VoiceOver default mode.

## 6. Risk Register

1. Race in modifier flags:
- mitigation: event-flag truth + delayed confirm.
2. Hidden second owner:
- mitigation: grep/review checklist по suppression entry points.
3. Focus regression:
- mitigation: startup phase guard + explicit log gate.
4. Diagnostic blind spots:
- mitigation: canonical logs and time-window correlation.

## 7. Rollout Plan

1. Implement phases 1-2.
2. Run automated tests.
3. Implement phases 3-5.
4. Run automated + manual smoke.
5. Freeze and document results.

Rollback:
- temporary `enable_keyboard_monitoring=false` if critical regression detected.

## 8. Acceptance (Definition of Done)

1. Target combo работает стабильно.
2. Любой non-target shortcut не перехватывается.
3. После `tray_ready` нет forced focus takeover.
4. VoiceOver default path не вмешивается в keyboard routing.
5. Логи однозначно подтверждают decision contract.
