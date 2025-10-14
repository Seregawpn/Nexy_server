#!/usr/bin/env python3
"""
Тест боевого слоя автопереключения
"""

import time
import logging
from autoswitch.battle_ready import BattleReadyAutoSwitch

# Настройка логирования
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def test_battle_ready():
    """Тестирует боевой слой"""
    print("⚔️  ТЕСТ БОЕВОГО СЛОЯ")
    print("=" * 50)
    
    # Создаем экземпляр
    autoswitch = BattleReadyAutoSwitch(logger_func=print)
    
    try:
        # Запускаем
        print("\n1️⃣ Запуск автопереключения...")
        autoswitch.start()
        
        # Ждем инициализации
        time.sleep(3)
        
        # Показываем статус
        print("\n2️⃣ Текущий статус:")
        status = autoswitch.get_status()
        for key, value in status.items():
            print(f"   {key}: {value}")
        
        # Тестируем принудительное переключение на AirPods
        print("\n3️⃣ Тестируем принудительное переключение на AirPods...")
        success = autoswitch.force_switch("Sergiy's AirPods")
        
        if success:
            print("✅ AirPods активированы успешно!")
        else:
            print("❌ AirPods не активированы")
        
        # Ждем и показываем финальный статус
        time.sleep(3)
        print("\n4️⃣ Финальный статус:")
        status = autoswitch.get_status()
        for key, value in status.items():
            print(f"   {key}: {value}")
        
        # Тестируем fallback на MacBook
        print("\n5️⃣ Тестируем fallback на MacBook...")
        autoswitch._fallback_builtin()
        
        time.sleep(2)
        
        # Финальный статус
        print("\n6️⃣ Финальный статус после fallback:")
        status = autoswitch.get_status()
        for key, value in status.items():
            print(f"   {key}: {value}")
        
    except KeyboardInterrupt:
        print("\n⏹️  Тест прерван пользователем")
    except Exception as e:
        print(f"\n❌ Ошибка в тесте: {e}")
    finally:
        # Останавливаем
        print("\n7️⃣ Остановка автопереключения...")
        autoswitch.stop()
        print("✅ Автопереключение остановлено")

def main():
    """Основная функция"""
    print("🎯 ТЕСТИРОВАНИЕ БОЕВОГО СЛОЯ")
    print("=" * 60)
    print("Цель: проверить работу с флаппингом HFP⇄A2DP")
    print("=" * 60)
    
    test_battle_ready()
    
    print("\n🎉 Тестирование завершено!")

if __name__ == "__main__":
    main()

"""
Тест боевого слоя автопереключения
"""

import time
import logging
from autoswitch.battle_ready import BattleReadyAutoSwitch

# Настройка логирования
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def test_battle_ready():
    """Тестирует боевой слой"""
    print("⚔️  ТЕСТ БОЕВОГО СЛОЯ")
    print("=" * 50)
    
    # Создаем экземпляр
    autoswitch = BattleReadyAutoSwitch(logger_func=print)
    
    try:
        # Запускаем
        print("\n1️⃣ Запуск автопереключения...")
        autoswitch.start()
        
        # Ждем инициализации
        time.sleep(3)
        
        # Показываем статус
        print("\n2️⃣ Текущий статус:")
        status = autoswitch.get_status()
        for key, value in status.items():
            print(f"   {key}: {value}")
        
        # Тестируем принудительное переключение на AirPods
        print("\n3️⃣ Тестируем принудительное переключение на AirPods...")
        success = autoswitch.force_switch("Sergiy's AirPods")
        
        if success:
            print("✅ AirPods активированы успешно!")
        else:
            print("❌ AirPods не активированы")
        
        # Ждем и показываем финальный статус
        time.sleep(3)
        print("\n4️⃣ Финальный статус:")
        status = autoswitch.get_status()
        for key, value in status.items():
            print(f"   {key}: {value}")
        
        # Тестируем fallback на MacBook
        print("\n5️⃣ Тестируем fallback на MacBook...")
        autoswitch._fallback_builtin()
        
        time.sleep(2)
        
        # Финальный статус
        print("\n6️⃣ Финальный статус после fallback:")
        status = autoswitch.get_status()
        for key, value in status.items():
            print(f"   {key}: {value}")
        
    except KeyboardInterrupt:
        print("\n⏹️  Тест прерван пользователем")
    except Exception as e:
        print(f"\n❌ Ошибка в тесте: {e}")
    finally:
        # Останавливаем
        print("\n7️⃣ Остановка автопереключения...")
        autoswitch.stop()
        print("✅ Автопереключение остановлено")

def main():
    """Основная функция"""
    print("🎯 ТЕСТИРОВАНИЕ БОЕВОГО СЛОЯ")
    print("=" * 60)
    print("Цель: проверить работу с флаппингом HFP⇄A2DP")
    print("=" * 60)
    
    test_battle_ready()
    
    print("\n🎉 Тестирование завершено!")

if __name__ == "__main__":
    main()
