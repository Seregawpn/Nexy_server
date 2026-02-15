-- Быстрая настройка PostgreSQL для Nexy Server
--
-- ⚠️ ВАЖНО: ОБЯЗАТЕЛЬНО установите переменную DB_PASSWORD перед запуском!
-- Скрипт остановится с ошибкой, если пароль не установлен.
--
-- ИСПОЛЬЗОВАНИЕ:
--   psql -U postgres -v DB_PASSWORD='ваш_надежный_пароль' -f scripts/quick_setup_db.sql
--
-- ИЛИ установите переменную в psql:
--   \set DB_PASSWORD 'ваш_надежный_пароль'
--   \i scripts/quick_setup_db.sql

-- Проверка: останавливаем выполнение, если пароль не установлен
DO $$
DECLARE
    db_password TEXT;
BEGIN
    -- Получаем переменную из psql через подстановку
    db_password := :'DB_PASSWORD';
    
    IF db_password IS NULL OR db_password = '' THEN
        RAISE EXCEPTION 'ОШИБКА БЕЗОПАСНОСТИ: Пароль не установлен! Используйте: psql -U postgres -v DB_PASSWORD=''ваш_пароль'' -f scripts/quick_setup_db.sql';
    END IF;
    
    IF length(db_password) < 8 THEN
        RAISE EXCEPTION 'ОШИБКА: Пароль слишком короткий! Минимальная длина пароля - 8 символов.';
    END IF;
    
    RAISE NOTICE 'Проверка пароля пройдена. Продолжаем настройку...';
END
$$;

-- Создание пользователя (если не существует)
DO $$
DECLARE
    user_password TEXT;
BEGIN
    -- Получаем пароль из переменной psql через подстановку
    user_password := :'DB_PASSWORD';
    
    IF NOT EXISTS (SELECT FROM pg_roles WHERE rolname = 'nexy_user') THEN
        EXECUTE format('CREATE USER nexy_user WITH PASSWORD %L', user_password);
        RAISE NOTICE 'Пользователь nexy_user создан';
    ELSE
        RAISE NOTICE 'Пользователь nexy_user уже существует';
    END IF;
END
$$;

-- Создание базы данных (если не существует)
SELECT 'CREATE DATABASE voice_assistant_db OWNER postgres'
WHERE NOT EXISTS (SELECT FROM pg_database WHERE datname = 'voice_assistant_db')\gexec

-- Предоставление минимально необходимых привилегий
GRANT CONNECT, TEMPORARY ON DATABASE voice_assistant_db TO nexy_user;

-- Подключение к базе данных и предоставление прав на схему
\c voice_assistant_db
REVOKE CREATE ON SCHEMA public FROM nexy_user;
GRANT USAGE ON SCHEMA public TO nexy_user;

REVOKE ALL PRIVILEGES ON ALL TABLES IN SCHEMA public FROM nexy_user;
GRANT SELECT, INSERT, UPDATE ON ALL TABLES IN SCHEMA public TO nexy_user;
REVOKE DELETE, TRUNCATE, REFERENCES, TRIGGER ON ALL TABLES IN SCHEMA public FROM nexy_user;

REVOKE ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public FROM nexy_user;
GRANT USAGE, SELECT, UPDATE ON ALL SEQUENCES IN SCHEMA public TO nexy_user;

REVOKE ALL PRIVILEGES ON ALL FUNCTIONS IN SCHEMA public FROM nexy_user;
GRANT EXECUTE ON ALL FUNCTIONS IN SCHEMA public TO nexy_user;

ALTER DEFAULT PRIVILEGES IN SCHEMA public REVOKE ALL ON TABLES FROM nexy_user;
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT SELECT, INSERT, UPDATE ON TABLES TO nexy_user;
ALTER DEFAULT PRIVILEGES IN SCHEMA public REVOKE DELETE, TRUNCATE, REFERENCES, TRIGGER ON TABLES FROM nexy_user;
ALTER DEFAULT PRIVILEGES IN SCHEMA public REVOKE ALL ON SEQUENCES FROM nexy_user;
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT USAGE, SELECT, UPDATE ON SEQUENCES TO nexy_user;
ALTER DEFAULT PRIVILEGES IN SCHEMA public REVOKE ALL ON FUNCTIONS FROM nexy_user;
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT EXECUTE ON FUNCTIONS TO nexy_user;

\echo '✅ База данных и пользователь настроены!'
\echo ''
\echo 'Следующие шаги:'
\echo '1. Обновите config.env:'
\echo '   DB_USER=nexy_user'
\echo '   DB_PASSWORD=<пароль_который_вы_указали_в_переменной_DB_PASSWORD>'
\echo ''
\echo '2. Примените схему:'
\echo '   psql -U postgres -d voice_assistant_db -f Docs/DATABASE_SCHEMA.sql'
\echo ''
\echo '3. Ужесточите защиту:'
\echo '   ./server/scripts/harden_database_protection.sh'
\echo ''
\echo '4. Проверьте подключение:'
\echo '   python scripts/test_db_connection.py'
