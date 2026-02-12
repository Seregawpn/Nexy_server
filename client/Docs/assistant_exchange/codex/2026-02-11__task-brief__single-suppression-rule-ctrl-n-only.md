# Task Brief — Single suppression rule (Ctrl+N only)

## Context
Пользователь уточнил обязательное ограничение: подавление допустимо только для одной текущей комбинации `Ctrl+N`. Никакие другие клавиши/комбинации блокироваться не должны.

## Change
Обновлён документ требований:
- `Docs/HOTKEY_COMBINATION_REQUIREMENTS.md`

Добавлено:
- `REQ-HK-000 Single Suppression Rule` (абсолютное правило одного suppression path).
- Прямой запрет в Hard NO на любой новый suppression path кроме `Ctrl+N`.

## Result
Требования теперь однозначно фиксируют: в системе разрешено только одно подавление — `Ctrl+N`; остальное всегда pass-through.
