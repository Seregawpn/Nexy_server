#!/usr/bin/env python3
"""
Тест AudioRecoveryManager - проверка автоматического восстановления аудио потока.
"""

import asyncio
import logging
import time
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

from audio_recovery_manager import AudioRecoveryManager, preflight_check, AudioConfig


async def test_preflight_check():
    """Тест preflight проверки."""
    print("\n🔍 ТЕСТ: Preflight Check")
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
    
    print(f"🎧 Тестируем устройство: {device_name} (ID: {device_id})")
    
    # Выполняем preflight проверку
    success, peak = await preflight_check(device_id, device_name, duration_ms=200)
    
    print(f"📊 Результат preflight:")
    print(f"  Success: {success}")
    print(f"  Peak: {peak:.6f}")
    
    if success:
        print("✅ Preflight check прошел успешно")
    else:
        print("❌ Preflight check не прошел - устройство возвращает тишину")


async def test_recovery_manager():
    """Тест RecoveryManager."""
    print("\n🔧 ТЕСТ: AudioRecoveryManager")
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
    
    print(f"🎧 Создаем RecoveryManager для: {device_name} (ID: {device_id})")
    
    # Создаем RecoveryManager
    recovery_manager = AudioRecoveryManager(device_id, device_name)
    
    # Тестируем пороги восстановления
    print("\n📊 Тестируем пороги восстановления:")
    
    # Симулируем пустые чанки
    silent_chunk = np.zeros((1024, 1), dtype='float32')
    
    for i in range(200):
        recovery_step = recovery_manager.on_chunk_received(silent_chunk, 0.0, 0.0)
        
        if recovery_step:
            print(f"  Порог {i+1}: {recovery_step.value}")
            
            # Симулируем выполнение восстановления
            async def mock_stream_callback(**kwargs):
                print(f"    Stream callback: {kwargs}")
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


async def test_audio_configs():
    """Тест различных конфигураций аудио."""
    print("\n🎛️ ТЕСТ: Audio Configurations")
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
    
    print(f"🎧 Тестируем конфигурации для: {device_name} (ID: {device_id})")
    
    # Тестируем различные конфигурации
    configs = [
        AudioConfig(48000, 1024, 'float32'),
        AudioConfig(44100, 1024, 'float32'),
        AudioConfig(44100, 512, 'int16'),
        AudioConfig(48000, 512, 'float32'),
    ]
    
    for config in configs:
        print(f"\n🔧 Тестируем конфигурацию: {config}")
        
        try:
            # Записываем короткий буфер с этой конфигурацией
            frames = int(config.samplerate * 0.1)  # 100ms
            audio_data = sd.rec(
                frames, 
                device=device_id, 
                samplerate=config.samplerate, 
                channels=config.channels,
                dtype=config.dtype
            )
            sd.wait()
            
            # Анализируем результат
            peak = float(np.abs(audio_data).max())
            rms = float(np.sqrt(np.mean(audio_data**2)))
            
            print(f"  Peak: {peak:.6f}")
            print(f"  RMS: {rms:.6f}")
            print(f"  Success: {'✅' if peak > 0.001 else '❌'}")
            
        except Exception as e:
            print(f"  Error: ❌ {e}")


async def test_ffmpeg_probe():
    """Тест ffmpeg probe."""
    print("\n🎬 ТЕСТ: FFmpeg Probe")
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
    
    print(f"🎧 Тестируем ffmpeg probe для: {device_name} (ID: {device_id})")
    
    # Создаем RecoveryManager
    recovery_manager = AudioRecoveryManager(device_id, device_name)
    
    # Выполняем ffmpeg probe
    print("🔍 Запускаем ffmpeg probe...")
    ffmpeg_ok = await recovery_manager._ffmpeg_probe_device()
    
    print(f"📊 Результат ffmpeg probe: {'✅' if ffmpeg_ok else '❌'}")
    
    if ffmpeg_ok:
        print("✅ FFmpeg слышит устройство - проблема в Python/CoreAudio")
    else:
        print("❌ FFmpeg тоже не слышит - требуется системное исправление")


async def main():
    """Основная функция тестирования."""
    print("🚀 ТЕСТИРОВАНИЕ AUDIO RECOVERY MANAGER")
    print("=" * 60)
    
    try:
        # Тест 1: Preflight check
        await test_preflight_check()
        
        # Тест 2: RecoveryManager
        await test_recovery_manager()
        
        # Тест 3: Audio configurations
        await test_audio_configs()
        
        # Тест 4: FFmpeg probe
        await test_ffmpeg_probe()
        
        print("\n✅ ВСЕ ТЕСТЫ ЗАВЕРШЕНЫ")
        
    except Exception as e:
        print(f"\n❌ ОШИБКА В ТЕСТАХ: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    asyncio.run(main())
