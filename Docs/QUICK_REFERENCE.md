# 🚀 БЫСТРАЯ СПРАВКА - NEXY AI ASSISTANT

**Дата создания:** 4 октября 2025  
**Назначение:** Быстрый доступ к основным командам и процедурам

---

## 🔍 **ДИАГНОСТИКА СЕРВЕРА**

### **Проверка статуса всех сервисов:**
```bash
# Health endpoints
curl -s http://20.151.51.172/health
curl -s http://20.151.51.172/status
curl -s http://20.151.51.172:8081/health

# AppCast
curl -s http://20.151.51.172:8081/appcast.xml
```

### **Проверка через Azure CLI:**
```bash
# Статус сервиса
az vm run-command invoke \
  --resource-group Nexy \
  --name nexy-regular \
  --command-id RunShellScript \
  --scripts "sudo systemctl status voice-assistant.service --no-pager -l | head -10"

# Активные порты
az vm run-command invoke \
  --resource-group Nexy \
  --name nexy-regular \
  --command-id RunShellScript \
  --scripts "ss -tlnp | grep -E ':(8080|8081|50051)'"

# Последние логи
az vm run-command invoke \
  --resource-group Nexy \
  --name nexy-regular \
  --command-id RunShellScript \
  --scripts "sudo journalctl -u voice-assistant.service --no-pager -n 20"
```

---

## 🔧 **ОБНОВЛЕНИЕ СЕРВЕРА**

### **Локальная синхронизация:**
```bash
cd /Users/sergiyzasorin/Development/Nexy/server
git add .
git commit -m "feat: Description of changes"
git push origin main
```

### **Production обновление:**
```bash
az vm run-command invoke \
  --resource-group Nexy \
  --name nexy-regular \
  --command-id RunShellScript \
  --scripts "
cd /home/azureuser/voice-assistant
git pull origin main
sudo systemctl restart voice-assistant.service
sleep 5
sudo systemctl status voice-assistant.service --no-pager -l | head -5
"
```

---

## 🛠️ **ИСПРАВЛЕНИЕ ПРОБЛЕМ**

### **TextProcessor не инициализирован:**
```bash
# Проверить config.env
az vm run-command invoke \
  --resource-group Nexy \
  --name nexy-regular \
  --command-id RunShellScript \
  --scripts "cd /home/azureuser/voice-assistant && grep GEMINI_API_KEY config.env"

# Перезапустить сервис
az vm run-command invoke \
  --resource-group Nexy \
  --name nexy-regular \
  --command-id RunShellScript \
  --scripts "sudo systemctl restart voice-assistant.service"
```

### **Update сервер не работает:**
```bash
# Проверить права доступа
az vm run-command invoke \
  --resource-group Nexy \
  --name nexy-regular \
  --command-id RunShellScript \
  --scripts "
cd /home/azureuser/voice-assistant
sudo chown -R root:root updates/
sudo chmod -R 755 updates/
ls -la updates/manifests/
"

# Проверить файлы манифестов
az vm run-command invoke \
  --resource-group Nexy \
  --name nexy-regular \
  --command-id RunShellScript \
  --scripts "ls -la /home/azureuser/voice-assistant/updates/manifests/"
```

### **Порт недоступен:**
```bash
# Проверить UFW firewall
az vm run-command invoke \
  --resource-group Nexy \
  --name nexy-regular \
  --command-id RunShellScript \
  --scripts "sudo ufw status"

# Открыть порт в UFW
az vm run-command invoke \
  --resource-group Nexy \
  --name nexy-regular \
  --command-id RunShellScript \
  --scripts "sudo ufw allow 8081/tcp"

# Проверить Azure NSG
az network nsg rule list --resource-group Nexy --nsg-name nexy-regular-nsg
```

---

## 📊 **МОНИТОРИНГ**

### **Логи в реальном времени:**
```bash
az vm run-command invoke \
  --resource-group Nexy \
  --name nexy-regular \
  --command-id RunShellScript \
  --scripts "
sudo journalctl -u voice-assistant.service -f --since '1 minute ago' | grep -E '(ERROR|WARNING|INFO)' &
MONITOR_PID=\$!
sleep 30
kill \$MONITOR_PID 2>/dev/null
"
```

### **Проверка производительности:**
```bash
az vm run-command invoke \
  --resource-group Nexy \
  --name nexy-regular \
  --command-id RunShellScript \
  --scripts "
echo 'Memory usage:'
free -h
echo 'CPU usage:'
top -bn1 | grep 'Cpu(s)'
echo 'Disk usage:'
df -h /
"
```

---

## 🔐 **БЕЗОПАСНОСТЬ**

### **Проверка прав доступа:**
```bash
az vm run-command invoke \
  --resource-group Nexy \
  --name nexy-regular \
  --command-id RunShellScript \
  --scripts "
cd /home/azureuser/voice-assistant
echo 'File ownership:'
ls -la config.env
ls -la updates/manifests/
echo 'Service user:'
ps aux | grep python | grep voice-assistant
"
```

### **Исправление прав:**
```bash
az vm run-command invoke \
  --resource-group Nexy \
  --name nexy-regular \
  --command-id RunShellScript \
  --scripts "
cd /home/azureuser/voice-assistant
sudo chown -R root:root .
sudo chmod -R 755 .
sudo chmod 644 config.env
"
```

---

## 🌐 **СЕТЬ**

### **Проверка сетевого доступа:**
```bash
# Локальный доступ
az vm run-command invoke \
  --resource-group Nexy \
  --name nexy-regular \
  --command-id RunShellScript \
  --scripts "
curl -s localhost:8080/health
curl -s localhost:8081/health
curl -s localhost:50051 || echo 'gRPC port check'
"

# Внешний доступ
curl -s http://20.151.51.172/health
curl -s http://20.151.51.172:8081/health
```

### **Открытие портов в Azure NSG:**
```bash
# Добавить правило для нового порта
az network nsg rule create \
  --resource-group Nexy \
  --nsg-name nexy-regular-nsg \
  --name allow-new-port \
  --priority 1005 \
  --source-address-prefixes '*' \
  --destination-address-prefixes '*' \
  --destination-port-ranges 8082 \
  --access Allow \
  --protocol Tcp
```

---

## 📝 **РАБОТА С MANIFEST**

### **Создание нового манифеста:**
```bash
# Локально
cd /Users/sergiyzasorin/Development/Nexy/server
cat > updates/manifests/manifest_1.0.1.json << 'EOF'
{
  "version": "1.0.1",
  "build": 10001,
  "release_date": "2025-10-04T15:00:00.000000Z",
  "artifact": {
    "type": "pkg",
    "url": "http://20.151.51.172:8081/downloads/Nexy-1.0.1.pkg",
    "size": 0,
    "sha256": "",
    "arch": "universal2",
    "min_os": "11.0",
    "ed25519": ""
  },
  "critical": false,
  "auto_install": false,
  "notes_url": "http://20.151.51.172:8081/downloads/release-notes.txt"
}
EOF

# Синхронизация
git add updates/manifests/manifest_1.0.1.json
git commit -m "feat: Add version 1.0.1 manifest"
git push origin main
```

---

## 🚨 **ЭКСТРЕННЫЕ СИТУАЦИИ**

### **Полный перезапуск сервера:**
```bash
az vm run-command invoke \
  --resource-group Nexy \
  --name nexy-regular \
  --command-id RunShellScript \
  --scripts "
sudo systemctl stop voice-assistant.service
sleep 3
sudo systemctl start voice-assistant.service
sleep 5
sudo systemctl status voice-assistant.service --no-pager -l | head -10
"
```

### **Откат к предыдущей версии:**
```bash
az vm run-command invoke \
  --resource-group Nexy \
  --name nexy-regular \
  --command-id RunShellScript \
  --scripts "
cd /home/azureuser/voice-assistant
git log --oneline -5
git reset --hard HEAD~1
sudo systemctl restart voice-assistant.service
"
```

### **Проверка всех сервисов:**
```bash
az vm run-command invoke \
  --resource-group Nexy \
  --name nexy-regular \
  --command-id RunShellScript \
  --scripts "
echo '=== SERVICE STATUS ==='
sudo systemctl status voice-assistant.service --no-pager -l | head -5
echo ''
echo '=== PORTS ==='
ss -tlnp | grep -E ':(8080|8081|50051)'
echo ''
echo '=== HEALTH CHECKS ==='
curl -s localhost:8080/health && echo ' HTTP OK' || echo ' HTTP FAIL'
curl -s localhost:8081/health | head -c 50 && echo ' Update OK' || echo ' Update FAIL'
"
```

---

## 📞 **КОНТАКТЫ И РЕСУРСЫ**

- **Azure VM:** `nexy-regular` (20.151.51.172)
- **GitHub:** `https://github.com/Seregawpn/Nexy_server.git`
- **Health Check:** `http://20.151.51.172/health`
- **AppCast:** `http://20.151.51.172:8081/appcast.xml`

---

**💡 Совет:** Сохраните эту шпаргалку в закладки для быстрого доступа!
