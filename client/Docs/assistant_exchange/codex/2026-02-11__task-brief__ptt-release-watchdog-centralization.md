# PTT release watchdog centralization

## Метаданные
- Ассистент: codex
- Тип: task-brief
- Дата: 2026-02-11
- ID (INS-###): n/a

## Diagnosis
- Runtime лог показал `RELEASE scheduled` без `RELEASE completed`; terminal stop не запускался, микрофон залипал в LISTENING.

## Root Cause
- Один edge callback `RELEASE` в boundary `Quartz -> InputProcessing` мог зависнуть/потеряться; fallback в health-check был недостаточно гарантирован.

## Optimal Fix
- Добавлен отдельный owner-side `release_watchdog` в `InputProcessingIntegration`, который armed на `LONG_PRESS` и завершает цикл через тот же `_request_terminal_stop()` при подтвержденном физическом отпускании.
- Сохранена централизация: fallback не вводит новый owner, а использует текущий terminal-stop path.
- Добавлен hardening health-check (`try/except` per-iteration) для исключения silent death фоновой задачи.
- На shutdown/reset добавлена явная отмена watchdog-задач.

## Verification
- `PYTHONPATH=. pytest -q tests/test_microphone_activation.py` -> `11 passed`.
- `python3 -m py_compile integration/integrations/input_processing_integration.py modules/input_processing/keyboard/mac/quartz_monitor.py tests/test_microphone_activation.py` -> ok.

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
- Дублирование: новый fallback не создает второй путь принятия решения; использует тот же terminal-stop owner.
- Feature Flags check: новых флагов нет.
- Race check: сценарий потери RELEASE; guard — lifecycle lock + idempotent `_try_mark_terminal_stop`.

## Запрос/цель
- Убрать залипание микрофона/режима при потере RELEASE callback.

## Контекст
- Файлы:
  - `/Users/sergiyzasorin/Fix_new/client/integration/integrations/input_processing_integration.py`
  - `/Users/sergiyzasorin/Fix_new/client/modules/input_processing/keyboard/mac/quartz_monitor.py`
  - `/Users/sergiyzasorin/Fix_new/client/tests/test_microphone_activation.py`

## Решения/выводы
- Централизация сохранена: stop/mode path остаются в текущих owners.
- Гонка callback-delivery закрыта owner-side watchdog fallback.

## Открытые вопросы
- Нет.

## Следующие шаги
- Проверить runtime логи с реальным `Ctrl+N`: `RELEASE completed` или `release fail-safe triggered` -> `voice.recording_stop`.
