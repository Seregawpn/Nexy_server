#!/usr/bin/env python3
"""
Быстрый тест улучшенного логирования в activate_accessibility().
"""

import asyncio
import sys
from pathlib import Path

# Добавляем путь к модулям
sys.path.insert(0, str(Path(__file__).parent))

from modules.permissions.first_run.activator import activate_accessibility
from modules.permissions.first_run.status_checker import check_accessibility_status


async def main():
    print("\n" + "="*60)
    print("ТЕСТ: Улучшенное логирование activate_accessibility()")
    print("="*60)
    
    print("\n📊 Статус ДО вызова:")
    status_before = check_accessibility_status()
    print(f"  → {status_before.value}")
    
    print("\n🚀 Вызов activate_accessibility()...")
    print("-" * 60)
    
    result = await activate_accessibility()
    
    print("-" * 60)
    print(f"\n📊 Результат: {result}")
    
    print("\n📊 Статус ПОСЛЕ вызова:")
    status_after = check_accessibility_status()
    print(f"  → {status_after.value}")
    
    print("\n✅ Тест завершён. Проверьте логи выше на наличие:")
    print("   - Exit code helper'а с интерпретацией")
    print("   - Статус до/после вызова")
    print("   - Любые ошибки в stderr")
    
    return 0


if __name__ == "__main__":
    try:
        sys.exit(asyncio.run(main()))
    except KeyboardInterrupt:
        print("\n\n⚠️  Прервано пользователем")
        sys.exit(130)
