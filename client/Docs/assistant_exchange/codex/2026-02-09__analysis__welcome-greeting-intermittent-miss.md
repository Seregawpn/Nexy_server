# Автор
Codex

# Запрос/цель
Разобрать редкий сценарий, когда приветствие на старте иногда не воспроизводится.

# Контекст
- `/Users/sergiyzasorin/Fix_new/client/integration/integrations/welcome_message_integration.py`
- `/Users/sergiyzasorin/Fix_new/client/modules/permissions/v2/integration.py`
- `/Users/sergiyzasorin/Fix_new/client/integration/core/event_bus.py`
- `/Users/sergiyzasorin/Fix_new/client/integration/integrations/first_run_permissions_integration.py`
- `/Users/sergiyzasorin/Fix_new/client/integration/core/simple_module_coordinator.py`

# Вывод
Корневая причина — гонка между `system.ready_to_greet` и `permissions.first_run_completed` + дублирование source-of-truth в `WelcomeMessageIntegration`.

Механизм:
1. V2 публикует `system.ready_to_greet`, затем legacy `permissions.first_run_completed`.
2. В `EventBus` при доставке в другой loop async callbacks планируются через `run_coroutine_threadsafe` и не await'ятся inline.
3. В `WelcomeMessageIntegration._on_ready_to_greet` есть локальный gate `snapshot.first_run` + `_deferred_until_first_run`.
4. При редком reorder `permissions.first_run_completed` может быть обработан до установки `_deferred_until_first_run=True`, затем `_on_first_run_completed` ничего не делает (guard `if not self._deferred_until_first_run: return`), а приветствие остаётся навсегда отложенным.

Это архитектурно лишний второй gate: решение "можно ли приветствовать" уже централизовано в событии `system.ready_to_greet`.

# Рекомендуемый фикс (primary)
- Убрать в `WelcomeMessageIntegration` зависимость запуска приветствия от локального `snapshot.first_run` и `_deferred_until_first_run`.
- Использовать `system.ready_to_greet` как единственный триггер (source of truth).
- `permissions.first_run_completed` оставить только как совместимый backup-триггер с idempotent guard (`_welcome_played`/lock), без зависимости от локального defer-флага.

# Риски
- Низкий риск регрессии: запуск уже защищён `_welcome_lock` + `_welcome_played`.
- Низкий риск дубля: guard уже централизован в `WelcomeMessageIntegration._request_welcome_play`.

# Следующие шаги
1. Изменить `WelcomeMessageIntegration` по схеме выше.
2. Добавить тест на reorder событий (`first_run_completed` -> `ready_to_greet` и наоборот), ожидать 1 запуск приветствия.
3. Прогнать startup smoke с искусственными `asyncio.sleep` в обработчиках.

# Открытые вопросы
- Нужна ли поддержка fallback-триггера `permissions.first_run_completed` при строгом V2-only контуре, или можно оставить только `system.ready_to_greet`.
