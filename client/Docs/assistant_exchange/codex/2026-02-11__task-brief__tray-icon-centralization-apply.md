# Tray icon centralization apply

## Метаданные
- Ассистент: codex
- Тип: task-brief
- Дата: 2026-02-11
- ID (INS-###): N/A

## Diagnosis
В tray icon pipeline оставались дублирующие пути применения состояния и не было защиты от устаревших UI-апдейтов.

## Root Cause
Несколько writer-путей внутри tray слоя + out-of-order `callAfter` без sequence guard приводили к риску неверного конечного статуса.

## Optimal Fix
- Централизован compute/apply путь в `TrayControllerIntegration`.
- Добавлен stale-drop guard (`_ui_apply_seq`) для `AppHelper.callAfter`.
- `permissions.first_run_started` принудительно применяет `LOCKED`.
- `permissions.first_run_completed/failed` принудительно возвращают иконку в статус из текущего `app.mode`.
- Удалены дубли:
  - неиспользуемый `_update_tray_status`
  - legacy `_ui_tick` runtime writer path
- Исправлен payload `previous_status` в `TrayController.update_status`.
- Убран блокирующий `time.sleep` из `MacOSTrayMenu.update_icon`.

## Verification
- `python3 -m py_compile integration/integrations/tray_controller_integration.py modules/tray_controller/core/tray_controller.py modules/tray_controller/macos/menu_handler.py` → OK

## Pre-Change Gate Evidence (обязательно)
- Прочитанные документы:
  - `AGENTS.md`
  - `Docs/DOCS_INDEX.md`
  - `Docs/PRE_CHANGE_CHECKLIST.md`
  - `Docs/PROJECT_REQUIREMENTS.md`
  - `Docs/ARCHITECTURE_OVERVIEW.md`
  - `Docs/FLOW_INTERACTION_SPEC.md`
  - `Docs/STATE_CATALOG.md`
  - `Docs/FEATURE_FLAGS.md`
  - `../Docs/ASSISTANT_COORDINATION_PROTOCOL.md`
  - `../Docs/CODEX_PROMPT.md`
  - `../Docs/ANTIGRAVITY_PROMPT.md`
  - `../Docs/assistant_exchange/TEMPLATE.md`
- Source of Truth:
  - `TrayControllerIntegration` (runtime owner UI статуса трея)
  - `ApplicationStateManager` оси через selectors
- Дублирование:
  - Найдено и объединено в один путь: `_update_tray_status`, `_ui_tick`, прямые конкурирующие apply ветки
- Feature Flags check:
  - Новые флаги не добавлялись, существующий `NEXY_DISABLE_TRAY` не менялся
- Race check:
  - Scenario: out-of-order `permissions.first_run_*` vs `app.mode_changed` + queued `callAfter`
  - Guard: `ui_seq` stale-drop + centralized recompute/apply

## Запрос/цель
Проверить корректность tray icon поведения с точки зрения централизации/гонок и применить исправления.

## Контекст
- Файлы:
  - `integration/integrations/tray_controller_integration.py`
  - `modules/tray_controller/core/tray_controller.py`
  - `modules/tray_controller/macos/menu_handler.py`

## Решения/выводы
- Риск гонок и дублирования устранен в пределах текущей архитектуры без добавления новых feature flags и без реархитектуры.

## Открытые вопросы
- Нужен ли `start_ui_timer/stop_ui_timer` API как legacy-слой, если runtime применяет статус только через `callAfter`?

## Следующие шаги
- Добавить интеграционный regression-тест на порядок событий:
  - `permissions.first_run_started -> app.mode_changed -> permissions.first_run_completed`.
