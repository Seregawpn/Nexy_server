# Инструкция по деплою close_app в production

## ✅ Результаты проверок

### Readiness-скрипты

#### Серверный скрипт: ✅ Все проверки пройдены
```bash
cd /Users/sergiyzasorin/Fix_new
python3 server/server/scripts/verify_close_app_production_readiness.py --project-root /Users/sergiyzasorin/Fix_new
```

**Результаты:**
- ✅ PASS - Фича-флаги (FORWARD_ASSISTANT_ACTIONS=true, kill-switch выключен)
- ✅ PASS - Системный промпт (содержит close_app, используется unified_config.py)
- ✅ PASS - MCP сервер (файл существует, путь корректен)

#### Клиентский скрипт: ✅ Все проверки пройдены
```bash
cd /Users/sergiyzasorin/Fix_new/client
python3 scripts/verify_close_app_client_readiness.py --project-root /Users/sergiyzasorin/Fix_new
```

**Результаты:**
- ✅ PASS - MCP конфигурация (enabled: true, файл существует)
- ✅ PASS - ActionExecutionIntegration (поддерживает close_app)
- ✅ PASS - Actions конфигурация (enabled: true, параметры корректны)

### E2E тесты

#### test_mcp_chain.py: ✅ Все тесты пройдены
```bash
cd /Users/sergiyzasorin/Fix_new
python3 server/server/scripts/test_mcp_chain.py
```

**Результаты:**
- ✅ PASS - Промпт (содержит все ключевые слова, включая close_app)
- ✅ PASS - Фича-флаги
- ✅ PASS - Парсер ответов (корректно обрабатывает close_app)
- ✅ PASS - Извлечение ACTION
- ✅ PASS - Конфигурация

#### test_close_app_e2e.py: ✅ E2E тест пройден
```bash
cd /Users/sergiyzasorin/Fix_new
python3 client/scripts/test_close_app_e2e.py
```

**Результаты:**
- ✅ Событие `actions.close_app.started` получено
- ✅ Событие `actions.close_app.completed` получено
- ✅ Приложение успешно закрыто через MCP

---

## 🚀 Деплой в production

### Шаг 1: Фиксация env-переменных

**Критично:** Без этих переменных `close_app` не будет работать!

На сервере (prod/stage) установить:

```bash
# В config.env или через переменные окружения:
export FORWARD_ASSISTANT_ACTIONS=true
export NEXY_KS_DISABLE_FORWARD_ASSISTANT_ACTIONS=false
```

**Или в `config.env`:**
```bash
# =====================================================
# MCP ACTION FORWARDING (close_app/open_app)
# =====================================================
# ⚠️  ВАЖНО: Включено для production
# CRITICAL: Must be true for close_app/open_app to work
FORWARD_ASSISTANT_ACTIONS=true
# CRITICAL: Must be false for close_app/open_app to work
# If set to true, command forwarding will be disabled immediately
NEXY_KS_DISABLE_FORWARD_ASSISTANT_ACTIONS=false
```

### Шаг 2: Проверка источника промпта

**Проверка:**
```bash
# Убедиться, что GEMINI_SYSTEM_PROMPT не установлен (или содержит close_app)
echo $GEMINI_SYSTEM_PROMPT | grep -i "close_app"

# Если не содержит - удалить или обновить:
unset GEMINI_SYSTEM_PROMPT
# Будет использоваться промпт из unified_config.py (содержит close_app)
```

### Шаг 3: Проверка MCP сервера

**Проверка:**
```bash
# Убедиться, что файл существует
ls -la /path/to/Nexy/mcp_close_app_test/server/close_app_server.py

# Убедиться, что файл исполняемый
chmod +x /path/to/Nexy/mcp_close_app_test/server/close_app_server.py
```

### Шаг 4: Финальная проверка

**Запустить readiness-скрипты на production сервере:**
```bash
# Сервер
python3 server/server/scripts/verify_close_app_production_readiness.py --project-root /path/to/Nexy

# Клиент
python3 client/scripts/verify_close_app_client_readiness.py --project-root /path/to/Nexy
```

**Ожидаемый результат:** Все проверки ✅ PASS

---

## 📋 Чек-лист деплоя

### Перед деплоем:
- [ ] `FORWARD_ASSISTANT_ACTIONS=true` установлен в production env
- [ ] `NEXY_KS_DISABLE_FORWARD_ASSISTANT_ACTIONS=false` установлен в production env
- [ ] `GEMINI_SYSTEM_PROMPT` не установлен ИЛИ содержит `close_app`
- [ ] MCP сервер `close_app_server.py` существует и исполняемый
- [ ] `mcp.close_app.enabled: true` в `unified_config.yaml`
- [ ] `actions.close_app.enabled: true` в `unified_config.yaml`

### После деплоя:
- [ ] Readiness-скрипты пройдены (3/3 для сервера, 3/3 для клиента)
- [ ] E2E тесты пройдены
- [ ] В логах видны события `actions.close_app.started/completed`
- [ ] Приложение реально закрывается при запросе

---

## 🔍 Мониторинг

### Проверка логов сервера

**Ожидаемые логи:**
```
✅ Валидирован action-ответ через Pydantic: command=close_app, session_id=...
✅ Command forwarded в gRPC
```

### Проверка логов клиента

**Ожидаемые логи:**
```
✅ actions.close_app.started - session_id=...
✅ actions.close_app.completed - app_name=...
```

### Проверка выполнения

**Ожидаемое поведение:**
1. Пользователь: "Close Safari"
2. LLM генерирует JSON с `"command": "close_app"`
3. Сервер валидирует и форвардит `command_payload`
4. Клиент получает событие `grpc.response.action`
5. `ActionExecutionIntegration` обрабатывает команду
6. MCP сервер выполняет `osascript -e 'quit app "Safari"'`
7. События `actions.close_app.started/completed` публикуются
8. Приложение закрывается

---

## ⚠️ Известные ограничения

1. **Тестовый путь MCP сервера:** В конфиге указан путь `mcp_close_app_test/server/close_app_server.py`
   - Если это production путь - всё ок
   - Если нужен другой путь - обновить `mcp.close_app.server_path` в `unified_config.yaml`

2. **Идемпотентность:** Два одновременных запроса на закрытие одного приложения - второй игнорируется
   - Это ожидаемое поведение для предотвращения race conditions

---

## 📝 Связанные документы

- `Docs/CLOSE_APP_PRODUCTION_CHECKLIST.md` - детальный чек-лист
- `Docs/CLOSE_APP_E2E_IMPLEMENTATION_GUIDE.md` - полная техническая инструкция
- `Docs/CLOSE_APP_SAFETY_FIXES.md` - исправления безопасности
