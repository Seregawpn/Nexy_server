#!/usr/bin/env python3
"""
Тесты для валидации baseline поведения текущей системы

Цель: Убедиться, что текущая система работает идеально в изолированной среде
и все известные проблемы воспроизводятся.
"""

import logging
import sys
import time
import sounddevice as sd
from typing import Optional, Dict, Any

# Импорты из прототипа
from device_params_normalizer import DeviceParamsNormalizer, InputParams, OutputParams
from audio_device_monitor import AudioDeviceMonitor

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def test_device_params_normalizer():
    """Тест нормализации параметров устройств"""
    logger.info("=" * 60)
    logger.info("ТЕСТ 1: DeviceParamsNormalizer")
    logger.info("=" * 60)
    
    normalizer = DeviceParamsNormalizer()
    
    # Тест OUTPUT нормализации
    logger.info("\n--- OUTPUT нормализация ---")
    try:
        default_output = sd.default.device
        if hasattr(default_output, '__getitem__'):
            output_id = default_output[1]
            output_info = sd.query_devices(output_id, 'output')
            if output_info:
                params = normalizer.select_output_params(output_info)
                logger.info(f"✅ OUTPUT нормализован: {params.sample_rate}Hz, {params.channels}ch")
                logger.info(f"   Исходный rate: {params.device_rate}Hz")
            else:
                logger.warning("⚠️ Не удалось получить OUTPUT устройство")
        else:
            logger.warning("⚠️ Не удалось получить default OUTPUT устройство")
    except Exception as e:
        logger.error(f"❌ Ошибка теста OUTPUT: {e}")
    
    # Тест INPUT нормализации
    logger.info("\n--- INPUT нормализация ---")
    try:
        default_input = sd.default.device
        if hasattr(default_input, '__getitem__'):
            input_id = default_input[0]
            input_info = sd.query_devices(input_id, 'input')
            if input_info:
                params = normalizer.select_input_params(input_info)
                logger.info(f"✅ INPUT нормализован: device_rate={params.device_rate}Hz, target_rate={params.target_rate}Hz, channels={params.channels}")
            else:
                logger.warning("⚠️ Не удалось получить INPUT устройство")
        else:
            logger.warning("⚠️ Не удалось получить default INPUT устройство")
    except Exception as e:
        logger.error(f"❌ Ошибка теста INPUT: {e}")
    
    logger.info("\n✅ Тест DeviceParamsNormalizer завершён\n")


def test_audio_device_monitor():
    """Тест мониторинга устройств"""
    logger.info("=" * 60)
    logger.info("ТЕСТ 2: AudioDeviceMonitor")
    logger.info("=" * 60)
    
    monitor = AudioDeviceMonitor(check_interval=0.5)
    
    # Проверка текущего устройства
    current_name = monitor.get_current_device_name()
    current_id = monitor.get_current_device()
    logger.info(f"Текущее устройство: \"{current_name}\" (ID: {current_id})")
    
    # Callback для отслеживания изменений
    changes = []
    def on_device_change(old_id, new_id):
        logger.info(f"🔄 Устройство изменилось: {old_id} → {new_id}")
        changes.append((old_id, new_id))
    
    monitor.set_device_change_callback(on_device_change)
    
    # Запуск мониторинга
    logger.info("\nЗапуск мониторинга на 10 секунд...")
    logger.info("Попробуйте подключить/отключить Bluetooth устройство")
    monitor.start_monitoring()
    
    try:
        time.sleep(10)
    except KeyboardInterrupt:
        logger.info("\nПрервано пользователем")
    finally:
        monitor.stop_monitoring()
    
    logger.info(f"\nЗафиксировано изменений: {len(changes)}")
    logger.info("✅ Тест AudioDeviceMonitor завершён\n")


def test_device_detection():
    """Тест определения устройств через разные источники"""
    logger.info("=" * 60)
    logger.info("ТЕСТ 3: Определение устройств")
    logger.info("=" * 60)
    
    # Метод 1: SwitchAudioSource
    logger.info("\n--- Метод 1: SwitchAudioSource ---")
    try:
        import subprocess
        import json
        
        result = subprocess.run(
            ['SwitchAudioSource', '-c', '-t', 'input', '-f', 'json'],
            capture_output=True,
            text=True,
            timeout=2
        )
        
        if result.returncode == 0:
            device_info = json.loads(result.stdout.strip())
            device_name = device_info.get('name', '')
            logger.info(f"✅ SwitchAudioSource: \"{device_name}\"")
        else:
            logger.warning("⚠️ SwitchAudioSource не доступен")
    except FileNotFoundError:
        logger.warning("⚠️ SwitchAudioSource не установлен")
    except Exception as e:
        logger.error(f"❌ Ошибка SwitchAudioSource: {e}")
    
    # Метод 2: PortAudio sd.default.device
    logger.info("\n--- Метод 2: PortAudio sd.default.device ---")
    try:
        default_setting = sd.default.device
        if hasattr(default_setting, '__getitem__'):
            input_id = default_setting[0]
            input_info = sd.query_devices(input_id, 'input')
            if input_info:
                device_name = input_info.get('name', 'Unknown')
                logger.info(f"✅ PortAudio default: \"{device_name}\" (ID: {input_id})")
            else:
                logger.warning("⚠️ Не удалось получить информацию об устройстве")
        else:
            logger.warning("⚠️ Не удалось получить default устройство")
    except Exception as e:
        logger.error(f"❌ Ошибка PortAudio: {e}")
    
    # Метод 3: Поиск по имени в PortAudio
    logger.info("\n--- Метод 3: Поиск по имени в PortAudio ---")
    try:
        # Получаем имя через SwitchAudioSource
        import subprocess
        import json
        
        result = subprocess.run(
            ['SwitchAudioSource', '-c', '-t', 'input', '-f', 'json'],
            capture_output=True,
            text=True,
            timeout=2
        )
        
        if result.returncode == 0:
            device_info = json.loads(result.stdout.strip())
            target_name = device_info.get('name', '')
            
            if target_name:
                # Ищем в PortAudio
                all_devices = sd.query_devices()
                found = False
                for idx, dev in enumerate(all_devices):
                    if dev.get('max_input_channels', 0) > 0:
                        if dev.get('name', '') == target_name:
                            logger.info(f"✅ Найдено в PortAudio: \"{target_name}\" → ID {idx}")
                            found = True
                            break
                
                if not found:
                    logger.warning(f"⚠️ Устройство \"{target_name}\" не найдено в PortAudio (известная проблема!)")
        else:
            logger.warning("⚠️ SwitchAudioSource не доступен для теста")
    except Exception as e:
        logger.error(f"❌ Ошибка поиска по имени: {e}")
    
    logger.info("\n✅ Тест определения устройств завершён\n")


def test_known_issues():
    """Тест известных проблем (должны воспроизводиться)"""
    logger.info("=" * 60)
    logger.info("ТЕСТ 4: Известные проблемы (baseline)")
    logger.info("=" * 60)
    
    logger.info("\n--- Проблема 1: Устаревший кэш PortAudio ---")
    logger.info("Ожидаемое поведение: Новые устройства могут не находиться сразу")
    logger.info("Проверка: Подключите BT устройство и проверьте, найдётся ли оно в PortAudio")
    
    logger.info("\n--- Проблема 2: Несинхронизация источников ---")
    logger.info("Ожидаемое поведение: SwitchAudioSource и PortAudio могут расходиться")
    logger.info("Проверка: Сравните результаты SwitchAudioSource и PortAudio")
    
    logger.info("\n--- Проблема 3: Race condition при подключении BT ---")
    logger.info("Ожидаемое поведение: При подключении BT устройство может не найтись сразу")
    logger.info("Проверка: Подключите BT устройство и сразу проверьте его наличие")
    
    logger.info("\n✅ Тест известных проблем завершён\n")


def main():
    """Главная функция запуска тестов"""
    logger.info("=" * 60)
    logger.info("ВАЛИДАЦИЯ BASELINE ПОВЕДЕНИЯ ТЕКУЩЕЙ СИСТЕМЫ")
    logger.info("=" * 60)
    logger.info("\nЦель: Убедиться, что текущая система работает идеально")
    logger.info("и все известные проблемы воспроизводятся.\n")
    
    try:
        # Тест 1: Нормализация параметров
        test_device_params_normalizer()
        
        # Тест 2: Мониторинг устройств
        test_audio_device_monitor()
        
        # Тест 3: Определение устройств
        test_device_detection()
        
        # Тест 4: Известные проблемы
        test_known_issues()
        
        logger.info("=" * 60)
        logger.info("✅ ВСЕ ТЕСТЫ ЗАВЕРШЕНЫ")
        logger.info("=" * 60)
        logger.info("\nЕсли все тесты прошли успешно, можно переходить к экспериментам")
        logger.info("с улучшениями в директории ../improvements/\n")
        
    except KeyboardInterrupt:
        logger.info("\n\nПрервано пользователем")
        sys.exit(0)
    except Exception as e:
        logger.error(f"\n❌ Критическая ошибка: {e}", exc_info=True)
        sys.exit(1)


if __name__ == "__main__":
    main()

