# Task Brief: Remove mode-only preempt path

## Context
Нужно убрать ложные preempt/cancel при `AppMode.PROCESSING`, когда реальной активной работы уже нет.

## Diagnosis
В `InputProcessingIntegration` preempt принимался по `mode == PROCESSING` как самостоятельному признаку, что создавало лишние `interrupt.request` в idle-ситуациях.

## Architecture Fit
- Owner: `InputProcessingIntegration` (decision layer для preempt на входе)
- Source of truth: internal inflight markers (`_playback_active`, `_session_waiting_grpc`, `_active_grpc_session_id`)
- Второй путь принятия решений не добавлен.

## Implementation
Файл: `integration/integrations/input_processing_integration.py`

Сделано:
1. Добавлен метод `_preempt_decision(session_id)`:
- `playback_active` -> preempt
- `waiting_grpc` -> preempt
- `active_grpc_session` -> preempt
- иначе -> no preempt

2. Заменены mode-based проверки в:
- `_handle_press`
- `_handle_long_press`
- `_cancel_short_tap`

3. Добавлен debug reason лог (`PRESS_PREEMPT reason=...`, `SHORT_TAP interrupt reason=...`).

## Concurrency / Race Guard
Использован state-guard без новых флагов/состояний; решение детерминировано от существующих inflight-маркеров.

## Verification
- `python3 -m py_compile integration/integrations/input_processing_integration.py` — OK.
- Поиск подтвердил отсутствие mode-only ветки (`current_mode == AppMode.PROCESSING`) в preempt decision.

## Информация об изменениях
- Что изменено:
  - Удален mode-only trigger для preempt.
  - Прерывание теперь только по реальным признакам активной работы.
- Список файлов:
  - `integration/integrations/input_processing_integration.py`
- Причина/цель изменений:
  - Убрать ложные циклы interrupt/cancel и стабилизировать UX при быстрых нажатиях.
- Проверка:
  - Синтаксическая проверка `py_compile` выполнена.
