#!/usr/bin/env python3
"""
Скрипт для обогащения базы данных WhatsApp именами контактов из macOS
Использует contact_resolver для получения имен и обновляет базу данных
"""

import sys
import sqlite3
import json
from pathlib import Path

# Добавляем путь к contact_resolver
messages_path = Path("/Users/sergiyzasorin/Messages")
sys.path.insert(0, str(messages_path))

try:
    from contact_resolver import resolve_contact
except ImportError:
    print("Ошибка: не удалось импортировать contact_resolver")
    sys.exit(1)

# Путь к базе данных WhatsApp
DB_PATH = Path(__file__).parent / "node_modules" / "@iflow-mcp" / "whatsapp-mcp-ts" / "data" / "whatsapp.db"

def enrich_chats_with_names():
    """Обогащает чаты именами из macOS контактов"""
    if not DB_PATH.exists():
        print(f"База данных не найдена: {DB_PATH}")
        return
    
    conn = sqlite3.connect(str(DB_PATH))
    cursor = conn.cursor()
    
    # Получаем все чаты без имен или с именами, которые являются номерами
    cursor.execute("""
        SELECT jid, name 
        FROM chats
        WHERE name IS NULL 
           OR name = ''
           OR name = substr(jid, 1, instr(jid, '@') - 1)
    """)
    
    chats = cursor.fetchall()
    print(f"Найдено чатов для обогащения: {len(chats)}\n")
    
    updated = 0
    for jid, current_name in chats:
        # Извлекаем номер телефона
        phone_number = jid.split('@')[0]
        
        # Получаем имя через contact_resolver
        contact = resolve_contact(phone_number)
        name = contact.get("display_label", phone_number)
        
        # Если имя отличается от номера, обновляем
        if name != phone_number and name != current_name:
            cursor.execute("""
                UPDATE chats 
                SET name = ? 
                WHERE jid = ?
            """, (name, jid))
            print(f"✅ Обновлено: {jid} -> {name}")
            updated += 1
        else:
            print(f"⏭️  Пропущено: {jid} (имя не найдено или уже установлено)")
    
    conn.commit()
    conn.close()
    
    print(f"\n✅ Обновлено чатов: {updated}")

if __name__ == "__main__":
    enrich_chats_with_names()

