#!/usr/bin/env python3
"""
Фокусный тест для AirPods - основная цель
"""

import time
import logging
from autoswitch import AutoSwitch, AudioCore

# Настройка логирования
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def test_airpods_specifically():
    """Тестирует именно AirPods"""
    print("🎧 ФОКУСНЫЙ ТЕСТ AIRPODS")
    print("=" * 50)
    
    core = AudioCore()
    
    # 1. Проверяем доступность AirPods
    print("\n1️⃣ ПРОВЕРКА ДОСТУПНОСТИ AIRPODS")
    print("-" * 40)
    
    inputs = core.list_inputs()
    outputs = core.list_outputs()
    
    airpods_input = None
    airpods_output = None
    
    for device in inputs:
        if "AirPods" in device:
            airpods_input = device
            print(f"✅ AirPods input найден: {device}")
            break
    
    for device in outputs:
        if "AirPods" in device:
            airpods_output = device
            print(f"✅ AirPods output найден: {device}")
            break
    
    if not airpods_input or not airpods_output:
        print("❌ AirPods не найдены в списке устройств")
        return False
    
    # 2. Тестируем сцепку IN+OUT
    print("\n2️⃣ ТЕСТ СЦЕПКИ IN+OUT")
    print("-" * 40)
    
    print("🔄 Устанавливаем сцепку IN+OUT на AirPods...")
    success = core.set_inout("Sergiy's AirPods")
    
    if success:
        print("✅ Сцепка установлена успешно")
        
        # Ждем стабилизации
        print("⏳ Ждем стабилизации (3 секунды)...")
        time.sleep(3)
        
        # 3. Проверяем health-check
        print("\n3️⃣ HEALTH-CHECK AIRPODS")
        print("-" * 40)
        
        print("🗣️  ГОВОРИТЕ В МИКРОФОН AIRPODS СЕЙЧАС!")
        print("⏳ Записываем 3 секунды...")
        
        is_working = core.is_device_working("Sergiy's AirPods")
        
        if is_working:
            print("🎉 УСПЕХ! AirPods микрофон работает!")
            print("✅ HFP профиль активирован!")
            return True
        else:
            print("❌ AirPods микрофон не работает (тишина)")
            print("⚠️  AirPods остались в A2DP режиме")
            return False
    else:
        print("❌ Не удалось установить сцепку")
        return False

def test_airpods_with_autoswitch():
    """Тестирует AirPods с автопереключением"""
    print("\n4️⃣ ТЕСТ С АВТОПЕРЕКЛЮЧЕНИЕМ")
    print("-" * 40)
    
    autoswitch = AutoSwitch(logger_func=print)
    
    try:
        # Запускаем автопереключение
        print("🚀 Запускаем автопереключение...")
        autoswitch.start()
        
        # Ждем инициализации
        time.sleep(2)
        
        # Принудительно переключаемся на AirPods
        print("🔄 Принудительное переключение на AirPods...")
        success = autoswitch.force_switch("Sergiy's AirPods")
        
        if success:
            print("✅ Автопереключение успешно")
            
            # Ждем стабилизации
            time.sleep(3)
            
            # Проверяем статус
            status = autoswitch.get_status()
            print(f"📊 Статус: {status['current_device']}")
            
            # Health-check
            print("🗣️  ГОВОРИТЕ В МИКРОФОН AIRPODS!")
            time.sleep(2)
            
            core = AudioCore()
            is_working = core.is_device_working("Sergiy's AirPods")
            
            if is_working:
                print("🎉 УСПЕХ! AirPods работают через автопереключение!")
                return True
            else:
                print("❌ AirPods не работают через автопереключение")
                return False
        else:
            print("❌ Автопереключение не удалось")
            return False
            
    finally:
        autoswitch.stop()

def main():
    """Основная функция"""
    print("🎯 ФОКУСНЫЙ ТЕСТ AIRPODS")
    print("=" * 60)
    print("Цель: проверить, работают ли AirPods как микрофон")
    print("=" * 60)
    
    # Тест 1: Прямая сцепка
    print("\n🔧 ТЕСТ 1: ПРЯМАЯ СЦЕПКА")
    success1 = test_airpods_specifically()
    
    # Тест 2: С автопереключением
    print("\n🤖 ТЕСТ 2: С АВТОПЕРЕКЛЮЧЕНИЕМ")
    success2 = test_airpods_with_autoswitch()
    
    # Итоги
    print("\n📊 ИТОГИ ТЕСТИРОВАНИЯ")
    print("=" * 40)
    print(f"Прямая сцепка: {'✅ УСПЕХ' if success1 else '❌ НЕ РАБОТАЕТ'}")
    print(f"Автопереключение: {'✅ УСПЕХ' if success2 else '❌ НЕ РАБОТАЕТ'}")
    
    if success1 or success2:
        print("\n🎉 AIRPODS РАБОТАЮТ!")
        print("✅ HFP профиль активирован")
        print("✅ Микрофон функционирует")
        print("✅ Готово к интеграции в приложение")
    else:
        print("\n❌ AIRPODS НЕ РАБОТАЮТ")
        print("⚠️  Остались в A2DP режиме")
        print("💡 Нужно активировать HFP профиль вручную")
    
    return success1 or success2

if __name__ == "__main__":
    main()

"""
Фокусный тест для AirPods - основная цель
"""

import time
import logging
from autoswitch import AutoSwitch, AudioCore

# Настройка логирования
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def test_airpods_specifically():
    """Тестирует именно AirPods"""
    print("🎧 ФОКУСНЫЙ ТЕСТ AIRPODS")
    print("=" * 50)
    
    core = AudioCore()
    
    # 1. Проверяем доступность AirPods
    print("\n1️⃣ ПРОВЕРКА ДОСТУПНОСТИ AIRPODS")
    print("-" * 40)
    
    inputs = core.list_inputs()
    outputs = core.list_outputs()
    
    airpods_input = None
    airpods_output = None
    
    for device in inputs:
        if "AirPods" in device:
            airpods_input = device
            print(f"✅ AirPods input найден: {device}")
            break
    
    for device in outputs:
        if "AirPods" in device:
            airpods_output = device
            print(f"✅ AirPods output найден: {device}")
            break
    
    if not airpods_input or not airpods_output:
        print("❌ AirPods не найдены в списке устройств")
        return False
    
    # 2. Тестируем сцепку IN+OUT
    print("\n2️⃣ ТЕСТ СЦЕПКИ IN+OUT")
    print("-" * 40)
    
    print("🔄 Устанавливаем сцепку IN+OUT на AirPods...")
    success = core.set_inout("Sergiy's AirPods")
    
    if success:
        print("✅ Сцепка установлена успешно")
        
        # Ждем стабилизации
        print("⏳ Ждем стабилизации (3 секунды)...")
        time.sleep(3)
        
        # 3. Проверяем health-check
        print("\n3️⃣ HEALTH-CHECK AIRPODS")
        print("-" * 40)
        
        print("🗣️  ГОВОРИТЕ В МИКРОФОН AIRPODS СЕЙЧАС!")
        print("⏳ Записываем 3 секунды...")
        
        is_working = core.is_device_working("Sergiy's AirPods")
        
        if is_working:
            print("🎉 УСПЕХ! AirPods микрофон работает!")
            print("✅ HFP профиль активирован!")
            return True
        else:
            print("❌ AirPods микрофон не работает (тишина)")
            print("⚠️  AirPods остались в A2DP режиме")
            return False
    else:
        print("❌ Не удалось установить сцепку")
        return False

def test_airpods_with_autoswitch():
    """Тестирует AirPods с автопереключением"""
    print("\n4️⃣ ТЕСТ С АВТОПЕРЕКЛЮЧЕНИЕМ")
    print("-" * 40)
    
    autoswitch = AutoSwitch(logger_func=print)
    
    try:
        # Запускаем автопереключение
        print("🚀 Запускаем автопереключение...")
        autoswitch.start()
        
        # Ждем инициализации
        time.sleep(2)
        
        # Принудительно переключаемся на AirPods
        print("🔄 Принудительное переключение на AirPods...")
        success = autoswitch.force_switch("Sergiy's AirPods")
        
        if success:
            print("✅ Автопереключение успешно")
            
            # Ждем стабилизации
            time.sleep(3)
            
            # Проверяем статус
            status = autoswitch.get_status()
            print(f"📊 Статус: {status['current_device']}")
            
            # Health-check
            print("🗣️  ГОВОРИТЕ В МИКРОФОН AIRPODS!")
            time.sleep(2)
            
            core = AudioCore()
            is_working = core.is_device_working("Sergiy's AirPods")
            
            if is_working:
                print("🎉 УСПЕХ! AirPods работают через автопереключение!")
                return True
            else:
                print("❌ AirPods не работают через автопереключение")
                return False
        else:
            print("❌ Автопереключение не удалось")
            return False
            
    finally:
        autoswitch.stop()

def main():
    """Основная функция"""
    print("🎯 ФОКУСНЫЙ ТЕСТ AIRPODS")
    print("=" * 60)
    print("Цель: проверить, работают ли AirPods как микрофон")
    print("=" * 60)
    
    # Тест 1: Прямая сцепка
    print("\n🔧 ТЕСТ 1: ПРЯМАЯ СЦЕПКА")
    success1 = test_airpods_specifically()
    
    # Тест 2: С автопереключением
    print("\n🤖 ТЕСТ 2: С АВТОПЕРЕКЛЮЧЕНИЕМ")
    success2 = test_airpods_with_autoswitch()
    
    # Итоги
    print("\n📊 ИТОГИ ТЕСТИРОВАНИЯ")
    print("=" * 40)
    print(f"Прямая сцепка: {'✅ УСПЕХ' if success1 else '❌ НЕ РАБОТАЕТ'}")
    print(f"Автопереключение: {'✅ УСПЕХ' if success2 else '❌ НЕ РАБОТАЕТ'}")
    
    if success1 or success2:
        print("\n🎉 AIRPODS РАБОТАЮТ!")
        print("✅ HFP профиль активирован")
        print("✅ Микрофон функционирует")
        print("✅ Готово к интеграции в приложение")
    else:
        print("\n❌ AIRPODS НЕ РАБОТАЮТ")
        print("⚠️  Остались в A2DP режиме")
        print("💡 Нужно активировать HFP профиль вручную")
    
    return success1 or success2

if __name__ == "__main__":
    main()
