# Analysis: Control Release Confirm Gating

## Observation
- Ложные `DEACTIVATION TRIGGERED` продолжались из-за подтверждения `pending release Control` без признака release по `N`.
- В логах это выглядело как: `pending release Control` -> `confirmed` -> `DEACTIVATION`, при этом combo фактически еще удерживалась.

## Root Cause
- `Quartz` разрешал подтверждение `Control`-release автономно, без связки с `pending release N`.
- Дополнительно в `flagsChanged` при `Control up` сбрасывался `_pending_n_release_at`, что ломало корреляцию двух клавиш.

## Fix Applied
- В `quartz_monitor.py`:
  - убран ранний сброс `_pending_n_release_at` на `Control up`;
  - подтверждение `pending release Control` теперь допускается только если уже есть `_pending_n_release_at`.

## Expected Effect
- `Control` больше не подтверждается в одиночку и не роняет combo при шуме.
- Деактивация происходит по согласованному release обеих клавиш (или fallback timeout).
