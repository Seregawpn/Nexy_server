# LISTENING/Mic Stuck After Combo Release

## Метаданные
- Ассистент: codex
- Тип: analysis
- Дата: 2026-02-11
- ID (INS-###): N/A

## Diagnosis
После `combo release` не произошло `voice.recording_stop`, поэтому не сработала цепочка `mode.request(PROCESSING|SLEEPING)` и приложение осталось в `AppMode.LISTENING` с активным STT циклом.

## Root Cause
Потерян терминальный сигнал остановки на границе `QuartzKeyboardMonitor -> InputProcessingIntegration` (release path) → `InputProcessingIntegration` не публикует `voice.recording_stop` → `VoiceRecognitionIntegration` не получает команду `stop_listening`, микрофон и режим остаются активными.

## Optimal Fix
Закрепить один надежный owner терминального перехода в `InputProcessingIntegration` и сделать release-path идемпотентным/последовательным:
1. Гарантировать последовательную обработку callback-цепочки `PRESS/LONG_PRESS/RELEASE` (без гонки порядка на async boundary).
2. В `InputProcessingIntegration` добавить fail-safe: если `PTTState.RECORDING` и физическое нажатие уже снято, но `voice.recording_stop` не был опубликован в допустимое окно, принудительно вызвать `_request_terminal_stop(...)`.
3. Логировать отдельный marker для пропущенного release (для быстрой диагностики).

Source of Truth: `integration/integrations/input_processing_integration.py` (terminal stop owner), `integration/integrations/mode_management_integration.py` (единственный применитель mode transitions).

## Verification
1. Удержать PTT (`Ctrl+N`) > threshold, затем отпустить.
2. Проверить обязательную последовательность: `combo release` -> `voice.recording_stop` -> `VOICE: recording_stop` -> `voice.mic_closed` -> `mode.request(PROCESSING|SLEEPING)`.
3. Убедиться, что `LISTENING` не залипает, а в логах нет повторяющегося `Listening...` после отпускания.

## Pre-Change Gate Evidence (обязательно)
- Прочитанные документы:
  - `AGENTS.md`
  - `Docs/DOCS_INDEX.md`
  - `Docs/PRE_CHANGE_CHECKLIST.md`
  - `Docs/PROJECT_REQUIREMENTS.md` (REQ-001, REQ-003, REQ-006, REQ-009A)
  - `Docs/ARCHITECTURE_OVERVIEW.md` (централизация mode/request, ownership интеграций input/voice/mode)
  - `Docs/FEATURE_FLAGS.md`
  - `Docs/ASSISTANT_COORDINATION_PROTOCOL.md`
  - `Docs/CODEX_PROMPT.md`
  - `Docs/ANTIGRAVITY_PROMPT.md`
  - `client/Docs/DOCS_INDEX.md`
  - `client/Docs/PRE_CHANGE_CHECKLIST.md`
- Source of Truth: `InputProcessingIntegration` (publish `voice.recording_start/stop`) + `ModeManagementIntegration` (apply mode change).
- Дублирование: none (анализ существующего пути `release -> _request_terminal_stop -> voice.recording_stop`).
- Feature Flags check: none (новые флаги не требуются).
- Race check: async ordering race на границе callback dispatcher -> coroutine scheduling; guard: state-guard + idempotent terminal stop.

## Запрос/цель
Определить, почему произошло залипание режима и микрофона по runtime-логу.

## Контекст
- Файлы:
  - `integration/integrations/input_processing_integration.py`
  - `modules/input_processing/keyboard/mac/quartz_monitor.py`
  - `integration/integrations/voice_recognition_integration.py`
  - `integration/integrations/mode_management_integration.py`
- Документы:
  - `Docs/PROJECT_REQUIREMENTS.md`
  - `Docs/ARCHITECTURE_OVERVIEW.md`
  - `Docs/FEATURE_FLAGS.md`
  - `Docs/PRE_CHANGE_CHECKLIST.md`
  - `Docs/ASSISTANT_COORDINATION_PROTOCOL.md`
- Ограничения: без обхода централизованного `mode.request`/ModeManagement.

## Решения/выводы
- Симптом подтвержден логом: release зафиксирован в monitor, но stop-событие в EventBus отсутствует.
- Проблема в terminal-stop path, а не в `ModeManagementIntegration`.
- Фикс должен усиливать текущего owner (`InputProcessingIntegration`), без нового owner/флага.

## Открытые вопросы
- Есть ли в полном логе `INPUT: suppressed spurious release` или `callback error`, не попавшие в предоставленный фрагмент.

## Следующие шаги
- Внести патч в release fail-safe + ordering guard.
- Прогнать ручной сценарий long-press/release и проверить event chain.
