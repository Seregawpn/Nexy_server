# 📋 Следующие шаги для развертывания

**Дата:** 02.01.2025  
**Статус:** Готово к развертыванию

---

## ✅ Что уже готово

- ✅ Скрипты для создания инфраструктуры
- ✅ Скрипты для настройки сервера
- ✅ Скрипты для проверки развертывания
- ✅ Документация
- ✅ Все файлы имеют права на выполнение

---

## 🔗 Доступ к серверу (Актуальные данные)

**⚠️ Важно:** Эти данные актуальны на момент развертывания. Если IP изменится, обновите этот раздел.

### Параметры сервера

- **Resource Group:** `NetworkWatcherRG`
- **VM Name:** `Nexy`
- **Location:** `canadacentral`
- **Public IP:** `20.63.24.187`
- **OS:** Ubuntu 24.04 LTS
- **Size:** Standard_D2s_v3 (2 vCPU, 8 GB RAM)
- **Admin Username:** `azureuser`

### SSH подключение

```bash
ssh azureuser@20.63.24.187
```

### Health Endpoints

```bash
# Health Check
curl -sk https://20.63.24.187/health

# Status API
curl -sk https://20.63.24.187/status

# Update Health
curl -sk https://20.63.24.187/updates/health

# AppCast
curl -sk https://20.63.24.187/appcast.xml
```

### Управление сервисом

```bash
# Подключение к серверу
ssh azureuser@20.63.24.187

# Статус сервиса
sudo systemctl status voice-assistant.service

# Перезапуск сервиса
sudo systemctl restart voice-assistant.service

# Логи сервиса
sudo journalctl -u voice-assistant.service -n 50 --no-pager

# Проверка Nginx
sudo systemctl status nginx
sudo nginx -t
```

### Конфигурация

**Файл конфигурации:** `/home/azureuser/voice-assistant/server/config.env`

**Редактирование:**
```bash
ssh azureuser@20.63.24.187
cd /home/azureuser/voice-assistant/server
nano config.env
sudo systemctl restart voice-assistant.service
```

**Необходимые переменные:**
```bash
# Обязательные
GEMINI_API_KEY=your_gemini_api_key_here

# Опциональные (для Azure Speech)
AZURE_SPEECH_KEY=your_azure_speech_key
AZURE_SPEECH_REGION=your_azure_region

# Окружение
NEXY_ENV=prod
```

### Удаленное управление через Azure CLI

```bash
# Статус сервиса
az vm run-command invoke \
  --resource-group NetworkWatcherRG \
  --name Nexy \
  --command-id RunShellScript \
  --scripts "sudo systemctl status voice-assistant.service"

# Логи сервиса
az vm run-command invoke \
  --resource-group NetworkWatcherRG \
  --name Nexy \
  --command-id RunShellScript \
  --scripts "sudo journalctl -u voice-assistant.service -n 50 --no-pager"

# Перезапуск сервиса
az vm run-command invoke \
  --resource-group NetworkWatcherRG \
  --name Nexy \
  --command-id RunShellScript \
  --scripts "sudo systemctl restart voice-assistant.service"
```

**Примечание:** Если IP адрес изменится, обновите этот раздел и клиентскую конфигурацию.

---

## 🚀 План действий

### ШАГ 1: Проверка предварительных требований

**1.1. Проверка Azure CLI:**

```bash
# Проверка установки
az --version

# Проверка авторизации
az account show

# Если не авторизован:
az login
```

**1.2. Выбор подписки (если несколько):**

```bash
# Список подписок
az account list --output table

# Выбор подписки
az account set --subscription "YOUR_SUBSCRIPTION_ID"
```

**1.3. Проверка прав доступа:**

Убедитесь, что у вас есть права на создание:
- Resource Groups
- Virtual Networks
- Public IPs
- Network Security Groups
- Virtual Machines

**1.4. Подготовка параметров (опционально):**

```bash
# Ваш IP адрес для ограничения SSH (рекомендуется)
MY_IP=$(curl -s ifconfig.me)
echo "Ваш IP: $MY_IP"

# SSH ключ (если есть)
ls -la ~/.ssh/id_rsa.pub
```

---

### ШАГ 2: Запуск развертывания

**Вариант A: Полностью автоматическое развертывание (рекомендуется)**

```bash
cd server/scripts
./deploy_new_azure_account.sh
```

Скрипт запросит:
- Resource Group name [по умолчанию: NetworkWatcherRG]
- Azure Location [по умолчанию: canadacentral]
- VM Name [по умолчанию: Nexy]
- VM Size [по умолчанию: Standard_D2s_v3]
- Admin IP для SSH [опционально]
- SSH Key Path [опционально]

**Примечание:** Текущая VM уже создана с параметрами выше. Если создаете новую, используйте эти значения.

**Вариант B: Пошаговое развертывание**

```bash
cd server/scripts

# Шаг 1: Создание инфраструктуры
export AZURE_RESOURCE_GROUP="NetworkWatcherRG"
export AZURE_LOCATION="canadacentral"
export AZURE_VM_NAME="Nexy"
export AZURE_VM_SIZE="Standard_D2s_v3"
export AZURE_ADMIN_IP="YOUR_IP_ADDRESS"  # опционально
./create_azure_infrastructure.sh

**Примечание:** Текущая VM уже создана. Эти команды для создания новой VM.

# Шаг 2: Настройка сервера (подождите 30 секунд после шага 1)
./setup_server.sh

# Шаг 3: Проверка развертывания
./verify_deployment.sh
```

---

### ШАГ 3: Настройка config.env

После успешного развертывания необходимо настроить API ключи:

**3.1. Получение Public IP:**

```bash
# Из скрипта или вручную
az vm show \
  --resource-group NetworkWatcherRG \
  --name Nexy \
  --show-details \
  --query "publicIps" -o tsv
```

**Актуальный Public IP:** `20.63.24.187` (см. раздел "Доступ к серверу" выше)

**3.2. Подключение к серверу:**

```bash
ssh azureuser@20.63.24.187
```

**3.3. Настройка config.env:**

```bash
cd /home/azureuser/voice-assistant/server
nano config.env
```

**Необходимые переменные:**
```bash
# Обязательные
GEMINI_API_KEY=your_gemini_api_key_here

# Опциональные (для Azure Speech)
AZURE_SPEECH_KEY=your_azure_speech_key
AZURE_SPEECH_REGION=your_azure_region

# Окружение
NEXY_ENV=prod
```

**3.4. Перезапуск сервиса:**

```bash
sudo systemctl restart voice-assistant.service
sudo systemctl status voice-assistant.service
```

---

### ШАГ 4: Проверка работоспособности

**4.1. Health Check:**

```bash
curl -sk https://20.63.24.187/health
```

Ожидаемый ответ:
```json
{
  "status": "ok",
  "latest_version": "1.0.2",
  "latest_build": "1.0.2"
}
```

**4.2. Status API:**

```bash
curl -sk https://20.63.24.187/status
```

**4.3. Update Health:**

```bash
curl -sk https://20.63.24.187/updates/health
```

**4.4. Проверка Cache-Control headers:**

```bash
# AppCast
curl -sI https://20.63.24.187/appcast.xml | grep -i "cache-control"
# Должно быть: max-age=60

# Health
curl -sI https://20.63.24.187/health | grep -i "cache-control"
# Должно быть: max-age=30
```

**4.5. Проверка безопасности (внутренние порты недоступны):**

```bash
# Должны вернуть ошибку подключения или таймаут
curl -v http://20.63.24.187:50051  # gRPC - должен быть недоступен
curl -v http://20.63.24.187:8080/health  # HTTP health - должен быть недоступен
curl -v http://20.63.24.187:8081/health  # Update server - должен быть недоступен
```

---

### ШАГ 5: Дополнительная настройка (опционально)

**5.1. Ограничение SSH доступа:**

Если при создании не указали Admin IP, можно обновить NSG правило:

```bash
# Получить ваш текущий IP
MY_IP=$(curl -s ifconfig.me)

# Обновить NSG правило
az network nsg rule update \
  --resource-group NetworkWatcherRG \
  --nsg-name Nexy-nsg \
  --name AllowSSH \
  --source-address-prefixes "$MY_IP"
```

**5.2. Настройка мониторинга:**

```bash
# Проверка статуса сервиса
az vm run-command invoke \
  --resource-group NetworkWatcherRG \
  --name Nexy \
  --command-id RunShellScript \
  --scripts "sudo systemctl status voice-assistant.service"

# Просмотр логов
az vm run-command invoke \
  --resource-group NetworkWatcherRG \
  --name Nexy \
  --command-id RunShellScript \
  --scripts "sudo journalctl -u voice-assistant.service -n 50 --no-pager"
```

**5.3. Обновление IP в клиентской конфигурации:**

Если IP адрес изменился, обновите его в клиентской конфигурации.

---

## 🔍 Устранение проблем

### Проблема: Azure CLI не установлен

**Решение:**
```bash
# macOS
brew install azure-cli

# Linux
curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash

# Затем авторизация
az login
```

### Проблема: Недостаточно прав в Azure

**Решение:**
- Обратитесь к администратору подписки
- Требуются права: Contributor или Owner

### Проблема: VM не создается (квота)

**Решение:**
```bash
# Проверка квот
az vm list-usage --location canadacentral --output table

# Попробуйте другой регион или меньший размер VM
export AZURE_LOCATION="westus"
export AZURE_VM_SIZE="Standard_D2s_v3"
```

### Проблема: Health endpoint не отвечает

**Решение:**
1. Проверьте статус сервиса:
```bash
ssh azureuser@20.63.24.187
sudo systemctl status voice-assistant.service
```

2. Проверьте логи:
```bash
sudo journalctl -u voice-assistant.service -n 50
```

3. Проверьте Nginx:
```bash
sudo systemctl status nginx
sudo nginx -t
```

4. Проверьте config.env на ошибки

---

## 📊 Чеклист готовности

Перед запуском убедитесь:

- [ ] Azure CLI установлен и авторизован
- [ ] Выбрана правильная подписка
- [ ] Есть права на создание ресурсов
- [ ] Знаете ваш IP адрес (для ограничения SSH)
- [ ] Есть API ключи (Gemini, Azure Speech - опционально)
- [ ] Готовы потратить 15-20 минут на развертывание

---

## 🎯 Быстрый старт (копипаста)

```bash
# 1. Проверка Azure CLI
az account show || az login

# 2. Переход в директорию скриптов
cd server/scripts

# 3. Запуск автоматического развертывания
./deploy_new_azure_account.sh

# 4. После завершения - настройка config.env
# ssh azureuser@20.63.24.187
# cd /home/azureuser/voice-assistant/server
# nano config.env
# sudo systemctl restart voice-assistant.service

# 5. Проверка
# curl -sk https://20.63.24.187/health
```

---

## 📚 Дополнительные ресурсы

- [AZURE_NEW_ACCOUNT_DEPLOYMENT.md](./AZURE_NEW_ACCOUNT_DEPLOYMENT.md) - детальное руководство
- [AZURE_DEPLOYMENT_OPTIONS.md](./AZURE_DEPLOYMENT_OPTIONS.md) - варианты решения
- [SERVER_REISSUE_REQUIREMENTS.md](./SERVER_REISSUE_REQUIREMENTS.md) - канонический чеклист

---

**Готовы начать? Запустите: `cd server/scripts && ./deploy_new_azure_account.sh` 🚀**
