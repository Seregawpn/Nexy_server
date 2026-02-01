# Исправления идемпотентности close_app

## Обзор

Исправлены две проблемы, выявленные в код-ревью:

1. **Отсутствие события для дубликатных сессий** (Medium)
2. **Чувствительность к регистру и пробелам** (Low)

---

## Исправление 1: Публикация события для дубликатных сессий

### Проблема

При обнаружении дубликата `close_app` для другого `session_id` код просто возвращался без публикации события. Это приводило к тому, что клиент/сервер "ждали" ответа, которого не будет.

### Решение

При обнаружении дубликата публикуется событие `actions.close_app.failed` с кодом `already_running`:

```python
# client/integration/integrations/action_execution_integration.py (строки 290-297)
if app_name_normalized in self._active_apps:
    existing_session = self._active_apps[app_name_normalized]
    logger.info(
        "[%s] close_app already running for app=%s (session=%s, new_session=%s)",
        feature_id, app_name, existing_session, session_id
    )
    # Публикуем событие failure для второй сессии
    await self._publish_failure(
        session_id=session_id,
        feature_id=action_feature_id,
        error_code="already_running",
        message=f"close_app already running for {app_name} (session={existing_session})",
        app_name=app_name,
    )
    return
```

### Результат

- ✅ Клиент/сервер получают ответ о том, что действие уже выполняется
- ✅ Нет "подвисших" запросов
- ✅ Улучшен UX и синхронизация

---

## Исправление 2: Нормализация app_name

### Проблема

Идемпотентность по `app_name` была чувствительна к регистру и пробелам:
- `"Safari"` и `"safari"` считались разными приложениями
- `"Safari "` (с пробелом) и `"Safari"` считались разными приложениями

Это могло привести к пропуску дубликатов и одновременному закрытию одного и того же приложения.

### Решение

Использование нормализованного ключа `app_name.strip().lower()` для проверки и регистрации в `_active_apps`, при сохранении оригинального `app_name` в `action_data` для передачи в MCP:

```python
# client/integration/integrations/action_execution_integration.py (строка 280)
app_name_normalized = app_name.strip().lower()

# Проверка (строка 281)
if app_name_normalized in self._active_apps:
    # ...

# Регистрация (строка 300)
self._active_apps[app_name_normalized] = session_id

# Очистка (строка 423)
app_name_normalized = app_name.strip().lower()
if self._active_apps.get(app_name_normalized) == session_id:
    self._active_apps.pop(app_name_normalized, None)
```

### Результат

- ✅ `"Safari"`, `"safari"`, `"Safari "` считаются одним приложением
- ✅ Дубликаты надежно обнаруживаются
- ✅ Предотвращены race conditions

---

## Измененные файлы

1. **`client/integration/integrations/action_execution_integration.py`**
   - Строки 279-300: Нормализация и публикация события при дубликате
   - Строки 420-430: Нормализация при очистке

2. **`Docs/CLOSE_APP_CODE_REVIEW.md`**
   - Обновлена секция с исправлениями

---

## Тестирование

### Проверка нормализации

```python
# Все эти варианты должны считаться одним приложением:
close_app("Safari")      # Первый запрос - выполняется
close_app("safari")      # Дубликат - событие already_running
close_app("Safari ")      # Дубликат - событие already_running
close_app("  SAFARI  ")   # Дубликат - событие already_running
```

### Проверка события

```python
# Первый запрос
close_app("Safari", session_id="session_1")
# → actions.close_app.started
# → actions.close_app.completed

# Второй запрос (дубликат)
close_app("Safari", session_id="session_2")
# → actions.close_app.failed (error_code="already_running")
```

---

## Статус

✅ **Исправлено и готово к production**

Оба исправления реализованы, протестированы и задокументированы. Код готов к merge.
