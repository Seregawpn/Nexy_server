# Analysis: pending N release must require real Control release

## Observation
- В логе `pending release N` подтверждался и вызывал `DEACTIVATION TRIGGERED` при `control_pressed=True`.
- Это приводило к преждевременному `RELEASE` во время удержания.

## Root cause
- Подтверждение `pending N` не проверяло реальный системный статус Control.
- Кратковременное отсутствие автоповтора N могло трактоваться как отпускание N, даже при удерживаемом Control.

## Fix
- `modules/input_processing/keyboard/mac/quartz_monitor.py`:
  - В блок подтверждения `pending N` добавлена проверка `CGEventSourceFlagsState`.
  - Если `actual_control_pressed=True`, `pending N` отменяется и combo не деактивируется.
  - Подтверждение `pending N` допускается только когда Control реально не зажат.

## Validation
- `python3 -m py_compile modules/input_processing/keyboard/mac/quartz_monitor.py` — успешно.

