# Исправления безопасности для close_app

## Проблемы и решения

### ✅ Проблема 1: Небезопасный дефолт флагов

**Проблема:** В `config.env.example` был установлен `FORWARD_ASSISTANT_ACTIONS=true`, что могло привести к автоматическому включению actions при копировании файла в production без правок.

**Решение:** Изменен дефолт на `false` с явным комментарием о необходимости осознанного включения.

**Изменения:**
- `server/server/config.env.example` (строки 30-37)
  ```bash
  # ⚠️  ВАЖНО: По умолчанию выключено для безопасности
  # Включите осознанно только в production/staging после проверки готовности
  FORWARD_ASSISTANT_ACTIONS=false
  # ⚠️  НЕ включайте в dev/локальном окружении без необходимости
  ```

**Rollback:** Вернуть `FORWARD_ASSISTANT_ACTIONS=true` (но это не рекомендуется)

---

### ✅ Проблема 2: Зависимость скриптов от структуры репозитория

**Проблема:** Скрипты проверки могли упасть при запуске вне репозитория или в другой структуре каталогов.

**Решение:** Добавлен параметр `--project-root` для указания кастомного пути к корню проекта.

**Изменения:**
- `server/server/scripts/verify_close_app_production_readiness.py`
  - Добавлена функция `get_project_root()` с автоматическим определением
  - Добавлен параметр `--project-root` для кастомных путей
  - Добавлена проверка структуры проекта (наличие `server/` и `client/`)

- `client/scripts/verify_close_app_client_readiness.py`
  - Аналогичные изменения

**Использование:**
```bash
# Автоматическое определение (из структуры репозитория)
python scripts/verify_close_app_production_readiness.py

# С кастомным путем
python scripts/verify_close_app_production_readiness.py --project-root /path/to/Nexy
```

---

### ✅ Проблема 3: Race condition при двойном close_app

**Проблема:** Если два разных запроса (с разными `session_id`) одновременно пытаются закрыть одно и то же приложение, может возникнуть race condition.

**Решение:** Добавлена идемпотентность по `app_name` для `close_app` (в дополнение к защите по `session_id`).

**Изменения:**
- `client/integration/integrations/action_execution_integration.py`
  - Добавлен `self._active_apps: Dict[str, str]` для отслеживания активных приложений
  - Проверка перед запуском: если приложение уже закрывается, новый запрос игнорируется
  - Очистка после завершения: приложение удаляется из `_active_apps`

**Логика:**
```python
# Защита по session_id (существующая)
if session_id in self._active_actions:
    return  # Действие уже выполняется для этой сессии

# Идемпотентность по app_name (новая для close_app)
if action_type == "close_app" and app_name:
    if app_name in self._active_apps:
        return  # Приложение уже закрывается (даже из другой сессии)
    self._active_apps[app_name] = session_id
```

**Edge cases:**
- Два запроса с разными `session_id` на закрытие одного приложения → второй игнорируется
- Запрос на закрытие приложения, которое уже закрывается → идемпотентность
- Запрос на закрытие другого приложения → выполняется параллельно

---

## Change Impact

### Simplifies system: ✅ Yes
- Безопасный дефолт предотвращает случайное включение
- Параметр `--project-root` упрощает использование в разных окружениях
- Идемпотентность предотвращает конфликты

### Removes code: ❌ No
- Добавлен код для идемпотентности
- Добавлен код для определения корня проекта

### Centralizes logic: ✅ Yes
- Логика идемпотентности централизована в `action_execution_integration.py`
- Проверка структуры проекта централизована в скриптах

### Risk of duplication: ✅ Low
- Нет дублирования логики
- Идемпотентность использует существующую структуру `_active_actions`

### Risk of race: ✅ Low
- Идемпотентность по `app_name` предотвращает race conditions
- Блокировка `_actions_lock` защищает от параллельных модификаций

---

## Definition of Done

### ✅ Безопасный дефолт
- [x] `FORWARD_ASSISTANT_ACTIONS=false` в `config.env.example`
- [x] Явный комментарий о необходимости осознанного включения
- [x] Предупреждение о не включении в dev/локальном окружении

### ✅ Гибкость скриптов
- [x] Параметр `--project-root` добавлен в оба скрипта
- [x] Автоматическое определение корня проекта
- [x] Проверка структуры проекта (наличие `server/` и `client/`)

### ✅ Идемпотентность close_app
- [x] Отслеживание активных приложений через `_active_apps`
- [x] Проверка перед запуском: игнорирование дубликатов по `app_name`
- [x] Очистка после завершения: удаление из `_active_apps`

### ✅ Тестирование
- [x] Линтеры пройдены без ошибок
- [x] Логика идемпотентности добавлена корректно
- [x] Документация обновлена

---

## Проверка исправлений

### 1. Проверка безопасного дефолта
```bash
grep "FORWARD_ASSISTANT_ACTIONS" server/server/config.env.example
# Должно быть: FORWARD_ASSISTANT_ACTIONS=false
```

### 2. Проверка параметра --project-root
```bash
cd server/server
python scripts/verify_close_app_production_readiness.py --help
# Должен показать опцию --project-root
```

### 3. Проверка идемпотентности
```bash
# Проверить наличие _active_apps в коде
grep "_active_apps" client/integration/integrations/action_execution_integration.py
# Должно быть несколько вхождений (инициализация, проверка, очистка)
```

---

## Связанные документы

- `Docs/CLOSE_APP_PRODUCTION_CHECKLIST.md` — обновлен с информацией о безопасном дефолте
- `Docs/CLOSE_APP_E2E_IMPLEMENTATION_GUIDE.md` — полная техническая инструкция
- `server/server/config.env.example` — обновлен с безопасным дефолтом
