#!/usr/bin/env python3
"""
Тестовый скрипт для проверки подключения аудио устройств

Этот скрипт позволяет:
- Просмотреть все доступные аудио устройства
- Протестировать подключение к каждому устройству
- Переключиться на конкретное устройство
- Проверить работу INPUT и OUTPUT функций
"""

import asyncio
import sys
import logging
from pathlib import Path

# Добавляем путь к клиенту
sys.path.insert(0, str(Path(__file__).parent / "client"))

from modules.audio_device_manager.core.audio_device_interface import AudioDeviceInterface
from modules.audio_device_manager.core.types import DeviceType

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class AudioDeviceTester:
    """Класс для тестирования аудио устройств"""
    
    def __init__(self):
        self.interface = AudioDeviceInterface()
        self.initialized = False
    
    async def initialize(self):
        """Инициализация тестера"""
        print("🔧 Инициализация тестера аудио устройств...")
        
        success = await self.interface.initialize()
        if success:
            self.initialized = True
            print("✅ Тестер инициализирован успешно")
        else:
            print("❌ Ошибка инициализации тестера")
        
        return success
    
    async def show_menu(self):
        """Показать меню"""
        print("\n" + "="*60)
        print("🎵 ТЕСТЕР АУДИО УСТРОЙСТВ")
        print("="*60)
        print("1. Показать все устройства")
        print("2. Показать INPUT устройства")
        print("3. Показать OUTPUT устройства")
        print("4. Показать BOTH устройства")
        print("5. Протестировать все устройства")
        print("6. Протестировать конкретное устройство")
        print("7. Переключиться на устройство по имени")
        print("8. Показать статус системы")
        print("9. Выход")
        print("="*60)
    
    async def show_all_devices(self):
        """Показать все устройства"""
        print("\n🔍 Получение списка всех устройств...")
        await self.interface.print_device_info()
    
    async def show_input_devices(self):
        """Показать INPUT устройства"""
        print("\n🎤 INPUT устройства:")
        devices = await self.interface.get_available_devices(DeviceType.INPUT)
        
        if not devices:
            print("   Нет доступных INPUT устройств")
            return
        
        for i, device in enumerate(devices, 1):
            status_icon = "✅" if device.is_available else "❌"
            print(f"   {i:2d}. {status_icon} {device.name}")
            print(f"       ID: {device.id}")
            print(f"       Тип: {device.type.value}")
            print(f"       Приоритет: {device.priority.value}")
            print(f"       Каналы: {device.channels}")
            print()
    
    async def show_output_devices(self):
        """Показать OUTPUT устройства"""
        print("\n🔊 OUTPUT устройства:")
        devices = await self.interface.get_available_devices(DeviceType.OUTPUT)
        
        if not devices:
            print("   Нет доступных OUTPUT устройств")
            return
        
        for i, device in enumerate(devices, 1):
            status_icon = "✅" if device.is_available else "❌"
            print(f"   {i:2d}. {status_icon} {device.name}")
            print(f"       ID: {device.id}")
            print(f"       Тип: {device.type.value}")
            print(f"       Приоритет: {device.priority.value}")
            print(f"       Каналы: {device.channels}")
            print()
    
    async def show_both_devices(self):
        """Показать BOTH устройства"""
        print("\n🎧 BOTH устройства (INPUT + OUTPUT):")
        devices = await self.interface.get_available_devices(DeviceType.BOTH)
        
        if not devices:
            print("   Нет доступных BOTH устройств")
            return
        
        for i, device in enumerate(devices, 1):
            status_icon = "✅" if device.is_available else "❌"
            print(f"   {i:2d}. {status_icon} {device.name}")
            print(f"       ID: {device.id}")
            print(f"       Тип: {device.type.value}")
            print(f"       Приоритет: {device.priority.value}")
            print(f"       Каналы: {device.channels}")
            print()
    
    async def test_all_devices(self):
        """Протестировать все устройства"""
        print("\n🧪 Тестирование всех устройств...")
        
        results = await self.interface.test_all_devices(test_duration_sec=1.0)
        
        if not results:
            print("   Нет устройств для тестирования")
            return
        
        print(f"\n📊 Результаты тестирования ({len(results)} устройств):")
        print("-" * 80)
        
        successful = 0
        failed = 0
        
        for result in results:
            status_icon = "✅" if result.success else "❌"
            print(f"{status_icon} {result.device.name}")
            print(f"   Тип: {result.device.type.value}")
            print(f"   Время теста: {result.test_duration_ms:.1f} мс")
            
            if result.success:
                print(f"   Качество: {result.audio_quality_score:.2f}")
                successful += 1
            else:
                print(f"   Ошибка: {result.error_message}")
                failed += 1
            print()
        
        print(f"📈 Итого: {successful} успешных, {failed} неудачных")
    
    async def test_specific_device(self):
        """Протестировать конкретное устройство"""
        print("\n🎯 Тестирование конкретного устройства")
        
        # Показываем список устройств
        devices = await self.interface.get_available_devices()
        if not devices:
            print("   Нет доступных устройств")
            return
        
        print("Доступные устройства:")
        for i, device in enumerate(devices, 1):
            print(f"   {i:2d}. {device.name} ({device.type.value})")
        
        try:
            choice = input("\nВведите номер устройства (или 0 для отмены): ").strip()
            if choice == "0":
                return
            
            device_index = int(choice) - 1
            if 0 <= device_index < len(devices):
                device = devices[device_index]
                
                print(f"\n🧪 Тестирование устройства: {device.name}")
                result = await self.interface.test_device_connection(device, test_duration_sec=2.0)
                
                if result.success:
                    print(f"✅ Устройство работает корректно!")
                    print(f"   Время теста: {result.test_duration_ms:.1f} мс")
                    print(f"   Качество: {result.audio_quality_score:.2f}")
                else:
                    print(f"❌ Ошибка тестирования: {result.error_message}")
            else:
                print("❌ Неверный номер устройства")
                
        except ValueError:
            print("❌ Неверный ввод")
        except KeyboardInterrupt:
            print("\n⏹️ Тестирование прервано")
    
    async def switch_to_device(self):
        """Переключиться на устройство по имени"""
        print("\n🔄 Переключение на устройство")
        
        device_name = input("Введите имя устройства (или часть имени): ").strip()
        if not device_name:
            print("❌ Имя устройства не может быть пустым")
            return
        
        # Ищем устройство
        device = await self.interface.find_device_by_name(device_name)
        if not device:
            print(f"❌ Устройство с именем '{device_name}' не найдено")
            return
        
        print(f"Найдено устройство: {device.name} ({device.type.value})")
        
        # Выбираем тип переключения
        if device.type == DeviceType.INPUT:
            print("Устройство поддерживает только INPUT")
            success = await self.interface.switch_to_input_device(device.id)
        elif device.type == DeviceType.OUTPUT:
            print("Устройство поддерживает только OUTPUT")
            success = await self.interface.switch_to_output_device(device.id)
        elif device.type == DeviceType.BOTH:
            print("Устройство поддерживает INPUT и OUTPUT")
            choice = input("Переключить INPUT (i) или OUTPUT (o)? ").strip().lower()
            
            if choice == "i":
                success = await self.interface.switch_to_input_device(device.id)
            elif choice == "o":
                success = await self.interface.switch_to_output_device(device.id)
            else:
                print("❌ Неверный выбор")
                return
        else:
            print(f"❌ Неподдерживаемый тип устройства: {device.type}")
            return
        
        if success:
            print(f"✅ Успешно переключились на {device.name}")
        else:
            print(f"❌ Не удалось переключиться на {device.name}")
    
    async def show_system_status(self):
        """Показать статус системы"""
        print("\n📊 Статус системы аудио устройств:")
        
        status = await self.interface.get_device_status()
        
        if "error" in status:
            print(f"❌ Ошибка: {status['error']}")
            return
        
        print(f"   Всего устройств: {status['total_devices']}")
        print(f"   INPUT устройств: {status['input_devices']}")
        print(f"   OUTPUT устройств: {status['output_devices']}")
        print(f"   BOTH устройств: {status['both_devices']}")
        print(f"   Лучшее INPUT: {status['best_input_device'] or 'Не найдено'}")
        print(f"   Лучшее OUTPUT: {status['best_output_device'] or 'Не найдено'}")
    
    async def run(self):
        """Запуск интерактивного тестера"""
        if not await self.initialize():
            return
        
        try:
            while True:
                await self.show_menu()
                choice = input("Выберите опцию (1-9): ").strip()
                
                if choice == "1":
                    await self.show_all_devices()
                elif choice == "2":
                    await self.show_input_devices()
                elif choice == "3":
                    await self.show_output_devices()
                elif choice == "4":
                    await self.show_both_devices()
                elif choice == "5":
                    await self.test_all_devices()
                elif choice == "6":
                    await self.test_specific_device()
                elif choice == "7":
                    await self.switch_to_device()
                elif choice == "8":
                    await self.show_system_status()
                elif choice == "9":
                    print("👋 До свидания!")
                    break
                else:
                    print("❌ Неверный выбор. Попробуйте снова.")
                
                input("\nНажмите Enter для продолжения...")
        
        except KeyboardInterrupt:
            print("\n👋 Выход по Ctrl+C")
        except Exception as e:
            print(f"❌ Ошибка: {e}")
        finally:
            await self.interface.cleanup()


async def main():
    """Главная функция"""
    print("🎵 Запуск тестера аудио устройств...")
    
    tester = AudioDeviceTester()
    await tester.run()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n👋 Программа завершена")
    except Exception as e:
        print(f"❌ Критическая ошибка: {e}")
        sys.exit(1)
