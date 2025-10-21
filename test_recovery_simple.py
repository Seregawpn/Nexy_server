#!/usr/bin/env python3
"""
Простой тест AudioRecoveryManager - проверка порогов восстановления.
"""

import asyncio
import logging
import numpy as np
import sounddevice as sd

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Импортируем наши модули
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'modules', 'voice_recognition', 'core'))

from audio_recovery_manager import AudioRecoveryManager


async def test_recovery_thresholds():
    """Тест порогов восстановления."""
    print("🚀 ТЕСТ ПОРОГОВ ВОССТАНОВЛЕНИЯ")
    print("=" * 50)
    
    # Получаем системное дефолтное устройство
    try:
        default_device = sd.default.device
        if hasattr(default_device, '__getitem__'):
            device_id = default_device[0]  # input device
        else:
            device_id = default_device
            
        if device_id is None:
            print("❌ Системное дефолтное устройство не установлено")
            return
            
        device_info = sd.query_devices(device_id)
        device_name = device_info['name']
        
    except Exception as e:
        print(f"❌ Ошибка получения дефолтного устройства: {e}")
        return
    
    print(f"🎧 Устройство: {device_name} (ID: {device_id})")
    
    # Создаем RecoveryManager
    recovery_manager = AudioRecoveryManager(device_id, device_name)
    
    # Симулируем пустые чанки
    silent_chunk = np.zeros((1024, 1), dtype='float32')
    
    print("\n📊 Симулируем пустые чанки и проверяем пороги:")
    
    for i in range(200):
        recovery_step = recovery_manager.on_chunk_received(silent_chunk, 0.0, 0.0)
        
        if recovery_step:
            print(f"  Порог {i+1}: {recovery_step.value}")
            
            # Симулируем выполнение восстановления
            async def mock_stream_callback(**kwargs):
                print(f"    🔧 Stream callback: {kwargs}")
                return True
            
            success = await recovery_manager.execute_recovery(recovery_step, mock_stream_callback)
            print(f"    Результат: {'✅' if success else '❌'}")
            
            if i >= 150:  # Останавливаем после порога D
                break
    
    # Показываем статистику
    print(f"\n📈 Статистика восстановления:")
    stats = recovery_manager.get_recovery_status()
    for key, value in stats.items():
        print(f"  {key}: {value}")


async def test_signal_recovery():
    """Тест восстановления сигнала."""
    print("\n🎉 ТЕСТ ВОССТАНОВЛЕНИЯ СИГНАЛА")
    print("=" * 50)
    
    # Получаем системное дефолтное устройство
    try:
        default_device = sd.default.device
        if hasattr(default_device, '__getitem__'):
            device_id = default_device[0]  # input device
        else:
            device_id = default_device
            
        if device_id is None:
            print("❌ Системное дефолтное устройство не установлено")
            return
            
        device_info = sd.query_devices(device_id)
        device_name = device_info['name']
        
    except Exception as e:
        print(f"❌ Ошибка получения дефолтного устройства: {e}")
        return
    
    print(f"🎧 Устройство: {device_name} (ID: {device_id})")
    
    # Создаем RecoveryManager
    recovery_manager = AudioRecoveryManager(device_id, device_name)
    
    # Симулируем 15 пустых чанков (порог A)
    silent_chunk = np.zeros((1024, 1), dtype='float32')
    signal_chunk = np.random.randn(1024, 1).astype('float32') * 0.1  # Слабый сигнал
    
    print("\n📊 Симулируем 15 пустых чанков:")
    for i in range(15):
        recovery_step = recovery_manager.on_chunk_received(silent_chunk, 0.0, 0.0)
        if recovery_step:
            print(f"  Порог {i+1}: {recovery_step.value}")
    
    print("\n🎉 Симулируем восстановление сигнала:")
    recovery_step = recovery_manager.on_chunk_received(signal_chunk, 0.1, 0.05)
    if recovery_step is None:
        print("  ✅ Сигнал восстановлен - recovery_step = None")
    
    # Показываем финальную статистику
    print(f"\n📈 Финальная статистика:")
    stats = recovery_manager.get_recovery_status()
    for key, value in stats.items():
        print(f"  {key}: {value}")


async def main():
    """Основная функция тестирования."""
    try:
        # Тест 1: Пороги восстановления
        await test_recovery_thresholds()
        
        # Тест 2: Восстановление сигнала
        await test_signal_recovery()
        
        print("\n✅ ВСЕ ТЕСТЫ ЗАВЕРШЕНЫ")
        
    except Exception as e:
        print(f"\n❌ ОШИБКА В ТЕСТАХ: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    asyncio.run(main())
