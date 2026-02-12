# Input Release Failsafe (No Duplicate Stop Path)

## Метаданные
- Ассистент: codex
- Тип: task-brief
- Дата: 2026-02-11
- ID (INS-###): N/A

## Diagnosis
В runtime-сценарии фиксировался `combo release`, но не всегда доходил terminal path `voice.recording_stop`, что приводило к залипанию `LISTENING` и активного микрофона.

## Root Cause
Потеря/пропуск release-сигнала на границе monitor→integration оставляла цикл в `PTTState.RECORDING` без перехода в terminal stop.

## Optimal Fix
Реализован fail-safe в существующем owner (`InputProcessingIntegration`), без нового stop-пайплайна:
- периодическая проверка в `_run_health_check` для Quartz;
- при `RECORDING` + физически отпущенном PTT + истекшем grace окне вызывается уже существующий `_request_terminal_stop(...)`;
- дальше используется текущая централизованная цепочка `mode.request(PROCESSING|SLEEPING)`.

## Verification
- `python3 -m py_compile integration/integrations/input_processing_integration.py` — OK.
- Runtime DoD:
  1. Long press `Ctrl+N`, затем release.
  2. Проверить логи: либо обычный `release` path, либо `INPUT release failsafe...`.
  3. В обоих случаях должны появиться `voice.recording_stop` и дальнейший уход из `LISTENING`.

## Pre-Change Gate Evidence (обязательно)
- Прочитанные документы:
  - `AGENTS.md`
  - `Docs/DOCS_INDEX.md`
  - `Docs/PRE_CHANGE_CHECKLIST.md`
  - `Docs/PROJECT_REQUIREMENTS.md`
  - `Docs/ARCHITECTURE_OVERVIEW.md`
  - `Docs/ASSISTANT_COORDINATION_PROTOCOL.md`
  - `Docs/FEATURE_FLAGS.md`
  - `Docs/CODEX_PROMPT.md`
  - `Docs/ANTIGRAVITY_PROMPT.md`
  - `client/Docs/DOCS_INDEX.md`
  - `client/Docs/PRE_CHANGE_CHECKLIST.md`
- Source of Truth: `integration/integrations/input_processing_integration.py` (terminal stop owner).
- Дублирование: новый path не создан; используется текущий `_request_terminal_stop`.
- Feature Flags check: новых флагов нет.
- Race check: guard через `PTTState` + idempotent terminal stop (`_try_mark_terminal_stop`).

## Запрос/цель
Исправить текущую ошибку залипания режима/микрофона без создания дублей.

## Контекст
- Файл: `integration/integrations/input_processing_integration.py`

## Решения/выводы
- Применен centralization-first подход: только усиление существующего owner.
- Добавлен диагностический marker для подтверждения, что сработал recovery.

## Открытые вопросы
- Нужен ли отдельный telemetry counter на частоту срабатывания `release_missed_failsafe` (пока не добавлялся).

## Следующие шаги
- Прогнать ручной стресс-тест (20–30 циклов удержания/отпускания).
- При необходимости добавить unit/integration тест на `missed release` сценарий.
