# Task Brief — hotkey conflict guard implementation plan

## Context
Пользователь попросил оформить отдельный документ по реализации согласованного плана: как исключить конфликты hotkey/focus/voiceover, не нарушая текущую архитектуру.

## Deliverable
Создан документ:
- `Docs/HOTKEY_CONFLICT_GUARD_IMPLEMENTATION_PLAN.md`

## Что зафиксировано
- Цели и scope реализации.
- Baseline-флаги, которые должны оставаться стабильными.
- Фазный план внедрения (focus safety, strict suppression, dedup/race cleanup, observability, verification gate).
- Риски и меры контроля.
- Verification matrix и acceptance criteria.
- Временная стратегия safe degradation (rollback).

## Architecture fit
- Централизация сохранена:
  - suppression owner: Quartz monitor,
  - PTT owner: InputProcessingIntegration,
  - focus owner: startup/tray path.
