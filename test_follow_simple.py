#!/usr/bin/env python3
"""
Тест упрощенной системы "Follow System Only"
"""

import time
import signal
import sys
from audio_default.core.manager_follow import FollowSystemAudioManager


def signal_handler(sig, frame):
    """Обработчик Ctrl+C"""
    print("\n⏹️ Тест прерван пользователем")
    if 'manager' in globals():
        manager.stop()
    sys.exit(0)


def main():
    """Основная функция теста"""
    print("🔧 ТЕСТ FOLLOW SYSTEM AUDIO MANAGER")
    print("=" * 60)
    print("🎯 Цель: Простое следование системному дефолту")
    print("🔧 Принцип: device=None, BT grace, 1 retry, без магии")
    
    # Устанавливаем обработчик сигналов
    signal.signal(signal.SIGINT, signal_handler)
    
    # Создаем менеджер
    global manager
    manager = FollowSystemAudioManager()
    
    try:
        # Запускаем менеджер
        print("\n🚀 Запуск упрощенного менеджера...")
        manager.start()
        
        print("\n📊 ИНСТРУКЦИЯ ДЛЯ ТЕСТА:")
        print("=" * 60)
        print("1. ✅ Старт без BT - должен открыться встроенный микрофон")
        print("2. 🎧 Подключение AirPods - должен переключиться автоматически")
        print("3. 🔄 Быстрый reconnect AirPods - без ошибок")
        print("4. 🎧 Отключение AirPods - возврат на встроенный микрофон")
        print("5. ⏹️ Нажмите Ctrl+C для остановки")
        print("\n🔧 УПРОЩЕННАЯ СИСТЕМА АКТИВНА!")
        print("=" * 60)
        
        # Основной цикл
        while True:
            # Показываем статус каждые 10 секунд
            status = manager.get_status()
            print(f"\n📊 СТАТУС: {time.strftime('%H:%M:%S')}")
            print("-" * 50)
            print(f"🔄 Запущен: {status['running']}")
            print(f"🎤 Поток активен: {status['stream_active']}")
            print(f"🆔 Текущий UID: {status['current_uid']}")
            print(f"📥 Размер очереди: {status['queue_size']}")
            
            time.sleep(10)
            
    except KeyboardInterrupt:
        print("\n⏹️ Тест прерван пользователем")
    except Exception as e:
        print(f"\n❌ Ошибка теста: {e}")
    finally:
        print("\n🛑 Остановка упрощенного менеджера...")
        manager.stop()
        print("✅ Тест завершен")


if __name__ == "__main__":
    main()

