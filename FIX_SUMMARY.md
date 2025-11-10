# Резюме исправлений для проблемы 502 Bad Gateway

**Дата:** 2 октября 2025

---

## 🔍 **Найденные проблемы**

### **1. Критическая ошибка: `name 'get_config' is not defined`**

**Проблема:**
- В `grpc_server.py` используется `get_config()` без импорта
- Сервер падает при инициализации и cleanup
- Сервис постоянно перезапускается (auto-restart)

**Местоположение:**
- Файл: `server/modules/grpc_service/core/grpc_server.py`
- Строка: 75 (в `__init__` методе `NewStreamingServicer`)

**Решение:**
- ✅ Добавлен импорт `from config.unified_config import get_config` в начало файла
- ✅ Импорт добавлен после других импортов, перед определением класса

**Код исправления:**
```python
# Импорт unified_config для доступа к конфигурации
sys.path.append(os.path.join(os.path.dirname(__file__), '../../..'))
from config.unified_config import get_config
```

---

### **2. Проблема с правами доступа: `Permission denied: '/home/azureuser/voice-assistant/server/updates/downloads'`**

**Проблема:**
- Update Server не может создать директорию `updates/downloads`
- Ошибка: `[Errno 13] Permission denied`
- Update Server не запускается (но это не критично, сервер может работать без него)

**Местоположение:**
- Файл: `server/modules/update/config.py`
- Метод: `__post_init__` (строка 61)

**Решение:**
- Нужно создать директории заранее с правильными правами
- Или обработать ошибку Permission denied (Update Server не критичен)

**Рекомендация:**
- Создать директории на сервере с правильными правами:
  ```bash
  sudo mkdir -p /home/azureuser/voice-assistant/server/updates/{downloads,keys,manifests}
  sudo chown -R azureuser:azureuser /home/azureuser/voice-assistant/server/updates
  ```

---

## ✅ **Что исправлено**

1. ✅ **Импорт `get_config`** в `grpc_server.py`
   - Добавлен импорт `from config.unified_config import get_config`
   - Исправлена критическая ошибка, которая вызывала падение сервера

---

## 📋 **Что нужно сделать на сервере**

### **Шаг 1: Закоммитить исправление**

```bash
git add server/modules/grpc_service/core/grpc_server.py
git commit -m "fix: add missing get_config import in grpc_server.py

- Добавлен импорт get_config из config.unified_config
- Исправлена критическая ошибка 'name get_config is not defined'
- Сервер теперь может корректно инициализироваться и выполнять cleanup"
```

### **Шаг 2: Задеплоить на сервер**

```bash
git push origin main
# Или использовать GitHub Actions для автоматического деплоя
```

### **Шаг 3: Исправить права доступа на сервере**

```bash
# Подключиться к серверу через SSH или Azure CLI
az vm run-command invoke \
  --resource-group Nexy \
  --name nexy-regular \
  --command-id RunShellScript \
  --scripts "
    cd /home/azureuser/voice-assistant
    sudo mkdir -p server/updates/{downloads,keys,manifests}
    sudo chown -R azureuser:azureuser server/updates
    sudo chmod -R 755 server/updates
  "
```

### **Шаг 4: Перезапустить сервис**

```bash
az vm run-command invoke \
  --resource-group Nexy \
  --name nexy-regular \
  --command-id RunShellScript \
  --scripts "sudo systemctl restart voice-assistant.service"
```

### **Шаг 5: Проверить статус**

```bash
# Проверить статус сервиса
az vm run-command invoke \
  --resource-group Nexy \
  --name nexy-regular \
  --command-id RunShellScript \
  --scripts "sudo systemctl status voice-assistant.service --no-pager -l | head -20"

# Проверить health endpoint
curl -sk https://20.151.51.172/health
```

---

## 🎯 **Ожидаемый результат**

После исправления:
- ✅ Сервис должен запуститься без ошибок
- ✅ Health endpoint должен отвечать корректно
- ✅ Публичный endpoint должен вернуть JSON вместо 502
- ✅ gRPC сервер должен работать корректно

---

## 📝 **Примечания**

1. **Update Server не критичен** - если он не запустится, основной сервер все равно будет работать
2. **Права доступа** - можно исправить позже, это не блокирует работу основного сервера
3. **Импорт `get_config`** - это критическое исправление, без него сервер не может работать

