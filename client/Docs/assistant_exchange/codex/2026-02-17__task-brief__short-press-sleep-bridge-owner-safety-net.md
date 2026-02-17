# Task Brief: Short-press sleep bridge owner safety-net

## Context
После preempt/cancel сценариев по логам оставался риск зависания в `PROCESSING` при отсутствии явного `mode.request -> SLEEPING`.

## Diagnosis
`keyboard.short_press` не был подписан в `ModeManagementIntegration` (bridge выключен), из-за чего в части idle/preempt веток событие cancel проходило без owner-перехода режима.

## Architecture Fit
- Source of Truth режима: `ModeManagementIntegration -> ModeController -> ApplicationStateManager`.
- Bridge публикует только `mode.request`, не меняет режим напрямую.
- Второй путь принятия решений не добавлен.

## Changes
- Включена подписка только на `keyboard.short_press` bridge:
  - `await self.event_bus.subscribe("keyboard.short_press", self._bridge_keyboard_short, EventPriority.MEDIUM)`
- `keyboard.long_press` и `keyboard.release` bridge оставлены отключенными, чтобы не вернуть дубли mode.request.

## Concurrency / Race Guard
- Добавлен safety-net owner-path для out-of-order сценария: short_press теперь гарантированно создает `mode.request` через централизованный owner.
- Дубликаты безопасны за счет existing dedup/idempotency в `_on_mode_request`.

## Verification
- `python3 -m py_compile integration/integrations/mode_management_integration.py integration/integrations/interrupt_management_integration.py integration/integrations/input_processing_integration.py` — OK.
- Проверка grep: подписка `keyboard.short_press -> _bridge_keyboard_short` присутствует.

## Информация об изменениях
- Что изменено:
  - Добавлен централизованный safety-net bridge для `keyboard.short_press` в owner-слое режима.
- Список файлов:
  - `integration/integrations/mode_management_integration.py`
- Причина/цель изменений:
  - Убрать остаточный gap возврата в sleep и снизить вероятность залипания `PROCESSING`.
- Проверка:
  - Выполнен `py_compile`; подтверждена активная подписка bridge.
