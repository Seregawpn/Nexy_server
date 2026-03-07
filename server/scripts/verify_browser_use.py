#!/usr/bin/env python3
"""
Скрипт для проверки регистрации browser_use модуля

Проверяет:
1. Установлены ли зависимости (browser-use, playwright)
2. Зарегистрирован ли модуль в ModuleCoordinator
3. Доступен ли модуль через координатор
"""

import sys
import asyncio
import logging
from pathlib import Path

# Добавляем путь к серверу
server_dir = Path(__file__).parent.parent
sys.path.insert(0, str(server_dir))

from config.unified_config import get_config
from integrations.service_integrations.module_coordinator import ModuleCoordinator
from integrations.core.module_factory import ModuleFactory

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


async def verify_browser_use():
    """Проверка регистрации browser_use модуля"""
    print("=" * 80)
    print("ПРОВЕРКА РЕГИСТРАЦИИ BROWSER_USE МОДУЛЯ")
    print("=" * 80)
    
    # 1. Проверка установки зависимостей
    print("\n1. Проверка зависимостей...")
    try:
        from browser_use import Agent, ChatGoogle
        print("   ✅ browser-use установлен")
        BROWSER_USE_AVAILABLE = True
    except ImportError as e:
        print(f"   ❌ browser-use не установлен: {e}")
        BROWSER_USE_AVAILABLE = False
        return False
    
    try:
        import playwright
        print("   ✅ playwright установлен")
    except ImportError as e:
        print(f"   ❌ playwright не установлен: {e}")
        return False
    
    # 2. Проверка создания модуля через ModuleFactory
    print("\n2. Проверка создания модуля через ModuleFactory...")
    try:
        module = ModuleFactory.create('browser_use')
        print(f"   ✅ Модуль создан: {module.name}")
    except Exception as e:
        print(f"   ❌ Ошибка создания модуля: {e}")
        return False
    
    # 3. Проверка регистрации в ModuleCoordinator
    print("\n3. Проверка регистрации в ModuleCoordinator...")
    try:
        unified_config = get_config()
        coordinator = ModuleCoordinator(unified_config.__dict__)
        
        # Получаем конфигурацию модуля
        module_config = unified_config.get_module_config('browser_use')
        
        # Регистрируем модуль
        success = await coordinator.register('browser_use', module, module_config)
        
        if success:
            print("   ✅ Модуль успешно зарегистрирован в координаторе")
        else:
            print("   ⚠️ Модуль зарегистрирован, но с предупреждениями")
        
        # Проверяем доступность через координатор
        if coordinator.has('browser_use'):
            print("   ✅ Модуль доступен через coordinator.has('browser_use')")
            browser_module = coordinator.get('browser_use')
            print(f"   ✅ Модуль получен через coordinator.get('browser_use'): {browser_module.name}")
            
            # Проверяем статус модуля
            status = browser_module.status()
            print(f"   ✅ Статус модуля: {status.state.value}, health: {status.health}")
        else:
            print("   ❌ Модуль НЕ доступен через координатор")
            return False
        
        # Очистка
        await coordinator.cleanup_all()
        
    except Exception as e:
        print(f"   ❌ Ошибка регистрации в координаторе: {e}")
        import traceback
        traceback.print_exc()
        return False
    
    print("\n" + "=" * 80)
    print("✅ ВСЕ ПРОВЕРКИ ПРОЙДЕНЫ УСПЕШНО")
    print("=" * 80)
    return True


if __name__ == "__main__":
    success = asyncio.run(verify_browser_use())
    sys.exit(0 if success else 1)
