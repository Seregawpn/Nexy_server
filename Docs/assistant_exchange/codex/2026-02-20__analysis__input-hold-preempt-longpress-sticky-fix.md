# Input Hold Preempt Longpress Sticky Fix

## Метаданные
- Ассистент: codex
- Тип: analysis
- Дата: 2026-02-20
- ID (INS-###): N/A

## Diagnosis
При удержании `Ctrl+N` во время активного playback происходил preempt/cancel, но иногда терялся `LONG_PRESS` callback и запись не стартовала до полного отпускания клавиш (ощущение "залипания").

## Root Cause
В owner-path `InputProcessingIntegration` состояние переводилось в `ARMED`, но при редком пропуске quartz long-press события не было fallback-механизма для старта записи при физически удерживаемой комбинации.

## Optimal Fix
В `InputProcessingIntegration` добавлен quartz long-press watchdog (в том же SoT):
1. При `PTTState.ARMED` и физически активной combo (`combo_active && control_pressed && n_pressed`) проверять elapsed от входа в ARMED.
2. Если elapsed > `long_press_threshold + margin`, синтетически вызвать `LONG_PRESS` через существующий `_handle_long_press`.
3. Гарантировать idempotency на `press_id` (watchdog fired один раз на цикл).

## Verification
- `python3 -m py_compile client/integration/integrations/input_processing_integration.py` — ok
- `pytest -q tests/test_interrupt_management_preempt_mode_skip.py tests/test_mode_management_mode_request_dedup.py` — all passed

## Информация об изменениях
- Что изменено:
  - добавлен fallback watchdog для потерянного long-press при удержании combo;
  - добавлены поля `armed_since_ts` и dedup marker watchdog по `press_id`;
  - вызов watchdog встроен в существующий quartz health-check loop.
- Файлы:
  - `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/integration/integrations/input_processing_integration.py`
- Причина/цель:
  - убрать "залипание" при hold-to-talk после preempt/cancel playback.
- Проверка:
  - py_compile + targeted pytest.

## Запрос/цель
Устранить залипание при зажатой комбинации во время прерывания речи.

## Контекст
- Файлы:
  - `client/integration/integrations/input_processing_integration.py`
  - `client/modules/input_processing/keyboard/mac/quartz_monitor.py`
- Ограничения:
  - без новых owner-path, только внутри existing SoT input lifecycle.

## Решения/выводы
- Проблема не в playback finalize, а в input lifecycle при редком пропуске `LONG_PRESS`.
- Watchdog внутри existing owner-path закрывает race без дублирования state-owner.

## Открытые вопросы
- Нужна ли телеметрия count для watchdog fire rate (чтобы понять частоту проблемы на проде).

## Следующие шаги
- Прогон руками: удержание `Ctrl+N` во время playback, проверить start recording без обязательного отпускания.
