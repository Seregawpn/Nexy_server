# Analysis: Quartz false Control release race during Ctrl+N hold

## Symptom from logs
- Периодически возникает `DEACTIVATION TRIGGERED` при `control_pressed=False, n_pressed=True`.
- Это происходит из `flagsChanged` path для Control, а не из `keyUp N`.
- После этого уходит `RELEASE` и стартует `PROCESSING`, затем при offline — `SLEEPING`.

## Root cause
- Даже после фикса `pending N release` оставался второй race-канал: ложный `flagsChanged Control up`.
- Текущая логика деактивировала combo сразу по одному такому событию.

## Fix applied
- В `modules/input_processing/keyboard/mac/quartz_monitor.py` добавлен симметричный guard:
  - `_pending_control_release_at`
  - `_control_release_confirm_delay_sec=0.09`
- Поведение:
  - При `flagsChanged Control up` во время `combo_active && n_pressed` деактивация не делается сразу, ставится pending.
  - Pending отменяется при следующем `Control down` или `keyDown N`.
  - В watchdog pending подтверждается через delay + проверку `CGEventSourceFlagsState`.
  - Только после подтверждения делается реальный `Control release` и `RELEASE` combo.

## Verification
- `python3 -m py_compile modules/input_processing/keyboard/mac/quartz_monitor.py` — успешно.

## Expected result
- Ложные `Control up` больше не должны обрывать удержание.
- Снизятся случайные ранние переходы в `PROCESSING/SLEEPING` и случаи «залипания» после ложной деактивации.
