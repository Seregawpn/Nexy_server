# Quartz Stale Timeout Reconcile

## Метаданные
- Ассистент: codex
- Тип: task-brief
- Дата: 2026-02-11
- ID (INS-###): N/A

## Diagnosis
- Пользовательский сценарий (Safari/YouTube/VO/Spotlight) указывает на stale keyboard state, который иногда снимается только после `Cmd+Tab`.
- В активном Quartz monitor не использовались `combo_timeout_sec` и `key_state_timeout_sec` для auto-heal.

## Root Cause
- Потерянные `flagsChanged/keyup` могли оставлять залипшие `combo_active/control_pressed/n_pressed` или `key_pressed`.
- Без timeout reconcile это состояние не восстанавливалось автоматически.

## Optimal Fix
- Добавлен централизованный `QuartzKeyboardMonitor._reconcile_stale_state_locked(now)`:
  - combo timeout -> `combo_timeout`;
  - single-key timeout -> `key_state_timeout`;
  - partial combo stale state reset после idle timeout.
- Подключены таймауты из `KeyboardConfig` в runtime monitor.

## Verification
- `pytest -q tests/test_quartz_stale_state_timeout.py tests/test_quartz_voiceover_passthrough.py tests/test_tray_quit_dispatch.py`
- Результат: `8 passed`.

## Запрос/цель
- Убрать блокировки shortcut/keys при активном приложении без поломки VO/system pass-through.

## Контекст
- Файлы: `modules/input_processing/keyboard/mac/quartz_monitor.py`, `tests/test_quartz_stale_state_timeout.py`
- Ограничения: без новых источников состояния и без реархитектуры.

## Решения/выводы
- Логика централизована в low-level adapter (один owner anti-stale).
- VoiceOver pass-through guard сохранен.

## Открытые вопросы
- Нужен ручной прогон на машине пользователя в реальном workflow для финального подтверждения.

## Следующие шаги
- Ручной сценарий: VO + Safari/YouTube + Spotlight + `Ctrl+N` (10–15 минут) и проверка отсутствия “оживления через Cmd+Tab”.
