# Task Brief: press_id lifecycle guard for input events

## Goal
Устранить cross-press race: старый `RELEASE/LONG_PRESS` не должен влиять на новый цикл удержания.

## Changes
- `modules/input_processing/keyboard/mac/quartz_monitor.py`
  - Добавлен `self._combo_press_id`.
  - На активации combo генерируется новый `press_id`.
  - `PRESS`, `LONG_PRESS`, `RELEASE` для combo теперь несут `data.press_id`.

- `integration/integrations/input_processing_integration.py`
  - Добавлен `self._active_press_id`.
  - На `PRESS` захватывается активный `press_id`.
  - `LONG_PRESS`/`RELEASE` с чужим `press_id` игнорируются.
  - Для Quartz `ctrl_n` события без `press_id` игнорируются как некорректные.
  - `press_id` добавлен в публикации `keyboard.press` и `voice.recording_start`.

## Validation
- `python3 -m py_compile modules/input_processing/keyboard/mac/quartz_monitor.py integration/integrations/input_processing_integration.py` — успешно.

## Expected impact
- Запоздалый `RELEASE` старого цикла больше не сможет остановить новую запись.
- Снижение спонтанных переходов в `PROCESSING/SLEEPING` при удержании.
