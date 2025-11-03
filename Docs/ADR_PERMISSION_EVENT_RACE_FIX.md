# ADR: Исправление гонки условий в событиях разрешений при перезапуске

**Дата**: 2025-11-03  
**Статус**: ✅ Реализовано  
**Контекст**: Критический баг в последовательности инициализации

## Проблема

При перезапуске приложения после first-run запроса разрешений обнаружена **критическая гонка условий** (race condition):

### Последовательность событий (ПРОБЛЕМНАЯ):

1. ✅ `coordinator.initialize()` → создание EventBus, StateManager
2. ✅ `coordinator._create_integrations()` → создание всех интеграций
3. ✅ `coordinator._initialize_integrations()` → инициализация интеграций
4. ✅ **FirstRunPermissionsIntegration.initialize()** обнаруживает флаг перезапуска
5. ✅ Публикует событие `permissions.first_run_completed`
6. ❌ **Координатор ЕЩЁ НЕ подписан** на это событие!
7. ❌ `coordinator._setup_coordination()` подписывается на события (уже поздно!)
8. ❌ Событие **потеряно**, флаг `_permissions_in_progress` не сбрасывается
9. ❌ Приложение зависает в неполном состоянии

### Последствия

- Приложение не завершает инициализацию после перезапуска
- Остальные интеграции (voice_recognition, input_processing) не запускаются
- Пользователь видит зависшее приложение с неактивным трей-меню

## Решение

Переместить подписки на критичные события **ДО** инициализации интеграций:

### Новая последовательность (ПРАВИЛЬНАЯ):

1. ✅ `coordinator.initialize()` → создание EventBus, StateManager
2. ✅ **`coordinator._setup_critical_subscriptions()`** → подписка на события разрешений
3. ✅ `coordinator._create_integrations()` → создание всех интеграций
4. ✅ `coordinator._initialize_integrations()` → инициализация интеграций
5. ✅ **FirstRunPermissionsIntegration.initialize()** обнаруживает флаг перезапуска
6. ✅ Публикует событие `permissions.first_run_completed`
7. ✅ **Координатор получает событие** → сбрасывает `_permissions_in_progress = False`
8. ✅ `coordinator._setup_coordination()` → остальные подписки
9. ✅ `coordinator.start()` → запуск всех интеграций (без блокировки)
10. ✅ Приложение работает корректно

## Изменения

### 1. Новый метод `_setup_critical_subscriptions()`

Создан отдельный метод для подписки на события разрешений:

```python
async def _setup_critical_subscriptions(self):
    """
    Настройка критичных подписок на события ДО инициализации интеграций.
    
    КРИТИЧНО: Должна вызываться ДО _initialize_integrations(), чтобы
    не потерять события permissions.first_run_completed, публикуемые
    в FirstRunPermissionsIntegration.initialize() при обнаружении
    флага перезапуска.
    """
    await self.event_bus.subscribe("permissions.first_run_started", ...)
    await self.event_bus.subscribe("permissions.first_run_completed", ...)
    await self.event_bus.subscribe("permissions.first_run_failed", ...)
    await self.event_bus.subscribe("permissions.first_run_restart_pending", ...)
```

### 2. Изменен порядок в `initialize()`

```python
# 1. Создаем core компоненты (EventBus, StateManager, ErrorHandler)
# 1.1 Запускаем фоновый asyncio loop
# 1.2 КРИТИЧНО: Подписываемся на события разрешений ДО инициализации
await self._setup_critical_subscriptions()
# 2. Создаем интеграции
# 3. Инициализируем интеграции (здесь публикуются события!)
# 4. Настраиваем остальную координацию
```

### 3. Удалены дублирующиеся подписки из `_setup_coordination()`

## Альтернативы

### 1. Отложенная публикация событий
- Разрешить интеграциям публиковать события только в `start()`, а не в `initialize()`
- ❌ Отклонено: нарушает логику first-run flow, требует изменения других интеграций

### 2. Очередь событий
- Накапливать события до настройки подписок, затем переигрывать
- ❌ Отклонено: излишняя сложность, требует изменений EventBus

### 3. Синхронные флаги вместо событий
- Использовать только флаги `_permissions_in_progress` без событий
- ❌ Отклонено: нарушает архитектуру event-driven, затрудняет наблюдаемость

## Риски и митигации

| Риск | Вероятность | Воздействие | Митигация |
|------|-------------|-------------|-----------|
| Другие интеграции тоже публикуют события в initialize() | Средняя | Средняя | Аудит всех интеграций, документирование паттерна |
| Порядок подписок влияет на другие события | Низкая | Низкая | EventBus обрабатывает подписки по приоритетам |
| Дублирование подписок (если забыть удалить из _setup_coordination) | Низкая | Средняя | Code review, линтер проверки дублей |

## Тестирование

### Сценарии проверки:

1. ✅ **Первый запуск**: Разрешения запрашиваются → приложение перезапускается
2. ✅ **Второй запуск (after restart)**: Событие `permissions.first_run_completed` получено → флаг сброшен → все интеграции запущены
3. ✅ **Обычный запуск (after first_run)**: Флаг существует → событие не публикуется → нормальный запуск

### Проверка:
```bash
# 1. Удалить флаги
rm ~/Library/Application\ Support/Nexy/permissions_first_run_completed.flag
rm ~/Library/Application\ Support/Nexy/restart_completed.flag

# 2. Первый запуск (запросит разрешения и перезапустится)
python client/main.py

# 3. После перезапуска проверить логи:
grep "permissions.first_run_completed" logs/nexy.log
grep "_permissions_in_progress" logs/nexy.log
# Ожидаемо: событие получено, флаг сброшен

# 4. Проверить что все интеграции запущены:
grep "✅.*запущен" logs/nexy.log
```

## Метрики

- `permission_flow_success` — процент успешных завершений потока разрешений (цель: ≥ 99%)
- `permission_restart_success_rate` — процент успешных автоматических перезапусков (цель: ≥ 98%)
- `coordinator_init_duration_ms` — длительность инициализации координатора (p95, цель: ≤ 2000ms)

## Ссылки

- Исходная проблема: приложение зависает после перезапуска при запросе разрешений
- Связанные файлы:
  - `integration/core/simple_module_coordinator.py` (основное исправление)
  - `integration/integrations/first_run_permissions_integration.py` (публикация событий)
  - `Docs/STATE_CATALOG.md` (оси состояния)
  - `Docs/PERMISSION_RESTART_KEY_POINTS.md` (документация перезапуска)

## Авторы

- **Разработчик**: AI Assistant
- **Дата**: 2025-11-03
- **Ревьюер**: Pending

