# Task Brief: Quartz autorepeat -> single press owner

## Context
В Dev-логах при удержании `Ctrl+N` появлялись повторные `QUARTZ_DECISION ... SUPPRESS+EMIT (target_combo_activation)` и последующие каскадные `interrupt.request`/`playback.cancelled`, что выглядело как зависание процесса.

## Diagnosis
Дубли рождались в low-level адаптере (`QuartzKeyboardMonitor`): autorepeat `KeyDown` периодически снова активировал combo и повторно эмитил `PRESS`.

## Architecture Fit
- Owner: `QuartzKeyboardMonitor` (low-level edge detection)
- Source of truth: `_combo_active` lifecycle
- Централизация сохранена: business-решения остались в `InputProcessingIntegration`.

## Implementation
В `modules/input_processing/keyboard/mac/quartz_monitor.py` добавлен state-guard:
- если combo уже активен (`_combo_active=True`), повторный target `KeyDown` только suppress (`combo_active_hold`) без нового `PRESS`.

## Concurrency / Race Guard
Использован существующий lock `state_lock` + state-guard по `_combo_active`, исключая повторный запуск цикла на autorepeat.

## Verification
- `python3 -m py_compile modules/input_processing/keyboard/mac/quartz_monitor.py` — OK.
- Проверка кода: есть новая ветка `reason=combo_active_hold`.

## Информация об изменениях
- Что изменено:
  - Добавлен dedup для autorepeat `KeyDown` при активном combo (`Ctrl+N` hold).
  - Предотвращена повторная эмиссия `PRESS` во время удержания.
- Список файлов:
  - `modules/input_processing/keyboard/mac/quartz_monitor.py`
- Причина/цель изменений:
  - Убрать циклические preempt/cancel при удержании hotkey и стабилизировать pipeline ввода.
- Проверка:
  - Синтаксическая проверка `py_compile` выполнена успешно.
