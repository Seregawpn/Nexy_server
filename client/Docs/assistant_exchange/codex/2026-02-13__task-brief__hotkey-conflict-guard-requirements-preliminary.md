# Task Brief — hotkey conflict guard requirements (preliminary)

## Context
Пользователь попросил подготовить предварительный документ требований к реализации, чтобы hotkey/focus/voiceover логика не перехватывала нецелевые комбинации, не создавала конфликтов, гонок и дублирования.

## Deliverable
Создан документ:
- `Docs/HOTKEY_CONFLICT_GUARD_REQUIREMENTS.md`

## Что зафиксировано
- Architecture fit и Source of Truth по suppression/PTT/focus/voiceover.
- Явные границы "что можно / что нельзя".
- Hard runtime invariants для strict `Ctrl+N` и pass-through остальных shortcuts.
- Добавлен отдельный запрет на постоянный возврат фокуса после `tray_ready`.
- Config baseline для безопасного поведения.
- Anti-race и zero-duplication требования.
- Verification matrix (DoD) для ручной и логовой проверки.

## Architecture fit
- Решение не меняет архитектуру.
- Централизация сохранена: owner suppression в Quartz path, owner PTT в InputProcessing.
