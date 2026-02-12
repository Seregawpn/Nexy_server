# Task Brief — hotkey combination requirements spec

## Context
Пользователь попросил сформировать формальный документ требований по комбинации `Ctrl+N`: стабильная работа PTT без ломки любых сторонних сочетаний клавиш и без побочных фокус/аудио эффектов.

## Deliverable
Создан документ:
- `Docs/HOTKEY_COMBINATION_REQUIREMENTS.md`

## Что зафиксировано
- Ownership и Source of Truth по hotkey/PTT.
- MUST-требования к strict chord policy (`Ctrl+N` only).
- Запрет на вмешательство в нецелевые комбинации.
- Требования по фокусу и VoiceOver isolation.
- Non-functional ограничения (latency/stability/race safety).
- Configuration contract и границы тюнинга.
- Hard NO изменения.
- Acceptance Criteria и verification matrix.

## Architecture fit
- Без изменения архитектуры.
- Централизация сохранена: input keyboard owner + input lifecycle owner.
