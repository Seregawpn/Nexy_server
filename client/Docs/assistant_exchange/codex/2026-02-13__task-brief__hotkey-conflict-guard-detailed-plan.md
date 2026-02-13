# Task Brief — hotkey conflict guard detailed plan

## Context
Пользователь запросил детальный план реализации для модели:
- перехват только target combo,
- все non-target shortcuts pass-through,
- без конфликтов VoiceOver/focus.

## Deliverable
Создан документ:
- `Docs/HOTKEY_CONFLICT_GUARD_DETAILED_PLAN.md`

## Что зафиксировано
- Цель и архитектурные границы (owners).
- Жесткий target predicate contract.
- Детальные фазы реализации (0-6) с exit criteria.
- Тест-стратегия (авто + manual + log checks).
- Risk register и rollout/rollback.
- Definition of Done.

## Architecture fit
- Централизация сохранена.
- Новые owner-path не добавляются.
