# Task Brief: Quartz non-target release confirm guard

## Context
В dev-логах во время удержания `Ctrl+N` периодически появлялся `combo release (non_target_interruption)`, после чего запись обрывалась и дальше приходил `unknown_value`.

## Diagnosis
Сброс происходил в low-level owner (`QuartzKeyboardMonitor`): при `KeyDown` для `N` с не-таргет флагами combo деактивировался сразу, без confirm-delay.

## Architecture Fit
- Owner: `QuartzKeyboardMonitor` (low-level edge detection)
- Source of truth: lifecycle `_combo_active` + pending release (`_schedule_pending_release_locked`)
- Централизация сохранена: lifecycle-решения выше по стеку не дублировались.

## Implementation
В `modules/input_processing/keyboard/mac/quartz_monitor.py` изменена ветка `KeyDown + not is_target`:
- удалён мгновенный `_deactivate_combo_locked(... non_target_interruption)`;
- при активном combo используется `pending release` (`reason=non_target_keydown_confirmed`) и suppress события;
- фактический release остаётся только через подтверждённый путь (`control_up_confirmed`/`n_keyup_confirmed` + finalize).

## Concurrency / Race Guard
Использован существующий `state_lock` и единый confirm-механизм pending release, что убирает race между transient flags и hard-release.

## Verification
- `python3 -m py_compile modules/input_processing/keyboard/mac/quartz_monitor.py` — OK.
- Проверка diff: отсутствует мгновенный release по `non_target_interruption`, добавлен `non_target_combo_pending_release`.

## Информация об изменениях
- Что изменено:
  - Убрана мгновенная деактивация combo при `KeyDown` с не-таргет флагами во время удержания.
  - Включён confirm-path release через pending-release.
- Список файлов:
  - `modules/input_processing/keyboard/mac/quartz_monitor.py`
  - `Docs/assistant_exchange/codex/2026-02-17__task-brief__quartz-nontarget-release-confirm-guard.md`
- Причина/цель изменений:
  - Устранить ложные обрывы удержания PTT и каскадный `recognition_failed` при активном удержании.
- Проверка:
  - Синтаксис файла проверен (`py_compile`), diff проверен вручную.
