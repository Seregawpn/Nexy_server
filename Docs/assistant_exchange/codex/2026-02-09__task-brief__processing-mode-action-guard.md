# processing-mode-action-guard

## Метаданные
- Ассистент: codex
- Тип: task-brief
- Дата: 2026-02-09
- ID (INS-###): INS-UNKNOWN

## Diagnosis
Режим мог перейти в `sleeping` до старта/финиша action при рассинхроне или отсутствии `session_id` в `grpc.response.action` и `actions.lifecycle.*`.

## Root Cause
Отсутствует fallback привязка action-событий к активной processing-сессии → блокеры `actions/action_intent` не ставятся на владельца режима → `mode.request(SLEEPING)` проходит раньше завершения действия.

## Optimal Fix
- Владелец логики: `ModeManagementIntegration` (единый центр принятия mode-решений).
- Добавлен fallback `session_id` для action intent/lifecycle: если `session_id` отсутствует, берется активная processing-сессия.
- Усилен sleep-guard: при `mode.request(SLEEPING)` для штатных источников используется `request_session || active_processing_session`.
- Добавлен global fallback blocker (`actions_any` / `action_intent_any`) для защиты от рассинхрона session.
- Добавлена диагностическая телеметрия `ACTION_INTENT received` и `ACTION_SESSION_FALLBACK`.

## Verification
- Новый тест: `tests/test_mode_management_processing_action_guard.py`
- Команда: `PYTHONPATH=. pytest -q ../tests/test_mode_management_processing_action_guard.py` (из `/Users/sergiyzasorin/Fix_new/client`)
- Результат: `3 passed`.

## Запрос/цель
Удерживать `processing` во время речи/действий и переходить в `sleeping` только после фактического завершения цепочки.

## Контекст
- Файлы:
  - `/Users/sergiyzasorin/Fix_new/client/integration/integrations/mode_management_integration.py`
  - `/Users/sergiyzasorin/Fix_new/tests/test_mode_management_processing_action_guard.py`
- Документы:
  - `/Users/sergiyzasorin/Fix_new/Docs/PROJECT_REQUIREMENTS.md`
  - `/Users/sergiyzasorin/Fix_new/Docs/ARCHITECTURE_OVERVIEW.md`
  - `/Users/sergiyzasorin/Fix_new/Docs/_archive/ASSISTANT_COORDINATION_PROTOCOL.md`
  - `/Users/sergiyzasorin/Fix_new/Docs/_archive/ANTIGRAVITY_PROMPT.md`
  - `/Users/sergiyzasorin/Fix_new/Docs/_archive/CODEX_PROMPT.md`
  - `/Users/sergiyzasorin/Fix_new/Docs/_archive/assistant_exchange/TEMPLATE.md`
- Ограничения: без изменения архитектуры централизованного mode управления.

## Решения/выводы
- Исправление выполнено в существующем owner-слое (`ModeManagementIntegration`) без второго источника истины.
- Ранний уход в `sleeping` при missing session_id в action-потоке теперь блокируется.

## Открытые вопросы
- Нет.

## Следующие шаги
- Проверить живой рантайм логи на наличие `ACTION_INTENT received` и последующего `actions.lifecycle.started/finished` для той же processing-сессии.
