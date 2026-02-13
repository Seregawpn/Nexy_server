# Task Brief — single-target predicate policy update

## Context
Пользователь потребовал убрать подход со списком комбинаций и закрепить принцип:
- активна только целевая комбинация,
- все остальное автоматически pass-through.

## Deliverable
Обновлены документы:
- `Docs/HOTKEY_CONFLICT_GUARD_REQUIREMENTS.md`
- `Docs/HOTKEY_CONFLICT_GUARD_IMPLEMENTATION_PLAN.md`

## Что изменено
1. Политика сформулирована как inverse-rule:
- если событие не удовлетворяет strict target predicate, оно не перехватывается.
2. Убрана зависимость policy от перечисления конкретных сторонних комбинаций.
3. Functional/DoD секции переписаны в терминах target vs non-target.

## Architecture fit
- Централизация не изменена.
- Single owner suppression path сохранен.
