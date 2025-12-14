"""
Тест Решения 3: Hybrid Monitoring

Тестирование гибридного подхода (Core Audio Notifications + Polling).
"""

import logging
import time
import sys
import os

# Добавляем путь к модулям проекта
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../../'))

from solution_3_hybrid_monitoring.device_switcher_hybrid import HybridDeviceSwitcher

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)


def test_hybrid_monitoring():
    """Тест гибридного мониторинга"""
    logger.info("=" * 60)
    logger.info("ТЕСТ: Hybrid Monitoring (Core Audio + Polling)")
    logger.info("=" * 60)
    
    device_changes = []
    
    def on_device_changed(device_name: str, device_id: int, device_info: dict):
        """Callback для переключения устройства"""
        logger.info(f"🔄 Устройство изменилось:")
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
    
    switcher = HybridDeviceSwitcher(
        device_type="input",
        callback=on_device_changed,
        poll_interval=0.5,
        max_poll_interval=5.0,
        backoff_factor=1.5
    )
    
    logger.info("🚀 Запуск гибридного мониторинга устройств...")
    if switcher.start():
        logger.info("✅ Мониторинг запущен")
        logger.info("📋 Инструкции:")
        logger.info("   1. Переключите устройство в System Preferences > Sound")
        logger.info("   2. Или подключите/отключите наушники/микрофон")
        logger.info("   3. Нажмите Ctrl+C для остановки")
        logger.info("")
        
        try:
            while True:
                time.sleep(1)
                # Показываем текущее устройство каждые 5 секунд
                if len(device_changes) == 0 or (time.time() - device_changes[-1]["timestamp"]) > 5:
                    current_name, current_id = switcher.get_current_device()
                    logger.debug(f"📊 Текущее устройство: {current_name} (ID: {current_id})")
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
                logger.info(f"  {i}. {change['name']} (ID: {change['id']}) - {change['info'].get('source', 'unknown')}")
            logger.info("=" * 60)
    else:
        logger.error("❌ Не удалось запустить мониторинг")


if __name__ == "__main__":
    test_hybrid_monitoring()
