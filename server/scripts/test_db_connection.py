#!/usr/bin/env python3
"""
Скрипт для проверки подключения к PostgreSQL базе данных
"""

import sys
import os
from pathlib import Path

# Добавляем путь к корню проекта
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from dotenv import load_dotenv
import psycopg2
from psycopg2 import sql

# Загружаем config.env
config_path = project_root / "config.env"
if config_path.exists():
    load_dotenv(config_path)
else:
    print("❌ Файл config.env не найден")
    sys.exit(1)

def test_connection():
    """Проверка подключения к базе данных"""
    print("=" * 50)
    print("Проверка подключения к PostgreSQL")
    print("=" * 50)
    print()
    
    # Получаем параметры подключения
    db_host = os.getenv('DB_HOST', 'localhost')
    db_port = int(os.getenv('DB_PORT', '5432'))
    db_name = os.getenv('DB_NAME', 'voice_assistant_db')
    db_user = os.getenv('DB_USER', 'postgres')
    db_password = os.getenv('DB_PASSWORD', '')
    
    # Проверяем наличие плейсхолдеров
    placeholder_values = {
        'YOUR_DB_USER_HERE',
        'YOUR_DB_PASSWORD_HERE',
        'YOUR_DB_NAME_HERE',
        'YOUR_DATABASE_USER_HERE',
        'YOUR_DATABASE_PASSWORD_HERE',
    }
    
    if db_user in placeholder_values:
        print(f"❌ DB_USER содержит плейсхолдер: {db_user}")
        print("   Пожалуйста, укажите реальное имя пользователя БД в config.env")
        return False
        
    if db_password in placeholder_values or not db_password:
        print(f"❌ DB_PASSWORD не заполнен или содержит плейсхолдер")
        print("   Пожалуйста, укажите реальный пароль БД в config.env")
        return False
    
    print(f"Параметры подключения:")
    print(f"  Host: {db_host}")
    print(f"  Port: {db_port}")
    print(f"  Database: {db_name}")
    print(f"  User: {db_user}")
    print(f"  Password: {'*' * len(db_password) if db_password else 'НЕ УСТАНОВЛЕН'}")
    print()
    
    # Пытаемся подключиться
    try:
        print("Попытка подключения...")
        conn = psycopg2.connect(
            host=db_host,
            port=db_port,
            database=db_name,
            user=db_user,
            password=db_password,
            connect_timeout=5
        )
        
        print("✅ Подключение успешно!")
        print()
        
        # Проверяем версию PostgreSQL
        cur = conn.cursor()
        cur.execute("SELECT version();")
        version = cur.fetchone()[0]
        print(f"Версия PostgreSQL: {version.split(',')[0]}")
        print()
        
        # Проверяем наличие таблиц
        print("Проверка схемы базы данных...")
        cur.execute("""
            SELECT table_name 
            FROM information_schema.tables 
            WHERE table_schema = 'public'
            ORDER BY table_name;
        """)
        tables = cur.fetchall()
        
        expected_tables = {
            'users', 'sessions', 'commands', 
            'llm_answers', 'screenshots', 'performance_metrics'
        }
        
        found_tables = {table[0] for table in tables}
        
        if found_tables:
            print(f"✅ Найдено таблиц: {len(found_tables)}")
            for table in sorted(found_tables):
                print(f"   - {table}")
        else:
            print("⚠️  Таблицы не найдены. Возможно, схема не применена.")
            print("   Примените схему: psql -U {db_user} -d {db_name} -f Docs/DATABASE_SCHEMA.sql")
        
        print()
        
        # Проверяем наличие всех необходимых таблиц
        missing_tables = expected_tables - found_tables
        if missing_tables:
            print(f"⚠️  Отсутствуют таблицы: {', '.join(sorted(missing_tables))}")
            print("   Примените схему базы данных для создания всех таблиц")
        else:
            print("✅ Все необходимые таблицы присутствуют")
        
        print()
        
        # Проверяем функции
        cur.execute("""
            SELECT routine_name 
            FROM information_schema.routines 
            WHERE routine_schema = 'public'
            AND routine_type = 'FUNCTION';
        """)
        functions = cur.fetchall()
        
        expected_functions = {
            'cleanup_expired_short_term_memory',
            'get_memory_stats'
        }
        
        found_functions = {func[0] for func in functions}
        
        if found_functions:
            print(f"✅ Найдено функций: {len(found_functions)}")
            for func in sorted(found_functions):
                print(f"   - {func}")
        else:
            print("⚠️  Функции не найдены")
        
        print()
        
        # Проверяем наличие всех необходимых функций
        missing_functions = expected_functions - found_functions
        if missing_functions:
            print(f"⚠️  Отсутствуют функции: {', '.join(sorted(missing_functions))}")
            print("   Примените схему базы данных для создания всех функций")
        else:
            print("✅ Все необходимые функции присутствуют")
        
        print()
        
        # Тестовая запись (опционально)
        print("Тестовая операция...")
        cur.execute("SELECT COUNT(*) FROM users;")
        user_count = cur.fetchone()[0]
        print(f"✅ Количество пользователей в БД: {user_count}")
        
        cur.close()
        conn.close()
        
        print()
        print("=" * 50)
        print("✅ Все проверки пройдены успешно!")
        print("=" * 50)
        return True
        
    except psycopg2.OperationalError as e:
        print(f"❌ Ошибка подключения: {e}")
        print()
        print("Возможные причины:")
        print("  1. PostgreSQL не запущен")
        print("  2. Неверные параметры подключения в config.env")
        print("  3. Пользователь или база данных не существуют")
        print("  4. Неверный пароль")
        print()
        print("Решение:")
        print("  1. Убедитесь, что PostgreSQL запущен")
        print("  2. Проверьте параметры в config.env")
        print("  3. Используйте скрипт setup_database.sh для настройки БД")
        return False
        
    except psycopg2.Error as e:
        print(f"❌ Ошибка базы данных: {e}")
        return False
        
    except Exception as e:
        print(f"❌ Неожиданная ошибка: {e}")
        return False

if __name__ == "__main__":
    success = test_connection()
    sys.exit(0 if success else 1)
