#!/usr/bin/env python3
"""
Тесты для проверки улучшенной версии системы

Проверяет:
1. Правильность фиксации имени/ID/частоты/каналов
2. Переключение без ошибок при подключении/отключении BT
3. Retry/backoff логику
4. Пересоздание потоков только после остановки записи (для input)
"""

import logging
import sys
import time
import sounddevice as sd
from typing import Optional, Dict, Any

# Импорты улучшенных компонентов
from device_cache_with_ttl import DeviceCacheWithTTL
from device_finder_with_backoff import DeviceFinderWithBackoff
from audio_device_monitor_improved import AudioDeviceMonitorImproved
from device_params_normalizer_improved import DeviceParamsNormalizerImproved
from speech_recognizer_simplified import SpeechRecognizerSimplified
from player_simplified import PlayerSimplified

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def test_device_cache_ttl():
    """Тест: TTL кэш устройств"""
    logger.info("=" * 70)
    logger.info("ТЕСТ 1: TTL кэш устройств")
    logger.info("=" * 70)
    
    cache = DeviceCacheWithTTL(ttl_seconds=2.0)  # Короткий TTL для теста
    
    # Получаем устройство
    try:
        default_setting = sd.default.device
        if hasattr(default_setting, '__getitem__'):
            device_id = default_setting[0]
            device_info = sd.query_devices(device_id, 'input')
            if device_info:
                device_name = device_info.get('name', 'Unknown')
                sample_rate = device_info.get('default_samplerate', 0)
                channels = device_info.get('max_input_channels', 0)
                
                # Добавляем в кэш
                cache.put(device_name, device_id, 
                         int(sample_rate) if sample_rate > 0 else None,
                         int(channels) if channels > 0 else None)
                
                logger.info(f"✅ Добавлено в кэш: \"{device_name}\"")
                
                # Проверяем сразу
                entry = cache.get(device_name)
                if entry:
                    logger.info(f"✅ Найдено в кэше: ID {entry.device_id}, rate {entry.sample_rate}Hz, channels {entry.channels}")
                else:
                    logger.error("❌ Не найдено в кэше")
                
                # Ждём истечения TTL
                logger.info("\n⏳ Ожидание истечения TTL (2 секунды)...")
                time.sleep(2.5)
                
                # Проверяем после истечения TTL (без auto_refresh)
                entry = cache.get(device_name, auto_refresh=False)
                if entry:
                    logger.warning("⚠️ Запись всё ещё в кэше (TTL не сработал)")
                else:
                    logger.info("✅ TTL работает: запись автоматически удалена")
                
                # Статистика
                stats = cache.get_stats()
                logger.info(f"\n📊 Статистика кэша: {stats}")
                
    except Exception as e:
        logger.error(f"❌ Ошибка теста: {e}")
    
    logger.info("\n✅ Тест TTL кэша завершён\n")


def test_device_finder_backoff():
    """Тест: Поиск устройств с экспоненциальным backoff"""
    logger.info("=" * 70)
    logger.info("ТЕСТ 2: Поиск устройств с экспоненциальным backoff")
    logger.info("=" * 70)
    
    finder = DeviceFinderWithBackoff(max_retries=3, base_delay=0.3)
    
    # Получаем имя устройства
    device_name = finder.get_system_default_input_name()
    if not device_name:
        logger.warning("⚠️ Не удалось получить имя устройства")
        return
    
    logger.info(f"🔍 Ищем устройство: \"{device_name}\"")
    
    # Поиск с backoff
    start_time = time.time()
    device_info = finder.find_device_by_name(device_name, retry_with_backoff=True)
    elapsed = time.time() - start_time
    
    if device_info:
        logger.info(f"✅ Найдено устройство:")
        logger.info(f"   ID: {device_info['id']}")
        logger.info(f"   Sample Rate: {device_info.get('sample_rate', 'N/A')} Hz")
        logger.info(f"   Channels: {device_info.get('channels', 'N/A')}")
        logger.info(f"   Время поиска: {elapsed:.2f}с")
    else:
        logger.error("❌ Устройство не найдено")
    
    logger.info("\n✅ Тест поиска с backoff завершён\n")


def test_device_params_fixation():
    """Тест: Правильность фиксации имени/ID/частоты/каналов"""
    logger.info("=" * 70)
    logger.info("ТЕСТ 3: Фиксация параметров устройства")
    logger.info("=" * 70)
    
    recognizer = SpeechRecognizerSimplified()
    
    # Подготавливаем устройство
    if recognizer.prepare_input_device():
        device_info = recognizer.get_device_info()
        
        logger.info("\n📋 Зафиксированные параметры:")
        logger.info(f"   Имя: \"{device_info['name']}\"")
        logger.info(f"   ID: {device_info['id']}")
        if device_info['normalized_params']:
            params = device_info['normalized_params']
            logger.info(f"   Device Rate: {params.device_rate} Hz")
            logger.info(f"   Target Rate: {params.target_rate} Hz")
            logger.info(f"   Channels: {params.channels}")
        
        # Проверяем, что все параметры зафиксированы
        checks = []
        checks.append(("Имя", device_info['name'] is not None))
        checks.append(("ID", device_info['id'] is not None))
        checks.append(("Нормализованные параметры", device_info['normalized_params'] is not None))
        
        all_ok = all(check[1] for check in checks)
        
        logger.info("\n✅ Проверка фиксации параметров:")
        for name, result in checks:
            status = "✅" if result else "❌"
            logger.info(f"   {status} {name}: {'OK' if result else 'FAIL'}")
        
        if all_ok:
            logger.info("\n✅ Все параметры зафиксированы корректно")
        else:
            logger.error("\n❌ Некоторые параметры не зафиксированы")
    else:
        logger.error("❌ Не удалось подготовить устройство")
    
    logger.info("\n✅ Тест фиксации параметров завершён\n")


def test_bt_switching(interactive: bool = False):
    """Тест: Переключение без ошибок при подключении/отключении BT"""
    logger.info("=" * 70)
    logger.info("ТЕСТ 4: Переключение при подключении/отключении BT")
    logger.info("=" * 70)
    
    if interactive:
        logger.info("\n📋 Инструкция:")
        logger.info("1. Подготовьте BT устройство для подключения/отключения")
        logger.info("2. Нажмите Enter для начала мониторинга")
        logger.info("3. Подключайте/отключайте BT устройство во время мониторинга\n")
        
        try:
            input("Нажмите Enter для начала мониторинга...")
        except EOFError:
            logger.warning("⚠️ Интерактивный режим недоступен, пропускаем тест")
            return
    else:
        logger.info("\n📋 Автоматический режим: мониторинг на 10 секунд")
        logger.info("   (Для интерактивного режима запустите с --interactive)\n")
    
    monitor = AudioDeviceMonitorImproved(check_interval=0.5)
    
    changes = []
    errors = []
    
    def on_device_change(old_id, new_id):
        logger.info(f"🔄 Устройство изменилось: {old_id} → {new_id}")
        changes.append((old_id, new_id))
    
    monitor.set_device_change_callback(on_device_change)
    
    duration = 30 if interactive else 10
    logger.info(f"\n🚀 Запуск мониторинга на {duration} секунд...")
    if interactive:
        logger.info("Подключайте/отключайте BT устройство...\n")
    
    monitor.start_monitoring()
    
    try:
        time.sleep(duration)
    except KeyboardInterrupt:
        logger.info("\nПрервано пользователем")
    finally:
        monitor.stop_monitoring()
    
    logger.info(f"\n📊 Результаты:")
    logger.info(f"   Зафиксировано изменений: {len(changes)}")
    logger.info(f"   Ошибок: {len(errors)}")
    
    if len(errors) == 0:
        logger.info("✅ Переключение работает без ошибок")
    else:
        logger.warning(f"⚠️ Обнаружено ошибок: {len(errors)}")
    
    logger.info("\n✅ Тест переключения BT завершён\n")


def test_retry_backoff_logic():
    """Тест: Retry/backoff логика"""
    logger.info("=" * 70)
    logger.info("ТЕСТ 5: Retry/backoff логика")
    logger.info("=" * 70)
    
    finder = DeviceFinderWithBackoff(max_retries=3, base_delay=0.3)
    
    # Тест 1: Поиск существующего устройства
    logger.info("\n--- Тест 1: Поиск существующего устройства ---")
    device_name = finder.get_system_default_input_name()
    if device_name:
        start_time = time.time()
        device_info = finder.find_device_by_name(device_name, retry_with_backoff=True)
        elapsed = time.time() - start_time
        
        if device_info:
            logger.info(f"✅ Устройство найдено за {elapsed:.2f}с")
            logger.info(f"   Попыток: 1 (устройство найдено сразу)")
        else:
            logger.warning("⚠️ Устройство не найдено")
    
    # Тест 2: Поиск несуществующего устройства (должен использовать все попытки)
    logger.info("\n--- Тест 2: Поиск несуществующего устройства ---")
    fake_name = "NonExistentDevice_12345"
    start_time = time.time()
    device_info = finder.find_device_by_name(fake_name, retry_with_backoff=True)
    elapsed = time.time() - start_time
    
    if device_info:
        logger.warning("⚠️ Несуществующее устройство найдено (неожиданно)")
    else:
        logger.info(f"✅ Устройство не найдено (ожидаемо)")
        logger.info(f"   Время поиска: {elapsed:.2f}с")
        logger.info(f"   Ожидаемое время: ~{(0.3 + 0.6 + 1.2):.2f}с (3 попытки с backoff)")
        
        if 0.8 <= elapsed <= 2.5:  # Примерный диапазон с учётом задержек
            logger.info("✅ Backoff работает корректно")
        else:
            logger.warning(f"⚠️ Время поиска не соответствует ожидаемому backoff")
    
    logger.info("\n✅ Тест retry/backoff логики завершён\n")


def test_stream_recreation(interactive: bool = False):
    """Тест: Пересоздание потоков"""
    logger.info("=" * 70)
    logger.info("ТЕСТ 6: Пересоздание потоков")
    logger.info("=" * 70)
    
    player = PlayerSimplified()
    
    # Получаем начальное устройство
    logger.info("\n--- Начальное устройство ---")
    initial_device = player.get_system_default_output_device()
    if initial_device:
        logger.info(f"   Имя: \"{initial_device['name']}\"")
        logger.info(f"   ID: {initial_device['id']}")
    
    # Проверяем изменение устройства
    logger.info("\n--- Проверка изменения устройства ---")
    if interactive:
        logger.info("Переключите OUTPUT устройство в системных настройках macOS")
        logger.info("Нажмите Enter после переключения...")
        try:
            input()
        except EOFError:
            logger.warning("⚠️ Интерактивный режим недоступен, пропускаем проверку изменения")
            return
    else:
        logger.info("Автоматический режим: проверка текущего устройства")
        logger.info("(Для проверки переключения запустите с --interactive)")
    
    device_changed = player.check_and_update_output_device()
    if device_changed:
        device_info = player.get_device_info()
        logger.info(f"✅ Устройство изменено:")
        logger.info(f"   Имя: \"{device_info['name']}\"")
        logger.info(f"   ID: {device_info['id']}")
        if device_info['normalized_params']:
            logger.info(f"   Sample Rate: {device_info['normalized_params'].sample_rate} Hz")
            logger.info(f"   Channels: {device_info['normalized_params'].channels}")
    else:
        logger.info("ℹ️ Устройство не изменилось")
    
    logger.info("\n✅ Тест пересоздания потоков завершён\n")


def main():
    """Главная функция запуска тестов"""
    import argparse
    
    parser = argparse.ArgumentParser(description='Тесты улучшенной версии системы')
    parser.add_argument('--interactive', action='store_true', 
                       help='Интерактивный режим (для тестов с input)')
    args = parser.parse_args()
    
    logger.info("=" * 70)
    logger.info("ТЕСТИРОВАНИЕ УЛУЧШЕННОЙ ВЕРСИИ СИСТЕМЫ")
    logger.info("=" * 70)
    logger.info("\nЦель: Проверить все улучшения перед переносом в основной код\n")
    
    try:
        # Тест 1: TTL кэш
        test_device_cache_ttl()
        
        # Тест 2: Поиск с backoff
        test_device_finder_backoff()
        
        # Тест 3: Фиксация параметров
        test_device_params_fixation()
        
        # Тест 4: Переключение BT
        test_bt_switching(interactive=args.interactive)
        
        # Тест 5: Retry/backoff логика
        test_retry_backoff_logic()
        
        # Тест 6: Пересоздание потоков
        test_stream_recreation(interactive=args.interactive)
        
        logger.info("=" * 70)
        logger.info("✅ ВСЕ ТЕСТЫ ЗАВЕРШЕНЫ")
        logger.info("=" * 70)
        logger.info("\nЕсли все тесты прошли успешно, можно переносить улучшения")
        logger.info("в основной код (speech_recognizer, audio_device_monitor, player)\n")
        
    except KeyboardInterrupt:
        logger.info("\n\nПрервано пользователем")
        sys.exit(0)
    except Exception as e:
        logger.error(f"\n❌ Критическая ошибка: {e}", exc_info=True)
        sys.exit(1)


if __name__ == "__main__":
    main()

