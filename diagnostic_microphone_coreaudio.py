#!/usr/bin/env python3
"""
Диагностический скрипт для проверки состояния CoreAudio и PortAudio
Проверяет, действительно ли macOS продолжает сообщать через CoreAudio/PortAudio,
что default-микрофон — это AirPods, даже если они уже не отображаются в настройках звука.
"""

import sys
import time
import logging
from pathlib import Path

# Добавляем пути к модулям
CLIENT_ROOT = Path(__file__).parent
sys.path.insert(0, str(CLIENT_ROOT))
sys.path.insert(0, str(CLIENT_ROOT / "modules"))
sys.path.insert(0, str(CLIENT_ROOT / "integration"))

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def check_coreaudio_devices():
    """Проверяет состояние аудио устройств через CoreAudio"""
    try:
        import sounddevice as sd
        
        logger.info("🔍 Проверяем состояние аудио устройств через PortAudio...")
        
        # Получаем список всех устройств
        devices = sd.query_devices()
        logger.info(f"📱 Найдено {len(devices)} аудио устройств:")
        
        for i, device in enumerate(devices):
            device_type = []
            if device.get('max_input_channels', 0) > 0:
                device_type.append("INPUT")
            if device.get('max_output_channels', 0) > 0:
                device_type.append("OUTPUT")
            
            logger.info(f"  {i}: {device.get('name', 'Unknown')} ({', '.join(device_type)})")
            logger.info(f"     - Input channels: {device.get('max_input_channels', 0)}")
            logger.info(f"     - Output channels: {device.get('max_output_channels', 0)}")
            logger.info(f"     - Default sample rate: {device.get('default_samplerate', 'N/A')}")
            logger.info(f"     - Host API: {device.get('hostapi', 'N/A')}")
        
        # Проверяем системные default устройства
        logger.info("\n🎯 Проверяем системные default устройства:")
        
        try:
            default_setting = sd.default.device
            logger.info(f"  sd.default.device: {default_setting}")
            
            if hasattr(default_setting, '__getitem__'):
                default_input = default_setting[0]
                default_output = default_setting[1] if len(default_setting) > 1 else None
                
                if default_input is not None:
                    try:
                        input_info = sd.query_devices(default_input, 'input')
                        logger.info(f"  Default INPUT: {default_input} - {input_info.get('name', 'Unknown')}")
                    except Exception as e:
                        logger.warning(f"  Default INPUT: {default_input} - Ошибка получения информации: {e}")
                
                if default_output is not None:
                    try:
                        output_info = sd.query_devices(default_output, 'output')
                        logger.info(f"  Default OUTPUT: {default_output} - {output_info.get('name', 'Unknown')}")
                    except Exception as e:
                        logger.warning(f"  Default OUTPUT: {default_output} - Ошибка получения информации: {e}")
        except Exception as e:
            logger.error(f"  Ошибка получения default устройств: {e}")
        
        # Проверяем host APIs
        logger.info("\n🔌 Проверяем Host APIs:")
        try:
            hostapis = sd.query_hostapis()
            for i, hostapi in enumerate(hostapis):
                logger.info(f"  {i}: {hostapi.get('name', 'Unknown')}")
                logger.info(f"     - Default input device: {hostapi.get('default_input_device', 'N/A')}")
                logger.info(f"     - Default output device: {hostapi.get('default_output_device', 'N/A')}")
        except Exception as e:
            logger.error(f"  Ошибка получения Host APIs: {e}")
        
        return True
        
    except ImportError:
        logger.error("❌ sounddevice не установлен")
        return False
    except Exception as e:
        logger.error(f"❌ Ошибка проверки CoreAudio: {e}")
        return False

def check_system_audio_settings():
    """Проверяет системные настройки звука через командную строку"""
    import subprocess
    
    logger.info("\n🔍 Проверяем системные настройки звука...")
    
    try:
        # Получаем текущее входное устройство
        result = subprocess.run(
            ["system_profiler", "SPAudioDataType", "-json"],
            capture_output=True,
            text=True,
            timeout=10
        )
        
        if result.returncode == 0:
            import json
            data = json.loads(result.stdout)
            
            logger.info("📱 Системные аудио устройства:")
            for item in data.get('SPAudioDataType', []):
                name = item.get('_name', 'Unknown')
                logger.info(f"  - {name}")
                
                # Проверяем, является ли это устройство по умолчанию
                if item.get('coreaudio_default_audio_system_device'):
                    logger.info(f"    ⭐ СИСТЕМНОЕ УСТРОЙСТВО ПО УМОЛЧАНИЮ")
                
                # Проверяем тип устройства
                if 'bluetooth' in name.lower() or 'airpods' in name.lower():
                    logger.info(f"    🔵 BLUETOOTH устройство")
                elif 'built-in' in name.lower() or 'internal' in name.lower():
                    logger.info(f"    🖥️ ВСТРОЕННОЕ устройство")
                elif 'iphone' in name.lower() or 'ipad' in name.lower():
                    logger.info(f"    📱 CONTINUITY устройство")
        else:
            logger.warning(f"⚠️ Не удалось получить системную информацию: {result.stderr}")
            
    except subprocess.TimeoutExpired:
        logger.error("❌ Таймаут при получении системной информации")
    except Exception as e:
        logger.error(f"❌ Ошибка проверки системных настроек: {e}")

def check_portaudio_cache():
    """Проверяет, можно ли сбросить кеш PortAudio"""
    try:
        import sounddevice as sd
        
        logger.info("\n🔄 Проверяем возможность сброса кеша PortAudio...")
        
        # Сохраняем текущие настройки
        original_default = sd.default.device
        
        # Пытаемся сбросить кеш
        logger.info("  Сбрасываем sd.default.device...")
        sd.default.device = (None, None)
        
        # Проверяем, изменились ли настройки
        new_default = sd.default.device
        logger.info(f"  Новые настройки: {new_default}")
        
        # Восстанавливаем оригинальные настройки
        sd.default.device = original_default
        logger.info(f"  Восстановлены оригинальные настройки: {sd.default.device}")
        
        return True
        
    except Exception as e:
        logger.error(f"❌ Ошибка сброса кеша PortAudio: {e}")
        return False

def main():
    """Главная функция диагностики"""
    logger.info("🚀 Запуск диагностики CoreAudio/PortAudio...")
    
    # Проверяем CoreAudio устройства
    coreaudio_ok = check_coreaudio_devices()
    
    # Проверяем системные настройки
    check_system_audio_settings()
    
    # Проверяем возможность сброса кеша
    cache_ok = check_portaudio_cache()
    
    logger.info("\n📊 Результаты диагностики:")
    logger.info(f"  CoreAudio/PortAudio: {'✅ OK' if coreaudio_ok else '❌ Ошибка'}")
    logger.info(f"  Сброс кеша PortAudio: {'✅ OK' if cache_ok else '❌ Ошибка'}")
    
    if coreaudio_ok and cache_ok:
        logger.info("\n✅ Диагностика завершена успешно")
        logger.info("💡 Рекомендации:")
        logger.info("  1. Если default-микрофон не соответствует системным настройкам,")
        logger.info("     попробуйте выполнить: sudo killall coreaudiod")
        logger.info("  2. После перезапуска CoreAudio проверьте настройки звука")
        logger.info("  3. Убедитесь, что Continuity-микрофон отключен")
    else:
        logger.error("\n❌ Диагностика выявила проблемы")
        logger.error("💡 Рекомендации:")
        logger.error("  1. Проверьте установку sounddevice: pip install sounddevice")
        logger.error("  2. Убедитесь, что у приложения есть разрешения на микрофон")
        logger.error("  3. Попробуйте перезапустить CoreAudio: sudo killall coreaudiod")

if __name__ == "__main__":
    main()
