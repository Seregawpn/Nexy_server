> [!WARNING] ARCHIVE NOTICE
> Этот документ архивный и не является source of truth.
> Актуальные каноны:
> - `server/Docs/SERVER_DEPLOYMENT_GUIDE.md` (деплой кода на удаленный сервер)
> - `server/Docs/RELEASE_AND_UPDATE_GUIDE.md` (публикация DMG/PKG и update-канал)
> - `server/Docs/DEPLOY_INCIDENT_RUNBOOK.md` (инциденты, зависимости, конфиги, rollback)

# 🚀 Развертывание на новом Azure аккаунте

**Дата создания:** $(date '+%d.%m.%Y')  
**Версия:** 1.0  
**Статус:** ✅ Готово к использованию

---

## 📋 Обзор

Это руководство описывает процесс полного развертывания Nexy Server на новом Azure аккаунте. Процесс автоматизирован через скрипты и включает:

1. Создание Azure инфраструктуры (Resource Group, VNet, Subnet, Public IP, NSG, VM)
2. Настройку сервера (Python, зависимости, systemd, Nginx)
3. Проверку всех требований

---

## 🔧 Предварительные требования

### Обязательные:
- ✅ Azure CLI установлен и авторизован (`az login`)
- ✅ Права на создание ресурсов в Azure подписке

### Опциональные:
- SSH ключ для безопасного доступа (рекомендуется)
- IP адрес для ограничения SSH доступа (рекомендуется)

---

## 🚀 Быстрый старт

### Вариант 1: Полное автоматическое развертывание (рекомендуется)

```bash
cd server/scripts
./deploy_new_azure_account.sh
```

Скрипт запросит все необходимые параметры и выполнит все шаги автоматически.

### Вариант 2: Пошаговое развертывание

#### Шаг 1: Создание инфраструктуры

```bash
cd server/scripts
./create_azure_infrastructure.sh
```

Или с параметрами:

```bash
export AZURE_RESOURCE_GROUP="Nexy"
export AZURE_LOCATION="eastus"
export AZURE_VM_NAME="nexy-regular"
export AZURE_VM_SIZE="Standard_B2s"
export AZURE_ADMIN_IP="YOUR_IP_ADDRESS"  # опционально
export AZURE_SSH_KEY_PATH="~/.ssh/azure_nexy_key"  # опционально

./create_azure_infrastructure.sh
```

#### Шаг 2: Настройка сервера

```bash
./setup_server.sh
```

Или с параметрами:

```bash
export AZURE_RESOURCE_GROUP="Nexy"
export AZURE_VM_NAME="nexy-regular"
export GITHUB_REPO="https://github.com/Seregawpn/Nexy_server.git"

./setup_server.sh
```

#### Шаг 3: Проверка развертывания

```bash
./verify_deployment.sh
```

---

## 📝 Детальное описание скриптов

### 1. `create_azure_infrastructure.sh`

Создает всю необходимую Azure инфраструктуру:

**Создаваемые ресурсы:**
- Resource Group
- Virtual Network (VNet) с Subnet
- Public IP (Static)
- Network Security Group (NSG) с правилами:
  - SSH (порт 22) - ограниченный или открытый
  - HTTP (порт 80) - публичный доступ
  - HTTPS (порт 443) - публичный доступ
- Network Interface (NIC)
- Virtual Machine (Ubuntu 22.04 LTS)

**Параметры (через переменные окружения):**
- `AZURE_RESOURCE_GROUP` - имя Resource Group (по умолчанию: `Nexy`)
- `AZURE_LOCATION` - регион Azure (по умолчанию: `eastus`)
- `AZURE_VM_NAME` - имя VM (по умолчанию: `nexy-regular`)
- `AZURE_VM_SIZE` - размер VM (по умолчанию: `Standard_B2s` - 2 vCPU, 4 GB RAM)
- `AZURE_DISK_SIZE` - размер диска в GB (по умолчанию: `64`)
- `AZURE_ADMIN_IP` - IP адрес для ограничения SSH (опционально)
- `AZURE_SSH_KEY_PATH` - путь к SSH ключу (опционально)

**Пример использования:**

```bash
export AZURE_RESOURCE_GROUP="Nexy"
export AZURE_LOCATION="eastus"
export AZURE_VM_NAME="nexy-regular"
export AZURE_VM_SIZE="Standard_B2s"
export AZURE_ADMIN_IP="1.2.3.4"  # Ваш IP адрес

./create_azure_infrastructure.sh
```

### 2. `setup_server.sh`

Настраивает сервер после создания VM:

**Выполняемые действия:**
1. Обновление системы
2. Установка Python 3.11
3. Установка Nginx
4. Клонирование репозитория
5. Создание virtual environment и установка зависимостей
6. Создание необходимых директорий (`updates/downloads`, `updates/keys`, `updates/manifests`)
7. Генерация SSL сертификатов (self-signed)
8. Настройка Nginx конфигурации
9. Создание systemd сервиса `voice-assistant.service`
10. Создание скрипта обновления `/home/azureuser/update-server.sh`
11. Запуск сервиса

**Параметры (через переменные окружения):**
- `AZURE_RESOURCE_GROUP` - имя Resource Group (по умолчанию: `Nexy`)
- `AZURE_VM_NAME` - имя VM (по умолчанию: `nexy-regular`)
- `AZURE_ADMIN_USERNAME` - имя пользователя (по умолчанию: `azureuser`)
- `GITHUB_REPO` - URL репозитория (по умолчанию: `https://github.com/Seregawpn/Nexy_server.git`)

**Пример использования:**

```bash
export AZURE_RESOURCE_GROUP="Nexy"
export AZURE_VM_NAME="nexy-regular"

./setup_server.sh
```

### 3. `verify_deployment.sh`

Проверяет все требования из `SERVER_REISSUE_REQUIREMENTS.md`:

**Проверки:**
1. ✅ HTTPS health endpoint (`/health`) - доступен и возвращает JSON
2. ✅ HTTPS status endpoint (`/status`) - доступен и возвращает JSON
3. ✅ Update health endpoint (`/updates/health`) - доступен
4. ✅ Cache-Control headers:
   - `/appcast.xml` → `max-age=60`
   - `/updates/health` → `max-age=30`
   - `/health` → `max-age=30`
5. ✅ Внутренние порты недоступны извне:
   - 50051 (gRPC)
   - 8080 (HTTP health)
   - 8081 (Update server)
6. ✅ gRPC smoke test (опционально)
7. ✅ Systemd сервис активен
8. ✅ Nginx конфигурация валидна

**Параметры (через переменные окружения):**
- `AZURE_RESOURCE_GROUP` - имя Resource Group (по умолчанию: `Nexy`)
- `AZURE_VM_NAME` - имя VM (по умолчанию: `nexy-regular`)

**Пример использования:**

```bash
export AZURE_RESOURCE_GROUP="Nexy"
export AZURE_VM_NAME="nexy-regular"

./verify_deployment.sh
```

### 4. `deploy_new_azure_account.sh`

Главный скрипт, объединяющий все шаги:

1. Проверка предварительных требований
2. Запрос параметров у пользователя
3. Выполнение всех трех скриптов последовательно
4. Вывод итоговой информации

**Пример использования:**

```bash
./deploy_new_azure_account.sh
```

---

## 🔄 Обновление сервера

После развертывания обновления можно применять вручную через скрипт на сервере:

```bash
# Подключение к серверу
ssh azureuser@<PUBLIC_IP>

# Запуск скрипта обновления
/home/azureuser/update-server.sh
```

Или удаленно через Azure CLI:

```bash
az vm run-command invoke \
  --resource-group Nexy \
  --name nexy-regular \
  --command-id RunShellScript \
  --scripts "/home/azureuser/update-server.sh"
```

**Примечание:** Автоматический деплой через GitHub Actions не настроен в рамках текущей задачи и может быть настроен позже при необходимости.

---

## ⚙️ Настройка config.env

После развертывания необходимо настроить API ключи:

```bash
# Подключение к серверу
ssh azureuser@<PUBLIC_IP>

# Редактирование config.env
cd /home/azureuser/voice-assistant/server
nano config.env
```

**Необходимые переменные:**
- `GEMINI_API_KEY` - ключ для Google Gemini API
- `AZURE_SPEECH_KEY` - ключ для Azure Speech Services (опционально)
- `AZURE_SPEECH_REGION` - регион Azure Speech Services (опционально)

После настройки перезапустите сервис:

```bash
sudo systemctl restart voice-assistant.service
```

---

## 🔍 Проверка работоспособности

### Health Check

```bash
curl -sk https://<PUBLIC_IP>/health
```

Ожидаемый ответ:
```json
{
  "status": "ok",
  "latest_version": "1.0.2",
  "latest_build": "1.0.2"
}
```

### Status API

```bash
curl -sk https://<PUBLIC_IP>/status
```

### Update Health

```bash
curl -sk https://<PUBLIC_IP>/updates/health
```

---

## 🛠️ Устранение проблем

### Проблема: VM не создается

**Решение:**
1. Проверьте права доступа в Azure подписке
2. Проверьте квоты на создание VM в регионе
3. Попробуйте другой регион или размер VM

### Проблема: Сервис не запускается

**Решение:**
1. Проверьте логи:
```bash
az vm run-command invoke \
  --resource-group Nexy \
  --name nexy-regular \
  --command-id RunShellScript \
  --scripts "sudo journalctl -u voice-assistant.service -n 50"
```

2. Проверьте config.env на наличие ошибок
3. Проверьте зависимости:
```bash
az vm run-command invoke \
  --resource-group Nexy \
  --name nexy-regular \
  --command-id RunShellScript \
  --scripts "cd /home/azureuser/voice-assistant && source venv/bin/activate && pip list"
```

### Проблема: Health endpoint недоступен

**Решение:**
1. Проверьте статус Nginx:
```bash
az vm run-command invoke \
  --resource-group Nexy \
  --name nexy-regular \
  --command-id RunShellScript \
  --scripts "sudo systemctl status nginx"
```

2. Проверьте конфигурацию Nginx:
```bash
az vm run-command invoke \
  --resource-group Nexy \
  --name nexy-regular \
  --command-id RunShellScript \
  --scripts "sudo nginx -t"
```

3. Проверьте, что `/health` и `/status` расположены ПЕРЕД `/` в конфигурации Nginx

### Проблема: Внутренние порты доступны извне

**Решение:**
1. Проверьте NSG правила:
```bash
az network nsg rule list \
  --resource-group Nexy \
  --nsg-name nexy-nsg \
  --output table
```

2. Убедитесь, что нет правил, открывающих порты 50051, 8080, 8081 для внешнего доступа

---

## 📊 Мониторинг

### Статус сервиса

```bash
az vm run-command invoke \
  --resource-group Nexy \
  --name nexy-regular \
  --command-id RunShellScript \
  --scripts "sudo systemctl status voice-assistant.service"
```

### Логи сервиса

```bash
az vm run-command invoke \
  --resource-group Nexy \
  --name nexy-regular \
  --command-id RunShellScript \
  --scripts "sudo journalctl -u voice-assistant.service -n 50 --no-pager"
```

### Использование ресурсов

```bash
az vm run-command invoke \
  --resource-group Nexy \
  --name nexy-regular \
  --command-id RunShellScript \
  --scripts "top -bn1 | head -20"
```

---

## 🔄 Обновление сервера

Обновления применяются вручную через скрипт на сервере.

Для обновления:

```bash
az vm run-command invoke \
  --resource-group Nexy \
  --name nexy-regular \
  --command-id RunShellScript \
  --scripts "/home/azureuser/update-server.sh"
```

---

## 📚 Дополнительные ресурсы

- [SERVER_REISSUE_REQUIREMENTS.md](./SERVER_REISSUE_REQUIREMENTS.md) - канонический чеклист требований
- [SERVER_DEPLOYMENT_GUIDE.md](./SERVER_DEPLOYMENT_GUIDE.md) - руководство по деплою
- [ARCHITECTURE_OVERVIEW.md](./ARCHITECTURE_OVERVIEW.md) - архитектурный обзор
- [SCALING_100_USERS_GUIDE.md](../SCALING_100_USERS_GUIDE.md) - масштабирование

---

## ✅ Чеклист развертывания

- [ ] Azure CLI установлен и авторизован
- [ ] Инфраструктура создана (`create_azure_infrastructure.sh`)
- [ ] Сервер настроен (`setup_server.sh`)
- [ ] Все проверки пройдены (`verify_deployment.sh`)
- [ ] `config.env` настроен с API ключами
- [ ] Health endpoints доступны
- [ ] Внутренние порты недоступны извне
- [ ] Cache-Control headers правильные
- [ ] Systemd сервис активен
- [ ] Nginx конфигурация валидна
- [ ] SSH доступ ограничен (рекомендуется)

---

**Готово к использованию! 🚀**
