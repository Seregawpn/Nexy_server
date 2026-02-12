# VoiceOver Hotkeys Pass-Through Guard

## Метаданные
- Ассистент: codex
- Тип: task-brief
- Дата: 2026-02-11
- ID (INS-###): N/A

## Diagnosis
- При VoiceOver chord (`Control+Option+...`) в single-key режиме (`left_control`) PTT мог входить в lifecycle.
- Это воспринимается как блокировка/ломание пользовательских комбинаций VoiceOver.

## Root Cause
- В `QuartzKeyboardMonitor._handle_single_key_event` не было жесткого guard на non-PTT modifiers (`Option`/`Command`).
- Механизм: `Control` флаг обрабатывался как PTT-press даже при VO chord.

## Optimal Fix
- Добавлен единый guard `_has_non_ptt_modifiers(flags)` и применен:
  - в combo path (`ctrl_n`) для консистентного блок-решения,
  - в single-key path (`left_control`) для pass-through VoiceOver chord.
- При активном non-PTT modifier lifecycle PTT не стартует; если уже активен, корректно завершается.

## Verification
- `pytest -q tests/test_quartz_voiceover_passthrough.py tests/test_tray_quit_dispatch.py`
- Результат: `5 passed`.

## Запрос/цель
- Обеспечить, чтобы сочетания VoiceOver не блокировались/не ломались из-за PTT-монитора.

## Контекст
- Файлы: `modules/input_processing/keyboard/mac/quartz_monitor.py`, `tests/test_quartz_voiceover_passthrough.py`
- Документы: `Docs/PROJECT_REQUIREMENTS.md`, `Docs/ARCHITECTURE_OVERVIEW.md`
- Ограничения: без новых источников состояния, без реархитектуры.

## Решения/выводы
- SoT не менялся: lifecycle остается в `InputProcessingIntegration`.
- Guard реализован в low-level adapter, что архитектурно корректно.

## Открытые вопросы
- Нужна ручная проверка на машине пользователя с реальным VoiceOver workflow.

## Следующие шаги
- Ручной smoke: `VO+комбинации`, `Cmd+Space`, `Ctrl+N` при активном VoiceOver.
