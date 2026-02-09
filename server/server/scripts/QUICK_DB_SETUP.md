# Краткая справка по настройке PostgreSQL

**Назначение:** Краткая справка с командами для быстрой настройки БД.  
**Для подробной информации:** см. `QUICK_START_DB.md` (полный гайд с вариантами и troubleshooting)

**Все команды выполняются из корня проекта.**

## Вариант 1: Используя SQL скрипт (самый быстрый)

**Важно:** Скрипт требует установки переменной `DB_PASSWORD` для безопасности.

1. **Запустите скрипт с переменной пароля:**
   ```bash
   psql -U postgres -v DB_PASSWORD='ваш_надежный_пароль' -f server/scripts/quick_setup_db.sql
   ```
   (Вам будет предложено ввести пароль пользователя `postgres`)

   **Или установите переменную в psql:**
   ```bash
   psql -U postgres
   \set DB_PASSWORD 'ваш_надежный_пароль'
   \i server/scripts/quick_setup_db.sql
   ```

   **Безопасность:** Скрипт проверяет, что пароль установлен и имеет минимум 8 символов.

2. **Примените схему:**
   ```bash
   psql -U nexy_user -d voice_assistant_db -f server/Docs/DATABASE_SCHEMA.sql
   ```

3. **Обновите config.env:**
   ```env
   DB_USER=nexy_user
   DB_PASSWORD=ваш_пароль_который_вы_указали_в_переменной_DB_PASSWORD
   ```

4. **Проверьте подключение:**
   ```bash
   python server/scripts/test_db_connection.py
   ```

---

## Вариант 2: Ручная настройка через psql

1. **Подключитесь к PostgreSQL:**
   ```bash
   psql -U postgres
   ```

2. **Выполните команды:**
   ```sql
   -- Создайте пользователя (замените пароль!)
   CREATE USER nexy_user WITH PASSWORD 'ваш_надежный_пароль';
   
   -- Создайте базу данных
   CREATE DATABASE voice_assistant_db OWNER nexy_user;
   
   -- Предоставьте привилегии
   GRANT ALL PRIVILEGES ON DATABASE voice_assistant_db TO nexy_user;
   
   -- Выйдите
   \q
   ```

3. **Примените схему:**
   ```bash
   psql -U nexy_user -d voice_assistant_db -f server/Docs/DATABASE_SCHEMA.sql
   ```

4. **Обновите config.env:**
   ```env
   DB_USER=nexy_user
   DB_PASSWORD=ваш_надежный_пароль
   ```

5. **Проверьте подключение:**
   ```bash
   python server/scripts/test_db_connection.py
   ```

---

## Вариант 3: Используя интерактивный скрипт

```bash
./server/scripts/setup_database.sh
```

Скрипт попросит ввести пароли интерактивно.

---

## После настройки

После успешной настройки проверьте, что сервер запускается без ошибок:

```bash
python server/main.py
```

В логах должно быть:
```
✅ Модуль 'database' зарегистрирован с capability 'database'
✅ DatabaseManager initialized successfully
```

Если видите ошибки подключения, проверьте:
1. Правильность пароля в `server/config.env`
2. Что PostgreSQL запущен: `pg_isready`
3. Что пользователь и база данных существуют
