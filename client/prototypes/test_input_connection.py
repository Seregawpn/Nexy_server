#!/usr/bin/env python3
"""
Прототип 3: Подключение к устройству (Input через Google Speech Recognition)

Цель: Проверить, что мы можем подключиться к устройству через Google Speech Recognition
"""

import sys
import logging
import time
from pathlib import Path

# Добавляем путь к проекту
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

try:
    import speech_recognition as sr
    SPEECH_RECOGNITION_AVAILABLE = True
    logger.info("✅ speech_recognition доступен")
except ImportError:
    SPEECH_RECOGNITION_AVAILABLE = False
    logger.error("❌ speech_recognition не доступен")
    sys.exit(1)

try:
    import sounddevice as sd
    SOUNDDEVICE_AVAILABLE = True
except ImportError:
    SOUNDDEVICE_AVAILABLE = False
    logger.error("❌ sounddevice не доступен")
    sys.exit(1)

# Импортируем функции из предыдущих прототипов
try:
    from test_device_discovery import DeviceDiscoveryPrototype
    from test_device_mapping import DeviceMappingPrototype
    PROTOTYPES_AVAILABLE = True
except ImportError:
    PROTOTYPES_AVAILABLE = False
    logger.warning("⚠️ Предыдущие прототипы не доступны")


class InputConnectionPrototype:
    """Прототип для тестирования подключения к input устройству"""
    
    def __init__(self):
        self.device_discovery = DeviceDiscoveryPrototype() if PROTOTYPES_AVAILABLE else None
        self.device_mapping = DeviceMappingPrototype() if PROTOTYPES_AVAILABLE else None
        self.recognizer = sr.Recognizer()
        self.current_microphone = None
    
    def test_microphone_with_device_index(self, device_index: int, device_name: str) -> bool:
        """Тестирование микрофона с конкретным device_index"""
        try:
            logger.info(f"🎤 Тестирование микрофона: {device_name} (index: {device_index})")
            
            # Создаем Microphone с device_index
            microphone = sr.Microphone(device_index=device_index)
            
            # Проверяем доступность
            with microphone as source:
                # Adjust for ambient noise
                logger.info("  🔊 Калибровка для окружающего шума...")
                self.recognizer.adjust_for_ambient_noise(source, duration=1)
                
                # Пытаемся записать короткий фрагмент
                logger.info("  🎙️ Запись тестового фрагмента (2 секунды)...")
                audio = self.recognizer.record(source, duration=2)
                
                logger.info(f"  ✅ Запись успешна: {len(audio.frame_data)} байт")
                return True
                
        except Exception as e:
            logger.error(f"  ❌ Ошибка записи: {e}")
            return False
    
    def test_microphone_system_default(self) -> bool:
        """Тестирование микрофона с system default"""
        try:
            logger.info("🎤 Тестирование микрофона: System Default")
            
            microphone = sr.Microphone()  # System default
            
            with microphone as source:
                logger.info("  🔊 Калибровка для окружающего шума...")
                self.recognizer.adjust_for_ambient_noise(source, duration=1)
                
                logger.info("  🎙️ Запись тестового фрагмента (2 секунды)...")
                audio = self.recognizer.record(source, duration=2)
                
                logger.info(f"  ✅ Запись успешна: {len(audio.frame_data)} байт")
                return True
                
        except Exception as e:
            logger.error(f"  ❌ Ошибка записи: {e}")
            return False
    
    def test_device_switching(self) -> list:
        """Тестирование переключения между устройствами"""
        logger.info("\n🔄 Тестирование переключения между устройствами...")
        
        if not self.device_discovery or not self.device_mapping:
            logger.warning("⚠️ Предыдущие прототипы не доступны, пропускаем тест")
            return []
        
        # Получаем устройства
        if not self.device_discovery.setup_audio_session():
            return []
        
        avf_devices = self.device_discovery.get_input_devices()
        if len(avf_devices) < 2:
            logger.warning("⚠️ Недостаточно устройств для тестирования переключения")
            return []
        
        results = []
        
        for device in avf_devices[:3]:  # Тестируем первые 3 устройства
            name = device['name']
            channels = device.get('channels', 1)
            
            # Получаем маппинг
            mapping_result = self.device_mapping.find_portaudio_match(name, channels)
            
            if mapping_result['confidence'] in ("HIGH", "MEDIUM") and mapping_result['device_index'] is not None:
                device_index = mapping_result['device_index']
                success = self.test_microphone_with_device_index(device_index, name)
                results.append({
                    "device": name,
                    "device_index": device_index,
                    "success": success
                })
                
                # Пауза между переключениями
                time.sleep(1)
        
        return results
    
    def run_tests(self):
        """Запуск всех тестов"""
        logger.info("=" * 80)
        logger.info("ПРОТОТИП 3: Подключение к устройству (Input)")
        logger.info("=" * 80)
        
        success_count = 0
        total_tests = 0
        
        # Тест 1: System default
        logger.info("\n📋 Тест 1: System Default Microphone")
        total_tests += 1
        if self.test_microphone_system_default():
            success_count += 1
        
        # Тест 2: Конкретное устройство (если доступны прототипы)
        if self.device_discovery and self.device_mapping:
            logger.info("\n📋 Тест 2: Конкретное устройство через маппинг")
            
            if self.device_discovery.setup_audio_session():
                avf_devices = self.device_discovery.get_input_devices()
                
                if avf_devices:
                    device = avf_devices[0]
                    name = device['name']
                    channels = device.get('channels', 1)
                    
                    mapping_result = self.device_mapping.find_portaudio_match(name, channels)
                    
                    if mapping_result['confidence'] in ("HIGH", "MEDIUM") and mapping_result['device_index'] is not None:
                        total_tests += 1
                        if self.test_microphone_with_device_index(mapping_result['device_index'], name):
                            success_count += 1
                    else:
                        logger.warning(f"⚠️ Не удалось найти маппинг для {name}")
        
        # Тест 3: Переключение между устройствами
        logger.info("\n📋 Тест 3: Переключение между устройствами")
        switching_results = self.test_device_switching()
        if switching_results:
            total_tests += len(switching_results)
            success_count += sum(1 for r in switching_results if r['success'])
        
        # Итоги
        logger.info("\n" + "=" * 80)
        logger.info("ИТОГИ ТЕСТИРОВАНИЯ:")
        logger.info("=" * 80)
        logger.info(f"Всего тестов: {total_tests}")
        logger.info(f"Успешных: {success_count}")
        logger.info(f"Проваленных: {total_tests - success_count}")
        
        success_rate = (success_count / total_tests * 100) if total_tests > 0 else 0
        logger.info(f"\n📊 Успешность: {success_rate:.1f}%")
        
        success = success_rate >= 80.0 and total_tests > 0
        
        if success:
            logger.info("\n✅ ПРОТОТИП 3 ПРОЙДЕН: Подключение к устройствам работает")
        else:
            logger.error("\n❌ ПРОТОТИП 3 ПРОВАЛЕН: Есть проблемы с подключением")
        
        return success


def main():
    """Главная функция"""
    prototype = InputConnectionPrototype()
    success = prototype.run_tests()
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()

