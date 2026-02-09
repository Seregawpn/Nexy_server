# Автор
Codex

# Запрос/цель
Устранить редкий пропуск приветствия на старте без добавления новых состояний, дублей и race-condition.

# Контекст
- `/Users/sergiyzasorin/Fix_new/client/integration/integrations/welcome_message_integration.py`
- `/Users/sergiyzasorin/Fix_new/client/tests/test_welcome_startup_sequence.py`

# Что сделано
1. Убран локальный defer-state (`_deferred_until_first_run`) из `WelcomeMessageIntegration`.
2. Убрана локальная проверка `snapshot.first_run` в `_on_ready_to_greet`.
3. `permissions.first_run_completed` оставлен как legacy backup-trigger, но без собственного state-gate; запуск идёт через общий `_request_welcome_play`.
4. Сохранён единый anti-duplication/anti-race guard: `_welcome_lock` + `_welcome_played` + `_pending_welcome`.
5. Добавлены регрессионные тесты на оба порядка событий:
   - `first_run_completed -> ready_to_greet`
   - `ready_to_greet -> first_run_completed`
   Ожидание: приветствие запускается ровно один раз.

# Проверка
- Команда: `pytest -q tests/test_welcome_startup_sequence.py`
- Результат: `2 passed`.

# Решение/вывод
Source of Truth для старта приветствия теперь централизован на событии готовности системы (`system.ready_to_greet`), без второго локального источника истины в `welcome`.

# Открытые вопросы
- Нет.

# Следующие шаги
1. Прогнать end-to-end smoke старта приложения с логами и проверить отсутствие редких пропусков приветствия в длительном прогоне.
