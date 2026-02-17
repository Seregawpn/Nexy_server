# Task Brief: interrupt preempt mode flicker fix

## Context
В логах при `keyboard.press_preempt` в `PROCESSING` наблюдался лишний переход режима `PROCESSING -> SLEEPING -> LISTENING`, что создавало mode-фликер и конкурирующие mode-chain события.

## Diagnosis
Root cause: `InterruptManagementIntegration._handle_speech_stop()` всегда публиковал `mode.request(SLEEPING)`, даже для preempt-веток клавиатуры (`keyboard.press_preempt`, `keyboard.long_press`), где input flow сразу стартует новую запись.

## Architecture Fit
- Owner mode-chain сохранен: `ModeManagementIntegration -> ModeController -> ApplicationStateManager`.
- Изменение сделано в owner-источнике interrupt side-effects, без локальных обходов mode-слоя.

## Changes
1. `integration/integrations/interrupt_management_integration.py`
- Для источников `keyboard.press_preempt` и `keyboard.long_press`:
  - speech stop / grpc cancel остаются;
  - публикация `mode.request(SLEEPING)` пропускается.
- Для остальных источников поведение без изменений.

2. `tests/test_interrupt_management_preempt_mode_skip.py` (новый)
- Проверка, что preempt-source не публикует `mode.request(SLEEPING)`.
- Проверка, что обычный source продолжает публиковать `mode.request(SLEEPING)`.

## Verification
- Команда: `PYTHONPATH=. pytest -q tests/test_interrupt_management_preempt_mode_skip.py tests/test_mode_management_sleep_guard_session_scope.py`
- Результат: `5 passed`.

## Информация об изменениях
- Что изменено:
  - Убран лишний mode-переход в preempt-ветке клавиатуры.
  - Сохранены cancel side-effects без дублирующего route принятия mode-решений.
  - Добавлен регресс-тест на контракт preempt interrupt.
- Список файлов:
  - `integration/integrations/interrupt_management_integration.py`
  - `tests/test_interrupt_management_preempt_mode_skip.py`
  - `Docs/assistant_exchange/codex/2026-02-17__task-brief__interrupt-preempt-mode-flicker-fix.md`
- Причина/цель изменений:
  - Убрать mode-фликер и race между interrupt-sleep и immediate input-start.
- Проверка:
  - Локальный pytest прогон новых и связанных тестов.
