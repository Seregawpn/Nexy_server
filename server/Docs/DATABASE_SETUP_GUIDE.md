# Руководство по настройке PostgreSQL для Nexy Server

Это руководство поможет вам правильно настроить PostgreSQL базу данных для работы с Nexy Server.

## Содержание

1. [Установка PostgreSQL](#установка-postgresql)
2. [Создание пользователя и базы данных](#создание-пользователя-и-базы-данных)
3. [Настройка config.env](#настройка-configenv)
4. [Применение схемы базы данных](#применение-схемы-базы-данных)
5. [Проверка подключения](#проверка-подключения)
6. [Автоматическая настройка](#автоматическая-настройка)

---

## Установка PostgreSQL

### macOS

```bash
# Используя Homebrew
brew install postgresql@15
brew services start postgresql@15

# Или используя Postgres.app (GUI)
# Скачайте с https://postgresapp.com/
```

### Linux (Ubuntu/Debian)

```bash
sudo apt update
sudo apt install postgresql postgresql-contrib
sudo systemctl start postgresql
sudo systemctl enable postgresql
```

### Linux (CentOS/RHEL)

```bash
sudo yum install postgresql-server postgresql-contrib
sudo postgresql-setup initdb
sudo systemctl start postgresql
sudo systemctl enable postgresql
```

### Windows

1. Скачайте установщик с https://www.postgresql.org/download/windows/
2. Запустите установщик и следуйте инструкциям
3. Запомните пароль для пользователя `postgres`

---

## Создание пользователя и базы данных

### Вариант 1: Используя psql (рекомендуется)

```bash
# Подключитесь к PostgreSQL как суперпользователь
psql -U postgres

# В psql выполните следующие команды:
```

```sql
-- Создайте пользователя (замените 'your_password' на надежный пароль)
CREATE USER nexy_user WITH PASSWORD 'your_secure_password_here';

-- Создайте базу данных (владелец не должен быть app-пользователем)
CREATE DATABASE voice_assistant_db OWNER postgres;

-- Предоставьте минимально необходимые права
GRANT CONNECT, TEMPORARY ON DATABASE voice_assistant_db TO nexy_user;
\c voice_assistant_db
REVOKE CREATE ON SCHEMA public FROM nexy_user;
GRANT USAGE ON SCHEMA public TO nexy_user;

-- Выйдите из psql
\q
```

### Вариант 2: Используя автоматический скрипт

```bash
# Используйте скрипт setup_database.sh (см. раздел "Автоматическая настройка")
./scripts/setup_database.sh
```

---

## Настройка config.env

Откройте файл `server/config.env` и обновите следующие параметры:

```env
# =====================================================
# POSTGRESQL DATABASE
# =====================================================
DB_HOST=localhost
DB_PORT=5432
DB_NAME=voice_assistant_db
DB_USER=nexy_user                    # Имя пользователя, созданного выше
DB_PASSWORD=your_secure_password_here # Пароль, который вы установили
```

**Важно:** 
- Не используйте плейсхолдеры типа `YOUR_DB_USER_HERE`
- Используйте надежные пароли
- Не коммитьте `config.env` в git (он уже в .gitignore)

---

## Применение схемы базы данных

После создания базы данных нужно применить схему:

### Вариант 1: Используя psql

```bash
psql -U postgres -d voice_assistant_db -f Docs/DATABASE_SCHEMA.sql
```

### Вариант 2: Используя Python скрипт

```bash
python scripts/apply_database_schema.py
```

### Вариант 3: Автоматически при первом запуске

Сервер автоматически попытается применить схему при первом подключении (если включены миграции).

---

## Проверка подключения

### Используя скрипт проверки

```bash
python scripts/test_db_connection.py
```

### Используя psql

```bash
psql -U nexy_user -d voice_assistant_db -h localhost
```

Если подключение успешно, вы увидите приглашение `voice_assistant_db=>`.

### Проверка через Python

```python
import psycopg2

try:
    conn = psycopg2.connect(
        host="localhost",
        port=5432,
        database="voice_assistant_db",
        user="nexy_user",
        password="your_secure_password_here"
    )
    print("✅ Подключение успешно!")
    conn.close()
except Exception as e:
    print(f"❌ Ошибка подключения: {e}")
```

---

## Автоматическая настройка

Для автоматической настройки используйте скрипт:

```bash
cd server
./scripts/setup_database.sh
```

Этот скрипт:
1. Проверит наличие PostgreSQL
2. Создаст пользователя и базу данных (если не существуют)
3. Применит схему базы данных
4. Проверит подключение

**Примечание:** Скрипт запросит пароль для пользователя `postgres` (суперпользователь).
**Канон операций backup/restore/drill:** `Docs/DB_BACKUP_AND_RESTORE_RUNBOOK.md`

### Hardening для защиты данных (обязательно для production)

После базовой настройки примените:

```bash
./scripts/harden_database_protection.sh
```

Скрипт делает:
1. `REVOKE` опасных прав (`DELETE/TRUNCATE/CREATE`) у `DB_USER`
2. `GRANT` только `SELECT/INSERT/UPDATE` + нужные права на sequence/function
3. Ставит trigger-защиту от hard-delete на критичные таблицы

---

## Устранение проблем

### Ошибка: "role does not exist"

**Проблема:** Пользователь БД не создан.

**Решение:**
```bash
psql -U postgres
CREATE USER nexy_user WITH PASSWORD 'your_password';
```

### Ошибка: "database does not exist"

**Проблема:** База данных не создана.

**Решение:**
```bash
psql -U postgres
CREATE DATABASE voice_assistant_db OWNER postgres;
```

### Ошибка: "password authentication failed"

**Проблема:** Неверный пароль в `config.env`.

**Решение:** Проверьте пароль в `config.env` и убедитесь, что он совпадает с паролем пользователя БД.

### Ошибка: "connection refused"

**Проблема:** PostgreSQL не запущен.

**Решение:**
```bash
# macOS
brew services start postgresql@15

# Linux
sudo systemctl start postgresql

# Windows
# Запустите PostgreSQL через Services или используйте pgAdmin
```

### Ошибка: "permission denied"

**Проблема:** Пользователь не имеет прав на базу данных.

**Решение:**
```bash
psql -U postgres
GRANT CONNECT, TEMPORARY ON DATABASE voice_assistant_db TO nexy_user;
\c voice_assistant_db
REVOKE CREATE ON SCHEMA public FROM nexy_user;
GRANT USAGE ON SCHEMA public TO nexy_user;
```

---

## Безопасность

### Рекомендации для production:

1. **Используйте отдельного пользователя БД** (не `postgres`)
2. **Используйте надежные пароли** (минимум 16 символов, смешанный регистр, цифры, символы)
3. **Ограничьте доступ** - используйте firewall для ограничения доступа к порту 5432
4. **Используйте SSL** - настройте SSL соединения для production
5. **Регулярные бэкапы** - настройте автоматические бэкапы базы данных
6. **Обязательный restore-drill** - минимум 1 раз в неделю проверяйте восстановление (`./scripts/db_restore_drill.sh`)

### Пример настройки SSL в config.env:

```env
DB_SSL_MODE=require
DB_SSL_CERT=/path/to/client-cert.pem
DB_SSL_KEY=/path/to/client-key.pem
DB_SSL_CA=/path/to/ca-cert.pem
```

---

## Проверка работоспособности

После настройки проверьте, что все работает:

```bash
# 1. Проверьте подключение
python scripts/test_db_connection.py

# 2. Запустите сервер
python server/main.py

# 3. Проверьте логи - не должно быть ошибок подключения к БД
```

Если все настроено правильно, в логах вы увидите:
```
✅ Модуль 'database' зарегистрирован с capability 'database'
✅ DatabaseManager initialized successfully
```

---

## Дополнительная информация

- Схема базы данных: `Docs/DATABASE_SCHEMA.sql`
- Конфигурация БД: `modules/database/config.py`
- Провайдер PostgreSQL: `modules/database/providers/postgresql_provider.py`

---

## Поддержка

Если у вас возникли проблемы:
1. Проверьте логи сервера
2. Проверьте логи PostgreSQL
3. Убедитесь, что все параметры в `config.env` заполнены корректно
4. Используйте скрипт проверки подключения
