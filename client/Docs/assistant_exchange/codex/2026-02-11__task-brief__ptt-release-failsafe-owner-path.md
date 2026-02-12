# PTT release fail-safe owner path

## Метаданные
- Ассистент: codex
- Тип: task-brief
- Дата: 2026-02-11
- ID (INS-###): n/a

## Diagnosis
- При некоторых циклах `Ctrl+N` release фиксировался в Quartz (`combo release`), но не доходил до owner terminal-stop.
- Это оставляло `voice.recording_stop` непубликованным и приводило к залипанию микрофона/режима.

## Root Cause
- Потеря RELEASE-callback на границе `QuartzKeyboardMonitor -> InputProcessingIntegration` → не вызывался `_request_terminal_stop()`.

## Optimal Fix
- Добавлен owner-side fail-safe в `InputProcessingIntegration`, который завершает PTT цикл при подтвержденном физическом отпускании и отсутствии RELEASE-callback.
- Логика пост-terminal перехода в режим вынесена в единый helper `_transition_after_terminal_stop()` для исключения дубля.
- В `QuartzKeyboardMonitor` добавлена диагностика доставки async RELEASE callback (scheduled/completed/exception).
- Добавлен тест восстановления при потере RELEASE callback.

## Verification
- Команда: `PYTHONPATH=. pytest -q tests/test_microphone_activation.py`
- Результат: `11 passed in 1.58s`
- Дополнительно: `python3 -m py_compile integration/integrations/input_processing_integration.py modules/input_processing/keyboard/mac/quartz_monitor.py tests/test_microphone_activation.py`

## Pre-Change Gate Evidence (обязательно)
- Прочитанные документы:
  - `/Users/sergiyzasorin/Fix_new/client/AGENTS.md`
  - `/Users/sergiyzasorin/Fix_new/Docs/DOCS_INDEX.md`
  - `/Users/sergiyzasorin/Fix_new/Docs/PRE_CHANGE_CHECKLIST.md`
  - `/Users/sergiyzasorin/Fix_new/Docs/ASSISTANT_COORDINATION_PROTOCOL.md`
  - `/Users/sergiyzasorin/Fix_new/client/Docs/DOCS_INDEX.md`
  - `/Users/sergiyzasorin/Fix_new/client/Docs/PRE_CHANGE_CHECKLIST.md`
  - `/Users/sergiyzasorin/Fix_new/client/Docs/PROJECT_REQUIREMENTS.md`
  - `/Users/sergiyzasorin/Fix_new/client/Docs/ARCHITECTURE_OVERVIEW.md`
  - `/Users/sergiyzasorin/Fix_new/client/Docs/FLOW_INTERACTION_SPEC.md`
  - `/Users/sergiyzasorin/Fix_new/client/Docs/STATE_CATALOG.md`
  - `/Users/sergiyzasorin/Fix_new/client/Docs/FEATURE_FLAGS.md`
- Source of Truth: `InputProcessingIntegration` (PTT lifecycle owner), `ApplicationStateManager` (session/mode SoT).
- Дублирование: объединен post-terminal transition в `_transition_after_terminal_stop`, новый параллельный owner не вводился.
- Feature Flags check: новых флагов не добавлено.
- Race check: сценарий потери RELEASE; guard — state-based fail-safe + idempotent terminal-stop.

## Запрос/цель
- Исправить залипание микрофона/режима при удержании и отпускании hotkey.

## Контекст
- Файлы:
  - `/Users/sergiyzasorin/Fix_new/client/integration/integrations/input_processing_integration.py`
  - `/Users/sergiyzasorin/Fix_new/client/modules/input_processing/keyboard/mac/quartz_monitor.py`
  - `/Users/sergiyzasorin/Fix_new/client/tests/test_microphone_activation.py`

## Решения/выводы
- Исправление выполнено без новых feature flags и без обхода центра mode ownership.
- Поведение стабилизировано owner-side fail-safe логикой.

## Открытые вопросы
- Нет.

## Следующие шаги
- Прогнать полный `problem_scan` / интеграционные PTT сценарии в runtime.
