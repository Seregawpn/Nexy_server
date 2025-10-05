# 🔧 РУКОВОДСТВО ПО РЕШЕНИЮ ПРОБЛЕМ

**Версия:** 1.0  
**Применимость:** Любой проект, сервер, технология  
**Использование:** Справочник для быстрого решения типичных проблем

---

## 🚨 **ЭКСТРЕННЫЕ ПРОБЛЕМЫ**

### **Сервис не запускается:**
```bash
# 1. Проверить статус сервиса
systemctl status service-name

# 2. Проверить логи
journalctl -u service-name --no-pager -n 50

# 3. Проверить конфигурацию
cat /path/to/config

# 4. Проверить права доступа
ls -la /path/to/files

# 5. Проверить зависимости
which python3
pip list | grep package-name
```

### **Сервис не отвечает:**
```bash
# 1. Проверить процесс
ps aux | grep service-name

# 2. Проверить порты
ss -tlnp | grep port-number

# 3. Проверить сеть
curl -v http://localhost:port/health

# 4. Проверить firewall
ufw status
iptables -L

# 5. Проверить DNS
nslookup hostname
```

### **Ошибки базы данных:**
```bash
# 1. Проверить статус БД
systemctl status postgresql

# 2. Проверить подключение
psql -h host -U user -d database

# 3. Проверить логи БД
tail -f /var/log/postgresql/postgresql.log

# 4. Проверить место на диске
df -h

# 5. Проверить права доступа
ls -la /var/lib/postgresql/
```

---

## 🔍 **ДИАГНОСТИКА ПО ЛОГАМ**

### **Анализ логов сервиса:**
```bash
# Последние ошибки
journalctl -u service-name --no-pager -n 100 | grep -i error

# Ошибки за последний час
journalctl -u service-name --since "1 hour ago" | grep -i error

# Поиск по ключевым словам
journalctl -u service-name | grep -E "(ERROR|CRITICAL|FATAL)"

# Логи в реальном времени
journalctl -u service-name -f
```

### **Анализ системных логов:**
```bash
# Системные ошибки
dmesg | grep -i error

# Ошибки загрузки
journalctl -b | grep -i error

# Ошибки сети
journalctl | grep -i network

# Ошибки диска
journalctl | grep -i disk
```

---

## 🌐 **ПРОБЛЕМЫ СЕТИ**

### **Проблемы с портами:**
```bash
# Проверить, что слушает порт
ss -tlnp | grep :port

# Проверить, кто использует порт
lsof -i :port

# Освободить порт
kill -9 PID

# Проверить firewall
ufw status numbered
iptables -L -n
```

### **Проблемы с DNS:**
```bash
# Проверить DNS
nslookup domain.com
dig domain.com

# Проверить hosts файл
cat /etc/hosts

# Проверить resolv.conf
cat /etc/resolv.conf

# Очистить DNS кеш
systemctl flush-dns
```

### **Проблемы с SSL:**
```bash
# Проверить сертификат
openssl x509 -in cert.pem -text -noout

# Проверить срок действия
openssl x509 -in cert.pem -dates -noout

# Проверить подключение
openssl s_client -connect host:port

# Проверить цепочку сертификатов
openssl verify -CAfile ca.pem cert.pem
```

---

## 💾 **ПРОБЛЕМЫ С РЕСУРСАМИ**

### **Проблемы с памятью:**
```bash
# Проверить использование памяти
free -h
top -o %MEM

# Найти процессы, потребляющие память
ps aux --sort=-%mem | head -10

# Проверить swap
swapon -s
cat /proc/meminfo | grep Swap

# Очистить кеш
sync && echo 3 > /proc/sys/vm/drop_caches
```

### **Проблемы с диском:**
```bash
# Проверить место на диске
df -h

# Найти большие файлы
find / -type f -size +100M 2>/dev/null

# Проверить inodes
df -i

# Очистить временные файлы
rm -rf /tmp/*
rm -rf /var/tmp/*
```

### **Проблемы с CPU:**
```bash
# Проверить нагрузку CPU
top -o %CPU
htop

# Найти процессы, потребляющие CPU
ps aux --sort=-%cpu | head -10

# Проверить системную нагрузку
uptime
cat /proc/loadavg
```

---

## 🔧 **ПРОБЛЕМЫ КОНФИГУРАЦИИ**

### **Проблемы с переменными окружения:**
```bash
# Проверить переменные окружения
env | grep VARIABLE_NAME

# Проверить .env файл
cat .env

# Проверить загрузку конфигурации
grep -r "load_dotenv" .

# Проверить права на конфигурацию
ls -la config.env
```

### **Проблемы с правами доступа:**
```bash
# Проверить права на файлы
ls -la /path/to/files

# Проверить пользователя процесса
ps aux | grep process-name

# Исправить права
chown -R user:group /path/to/files
chmod -R 755 /path/to/files

# Проверить SELinux (если включен)
sestatus
getenforce
```

---

## 🐛 **ПРОБЛЕМЫ ПРИЛОЖЕНИЯ**

### **Ошибки инициализации:**
```bash
# Проверить зависимости
pip list | grep package
npm list | grep package

# Проверить версии
python --version
node --version

# Проверить импорты
python -c "import package"

# Проверить конфигурацию
python -c "from config import settings; print(settings)"
```

### **Ошибки API:**
```bash
# Проверить endpoints
curl -v http://localhost:port/health
curl -v http://localhost:port/status

# Проверить gRPC
grpcurl -plaintext localhost:port list

# Проверить логи API
tail -f /var/log/api.log

# Проверить rate limiting
curl -v -H "X-API-Key: key" http://localhost:port/api
```

---

## 🔄 **ПРОБЛЕМЫ ДЕПЛОЯ**

### **Проблемы с Git:**
```bash
# Проверить статус
git status

# Проверить remote
git remote -v

# Решить конфликты
git status
git add .
git commit -m "Resolve conflicts"

# Принудительный pull
git fetch origin
git reset --hard origin/main
```

### **Проблемы с зависимостями:**
```bash
# Обновить зависимости
pip install -r requirements.txt
npm install

# Очистить кеш
pip cache purge
npm cache clean --force

# Переустановить зависимости
rm -rf node_modules
npm install
```

---

## 📊 **МОНИТОРИНГ И АЛЕРТЫ**

### **Проверка мониторинга:**
```bash
# Проверить метрики
curl http://localhost:port/metrics

# Проверить health checks
curl http://localhost:port/health

# Проверить статус
curl http://localhost:port/status

# Проверить алерты
systemctl status alertmanager
```

### **Проверка логов:**
```bash
# Централизованные логи
tail -f /var/log/centralized.log

# Логи приложения
tail -f /var/log/app.log

# Логи системы
tail -f /var/log/syslog

# Логи безопасности
tail -f /var/log/auth.log
```

---

## 🚨 **ЭКСТРЕННОЕ ВОССТАНОВЛЕНИЕ**

### **Быстрый откат:**
```bash
# Откат к предыдущей версии
git reset --hard HEAD~1

# Перезапуск сервиса
systemctl restart service-name

# Восстановление из backup
cp -r backup/ current/

# Откат конфигурации
cp config.backup config
```

### **Восстановление данных:**
```bash
# Восстановление БД
pg_restore -h host -U user -d database backup.sql

# Восстановление файлов
rsync -av backup/ current/

# Восстановление конфигурации
cp -r config.backup/ config/
```

---

## 📋 **ЧЕКЛИСТ ДИАГНОСТИКИ**

### **Быстрая диагностика:**
- [ ] Проверить статус сервиса
- [ ] Проверить логи на ошибки
- [ ] Проверить использование ресурсов
- [ ] Проверить сетевую доступность
- [ ] Проверить конфигурацию
- [ ] Проверить права доступа
- [ ] Проверить зависимости

### **Глубокая диагностика:**
- [ ] Анализ логов за последние 24 часа
- [ ] Проверка системных ресурсов
- [ ] Анализ сетевого трафика
- [ ] Проверка безопасности
- [ ] Анализ производительности
- [ ] Проверка backup и восстановления

---

## 📝 **ДОКУМЕНТИРОВАНИЕ ПРОБЛЕМ**

### **Шаблон отчета об инциденте:**
```
**Дата:** _______________
**Время:** _______________
**Сервис:** _______________
**Проблема:** _______________
**Симптомы:** _______________
**Причина:** _______________
**Решение:** _______________
**Время решения:** _______________
**Предотвращение:** _______________
```

---

**Помните: хорошая диагностика - половина решения проблемы!** 🔧
