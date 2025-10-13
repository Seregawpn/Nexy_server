#!/usr/bin/env python3
"""
Тест AudioDeviceManager - проверка обнаружения устройств, приоритетов и переключения
"""

import asyncio
import logging
import sys
import os
from typing import Dict, Any, Optional

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '.'))

from modules.audio_device_manager.core.device_manager import AudioDeviceManager
from modules.audio_device_manager.core.types import AudioDeviceManagerConfig, DeviceType, AudioDevice
from config.unified_config_loader import UnifiedConfigLoader

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class AudioDeviceManagerTester:
    """Тестер AudioDeviceManager"""
    
    def __init__(self):
        self.manager = None
        self.test_results = {}
        
    async def setup(self):
        """Настройка тестера"""
        logger.info("🔧 Настройка AudioDeviceManager...")
        
        # Загружаем конфигурацию
        config_loader = UnifiedConfigLoader()
        audio_config_data = config_loader.get_audio_config()
        
        # Создаем конфигурацию
        device_manager_config = audio_config_data['device_manager']
        config = AudioDeviceManagerConfig(
            auto_switch_enabled=device_manager_config.get('auto_switch_to_best', True),
            monitoring_interval=device_manager_config.get('cache_timeout', 5.0),
            switch_delay=device_manager_config.get('switch_delay', 0.5),
            user_preferences=device_manager_config.get('user_preferences', {}),
            macos_settings=device_manager_config.get('macos_settings', {}),
            separate_input_output_management=device_manager_config.get('separate_input_output_management', True),
            input_device_priorities=audio_config_data.get('input_device_priorities', {}),
            output_device_priorities=audio_config_data.get('output_device_priorities', {})
        )
        
        # Создаем менеджер
        self.manager = AudioDeviceManager(config)
        logger.info("✅ AudioDeviceManager настроен")
        
    async def test_device_discovery(self):
        """Тест обнаружения устройств"""
        logger.info("🔍 ТЕСТ: Обнаружение устройств")
        
        try:
            # Запускаем менеджер
            await self.manager.start()
            
            # Получаем все устройства
            all_devices = await self.manager.get_available_devices()
            logger.info(f"📱 Найдено {len(all_devices)} устройств")
            
            # Проверяем INPUT устройства
            input_devices = await self.manager.get_available_devices(DeviceType.INPUT)
            logger.info(f"🎤 INPUT устройств: {len(input_devices)}")
            for device in input_devices:
                logger.info(f"  - {device.name} (тип: {device.type.value}, приоритет: {device.priority.value}, portaudio_index: {device.portaudio_index})")
            
            # Проверяем OUTPUT устройства
            output_devices = await self.manager.get_available_devices(DeviceType.OUTPUT)
            logger.info(f"🔊 OUTPUT устройств: {len(output_devices)}")
            for device in output_devices:
                logger.info(f"  - {device.name} (тип: {device.type.value}, приоритет: {device.priority.value}, portaudio_index: {device.portaudio_index})")
            
            self.test_results['device_discovery'] = {
                'total_devices': len(all_devices),
                'input_devices': len(input_devices),
                'output_devices': len(output_devices),
                'success': len(all_devices) > 0
            }
            
            return len(all_devices) > 0
            
        except Exception as e:
            logger.error(f"❌ Ошибка обнаружения устройств: {e}")
            self.test_results['device_discovery'] = {'success': False, 'error': str(e)}
            return False
    
    async def test_device_priorities(self):
        """Тест приоритетов устройств"""
        logger.info("🎯 ТЕСТ: Приоритеты устройств")
        
        try:
            # Получаем лучшее INPUT устройство
            best_input = await self.manager.get_best_input_device()
            if best_input:
                logger.info(f"🏆 Лучшее INPUT устройство: {best_input.name} (приоритет: {best_input.priority.value})")
            else:
                logger.warning("⚠️ Нет INPUT устройств")
            
            # Получаем лучшее OUTPUT устройство
            best_output = await self.manager.get_best_output_device()
            if best_output:
                logger.info(f"🏆 Лучшее OUTPUT устройство: {best_output.name} (приоритет: {best_output.priority.value})")
            else:
                logger.warning("⚠️ Нет OUTPUT устройств")
            
            # Проверяем что MacBook Air Microphone имеет приоритет над iPhone Microphone
            input_devices = await self.manager.get_available_devices(DeviceType.INPUT)
            macbook_mic = None
            iphone_mic = None
            
            for device in input_devices:
                if 'macbook air microphone' in device.name.lower():
                    macbook_mic = device
                elif 'iphone' in device.name.lower() and 'microphone' in device.name.lower():
                    iphone_mic = device
            
            priority_correct = True
            if macbook_mic and iphone_mic:
                macbook_priority = self.manager._get_input_priority(macbook_mic)
                iphone_priority = self.manager._get_input_priority(iphone_mic)
                priority_correct = macbook_priority < iphone_priority
                logger.info(f"📊 Приоритеты: MacBook={macbook_priority}, iPhone={iphone_priority}, Корректно={priority_correct}")
            
            self.test_results['device_priorities'] = {
                'best_input': best_input.name if best_input else None,
                'best_output': best_output.name if best_output else None,
                'priority_correct': priority_correct,
                'success': best_input is not None and best_output is not None and priority_correct
            }
            
            return best_input is not None and best_output is not None and priority_correct
            
        except Exception as e:
            logger.error(f"❌ Ошибка тестирования приоритетов: {e}")
            self.test_results['device_priorities'] = {'success': False, 'error': str(e)}
            return False
    
    async def test_device_switching(self):
        """Тест переключения устройств"""
        logger.info("🔄 ТЕСТ: Переключение устройств")
        
        try:
            # Тестируем переключение на лучшее INPUT устройство
            input_switched = await self.manager.device_switcher.switch_to_best_input_device()
            logger.info(f"🎤 Переключение на лучшее INPUT: {'✅' if input_switched else '❌'}")
            
            # Тестируем переключение на лучшее OUTPUT устройство
            output_switched = await self.manager.device_switcher.switch_to_best_output_device()
            logger.info(f"🔊 Переключение на лучшее OUTPUT: {'✅' if output_switched else '❌'}")
            
            self.test_results['device_switching'] = {
                'input_switched': input_switched,
                'output_switched': output_switched,
                'success': input_switched and output_switched
            }
            
            return input_switched and output_switched
            
        except Exception as e:
            logger.error(f"❌ Ошибка переключения устройств: {e}")
            self.test_results['device_switching'] = {'success': False, 'error': str(e)}
            return False
    
    async def test_portaudio_mapping(self):
        """Тест маппинга portaudio_index"""
        logger.info("🗺️ ТЕСТ: Маппинг portaudio_index")
        
        try:
            devices = await self.manager.get_available_devices()
            devices_with_index = [d for d in devices if d.portaudio_index is not None]
            
            logger.info(f"📊 Устройств с portaudio_index: {len(devices_with_index)}/{len(devices)}")
            
            for device in devices_with_index:
                logger.info(f"  - {device.name}: portaudio_index={device.portaudio_index}")
            
            success = len(devices_with_index) > 0
            self.test_results['portaudio_mapping'] = {
                'devices_with_index': len(devices_with_index),
                'total_devices': len(devices),
                'success': success
            }
            
            return success
            
        except Exception as e:
            logger.error(f"❌ Ошибка маппинга portaudio_index: {e}")
            self.test_results['portaudio_mapping'] = {'success': False, 'error': str(e)}
            return False
    
    async def run_all_tests(self):
        """Запуск всех тестов"""
        logger.info("🚀 ЗАПУСК ТЕСТОВ AudioDeviceManager")
        
        await self.setup()
        
        tests = [
            ("Обнаружение устройств", self.test_device_discovery),
            ("Приоритеты устройств", self.test_device_priorities),
            ("Переключение устройств", self.test_device_switching),
            ("Маппинг portaudio_index", self.test_portaudio_mapping)
        ]
        
        results = {}
        for test_name, test_func in tests:
            logger.info(f"\n{'='*50}")
            logger.info(f"🧪 {test_name}")
            logger.info(f"{'='*50}")
            
            try:
                result = await test_func()
                results[test_name] = result
                logger.info(f"✅ {test_name}: {'ПРОЙДЕН' if result else 'ПРОВАЛЕН'}")
            except Exception as e:
                logger.error(f"❌ {test_name}: ОШИБКА - {e}")
                results[test_name] = False
        
        # Итоговый отчет
        logger.info(f"\n{'='*50}")
        logger.info("📊 ИТОГОВЫЙ ОТЧЕТ")
        logger.info(f"{'='*50}")
        
        passed = sum(1 for result in results.values() if result)
        total = len(results)
        
        for test_name, result in results.items():
            status = "✅ ПРОЙДЕН" if result else "❌ ПРОВАЛЕН"
            logger.info(f"  {test_name}: {status}")
        
        logger.info(f"\n🎯 РЕЗУЛЬТАТ: {passed}/{total} тестов пройдено")
        
        if passed == total:
            logger.info("🎉 ВСЕ ТЕСТЫ ПРОЙДЕНЫ!")
        else:
            logger.warning(f"⚠️ {total - passed} тестов провалено")
        
        return passed == total

async def main():
    """Главная функция"""
    tester = AudioDeviceManagerTester()
    success = await tester.run_all_tests()
    return 0 if success else 1

if __name__ == "__main__":
    exit_code = asyncio.run(main())
    sys.exit(exit_code)
