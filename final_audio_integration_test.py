#!/usr/bin/env python3
"""
Финальный интеграционный тест аудио системы
Проверяет все компоненты в реальных условиях
"""

import asyncio
import logging
import sys
import time
from typing import List, Dict, Any

# Добавляем корневую директорию проекта в sys.path
sys.path.insert(0, '.')

from modules.audio_device_manager.core.audio_device_interface import AudioDeviceInterface
from modules.audio_device_manager.core.types import AudioDevice, DeviceType, DeviceStatus, DevicePriority

# Настройка логирования
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class FinalIntegrationTest:
    """Финальный интеграционный тест"""
    
    def __init__(self):
        self.interface = AudioDeviceInterface()
        self.test_results = {}
        
    async def run_all_tests(self):
        """Запуск всех интеграционных тестов"""
        print("🚀 ФИНАЛЬНЫЕ ИНТЕГРАЦИОННЫЕ ТЕСТЫ АУДИО СИСТЕМЫ")
        print("="*70)
        
        tests = [
            ("A", "Инициализация системы", self.test_system_initialization),
            ("B", "Обнаружение устройств", self.test_device_discovery),
            ("C", "Категоризация устройств", self.test_device_categorization),
            ("D", "Переключение устройств", self.test_device_switching),
            ("E", "Тестирование устройств", self.test_device_testing),
            ("F", "Интеграция с приложением", self.test_application_integration)
        ]
        
        passed = 0
        total = len(tests)
        
        for test_id, test_name, test_func in tests:
            print(f"\n🧪 Тест {test_id}: {test_name}")
            print("-" * 50)
            
            try:
                result = await test_func()
                if result:
                    print(f"✅ Тест {test_id} ПРОЙДЕН")
                    passed += 1
                else:
                    print(f"❌ Тест {test_id} ПРОВАЛЕН")
            except Exception as e:
                print(f"💥 Тест {test_id} ОШИБКА: {e}")
                logger.error(f"Ошибка в тесте {test_id}: {e}")
        
        print("\n" + "="*70)
        print(f"📊 РЕЗУЛЬТАТЫ: {passed}/{total} тестов пройдено")
        print(f"📈 Успешность: {(passed/total)*100:.1f}%")
        
        if passed == total:
            print("🎉 ВСЕ ТЕСТЫ ПРОЙДЕНЫ! СИСТЕМА ГОТОВА К ПРОДАКШЕНУ!")
        else:
            print("⚠️ ЕСТЬ ПРОБЛЕМЫ, ТРЕБУЕТСЯ ДОРАБОТКА")
        
        await self.interface.cleanup()
        return passed == total
    
    async def test_system_initialization(self) -> bool:
        """Тест A: Инициализация системы"""
        try:
            print("🔧 Инициализация AudioDeviceInterface...")
            success = await self.interface.initialize()
            
            if success:
                print("✅ Система инициализирована успешно")
                return True
            else:
                print("❌ Ошибка инициализации системы")
                return False
                
        except Exception as e:
            print(f"💥 Ошибка инициализации: {e}")
            return False
    
    async def test_device_discovery(self) -> bool:
        """Тест B: Обнаружение устройств"""
        try:
            print("🔍 Обнаружение всех устройств...")
            all_devices = await self.interface.get_all_devices()
            
            if len(all_devices) > 0:
                print(f"✅ Найдено {len(all_devices)} устройств")
                for device in all_devices:
                    print(f"   📱 {device.name} ({device.type.value})")
                return True
            else:
                print("❌ Устройства не найдены")
                return False
                
        except Exception as e:
            print(f"💥 Ошибка обнаружения: {e}")
            return False
    
    async def test_device_categorization(self) -> bool:
        """Тест C: Категоризация устройств"""
        try:
            print("📊 Категоризация устройств...")
            
            input_devices = await self.interface.get_input_devices()
            output_devices = await self.interface.get_output_devices()
            
            print(f"   🎤 INPUT устройств: {len(input_devices)}")
            print(f"   🔊 OUTPUT устройств: {len(output_devices)}")
            
            # Проверяем, что есть хотя бы одно устройство каждого типа
            has_input = len(input_devices) > 0
            has_output = len(output_devices) > 0
            
            if has_input and has_output:
                print("✅ Категоризация работает корректно")
                return True
            else:
                print("❌ Неполная категоризация устройств")
                return False
                
        except Exception as e:
            print(f"💥 Ошибка категоризации: {e}")
            return False
    
    async def test_device_switching(self) -> bool:
        """Тест D: Переключение устройств"""
        try:
            print("🔄 Тестирование переключения устройств...")
            
            # Получаем лучшие устройства
            best_input = await self.interface.get_best_input_device()
            best_output = await self.interface.get_best_output_device()
            
            if not best_input or not best_output:
                print("❌ Не найдены лучшие устройства для тестирования")
                return False
            
            print(f"   🎤 Лучшее INPUT: {best_input.name}")
            print(f"   🔊 Лучшее OUTPUT: {best_output.name}")
            
            # Тестируем переключение
            input_success = await self.interface.switch_to_input_device(best_input.id)
            output_success = await self.interface.switch_to_output_device(best_output.id)
            
            if input_success and output_success:
                print("✅ Переключение устройств работает")
                return True
            else:
                print("❌ Ошибки при переключении устройств")
                return False
                
        except Exception as e:
            print(f"💥 Ошибка переключения: {e}")
            return False
    
    async def test_device_testing(self) -> bool:
        """Тест E: Тестирование устройств"""
        try:
            print("🧪 Тестирование всех устройств...")
            
            all_devices = await self.interface.get_all_devices()
            successful_tests = 0
            
            for device in all_devices:
                print(f"   🔍 Тестирование: {device.name}")
                result = await self.interface.test_device_connection(device)
                
                if result.success:
                    successful_tests += 1
                    print(f"      ✅ Успешно ({result.test_duration_ms:.1f}мс)")
                else:
                    print(f"      ❌ Неудачно: {result.error_message}")
            
            success_rate = (successful_tests / len(all_devices)) * 100 if all_devices else 0
            print(f"📊 Успешность тестирования: {success_rate:.1f}% ({successful_tests}/{len(all_devices)})")
            
            # Считаем тест пройденным, если хотя бы 80% устройств работают
            return success_rate >= 80.0
                
        except Exception as e:
            print(f"💥 Ошибка тестирования: {e}")
            return False
    
    async def test_application_integration(self) -> bool:
        """Тест F: Интеграция с приложением"""
        try:
            print("🔗 Тестирование интеграции с приложением...")
            
            # Проверяем статус системы
            status = await self.interface.get_system_status()
            
            print(f"   📊 Всего устройств: {status['total_devices']}")
            print(f"   🎤 INPUT устройств: {status['input_devices_count']}")
            print(f"   🔊 OUTPUT устройств: {status['output_devices_count']}")
            print(f"   🎧 BOTH устройств: {status['both_devices_count']}")
            print(f"   🔄 Менеджер запущен: {status['is_manager_running']}")
            
            # Проверяем, что система полностью функциональна
            is_functional = (
                status['total_devices'] > 0 and
                status['input_devices_count'] > 0 and
                status['output_devices_count'] > 0 and
                status['is_manager_running']
            )
            
            if is_functional:
                print("✅ Интеграция с приложением работает")
                return True
            else:
                print("❌ Проблемы с интеграцией")
                return False
                
        except Exception as e:
            print(f"💥 Ошибка интеграции: {e}")
            return False

async def main():
    """Главная функция"""
    test_suite = FinalIntegrationTest()
    success = await test_suite.run_all_tests()
    
    if success:
        print("\n🎉 ВСЕ ИНТЕГРАЦИОННЫЕ ТЕСТЫ ПРОЙДЕНЫ!")
        print("🚀 АУДИО СИСТЕМА ГОТОВА К ПРОДАКШЕНУ!")
        sys.exit(0)
    else:
        print("\n⚠️ ЕСТЬ ПРОБЛЕМЫ В ИНТЕГРАЦИОННЫХ ТЕСТАХ")
        print("🔧 ТРЕБУЕТСЯ ДОРАБОТКА")
        sys.exit(1)

if __name__ == "__main__":
    asyncio.run(main())
