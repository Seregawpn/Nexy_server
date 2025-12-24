#!/usr/bin/env python3
"""
Прототип 1: Поиск и определение устройств через AVFoundation

Цель: Проверить, что AVFoundation корректно находит устройства и мы можем их идентифицировать
"""

import sys
import logging
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
    from Foundation import NSNotificationCenter, NSObject
    from AVFoundation import AVAudioSession, AVAudioSessionPortOverride
    from PyObjC import objc
    PYOBJC_AVAILABLE = True
    logger.info("✅ PyObjC доступен")
except ImportError as e:
    PYOBJC_AVAILABLE = False
    logger.error(f"❌ PyObjC не доступен: {e}")
    sys.exit(1)


class DeviceDiscoveryPrototype:
    """Прототип для тестирования поиска устройств"""
    
    def __init__(self):
        self.session = None
        self.devices_found = []
    
    def setup_audio_session(self):
        """Настройка AVAudioSession"""
        try:
            self.session = AVAudioSession.sharedInstance()
            
            # Настройка категории
            error = None
            success = self.session.setCategory_withOptions_error_(
                "AVAudioSessionCategoryPlayAndRecord",
                AVAudioSessionCategoryOptionDefaultToSpeaker,
                error
            )
            
            if not success:
                logger.error("❌ Ошибка настройки категории AVAudioSession")
                return False
            
            # Активация сессии
            success = self.session.setActive_error_(True, error)
            if not success:
                logger.error("❌ Ошибка активации AVAudioSession")
                return False
            
            logger.info("✅ AVAudioSession настроен и активирован")
            return True
            
        except Exception as e:
            logger.error(f"❌ Ошибка настройки AVAudioSession: {e}")
            return False
    
    def get_input_devices(self):
        """Получение списка input устройств"""
        try:
            # Получаем доступные входы
            available_inputs = self.session.availableInputs()
            
            devices = []
            for input_port in available_inputs:
                port_name = input_port.portName()
                port_type = input_port.portType()
                uid = input_port.UID()
                
                # Получаем данные источника
                data_sources = input_port.dataSources()
                channels = 1  # По умолчанию
                if data_sources and len(data_sources) > 0:
                    # Пытаемся получить количество каналов
                    # Это может потребовать дополнительных вызовов
                    pass
                
                device_info = {
                    "name": port_name,
                    "uid": uid,
                    "type": port_type,
                    "channels": channels,
                }
                devices.append(device_info)
                logger.info(f"  📱 Найдено устройство: {port_name} (UID: {uid}, Type: {port_type})")
            
            return devices
            
        except Exception as e:
            logger.error(f"❌ Ошибка получения input устройств: {e}")
            return []
    
    def get_current_input(self):
        """Получение текущего input устройства"""
        try:
            current_route = self.session.currentRoute()
            inputs = current_route.inputs()
            
            if inputs and len(inputs) > 0:
                input_port = inputs[0]
                return {
                    "name": input_port.portName(),
                    "uid": input_port.UID(),
                    "type": input_port.portType(),
                }
            
            return None
            
        except Exception as e:
            logger.error(f"❌ Ошибка получения текущего input: {e}")
            return None
    
    def get_current_output(self):
        """Получение текущего output устройства"""
        try:
            current_route = self.session.currentRoute()
            outputs = current_route.outputs()
            
            if outputs and len(outputs) > 0:
                output_port = outputs[0]
                return {
                    "name": output_port.portName(),
                    "uid": output_port.UID(),
                    "type": output_port.portType(),
                }
            
            return None
            
        except Exception as e:
            logger.error(f"❌ Ошибка получения текущего output: {e}")
            return None
    
    def normalize_device_name(self, name: str) -> str:
        """Нормализация имени устройства"""
        normalized = name.strip()
        
        # Удаляем Bluetooth суффиксы
        suffixes = [" (Hands-Free)", " HFP", " Hands-Free", " Bluetooth"]
        for suffix in suffixes:
            if normalized.endswith(suffix):
                normalized = normalized[:-len(suffix)]
                break
        
        return normalized
    
    def detect_transport(self, name: str, port_type: str) -> str:
        """Определение типа транспорта"""
        name_lower = name.lower()
        type_lower = port_type.lower() if port_type else ""
        
        if "bluetooth" in name_lower or "bluetooth" in type_lower or "airpods" in name_lower:
            return "bluetooth"
        elif "usb" in name_lower or "usb" in type_lower:
            return "usb"
        elif "built-in" in name_lower or "builtin" in name_lower or "internal" in name_lower:
            return "built_in"
        else:
            return "unknown"
    
    def run_tests(self):
        """Запуск всех тестов"""
        logger.info("=" * 80)
        logger.info("ПРОТОТИП 1: Поиск и определение устройств")
        logger.info("=" * 80)
        
        # 1. Настройка сессии
        if not self.setup_audio_session():
            logger.error("❌ Не удалось настроить AVAudioSession")
            return False
        
        # 2. Получение input устройств
        logger.info("\n📥 Получение списка input устройств...")
        input_devices = self.get_input_devices()
        logger.info(f"✅ Найдено {len(input_devices)} input устройств")
        
        if len(input_devices) == 0:
            logger.warning("⚠️ Input устройства не найдены")
            return False
        
        # 3. Получение текущего input
        logger.info("\n📥 Получение текущего input устройства...")
        current_input = self.get_current_input()
        if current_input:
            logger.info(f"✅ Текущий input: {current_input['name']} (UID: {current_input['uid']})")
        else:
            logger.warning("⚠️ Текущий input не определен")
        
        # 4. Получение текущего output
        logger.info("\n📤 Получение текущего output устройства...")
        current_output = self.get_current_output()
        if current_output:
            logger.info(f"✅ Текущий output: {current_output['name']} (UID: {current_output['uid']})")
        else:
            logger.warning("⚠️ Текущий output не определен")
        
        # 5. Нормализация и определение транспорта
        logger.info("\n🔍 Нормализация имен и определение транспорта...")
        for device in input_devices:
            normalized = self.normalize_device_name(device['name'])
            transport = self.detect_transport(device['name'], device.get('type', ''))
            logger.info(f"  {device['name']} → {normalized} ({transport})")
        
        # 6. Итоги
        logger.info("\n" + "=" * 80)
        logger.info("ИТОГИ ТЕСТИРОВАНИЯ:")
        logger.info("=" * 80)
        logger.info(f"✅ Input устройств найдено: {len(input_devices)}")
        logger.info(f"✅ Текущий input определен: {current_input is not None}")
        logger.info(f"✅ Текущий output определен: {current_output is not None}")
        
        success = (
            len(input_devices) > 0 and
            current_input is not None and
            current_output is not None
        )
        
        if success:
            logger.info("\n✅ ПРОТОТИП 1 ПРОЙДЕН: Все проверки успешны")
        else:
            logger.error("\n❌ ПРОТОТИП 1 ПРОВАЛЕН: Есть проблемы")
        
        return success


def main():
    """Главная функция"""
    prototype = DeviceDiscoveryPrototype()
    success = prototype.run_tests()
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()

