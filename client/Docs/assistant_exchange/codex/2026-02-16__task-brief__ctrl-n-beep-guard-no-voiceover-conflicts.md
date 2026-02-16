# Ctrl+N beep guard without VoiceOver/system conflicts

## Метаданные
- Ассистент: codex
- Тип: task-brief
- Дата: 2026-02-16
- ID (INS-###): N/A

## Diagnosis
При временно неактивном Quartz tap (`Secure Input`/edge runtime) `Ctrl+N` доходит до AppKit и вызывает системный beep. Текущий owner hotkey-логики (Quartz/InputProcessing) не имеет локального consume-guard для этого окна.

## Root Cause
Отсутствие UI-level consume path для strict `Ctrl+N` -> AppKit получает необработанный key equivalent в активном окне -> macOS проигрывает error beep.

## Optimal Fix
- Добавлен lifecycle-managed AppKit hidden menu consume-handler для strict `Ctrl+N` в `InputProcessingIntegration`.
- Guard не публикует событий и не меняет PTT/mode workflow; owner hotkey решения остается `QuartzKeyboardMonitor` + `InputProcessingIntegration`.
- Установка/удаление выполняются через `NSOperationQueue.mainQueue()`.

## Verification
- `python3 -m py_compile integration/integrations/input_processing_integration.py`
- `PYTHONPATH=. pytest -q tests/test_quartz_monitor_chord_logic.py`
- Результат: `2 passed`.

## Контекст
- Файлы: `integration/integrations/input_processing_integration.py`
- Документы: `AGENTS.md`, `Docs/PROJECT_REQUIREMENTS.md`, `Docs/ARCHITECTURE_OVERVIEW.md`, `../Docs/ASSISTANT_COORDINATION_PROTOCOL.md`, `../Docs/ANTIGRAVITY_PROMPT.md`, `../Docs/CODEX_PROMPT.md`, `../Docs/assistant_exchange/TEMPLATE.md`, `../Docs/ARCHITECTURE_GOVERNANCE.md`

## Architecture Gates
- Single Owner Gate: owner hotkey decision не изменён; guard только consume UI-beep.
- Zero Duplication Gate: переиспользована существующая идея hidden handler, без второго event/ptt пути.
- Anti-Race Gate: lifecycle cleanup на `start/stop`, операции меню сериализованы main queue.
- Flag Lifecycle Gate: новые feature flags не добавлялись.
