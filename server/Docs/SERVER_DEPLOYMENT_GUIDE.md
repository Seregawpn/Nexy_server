# 🚀 РУКОВОДСТВО ПО ДЕПЛОЮ СЕРВЕРА НА AZURE

**Дата создания:** 1 октября 2025  
**Версия:** 2.2  
**Статус:** ✅ Активно используется  
**Последнее обновление:** 2 октября 2025 - Обновлен статус Azure VM, автоматического деплоя и системы мониторинга

---

## 📋 **ОБЯЗАТЕЛЬНЫЕ ТРЕБОВАНИЯ**

### **🔐 GitHub Secrets (КРИТИЧНО):**

**Должен быть настроен в** `https://github.com/Seregawpn/Nexy_server/settings/secrets/actions`:

**Секрет:** `AZURE_CREDENTIALS` (формат JSON)

**Структура секрета:**
```json
{
  "clientId": "YOUR_AZURE_CLIENT_ID",
  "clientSecret": "YOUR_AZURE_CLIENT_SECRET",
  "subscriptionId": "YOUR_AZURE_SUBSCRIPTION_ID",
  "tenantId": "YOUR_AZURE_TENANT_ID"
}
```

**📝 Примечание:** Реальные значения хранятся только в GitHub Secrets и локально. Никогда не коммитьте секреты в репозиторий.

**✅ Как получить реальные значения:**
1. Выполните локально: `cat /tmp/azure_credentials.json` (если сохраняли ранее)
2. Или используйте Azure CLI: `az ad sp show --id <client-id>`
3. Добавьте значения в GitHub Secrets как описано выше

### **📁 Структура файлов (ОБЯЗАТЕЛЬНО):**
```
nexy_new/server/          ← Исходный код
├── main.py              ← Основной файл сервера
├── modules/             ← Все модули (8 штук)
├── integrations/        ← Все интеграции
├── config/              ← Конфигурация
├── requirements.txt     ← Зависимости Python
├── .github/workflows/   ← GitHub Actions
└── Docs/                ← Документация
```

---

## 🔄 **ПОШАГОВАЯ ИНСТРУКЦИЯ ДЕПЛОЯ**

### **ШАГ 1: ПОДГОТОВКА (1-2 минуты)**

**1.1. Убедитесь, что изменения готовы:**
```bash
# Проверьте, что все изменения сохранены
cd /Users/sergiyzasorin/Library/Mobile\ Documents/com~apple~CloudDocs/Development/Nexy/server
git status
```

**1.2. Создайте временную директорию:**
```bash
cd /tmp
rm -rf nexy_server_temp  # Очистить, если существует
```

### **ШАГ 2: КЛОНИРОВАНИЕ РЕПОЗИТОРИЯ (30 секунд)**

```bash
# Клонируем серверный репозиторий
git clone https://github.com/Seregawpn/Nexy_server.git nexy_server_temp
cd nexy_server_temp
```

### **ШАГ 3: ОЧИСТКА И КОПИРОВАНИЕ (1 минута)**

```bash
# ОБЯЗАТЕЛЬНО: Очистить все старые файлы
rm -rf * .* 2>/dev/null || true

# ОБЯЗАТЕЛЬНО: Скопировать только серверные файлы
cp -r /Users/sergiyzasorin/Library/Mobile\ Documents/com~apple~CloudDocs/Development/Nexy/server/* .
# НЕ копируем скрытые файлы из корня проекта (они могут содержать клиентские данные)

**Что копируется:**
- ✅ `main.py` - основной файл сервера
- ✅ `modules/` - все 8 модулей сервера (text_processing, audio_generation, session_management, memory_management, interrupt_handling, text_filtering, update, grpc_service)
- ✅ `integrations/` - интеграции сервера
- ✅ `config/` - конфигурация сервера
- ✅ `requirements.txt` - зависимости
- ✅ `.github/` - GitHub Actions
- ✅ `Docs/` - серверная документация
- ✅ `monitoring/` - система мониторинга

**Что НЕ копируется:**
- ❌ `client/` - клиентская часть (остается в nexy_new)
- ❌ Скрытые файлы из корня проекта
- ❌ Клиентские конфигурации
```

### **ШАГ 4: НАСТРОЙКА GIT (30 секунд)**

```bash
# ОБЯЗАТЕЛЬНО: Инициализировать git
git init

# ОБЯЗАТЕЛЬНО: Добавить remote
git remote add origin https://github.com/Seregawpn/Nexy_server.git
```

### **ШАГ 5: COMMIT И PUSH (1 минута)**

```bash
# ОБЯЗАТЕЛЬНО: Добавить все файлы
git add .

# ОБЯЗАТЕЛЬНО: Commit с описательным сообщением
git commit -m "🚀 Обновление сервера: [ОПИСАНИЕ ИЗМЕНЕНИЙ]

- Дата: $(date '+%d.%m.%Y %H:%M')
- Изменения: [краткое описание]
- Модули: [список затронутых модулей]"

# ОБЯЗАТЕЛЬНО: Force push
git push origin main --force
```

### **ШАГ 6: ОЧИСТКА (10 секунд)**

```bash
# ОБЯЗАТЕЛЬНО: Очистить временную директорию
cd /tmp
rm -rf nexy_server_temp
```

---

## ⏱️ **АВТОМАТИЧЕСКИЙ ДЕПЛОЙ (2-3 минуты)**

После push в GitHub автоматически запускается:

### **🤖 GitHub Actions процесс:**
1. **Триггер:** Push в main ветку (изменения в `main.py`, `modules/**`, `integrations/**`, `config/**`, `requirements.txt`)
2. **Аутентификация:** GitHub Secrets + Azure Service Principal
3. **Команда:** `az vm run-command invoke` → `/home/azureuser/update-server.sh`
4. **Обновление:** 
   - `git stash` + `git clean` (очистка локальных изменений)
   - `git pull origin main` (получение обновлений)
   - `pip install -r requirements.txt` (установка зависимостей)
   - `systemctl restart voice-assistant.service` (перезапуск сервиса)
   - **Регенерация protobuf файлов** (при необходимости)
5. **Проверка:** Health checks + откат при ошибках

### **📊 Мониторинг деплоя:**
- **GitHub Actions:** `https://github.com/Seregawpn/Nexy_server/actions`
- **Health check:** `http://20.151.51.172/health`
- **Status API:** `http://20.151.51.172/status`

---

## ✅ **ПРОВЕРКА УСПЕШНОГО ДЕПЛОЯ**

### **1. Health Check:**
```bash
curl http://20.151.51.172/health
# Ожидаемый результат: "OK"
```

### **2. Status API:**
```bash
curl http://20.151.51.172/status
# Ожидаемый результат: JSON с информацией о сервисе
```

### **3. Проверка на сервере:**
```bash
# Проверить, что изменения применились
az vm run-command invoke \
  --resource-group Nexy \
  --name nexy-regular \
  --command-id RunShellScript \
  --scripts "
    cd /home/azureuser/voice-assistant
    git log --oneline -1
  "
```

---

## ⚠️ **КРИТИЧЕСКИЕ МОМЕНТЫ**

### **🚨 НЕ ДЕЛАЙТЕ:**
- ❌ Не клонируйте в существующую директорию
- ❌ Не забывайте очищать старые файлы
- ❌ Не используйте обычный push (только --force)
- ❌ Не оставляйте временные директории

### **✅ ОБЯЗАТЕЛЬНО:**
- ✅ Всегда используйте `/tmp` для временных файлов
- ✅ Всегда очищайте старые файлы перед копированием
- ✅ Всегда используйте описательные commit сообщения
- ✅ Всегда проверяйте health endpoint после деплоя

---

## 🔧 **УСТРАНЕНИЕ ПРОБЛЕМ**

### **Проблема: GitHub Actions не запускается**
**Решение:**
1. Проверить GitHub Secrets в настройках репозитория
2. Убедиться, что workflow файл в `.github/workflows/`
3. Проверить триггеры в workflow
4. Проверить, что GitHub Actions включен в Settings > Actions > General

### **Проблема: Деплой не завершается**
**Решение:**
1. Проверить логи GitHub Actions
2. Запустить обновление вручную на сервере:
```bash
az vm run-command invoke \
  --resource-group Nexy \
  --name nexy-regular \
  --command-id RunShellScript \
  --scripts "/home/azureuser/update-server.sh"
```

### **Проблема: Health check не проходит**
**Решение:**
1. Проверить статус сервиса на сервере
2. Посмотреть логи сервиса
3. Перезапустить сервис вручную

### **Проблема: Protobuf version mismatch**
**Ошибка:** `VersionError: Detected mismatched Protobuf Gencode/Runtime major versions`
**Решение:**
```bash
# На сервере выполнить:
cd /home/azureuser/voice-assistant
source venv/bin/activate
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. modules/grpc_service/streaming.proto
sudo systemctl restart voice-assistant.service
```

### **Проблема: Git pull не работает**
**Ошибка:** `fatal: refusing to merge unrelated histories` или локальные изменения
**Решение:**
```bash
# Скрипт автоматически решает эту проблему:
git stash  # Сохраняет локальные изменения
git clean -fd --exclude=venv/  # Очищает неотслеживаемые файлы
git pull origin main  # Получает обновления
```

### **Проблема: Сервис не запускается после обновления**
**Решение:**
1. Скрипт автоматически откатывается к предыдущему коммиту
2. Проверить логи сервиса:
```bash
sudo journalctl -u voice-assistant.service --no-pager -n 20
```
3. При необходимости регенерировать protobuf файлы

---

## 📊 **ВРЕМЕННЫЕ РАМКИ**

| Этап | Время | Описание |
|------|-------|----------|
| Подготовка | 1-2 мин | Проверка изменений |
| Клонирование | 30 сек | Скачивание репозитория |
| Копирование | 1 мин | Синхронизация файлов |
| Git операции | 1 мин | Commit и push |
| Очистка | 10 сек | Удаление временных файлов |
| **Автоматический деплой** | **2-3 мин** | **GitHub Actions → Azure** |
| **ИТОГО** | **5-7 мин** | **Полный цикл** |

---

## 🎯 **ПРИМЕРЫ COMMIT СООБЩЕНИЙ**

### **✅ ХОРОШИЕ ПРИМЕРЫ:**
```bash
git commit -m "🚀 Обновление сервера: исправление text_processing

- Дата: 01.10.2025 16:45
- Изменения: исправлена обработка длинных текстов
- Модули: text_processing, integrations"

git commit -m "🚀 Обновление сервера: добавление нового провайдера

- Дата: 01.10.2025 17:20
- Изменения: добавлен Azure TTS провайдер
- Модули: audio_generation, providers"
```

### **❌ ПЛОХИЕ ПРИМЕРЫ:**
```bash
git commit -m "update"
git commit -m "fix"
git commit -m "changes"
```

---

## 🛠️ **ДОПОЛНИТЕЛЬНЫЕ КОМАНДЫ ДЛЯ УПРАВЛЕНИЯ СЕРВЕРОМ**

### **Проверка статуса сервера:**
```bash
# Статус сервиса
az vm run-command invoke \
  --resource-group Nexy \
  --name nexy-regular \
  --command-id RunShellScript \
  --scripts "systemctl status voice-assistant.service"

# Health check
curl http://20.151.51.172/health

# Логи сервиса
az vm run-command invoke \
  --resource-group Nexy \
  --name nexy-regular \
  --command-id RunShellScript \
  --scripts "sudo journalctl -u voice-assistant.service --no-pager -n 20"
```

### **Ручное управление сервисом:**
```bash
# Перезапуск сервиса
az vm run-command invoke \
  --resource-group Nexy \
  --name nexy-regular \
  --command-id RunShellScript \
  --scripts "sudo systemctl restart voice-assistant.service"

# Остановка сервиса
az vm run-command invoke \
  --resource-group Nexy \
  --name nexy-regular \
  --command-id RunShellScript \
  --scripts "sudo systemctl stop voice-assistant.service"

# Запуск сервиса
az vm run-command invoke \
  --resource-group Nexy \
  --name nexy-regular \
  --command-id RunShellScript \
  --scripts "sudo systemctl start voice-assistant.service"
```

### **Проверка обновлений:**
```bash
# Проверить последний коммит на сервере
az vm run-command invoke \
  --resource-group Nexy \
  --name nexy-regular \
  --command-id RunShellScript \
  --scripts "cd /home/azureuser/voice-assistant && git log --oneline -1"

# Проверить статус git
az vm run-command invoke \
  --resource-group Nexy \
  --name nexy-regular \
  --command-id RunShellScript \
  --scripts "cd /home/azureuser/voice-assistant && git status"
```

---

## 🚀 **ГОТОВО К ИСПОЛЬЗОВАНИЮ**

**Следуйте этой инструкции для каждого обновления сервера.**

**При возникновении проблем - обращайтесь к разделу "Устранение проблем".**

**Автоматический деплой работает и включает в себя:**
- ✅ Автоматическую очистку локальных изменений
- ✅ Безопасное обновление кода
- ✅ Установку зависимостей
- ✅ Перезапуск сервиса
- ✅ Проверку работоспособности
- ✅ Автоматический откат при ошибках

---

**📞 Поддержка:** Документация в `Docs/` папке  
**🔗 Репозиторий:** `https://github.com/Seregawpn/Nexy_server`  
**🌐 Сервер:** `http://20.151.51.172`  
**📊 GitHub Actions:** `https://github.com/Seregawpn/Nexy_server/actions`

---

## 🚀 **СИСТЕМА ОБНОВЛЕНИЯ ПРИЛОЖЕНИЙ ЧЕРЕЗ GITHUB**

### **📋 Обзор процесса:**
1. **Упаковка** → создание DMG файла
2. **Деплой** → `scripts/deploy.sh Nexy.dmg`
3. **GitHub Release** → автоматическое создание релиза с тегом `Update`
4. **Azure сервер** → обновление манифеста и AppCast XML
5. **Клиенты** → получают обновления через GitHub CDN

### **🔧 Требования:**
- ✅ **GitHub CLI** (`brew install gh && gh auth login`)
- ✅ **Azure CLI** (`brew install azure-cli && az login`)
- ✅ **DMG файл** готов к загрузке
- ✅ **Права доступа** к репозиторию `Seregawpn/Nexy_production`
- ✅ **Права доступа** к Azure VM `nexy-regular`

### **🚀 Использование:**
```bash
# Развернуть обновление
cd scripts/
./deploy.sh ../Nexy.dmg
```

### **📊 Результат:**
- ✅ **GitHub релиз** создан с тегом `Update`
- ✅ **DMG файл** доступен по прямой ссылке через GitHub CDN
- ✅ **Azure сервер** обновлен с новой ссылкой
- ✅ **AppCast XML** обновлен автоматически
- ✅ **Клиенты** получают обновления через GitHub CDN
- ✅ **Проверка целостности** работает (SHA256)

### **🔗 Ссылки:**
- **📥 Скачать:** `https://github.com/Seregawpn/Nexy_production/releases/download/Update/Nexy.dmg`
- **📰 AppCast:** `http://20.151.51.172:8081/appcast.xml`
- **📋 Манифест:** `http://20.151.51.172:8081/manifests/manifest_1.0.0.json`
- **📁 Релиз:** `https://github.com/Seregawpn/Nexy_production/releases/tag/Update`
