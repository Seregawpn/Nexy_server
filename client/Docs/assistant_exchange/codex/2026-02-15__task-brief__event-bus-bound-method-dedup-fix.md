# Task Brief: EventBus bound-method dedup fix

## Context
- В логах наблюдались повторные подписки, которые могли выглядеть как дубли.
- Централизованная дедупликация подписок находится в `integration/core/event_bus.py`.

## Problem
- В `subscribe()` дедуп проверял `sub["callback"] is callback`.
- Для bound-method (`self.method`) это ненадежно: повторные обращения создают разные method-объекты.

## Changes
- Добавлен стабильный ключ callback:
  - bound-method: `("bound_method", id(owner), func)`
  - прочие callable: `("callable", callback)`
- `subscribe()` теперь дедуплицирует по `callback_key`.
- `unsubscribe()` удаляет по тому же ключу (симметрично).
- Добавлено диагностическое имя callback в warning о дубле.

## Tests
- Добавлен файл `tests/test_event_bus_subscription_dedup.py`:
  1. Повторная подписка того же bound-method игнорируется.
  2. Разные инстансы с одним методом считаются разными подписчиками.
  3. `unsubscribe` корректно удаляет bound-method подписку.
- Прогон:
  - `PYTHONPATH=. pytest -q tests/test_event_bus_subscription_dedup.py` → `3 passed`
  - `PYTHONPATH=. pytest -q tests/test_mode_management_mode_request_dedup.py tests/test_voiceover_ducking_mode_guard.py tests/test_coordinator_critical_subscriptions.py` → `10 passed`

## Result
- Устранен системный источник ложных дублей на уровне EventBus.
- Логика осталась централизованной, без локальных флагов в интеграциях.
