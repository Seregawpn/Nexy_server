# Tray icon centralization race audit

## Метаданные
- Ассистент: codex
- Тип: analysis
- Дата: 2026-02-11
- ID (INS-###): N/A

## Diagnosis
Логика состояния иконки трея частично централизована в `TrayControllerIntegration`, но в коде остались параллельные пути применения UI и статуса, что создает риск гонок и «залипания» иконки.

## Root Cause
Архитектурно есть один owner (`TrayControllerIntegration`), но фактически присутствуют несколько путей применения состояния (`_apply_status_ui_sync`, `_ui_tick`, `TrayController.update_status`) и нет order-guard между событиями `permissions.first_run_*` и `app.mode_changed`, что приводит к недетерминированному итоговому состоянию.

## Optimal Fix
Цель: закрепить единственный путь вычисления и применения tray icon состояния, убрать дубли и добавить защиту от out-of-order UI-апдейтов.

Architecture Fit:
- Где живет: `integration/integrations/tray_controller_integration.py`
- Source of Truth: вычисление статуса иконки из централизованных осей (`app.mode` + `first_run_in_progress`) через селекторы.
- Архитектура не ломается: да (только consolidation внутри текущего owner).

План внедрения:
1. Вынести единый compute-метод в `TrayControllerIntegration`, например `_compute_tray_status()` с приоритетом:
   - `first_run_in_progress=true` -> `TrayStatus.LOCKED`
   - иначе `mode_to_status[current_mode]`
2. Любые события (`app.mode_changed`, `permissions.first_run_started/completed/failed`) только триггерят единый путь `recompute -> schedule_ui_apply`.
3. Добавить order-guard (`_ui_seq`), чтобы устаревший `AppHelper.callAfter` не мог перезаписать более новое состояние.
4. Удалить/заморозить дублирующий путь `_update_tray_status` (не используется) и legacy `_ui_tick` ветку.
5. В `TrayController.update_status` исправить payload `previous_status` (сейчас отправляется уже новое значение).
6. Проверить отсутствие новых флагов/стейтов: использовать существующие `StateKeys.FIRST_RUN_IN_PROGRESS` и `selectors.get_current_mode()`.

Code Touchpoints:
- `integration/integrations/tray_controller_integration.py`
- `modules/tray_controller/core/tray_controller.py`

Concurrency Guard (if needed):
- `state-guard` + monotonic sequence (`_ui_seq`) для отбрасывания stale UI-апдейтов.

What to remove / merge:
- Дублирующая функция `_update_tray_status` (merge into single recompute/apply path).
- Нерабочий/лишний путь `_ui_tick` (если таймер не используется в runtime).

## Verification
DoD:
1. Во время first-run иконка всегда `LOCKED`, независимо от промежуточных `mode_changed`.
2. После `permissions.first_run_completed|failed` иконка гарантированно возвращается в статус из текущего `app.mode` без ожидания следующего mode event.
3. При быстрых переходах `LISTENING -> PROCESSING -> SLEEPING` итоговая иконка всегда соответствует последнему состоянию.
4. В логах нет конкурирующих применений статуса из разных путей.

## Pre-Change Gate Evidence (обязательно)
- Прочитанные документы:
  - `AGENTS.md`
  - `Docs/DOCS_INDEX.md`
  - `Docs/PRE_CHANGE_CHECKLIST.md`
  - `Docs/PROJECT_REQUIREMENTS.md` (REQ-001, REQ-003, REQ-004, REQ-019, REQ-020, REQ-021)
  - `Docs/ARCHITECTURE_OVERVIEW.md` (tray_controller ownership, EventBus contracts)
  - `Docs/FLOW_INTERACTION_SPEC.md` (mode/event invariants)
  - `Docs/STATE_CATALOG.md` (axes ownership, firstRun/appMode source)
  - `Docs/FEATURE_FLAGS.md`
  - `../Docs/ASSISTANT_COORDINATION_PROTOCOL.md`
  - `../Docs/ANTIGRAVITY_PROMPT.md`
  - `../Docs/CODEX_PROMPT.md`
  - `../Docs/assistant_exchange/TEMPLATE.md`
- Source of Truth:
  - UI owner: `TrayControllerIntegration`
  - State owner: `ApplicationStateManager` axes via selectors
- Дублирование:
  - Найдено: `_apply_status_ui_sync` + `_ui_tick` + `TrayController.update_status` + unused `_update_tray_status`
  - План: merge to single recompute/apply path in `TrayControllerIntegration`
- Feature Flags check:
  - Используется существующий `NEXY_DISABLE_TRAY`; новые флаги не требуются
- Race check:
  - Сценарий: out-of-order `permissions.first_run_*` и `app.mode_changed` + queued `callAfter`
  - Guard: sequence-based stale drop + centralized recompute

## Запрос/цель
Проверить, корректна ли текущая реализация отображения иконки в меню, найти конфликтные/гонкоопасные места и определить правильный способ внесения изменений.

## Контекст
- Файлы:
  - `integration/integrations/tray_controller_integration.py`
  - `modules/tray_controller/core/tray_controller.py`
  - `modules/tray_controller/macos/menu_handler.py`
  - `integration/core/event_bus.py`
  - `integration/core/selectors.py`
  - `integration/core/state_manager.py`
- Документы:
  - `Docs/PROJECT_REQUIREMENTS.md`
  - `Docs/ARCHITECTURE_OVERVIEW.md`
  - `Docs/FLOW_INTERACTION_SPEC.md`
  - `Docs/STATE_CATALOG.md`
  - `Docs/FEATURE_FLAGS.md`
- Ограничения:
  - Без реархитектуры; только в рамках существующего owner и слоев.

## Решения/выводы
- Частично корректно: owner задан правильно, но реализация не полностью centralized из-за дублирующих путей обновления и отсутствия order-guard.
- Основной риск: несогласованность icon state при близких по времени событиях.
- Рекомендуемый путь: consolidation в `TrayControllerIntegration` + sequence guard.

## Открытые вопросы
- Нужен ли runtime `_ui_tick` вообще, если фактическое применение идет через `AppHelper.callAfter`?
- Нужен ли публичный `TrayController.update_status` в runtime path или оставить только для тестов/demo?

## Следующие шаги
- Внести consolidation-фикс в 2 файла (`tray_controller_integration.py`, `tray_controller.py`) и добавить regression-тест на порядок событий `permissions.first_run_*` vs `app.mode_changed`.
