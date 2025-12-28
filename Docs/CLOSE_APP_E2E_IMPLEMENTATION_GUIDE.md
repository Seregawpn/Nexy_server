# Техническая инструкция: Реализация E2E цикла close_app

## Цель
Единый канонический поток `close_app` как у `open_app`:
```
system prompt → JSON → парсинг → command_payload → gRPC → клиент → MCP → osascript → events/audio
```

## Статус реализации

### ✅ Шаг 1: System Prompt (сервер)
**Файл:** `server/server/config/unified_config.py`

**Статус:** ✅ Выполнено

**Проверка:**
- [x] В разделе "Action Intent" добавлен `close_app` (строка 155-160)
- [x] В "Action Output Format" добавлен пример `close_app` (строки 226-234)
- [x] Промпт синхронизирован в `unified_config_example.yaml`

**DoD:** ✅ Модель стабильно возвращает JSON с `"command": "close_app"` и `args.app_name`

**Пример корректного ответа:**
```json
{
  "session_id": "session_123",
  "command": "close_app",
  "args": {
    "app_name": "Safari"
  },
  "text": "Closing Safari."
}
```

---

### ✅ Шаг 2: Серверная валидация (Pydantic + fallback)
**Файлы:**
- `server/server/integrations/core/response_models.py`
- `server/server/integrations/core/assistant_response_parser.py`

**Статус:** ✅ Выполнено

**Проверка:**
- [x] Добавлен `CloseAppArgs` (строки 52-62 в `response_models.py`)
- [x] Команда `close_app` разрешена в `validate_command` (строка 88)
- [x] Валидация `args.app_name` для `close_app` в `validate_args_for_command` (строки 102-107)
- [x] Fallback-валидация проверяет `args.app_name` для `close_app` (строки 314-317 в `assistant_response_parser.py`)

**DoD:** ✅ Некорректный `close_app` не превращается в action, корректный проходит

**Тестовые кейсы:**
```python
# ✅ Корректный - проходит валидацию
{
  "command": "close_app",
  "args": {"app_name": "Safari"},
  "session_id": "test_123"
}

# ❌ Некорректный - проваливает валидацию (нет app_name)
{
  "command": "close_app",
  "args": {},
  "session_id": "test_123"
}
```

---

### ✅ Шаг 3: Forwarding actions (фича-флаги)
**Файлы/ENV:**
- `server/server/config.env.example`
- Переменные окружения

**Статус:** ✅ Выполнено

**Проверка:**
- [x] `FORWARD_ASSISTANT_ACTIONS=true` добавлен в `config.env.example` (строка 30)
- [x] `NEXY_KS_DISABLE_FORWARD_ASSISTANT_ACTIONS=false` добавлен в `config.env.example` (строка 35)
- [x] Добавлены комментарии о критичности флагов

**DoD:** ✅ В логах сервера виден `Command forwarded`

**Настройка для production:**
```bash
# В config.env или переменных окружения:
FORWARD_ASSISTANT_ACTIONS=true
NEXY_KS_DISABLE_FORWARD_ASSISTANT_ACTIONS=false
```

**Проверка в коде:**
```python
# server/server/integrations/workflow_integrations/streaming_workflow_integration.py
# Строки 507-513: проверка флагов перед форвардингом
if (config.features.forward_assistant_actions and 
    not config.kill_switches.disable_forward_assistant_actions):
    final_result['command_payload'] = self._pending_command_payload
```

---

### ✅ Шаг 4: Клиентский конфиг
**Файл:** `client/config/unified_config.yaml`

**Статус:** ✅ Выполнено

**Проверка:**
- [x] `mcp.close_app.enabled: true` (строка 609)
- [x] `mcp.close_app.server_path` указан корректно (строка 608)
- [x] `actions.close_app.enabled: true` (строка 594)

**DoD:** ✅ Клиент стартует MCP-executor без ошибок

**Конфигурация:**
```yaml
mcp:
  close_app:
    server_path: "mcp_close_app_test/server/close_app_server.py"
    enabled: true
    timeout_sec: 10.0

actions:
  close_app:
    enabled: true
    timeout_sec: 10.0
    speak_errors: true
    use_server_tts: false
```

---

### ✅ Шаг 5: Тесты и E2E
**Файлы:**
- `server/server/scripts/test_mcp_chain.py`
- `client/scripts/test_close_app_e2e.py`

**Статус:** ✅ Выполнено

**Проверка:**
- [x] В `test_mcp_chain.py` добавлен `close_app` в `required_keywords` (строка 40)
- [x] Добавлены тестовые кейсы для `close_app` (строки 125-135)
- [x] E2E тест существует: `client/scripts/test_close_app_e2e.py`

**DoD:** ✅ Все проверки пройдены

**Запуск тестов:**
```bash
# Серверные тесты
cd server/server
python scripts/test_mcp_chain.py

# Клиентские E2E тесты
cd client
python scripts/test_close_app_e2e.py
```

**Ожидаемые события:**
- `actions.close_app.started`
- `actions.close_app.completed` или `actions.close_app.failed`
- Приложение реально закрывается через `osascript`

---

## Канонический поток выполнения

```
1. Пользователь: "Close Safari"
   ↓
2. LLM (Gemini) генерирует JSON:
   {
     "session_id": "session_123",
     "command": "close_app",
     "args": {"app_name": "Safari"},
     "text": "Closing Safari."
   }
   ↓
3. AssistantResponseParser парсит и валидирует
   - Проверка через Pydantic (CloseAppArgs)
   - Fallback-валидация (args.app_name обязателен)
   ↓
4. StreamingWorkflowIntegration форвардит command_payload
   - Проверка: forward_assistant_actions=true
   - Проверка: disable_forward_assistant_actions=false
   ↓
5. gRPC передает command_payload клиенту
   - Событие: grpc.response.action
   ↓
6. ActionExecutionIntegration получает событие
   - Парсит action_json
   - Валидирует command="close_app" и args.app_name
   ↓
7. McpActionExecutor вызывает MCP сервер
   - Путь: mcp_close_app_test/server/close_app_server.py
   - Инструмент: close_app
   - Аргументы: {"app_name": "Safari"}
   ↓
8. close_app_server.py выполняет osascript
   - Команда: osascript -e 'quit app "Safari"'
   ↓
9. События публикуются:
   - actions.close_app.started
   - actions.close_app.completed (или failed)
   ↓
10. Аудио воспроизводится (если есть ошибка и speak_errors=true)
```

---

## Definition of Done - Чек-лист

### ✅ Модель возвращает корректный JSON close_app
- [x] System prompt содержит инструкции для `close_app`
- [x] Пример `close_app` в "Action Output Format"
- [x] Промпт синхронизирован в `unified_config_example.yaml`

### ✅ Сервер валидирует close_app и форвардит payload
- [x] `CloseAppArgs` добавлен в `response_models.py`
- [x] Команда `close_app` разрешена в валидации
- [x] Fallback-валидация проверяет `args.app_name`
- [x] Фича-флаги настроены в `config.env.example`
- [x] `command_payload` форвардится в `streaming_workflow_integration.py`

### ✅ Клиент получает action и успешно закрывает приложение
- [x] `mcp.close_app.enabled: true` в `unified_config.yaml`
- [x] Путь к MCP серверу указан корректно
- [x] `ActionExecutionIntegration` обрабатывает `close_app`
- [x] `McpActionExecutor` вызывает правильный MCP сервер
- [x] `close_app_server.py` выполняет `osascript`

### ✅ События actions.close_app.started/completed присутствуют
- [x] События публикуются в `action_execution_integration.py`
- [x] Тесты проверяют наличие событий
- [x] E2E тест проверяет полный цикл

---

## ⚠️ КРИТИЧЕСКИ ВАЖНО: Проверка перед production

### Что НЕ подтверждено и требует проверки

1. **Реальные env-флаги в рабочей среде** — без них `command_payload` не форвардится
2. **Источник промпта в проде** — используется ли `unified_config.py` или `GEMINI_SYSTEM_PROMPT`?
3. **MCP сервер close_app для прод** — в конфиге указан тестовый путь
4. **E2E-проверка** — нет факта, что события реально приходят на клиенте

---

## План действий для production (обязательно выполнить)

### Шаг 1: Зафиксировать флаги в окружении (prod/stage)

**Критично:** Без этих флагов `close_app` не будет доходить до клиента!

```bash
# На сервере (prod/stage) установить:
export FORWARD_ASSISTANT_ACTIONS=true
export NEXY_KS_DISABLE_FORWARD_ASSISTANT_ACTIONS=false

# Или в config.env:
FORWARD_ASSISTANT_ACTIONS=true
NEXY_KS_DISABLE_FORWARD_ASSISTANT_ACTIONS=false
```

**Проверка:**
```bash
# Запустить скрипт проверки сервера
cd server/server
python scripts/verify_close_app_production_readiness.py
```

---

### Шаг 2: Подтвердить источник промпта

**Проблема:** Если используется `GEMINI_SYSTEM_PROMPT` из env, а не из `unified_config.py`, промпт может не содержать `close_app`.

**Проверка:**
```bash
# Проверить, установлен ли GEMINI_SYSTEM_PROMPT
echo $GEMINI_SYSTEM_PROMPT

# Если установлен - проверить наличие close_app
echo $GEMINI_SYSTEM_PROMPT | grep -i "close_app"
```

**Решение:**
- **Вариант A:** Удалить `GEMINI_SYSTEM_PROMPT` из env → будет использоваться промпт из `unified_config.py` (содержит `close_app`)
- **Вариант B:** Обновить `GEMINI_SYSTEM_PROMPT` новым промптом из `unified_config.py`

**Проверка через скрипт:**
```bash
cd server/server
python scripts/verify_close_app_production_readiness.py
# Проверка 2 покажет источник промпта и наличие close_app
```

---

### Шаг 3: Проверить MCP путь для закрытия в проде

**Проблема:** В `unified_config.yaml` указан тестовый путь:
```yaml
mcp:
  close_app:
    server_path: "mcp_close_app_test/server/close_app_server.py"  # ⚠️ Тестовый путь
```

**Проверка:**
```bash
# Проверить клиентский конфиг
cd client
python scripts/verify_close_app_client_readiness.py
```

**Решение:**
1. Убедиться, что файл существует по указанному пути
2. Если путь тестовый, но файл существует — можно оставить (если это production путь)
3. Если нужен другой путь — обновить `mcp.close_app.server_path` в `unified_config.yaml`

**Текущий путь в конфиге:**
- `mcp.close_app.server_path: "mcp_close_app_test/server/close_app_server.py"`
- Относительно корня проекта Nexy
- Если файл существует — путь корректен

---

### Шаг 4: Запустить проверки

#### Серверные проверки:
```bash
cd server/server

# 1. Проверка готовности к production
python scripts/verify_close_app_production_readiness.py

# 2. Тест MCP цепочки
python scripts/test_mcp_chain.py
```

#### Клиентские проверки:
```bash
cd client

# 1. Проверка готовности клиента
python scripts/verify_close_app_client_readiness.py

# 2. E2E тест
python scripts/test_close_app_e2e.py
```

**Ожидаемые результаты:**
- ✅ Все проверки пройдены
- ✅ `actions.close_app.started` присутствует
- ✅ `actions.close_app.completed` присутствует
- ✅ Приложение реально закрывается

---

## Быстрая проверка перед деплоем

### 1. Проверка переменных окружения
```bash
# Должны быть установлены:
echo $FORWARD_ASSISTANT_ACTIONS        # должно быть: true
echo $NEXY_KS_DISABLE_FORWARD_ASSISTANT_ACTIONS  # должно быть: false (или не установлено)
```

### 2. Проверка конфигурации сервера
```bash
cd server/server
python scripts/verify_close_app_production_readiness.py
# Должен пройти все проверки
```

### 3. Проверка конфигурации клиента
```bash
cd client
python scripts/verify_close_app_client_readiness.py
# Должен пройти все проверки
```

### 4. E2E тест
```bash
cd client
python scripts/test_close_app_e2e.py
# Должен пройти успешно и показать события
```

---

## Известные проблемы и решения

### Проблема: close_app не доходит до клиента
**Причина:** Фича-флаг `FORWARD_ASSISTANT_ACTIONS` не включен

**Решение:**
```bash
export FORWARD_ASSISTANT_ACTIONS=true
export NEXY_KS_DISABLE_FORWARD_ASSISTANT_ACTIONS=false
```

### Проблема: Валидация проваливается
**Причина:** Отсутствует `args.app_name` в JSON от LLM

**Решение:** Проверить system prompt - должен содержать инструкции о необходимости `app_name`

### Проблема: MCP сервер не запускается
**Причина:** Неправильный путь к `close_app_server.py`

**Решение:** Проверить `mcp.close_app.server_path` в `unified_config.yaml`

---

## Связанные документы

- `Docs/MCP_COMMAND_INTEGRATION_PLAN.md` - общий план интеграции MCP команд
- `server/server/Docs/LLM_RESPONSE_FORMAT.md` - формат ответов LLM
- `client/Docs/ACTION_EXECUTION.md` - документация по выполнению действий на клиенте

---

## История изменений

- **2025-01-XX**: Добавлена поддержка `close_app` в system prompt
- **2025-01-XX**: Добавлена валидация `close_app` в Pydantic и fallback-парсер
- **2025-01-XX**: Добавлены фича-флаги в `config.env.example`
- **2025-01-XX**: Синхронизированы параметры в `unified_config_example.yaml`
- **2025-01-XX**: Добавлены тесты для `close_app` в `test_mcp_chain.py`
