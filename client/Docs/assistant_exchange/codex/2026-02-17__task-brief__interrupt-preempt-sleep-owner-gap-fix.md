# Task Brief: Interrupt preempt sleep owner gap fix

## Context
По логам после `keyboard.press_preempt` режим иногда оставался в `PROCESSING` и не возвращался в `SLEEPING`.

## Diagnosis
В `InterruptManagementIntegration` был special-case для preempt-источников, который пропускал `mode.request -> SLEEPING`.
Это создавало разрыв в едином owner-пути interrupt->mode и давало race-залипание.

## Architecture Fit
- Owner mode transition сохранен: `ModeManagementIntegration` через `mode.request`.
- Owner interrupt path: `InterruptManagementIntegration`.
- Второй путь принятия решений удален (локальный skip).

## Changes
- Удален локальный bypass `skip_sleep_mode_request` в `_handle_speech_stop`.
- Теперь `InterruptManagementIntegration` всегда публикует `mode.request` в `SLEEPING` при speech stop.
- Комментарий обновлен под single-owner правило.

## Concurrency / Race Guard
- Устранен out-of-order gap: preempt interrupt больше не зависит от внешнего follow-up события для возврата в sleep.
- Идемпотентность сохраняется в `ModeManagementIntegration` (dedup/ignored same-mode).

## Verification
- `python3 -m py_compile integration/integrations/interrupt_management_integration.py integration/workflows/processing_workflow.py integration/integrations/speech_playback_integration.py integration/integrations/input_processing_integration.py integration/integrations/welcome_message_integration.py` — OK.
- Проверен diff: ветка `skip mode.request SLEEPING for preempt` удалена.

## Информация об изменениях
- Что изменено:
  - Удален special-case, пропускавший `SLEEPING` при preempt interrupt.
  - Восстановлен единый централизованный путь interrupt->mode.
- Список файлов:
  - `integration/integrations/interrupt_management_integration.py`
- Причина/цель изменений:
  - Убрать залипание `PROCESSING` из-за condition gap и усилить single-owner централизацию режима.
- Проверка:
  - Выполнен `py_compile` целевых модулей; подтверждено удаление bypass-ветки.
