#!/usr/bin/env python3
"""
Быстрый тест аудио устройств

Автоматически тестирует все доступные устройства и выводит результаты
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
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


async def quick_test():
    """Быстрый тест всех аудио устройств"""
    print("🚀 Быстрый тест аудио устройств")
    print("=" * 50)
    
    # Создаем интерфейс
    interface = AudioDeviceInterface()
    
    try:
        # Инициализируем
        print("🔧 Инициализация...")
        if not await interface.initialize():
            print("❌ Ошибка инициализации")
            return False
        
        print("✅ Инициализация успешна")
        
        # Получаем информацию об устройствах
        print("\n📊 Информация об устройствах:")
        await interface.print_device_info()
        
        # Тестируем все устройства
        print("\n🧪 Тестирование устройств...")
        results = await interface.test_all_devices(test_duration_sec=0.5)
        
        if not results:
            print("❌ Нет устройств для тестирования")
            return False
        
        # Анализируем результаты
        successful = [r for r in results if r.success]
        failed = [r for r in results if not r.success]
        
        print(f"\n📈 Результаты тестирования:")
        print(f"   ✅ Успешных: {len(successful)}")
        print(f"   ❌ Неудачных: {len(failed)}")
        print(f"   📊 Общий процент успеха: {len(successful)/len(results)*100:.1f}%")
        
        # Показываем успешные устройства
        if successful:
            print(f"\n✅ Успешно работающие устройства:")
            for result in successful:
                print(f"   🎵 {result.device.name} ({result.device.type.value})")
                print(f"      Качество: {result.audio_quality_score:.2f}")
                print(f"      Время теста: {result.test_duration_ms:.1f} мс")
        
        # Показываем проблемные устройства
        if failed:
            print(f"\n❌ Проблемные устройства:")
            for result in failed:
                print(f"   🚫 {result.device.name} ({result.device.type.value})")
                print(f"      Ошибка: {result.error_message}")
        
        # Тестируем переключение на лучшие устройства
        print(f"\n🔄 Тестирование переключения на лучшие устройства:")
        
        best_input = await interface.get_best_input_device()
        if best_input:
            print(f"   🎤 Лучшее INPUT: {best_input.name}")
            success = await interface.switch_to_input_device(best_input.id)
            print(f"      Переключение: {'✅ Успешно' if success else '❌ Неудачно'}")
        
        best_output = await interface.get_best_output_device()
        if best_output:
            print(f"   🔊 Лучшее OUTPUT: {best_output.name}")
            success = await interface.switch_to_output_device(best_output.id)
            print(f"      Переключение: {'✅ Успешно' if success else '❌ Неудачно'}")
        
        # Финальный статус
        print(f"\n🎯 Финальный статус:")
        status = await interface.get_device_status()
        if "error" not in status:
            print(f"   Всего устройств: {status['total_devices']}")
            print(f"   INPUT устройств: {status['input_devices']}")
            print(f"   OUTPUT устройств: {status['output_devices']}")
            print(f"   BOTH устройств: {status['both_devices']}")
        
        print(f"\n🎉 Тест завершен успешно!")
        return True
        
    except Exception as e:
        print(f"❌ Ошибка во время теста: {e}")
        logger.exception("Детали ошибки:")
        return False
    
    finally:
        # Очищаем ресурсы
        await interface.cleanup()


async def main():
    """Главная функция"""
    success = await quick_test()
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n⏹️ Тест прерван пользователем")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Критическая ошибка: {e}")
        sys.exit(1)
