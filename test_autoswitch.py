#!/usr/bin/env python3
"""
Тестовый скрипт для модуля автопереключения аудио устройств
"""

import time
import logging
from autoswitch import AutoSwitch, get_config

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

def test_autoswitch():
    """Тестирует модуль автопереключения"""
    print("🚀 ТЕСТ МОДУЛЯ AUTOSWITCH")
    print("=" * 50)
    
    # Создаем экземпляр AutoSwitch
    autoswitch = AutoSwitch(logger_func=print)
    
    try:
        # Запускаем автопереключение
        print("\n1️⃣ Запуск автопереключения...")
        autoswitch.start()
        
        # Ждем немного для инициализации
        time.sleep(2)
        
        # Показываем статус
        print("\n2️⃣ Текущий статус:")
        status = autoswitch.get_status()
        for key, value in status.items():
            print(f"   {key}: {value}")
        
        # Тестируем принудительное переключение
        print("\n3️⃣ Тестируем принудительное переключение...")
        
        # Пытаемся переключиться на AirPods
        if autoswitch.force_switch("Sergiy's AirPods"):
            print("✅ Успешно переключились на AirPods")
        else:
            print("❌ Не удалось переключиться на AirPods")
        
        time.sleep(2)
        
        # Пытаемся переключиться на MacBook микрофон
        if autoswitch.force_switch("MacBook Air Microphone"):
            print("✅ Успешно переключились на MacBook микрофон")
        else:
            print("❌ Не удалось переключиться на MacBook микрофон")
        
        # Ждем и показываем финальный статус
        time.sleep(3)
        print("\n4️⃣ Финальный статус:")
        status = autoswitch.get_status()
        for key, value in status.items():
            print(f"   {key}: {value}")
        
        # Тестируем сброс карантина
        print("\n5️⃣ Тестируем сброс карантина...")
        autoswitch.reset_quarantine()
        print("✅ Карантин сброшен")
        
    except KeyboardInterrupt:
        print("\n⏹️  Тест прерван пользователем")
    except Exception as e:
        print(f"\n❌ Ошибка в тесте: {e}")
    finally:
        # Останавливаем автопереключение
        print("\n6️⃣ Остановка автопереключения...")
        autoswitch.stop()
        print("✅ Автопереключение остановлено")

def test_manual_switching():
    """Тестирует ручное переключение устройств"""
    print("\n🔧 ТЕСТ РУЧНОГО ПЕРЕКЛЮЧЕНИЯ")
    print("=" * 40)
    
    from autoswitch import AudioCore
    
    core = AudioCore()
    
    # Показываем доступные устройства
    print("📱 Доступные input устройства:")
    inputs = core.list_inputs()
    for i, device in enumerate(inputs):
        print(f"   {i}: {device}")
    
    print("\n📱 Доступные output устройства:")
    outputs = core.list_outputs()
    for i, device in enumerate(outputs):
        print(f"   {i}: {device}")
    
    # Показываем текущие устройства
    print(f"\n🎤 Текущий input: {core.get_current_input()}")
    print(f"🔊 Текущий output: {core.get_current_output()}")
    
    # Тестируем health check
    print("\n🔍 Тестируем health check...")
    for device in inputs[:3]:  # Тестируем первые 3 устройства
        print(f"   Тестируем {device}...")
        is_working = core.is_device_working(device)
        print(f"   Результат: {'✅ работает' if is_working else '❌ не работает'}")

def main():
    """Основная функция"""
    print("🎯 ТЕСТИРОВАНИЕ МОДУЛЯ AUTOSWITCH")
    print("=" * 60)
    
    # Проверяем зависимости
    try:
        import sounddevice as sd
        import numpy as np
        print("✅ Зависимости установлены")
    except ImportError as e:
        print(f"❌ Отсутствуют зависимости: {e}")
        print("Установите: pip install sounddevice numpy")
        return
    
    # Проверяем SwitchAudioSource
    try:
        import subprocess
        result = subprocess.run(['SwitchAudioSource', '-h'], capture_output=True, text=True)
        if result.returncode == 0:
            print("✅ SwitchAudioSource доступен")
        else:
            print("❌ SwitchAudioSource недоступен")
            print("Установите: brew install switchaudio-osx")
            return
    except Exception as e:
        print(f"❌ Ошибка проверки SwitchAudioSource: {e}")
        return
    
    # Запускаем тесты
    test_manual_switching()
    test_autoswitch()
    
    print("\n🎉 Тестирование завершено!")

if __name__ == "__main__":
    main()

"""
Тестовый скрипт для модуля автопереключения аудио устройств
"""

import time
import logging
from autoswitch import AutoSwitch, get_config

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

def test_autoswitch():
    """Тестирует модуль автопереключения"""
    print("🚀 ТЕСТ МОДУЛЯ AUTOSWITCH")
    print("=" * 50)
    
    # Создаем экземпляр AutoSwitch
    autoswitch = AutoSwitch(logger_func=print)
    
    try:
        # Запускаем автопереключение
        print("\n1️⃣ Запуск автопереключения...")
        autoswitch.start()
        
        # Ждем немного для инициализации
        time.sleep(2)
        
        # Показываем статус
        print("\n2️⃣ Текущий статус:")
        status = autoswitch.get_status()
        for key, value in status.items():
            print(f"   {key}: {value}")
        
        # Тестируем принудительное переключение
        print("\n3️⃣ Тестируем принудительное переключение...")
        
        # Пытаемся переключиться на AirPods
        if autoswitch.force_switch("Sergiy's AirPods"):
            print("✅ Успешно переключились на AirPods")
        else:
            print("❌ Не удалось переключиться на AirPods")
        
        time.sleep(2)
        
        # Пытаемся переключиться на MacBook микрофон
        if autoswitch.force_switch("MacBook Air Microphone"):
            print("✅ Успешно переключились на MacBook микрофон")
        else:
            print("❌ Не удалось переключиться на MacBook микрофон")
        
        # Ждем и показываем финальный статус
        time.sleep(3)
        print("\n4️⃣ Финальный статус:")
        status = autoswitch.get_status()
        for key, value in status.items():
            print(f"   {key}: {value}")
        
        # Тестируем сброс карантина
        print("\n5️⃣ Тестируем сброс карантина...")
        autoswitch.reset_quarantine()
        print("✅ Карантин сброшен")
        
    except KeyboardInterrupt:
        print("\n⏹️  Тест прерван пользователем")
    except Exception as e:
        print(f"\n❌ Ошибка в тесте: {e}")
    finally:
        # Останавливаем автопереключение
        print("\n6️⃣ Остановка автопереключения...")
        autoswitch.stop()
        print("✅ Автопереключение остановлено")

def test_manual_switching():
    """Тестирует ручное переключение устройств"""
    print("\n🔧 ТЕСТ РУЧНОГО ПЕРЕКЛЮЧЕНИЯ")
    print("=" * 40)
    
    from autoswitch import AudioCore
    
    core = AudioCore()
    
    # Показываем доступные устройства
    print("📱 Доступные input устройства:")
    inputs = core.list_inputs()
    for i, device in enumerate(inputs):
        print(f"   {i}: {device}")
    
    print("\n📱 Доступные output устройства:")
    outputs = core.list_outputs()
    for i, device in enumerate(outputs):
        print(f"   {i}: {device}")
    
    # Показываем текущие устройства
    print(f"\n🎤 Текущий input: {core.get_current_input()}")
    print(f"🔊 Текущий output: {core.get_current_output()}")
    
    # Тестируем health check
    print("\n🔍 Тестируем health check...")
    for device in inputs[:3]:  # Тестируем первые 3 устройства
        print(f"   Тестируем {device}...")
        is_working = core.is_device_working(device)
        print(f"   Результат: {'✅ работает' if is_working else '❌ не работает'}")

def main():
    """Основная функция"""
    print("🎯 ТЕСТИРОВАНИЕ МОДУЛЯ AUTOSWITCH")
    print("=" * 60)
    
    # Проверяем зависимости
    try:
        import sounddevice as sd
        import numpy as np
        print("✅ Зависимости установлены")
    except ImportError as e:
        print(f"❌ Отсутствуют зависимости: {e}")
        print("Установите: pip install sounddevice numpy")
        return
    
    # Проверяем SwitchAudioSource
    try:
        import subprocess
        result = subprocess.run(['SwitchAudioSource', '-h'], capture_output=True, text=True)
        if result.returncode == 0:
            print("✅ SwitchAudioSource доступен")
        else:
            print("❌ SwitchAudioSource недоступен")
            print("Установите: brew install switchaudio-osx")
            return
    except Exception as e:
        print(f"❌ Ошибка проверки SwitchAudioSource: {e}")
        return
    
    # Запускаем тесты
    test_manual_switching()
    test_autoswitch()
    
    print("\n🎉 Тестирование завершено!")

if __name__ == "__main__":
    main()
