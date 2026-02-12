# Task Brief: remove locked tray status (3-mode enforcement)

## Context
- Запрошено оставить только 3 режима tray: `SLEEPING`, `LISTENING`, `PROCESSING`.
- Отдельный режим блокировки (`LOCKED`) должен быть удален, чтобы не создавать конфликт с моделью режимов.

## Changes
1. Удален `LOCKED` из enum:
   - `modules/tray_controller/core/tray_types.py`
2. Удалены color/icon mappings для `LOCKED`:
   - `modules/tray_controller/core/tray_types.py`
3. Убрано runtime-переключение в `LOCKED` на `permissions.first_run_started`:
   - `integration/integrations/tray_controller_integration.py::_on_permissions_blocked`
   - Поведение заменено на sync c текущим app mode (без четвертого состояния).
4. Обновлены актуальные план/requirements документы:
   - `Docs/assistant_exchange/codex/2026-02-11__task-brief__first-run-restart-centralization-governance-plan.md`
   - `Docs/assistant_exchange/codex/2026-02-11__analysis__first-run-permissions-requirements-and-sequence.md`

## Validation
- Поиск `TrayStatus.LOCKED` в актуальном runtime-коде и новых docs: не найден.
- `py_compile` для измененных python-файлов: успешно.

## Result
- Tray модель централизована до 3 режимов без отдельного "blocked/locked" статуса.
- First-run события больше не добавляют новый режим и не конфликтуют с каноном `app.mode_changed`.

