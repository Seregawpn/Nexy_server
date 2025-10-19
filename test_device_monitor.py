#!/usr/bin/env python3
"""
Простой тест для проверки работы AudioDeviceMonitor
"""

import sys
import os
import time
import logging

# Добавляем путь к модулям
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'modules'))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'integration'))

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)

def test_device_monitor():
    """Тест монитора устройств"""
    try:
        from modules.voice_recognition.core.audio_device_monitor import AudioDeviceMonitor
        
        logger.info("🧪 Запуск теста AudioDeviceMonitor")
        
        # Создаем монитор
        monitor = AudioDeviceMonitor(check_interval=0.5)
        
        # Callback для отслеживания смены устройств
        device_changes = []
        
        def on_device_change(old_device, new_device):
            device_changes.append((old_device, new_device))
            logger.info(f"🔄 Callback: {old_device} -> {new_device}")
        
        monitor.set_device_change_callback(on_device_change)
        
        # Запускаем мониторинг
        logger.info("🚀 Запуск мониторинга...")
        monitor.start_monitoring()
        
        # Ждем некоторое время
        logger.info("⏳ Мониторинг работает 10 секунд...")
        time.sleep(10)
        
        # Останавливаем мониторинг
        logger.info("🛑 Остановка мониторинга...")
        monitor.stop_monitoring()
        
        # Результаты
        logger.info(f"📊 Результаты теста:")
        logger.info(f"   - Текущее устройство: {monitor.get_current_device()}")
        logger.info(f"   - Количество смен устройств: {len(device_changes)}")
        
        if device_changes:
            logger.info("   - Смены устройств:")
            for i, (old, new) in enumerate(device_changes):
                logger.info(f"     {i+1}. {old} -> {new}")
        else:
            logger.info("   - Смены устройств не обнаружено")
        
        logger.info("✅ Тест завершен успешно")
        return True
        
    except Exception as e:
        logger.error(f"❌ Ошибка в тесте: {e}")
        return False

def test_speech_recognizer_stabilization():
    """Тест стабилизации в SpeechRecognizer"""
    try:
        from modules.voice_recognition.core.speech_recognizer import SpeechRecognizer
        from modules.voice_recognition.config.default_config import DEFAULT_RECOGNITION_CONFIG
        
        logger.info("🧪 Запуск теста стабилизации SpeechRecognizer")
        
        # Создаем распознаватель
        recognizer = SpeechRecognizer(DEFAULT_RECOGNITION_CONFIG)
        
        # Проверяем инициализацию монитора
        logger.info(f"📊 Монитор устройств создан: {recognizer.device_monitor is not None}")
        logger.info(f"📊 Задержка стабилизации: {recognizer.stabilization_delay}с")
        logger.info(f"📊 Текущее устройство: {recognizer.device_monitor.get_current_device()}")
        
        # Симулируем смену устройства
        logger.info("🔄 Симуляция смены устройства...")
        recognizer._on_device_changed(1, 2)
        
        # Проверяем время последней смены
        logger.info(f"📊 Время последней смены: {recognizer.last_device_change_time}")
        
        logger.info("✅ Тест стабилизации завершен успешно")
        return True
        
    except Exception as e:
        logger.error(f"❌ Ошибка в тесте стабилизации: {e}")
        return False

if __name__ == "__main__":
    logger.info("🚀 Запуск тестов AudioDeviceMonitor")
    
    # Тест 1: Монитор устройств
    test1_result = test_device_monitor()
    
    # Тест 2: Стабилизация в SpeechRecognizer
    test2_result = test_speech_recognizer_stabilization()
    
    # Итоги
    logger.info("📊 Итоги тестирования:")
    logger.info(f"   - Тест монитора устройств: {'✅ ПРОЙДЕН' if test1_result else '❌ ПРОВАЛЕН'}")
    logger.info(f"   - Тест стабилизации: {'✅ ПРОЙДЕН' if test2_result else '❌ ПРОВАЛЕН'}")
    
    if test1_result and test2_result:
        logger.info("🎉 Все тесты пройдены успешно!")
        sys.exit(0)
    else:
        logger.error("💥 Некоторые тесты провалены")
        sys.exit(1)
