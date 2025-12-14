"""
Тест Решения 1: Core Audio Notifications

Тестирование переключения устройств через Core Audio Property Listeners.
"""

import logging
import time
import sys
import os

# Добавляем путь к модулям проекта
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../../'))

from solution_1_core_audio_notifications.device_switcher_core_audio import CoreAudioDeviceSwitcher

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)


def test_input_device_switching():
    """Тест переключения INPUT устройств"""
    logger.info("=" * 60)
    logger.info("ТЕСТ: Переключение INPUT устройств")
    logger.info("=" * 60)
    
    device_changes = []
    
    def on_input_device_changed(device_name: str, device_id: int, device_info: dict):
        """Callback для переключения INPUT устройства"""
        logger.info(f"🔄 INPUT устройство изменилось:")
        logger.info(f"   Имя: {device_name}")
        logger.info(f"   ID: {device_id}")
        logger.info(f"   Bluetooth: {device_info.get('is_bluetooth', False)}")
        logger.info(f"   Источник: {device_info.get('source', 'unknown')}")
        device_changes.append({
            "name": device_name,
            "id": device_id,
            "info": device_info,
            "timestamp": time.time()
        })
    
    switcher = CoreAudioDeviceSwitcher(
        device_type="input",
        callback=on_input_device_changed
    )
    
    logger.info("🚀 Запуск мониторинга INPUT устройств...")
    if switcher.start():
        logger.info("✅ Мониторинг запущен")
        logger.info("📋 Инструкции:")
        logger.info("   1. Переключите INPUT устройство в System Preferences > Sound > Input")
        logger.info("   2. Или подключите/отключите наушники/микрофон")
        logger.info("   3. Нажмите Ctrl+C для остановки")
        logger.info("")
        
        try:
            while True:
                time.sleep(1)
                # Показываем текущее устройство каждые 5 секунд
                if len(device_changes) == 0 or (time.time() - device_changes[-1]["timestamp"]) > 5:
                    current_name, current_id = switcher.get_current_device()
                    logger.debug(f"📊 Текущее INPUT устройство: {current_name} (ID: {current_id})")
        except KeyboardInterrupt:
            logger.info("\n🛑 Остановка мониторинга...")
            switcher.stop()
            logger.info("✅ Мониторинг остановлен")
            
            # Результаты
            logger.info("")
            logger.info("=" * 60)
            logger.info("РЕЗУЛЬТАТЫ ТЕСТА:")
            logger.info("=" * 60)
            logger.info(f"Всего переключений: {len(device_changes)}")
            for i, change in enumerate(device_changes, 1):
                logger.info(f"  {i}. {change['name']} (ID: {change['id']})")
            logger.info("=" * 60)
    else:
        logger.error("❌ Не удалось запустить мониторинг (используйте fallback на polling)")


def test_output_device_switching():
    """Тест переключения OUTPUT устройств"""
    logger.info("=" * 60)
    logger.info("ТЕСТ: Переключение OUTPUT устройств")
    logger.info("=" * 60)
    
    device_changes = []
    
    def on_output_device_changed(device_name: str, device_id: int, device_info: dict):
        """Callback для переключения OUTPUT устройства"""
        logger.info(f"🔄 OUTPUT устройство изменилось:")
        logger.info(f"   Имя: {device_name}")
        logger.info(f"   ID: {device_id}")
        logger.info(f"   Bluetooth: {device_info.get('is_bluetooth', False)}")
        logger.info(f"   Источник: {device_info.get('source', 'unknown')}")
        device_changes.append({
            "name": device_name,
            "id": device_id,
            "info": device_info,
            "timestamp": time.time()
        })
    
    switcher = CoreAudioDeviceSwitcher(
        device_type="output",
        callback=on_output_device_changed
    )
    
    logger.info("🚀 Запуск мониторинга OUTPUT устройств...")
    if switcher.start():
        logger.info("✅ Мониторинг запущен")
        logger.info("📋 Инструкции:")
        logger.info("   1. Переключите OUTPUT устройство в System Preferences > Sound > Output")
        logger.info("   2. Или подключите/отключите наушники/динамики")
        logger.info("   3. Нажмите Ctrl+C для остановки")
        logger.info("")
        
        try:
            while True:
                time.sleep(1)
                # Показываем текущее устройство каждые 5 секунд
                if len(device_changes) == 0 or (time.time() - device_changes[-1]["timestamp"]) > 5:
                    current_name, current_id = switcher.get_current_device()
                    logger.debug(f"📊 Текущее OUTPUT устройство: {current_name} (ID: {current_id})")
        except KeyboardInterrupt:
            logger.info("\n🛑 Остановка мониторинга...")
            switcher.stop()
            logger.info("✅ Мониторинг остановлен")
            
            # Результаты
            logger.info("")
            logger.info("=" * 60)
            logger.info("РЕЗУЛЬТАТЫ ТЕСТА:")
            logger.info("=" * 60)
            logger.info(f"Всего переключений: {len(device_changes)}")
            for i, change in enumerate(device_changes, 1):
                logger.info(f"  {i}. {change['name']} (ID: {change['id']})")
            logger.info("=" * 60)
    else:
        logger.error("❌ Не удалось запустить мониторинг (используйте fallback на polling)")


if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="Тест Core Audio Notifications")
    parser.add_argument(
        "--type",
        choices=["input", "output", "both"],
        default="both",
        help="Тип устройства для тестирования"
    )
    
    args = parser.parse_args()
    
    if args.type == "input" or args.type == "both":
        test_input_device_switching()
        if args.type == "both":
            logger.info("\n" + "=" * 60 + "\n")
            time.sleep(2)
    
    if args.type == "output" or args.type == "both":
        test_output_device_switching()
