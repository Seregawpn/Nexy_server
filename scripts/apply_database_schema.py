#!/usr/bin/env python3
"""
Скрипт для применения схемы базы данных PostgreSQL
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

def apply_schema():
    """Применение схемы базы данных"""
    print("=" * 50)
    print("Применение схемы базы данных PostgreSQL")
    print("=" * 50)
    print()
    
    # Получаем параметры подключения
    db_host = os.getenv('DB_HOST', 'localhost')
    db_port = int(os.getenv('DB_PORT', '5432'))
    db_name = os.getenv('DB_NAME', 'voice_assistant_db')
    db_user = os.getenv('DB_USER', 'postgres')
    db_password = os.getenv('DB_PASSWORD', '')
    
    # Путь к файлу схемы
    schema_file = project_root / "Docs" / "DATABASE_SCHEMA.sql"
    
    if not schema_file.exists():
        print(f"❌ Файл схемы не найден: {schema_file}")
        sys.exit(1)
    
    print(f"Параметры подключения:")
    print(f"  Host: {db_host}")
    print(f"  Port: {db_port}")
    print(f"  Database: {db_name}")
    print(f"  User: {db_user}")
    print(f"  Schema file: {schema_file}")
    print()
    
    # Пытаемся подключиться и применить схему
    try:
        print("Подключение к базе данных...")
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
        
        # Читаем файл схемы
        print(f"Чтение файла схемы: {schema_file}")
        with open(schema_file, 'r', encoding='utf-8') as f:
            schema_sql = f.read()
        
        print("Применение схемы...")
        cur = conn.cursor()
        cur.execute(schema_sql)
        conn.commit()
        
        print("✅ Схема применена успешно!")
        print()
        
        # Проверяем созданные таблицы
        cur.execute("""
            SELECT table_name 
            FROM information_schema.tables 
            WHERE table_schema = 'public'
            ORDER BY table_name;
        """)
        tables = cur.fetchall()
        
        if tables:
            print(f"✅ Создано таблиц: {len(tables)}")
            for table in tables:
                print(f"   - {table[0]}")
        else:
            print("⚠️  Таблицы не найдены")
        
        print()
        
        # Проверяем созданные функции
        cur.execute("""
            SELECT routine_name 
            FROM information_schema.routines 
            WHERE routine_schema = 'public'
            AND routine_type = 'FUNCTION';
        """)
        functions = cur.fetchall()
        
        if functions:
            print(f"✅ Создано функций: {len(functions)}")
            for func in functions:
                print(f"   - {func[0]}")
        else:
            print("⚠️  Функции не найдены")
        
        cur.close()
        conn.close()
        
        print()
        print("=" * 50)
        print("✅ Схема базы данных применена успешно!")
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
        return False
        
    except psycopg2.Error as e:
        print(f"❌ Ошибка базы данных: {e}")
        print()
        print("Возможно, схема уже применена или произошла ошибка при выполнении SQL")
        return False
        
    except Exception as e:
        print(f"❌ Неожиданная ошибка: {e}")
        return False

if __name__ == "__main__":
    success = apply_schema()
    sys.exit(0 if success else 1)
