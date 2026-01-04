# Быстрая настройка PostgreSQL для Nexy Server

**Назначение:** Полный гайд с вариантами настройки, troubleshooting и проверками.  
**Для краткой справки:** см. `QUICK_DB_SETUP.md` (только команды без подробностей)

## Вариант 1: Быстрая настройка через SQL (рекомендуется)

**Шаг 1:** Создание пользователя и базы данных
```bash
psql -U postgres -v DB_PASSWORD='TestPass123!' -f server/scripts/quick_setup_db.sql
```
⚠️ **Важно:** Замените `TestPass123!` на свой надежный пароль (минимум 8 символов)

**Шаг 2:** Применение схемы базы данных
```bash
psql -U nexy_user -d voice_assistant_db -f server/Docs/DATABASE_SCHEMA.sql
```

**Шаг 3:** Проверка подключения
```bash
python server/scripts/test_db_connection.py
```

---

## Вариант 2: Автоматическая настройка через скрипт

```bash
./server/scripts/setup_database.sh
python server/scripts/test_db_connection.py
```

Скрипт попросит ввести пароли интерактивно.

---

## Вариант 3: Настройка/обновление config.env

Если база данных уже настроена, но нужно обновить `config.env`:

```bash
./server/scripts/configure_db_connection.sh
```

Скрипт:
- Проверит подключение к БД
- Обновит `config.env` с правильными значениями
- Создаст резервную копию `config.env.backup`

**После выполнения в `server/config.env` должны быть:**
```env
DB_HOST=localhost
DB_PORT=5432
DB_NAME=voice_assistant_db
DB_USER=nexy_user
DB_PASSWORD=<ваш_пароль>
```

---

## Проверка подключения

После настройки проверьте подключение:

```bash
python server/scripts/test_db_connection.py
```

### Возможные ошибки:

**Ошибка: `role does not exist`**
- **Причина:** Пользователь БД не создан
- **Решение:** Выполните шаг 1 из Варианта 1 или используйте Вариант 2

**Ошибка: `password authentication failed`**
- **Причина:** Неверный пароль в `config.env`
- **Решение:** 
  1. Проверьте пароль в `server/config.env`
  2. Или используйте `./server/scripts/configure_db_connection.sh` для обновления

**Ошибка: `database does not exist`**
- **Причина:** База данных не создана
- **Решение:** Выполните шаг 1 из Варианта 1

**Ошибка: `connection refused`**
- **Причина:** PostgreSQL не запущен
- **Решение:** 
  - macOS: `brew services start postgresql@15`
  - Linux: `sudo systemctl start postgresql`

---

## После успешной настройки

Запустите сервер:

```bash
python server/main.py
```

В логах должно быть:
```
✅ Модуль 'database' зарегистрирован с capability 'database'
✅ DatabaseManager initialized successfully
```

Если видите:
```
⚠️ Модуль 'database' не инициализирован (опциональный)
```

Это означает, что модуль database опциональный и сервер продолжит работу без БД. Проверьте конфигурацию БД в `server/config.env`.

---

## Дополнительная информация

- Полное руководство: `server/Docs/DATABASE_SETUP_GUIDE.md`
- Схема БД: `server/Docs/DATABASE_SCHEMA.sql`
- Отчет о проверке: `server/Docs/DATABASE_FIX_VERIFICATION.md`
