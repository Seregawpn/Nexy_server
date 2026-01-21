#!/usr/bin/env python3
"""
Комплексный интеграционный тест нормализации

Проверяет:
1. Нормализацию параметров реальных устройств
2. Конвертацию аудио данных
3. Реальное воспроизведение с нормализацией
4. Переключение устройств с автоматической нормализацией
"""

import logging
import time
import sounddevice as sd
import numpy as np
from device_params_normalizer import DeviceParamsNormalizer
from audio_converter import AudioConverter
from test_player import TestPlayer, PlayerConfig

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def test_device_normalization_real():
    """Тест нормализации реальных устройств"""
    print("=" * 70)
    print("ТЕСТ 1: Нормализация реальных устройств")
    print("=" * 70)
    print("")
    
    config = {
        'output_min_rate': 16000,
        'output_max_rate': 48000,
        'output_default_rate': 48000,
        'output_max_channels': 2,
    }
    
    normalizer = DeviceParamsNormalizer(config)
    
    # Получаем default OUTPUT устройство
    try:
        default = sd.default.device
        if hasattr(default, '__getitem__'):
            device_id = default[1]
            device_info = sd.query_devices(device_id, 'output')
            
            device_name = device_info.get('name', 'Unknown')
            raw_rate = device_info.get('default_samplerate', 0)
            raw_channels = device_info.get('max_output_channels', 0)
            
            print(f"🔍 Текущее OUTPUT устройство: \"{device_name}\" (ID={device_id})")
            print(f"   Исходные параметры: {raw_rate} Hz, {raw_channels} каналов")
            
            # Нормализуем
            normalized = normalizer.select_output_params(device_info)
            
            print(f"   ✅ Нормализовано: {normalized.sample_rate} Hz, {normalized.channels} каналов")
            
            # Проверяем что параметры в допустимом диапазоне
            assert 16000 <= normalized.sample_rate <= 48000, f"Sample rate вне диапазона: {normalized.sample_rate}"
            assert normalized.channels in (1, 2), f"Channels не 1 или 2: {normalized.channels}"
            
            print(f"   ✅ Параметры в допустимом диапазоне")
            print("")
            
            return True
        else:
            print("⚠️ Не удалось получить default устройство")
            return False
    except Exception as e:
        print(f"❌ Ошибка: {e}")
        return False


def test_audio_conversion_real():
    """Тест конвертации аудио с реальными параметрами"""
    print("=" * 70)
    print("ТЕСТ 2: Конвертация аудио данных")
    print("=" * 70)
    print("")
    
    converter = AudioConverter()
    
    # Симуляция: TTS выдаёт 24 kHz mono, устройство хочет 48 kHz stereo
    internal_rate = 24000
    device_rate = 48000
    internal_channels = 1
    device_channels = 2
    
    # Генерируем тестовый сигнал (0.5 секунды, 440 Hz синусоида)
    duration = 0.5
    t = np.linspace(0, duration, int(internal_rate * duration))
    tts_audio = np.sin(2 * np.pi * 440 * t).astype(np.float32)
    
    print(f"📊 Внутренний формат (TTS): {len(tts_audio)} samples, {internal_rate} Hz, {internal_channels} ch")
    
    # Конвертируем
    device_audio = converter.convert_for_output(
        tts_audio,
        internal_rate=internal_rate,
        device_rate=device_rate,
        internal_channels=internal_channels,
        device_channels=device_channels
    )
    
    print(f"📊 Формат устройства: {device_audio.shape}, {device_rate} Hz, {device_channels} ch")
    
    # Проверяем
    expected_length = int(device_rate * duration)
    actual_length = device_audio.shape[0]
    
    assert device_audio.shape[1] == device_channels, f"Неверное количество каналов: {device_audio.shape[1]}"
    assert abs(actual_length - expected_length) < 50, f"Неверная длина: {actual_length} vs {expected_length}"
    
    print(f"   ✅ Форма корректна: {device_audio.shape}")
    print(f"   ✅ Длина корректна: {actual_length} (ожидалось ~{expected_length})")
    print("")
    
    return True


def test_playback_with_normalization():
    """Тест реального воспроизведения с нормализацией"""
    print("=" * 70)
    print("ТЕСТ 3: Реальное воспроизведение с нормализацией")
    print("=" * 70)
    print("")
    
    # Создаём плеер
    config = PlayerConfig(
        sample_rate=24000,  # Внутренний формат (будет нормализован)
        channels=1,
        dtype='int16',
        buffer_size=512
    )
    
    player = TestPlayer(config, enable_realtime_monitoring=False)
    
    try:
        # Генерируем тестовый сигнал (1 секунда, 440 Hz)
        duration = 1.0
        internal_rate = 24000
        t = np.linspace(0, duration, int(internal_rate * duration))
        audio_data = (np.sin(2 * np.pi * 440 * t) * 0.3).astype(np.float32)
        
        # Конвертируем в int16
        audio_int16 = (audio_data * 32767).astype(np.int16)
        
        print(f"📊 Генерируем тестовый сигнал: {len(audio_int16)} samples, {internal_rate} Hz, mono")
        print(f"   Частота: 440 Hz (нота A4)")
        print("")
        
        # Добавляем аудио в плеер
        session_id = "test_session_1"
        print(f"▶️  Начинаем воспроизведение (session_id={session_id})...")
        player.add_audio_data(audio_int16, metadata={'session_id': session_id})
        
        # Ждём пока воспроизведение завершится
        time.sleep(duration + 0.5)
        
        # Проверяем что поток создан и параметры нормализованы
        if player._normalized_params:
            print(f"✅ Параметры нормализованы:")
            print(f"   Sample Rate: {player._normalized_params.sample_rate} Hz")
            print(f"   Channels: {player._normalized_params.channels}")
            print(f"   Device Rate: {player._normalized_params.device_rate or 'N/A'}")
        
        print("✅ Воспроизведение завершено")
        print("")
        
        # Останавливаем плеер
        player.stop()
        
        return True
        
    except Exception as e:
        print(f"❌ Ошибка воспроизведения: {e}")
        import traceback
        traceback.print_exc()
        return False
    finally:
        player.stop()


def test_device_switching_with_normalization():
    """Тест переключения устройств с автоматической нормализацией"""
    print("=" * 70)
    print("ТЕСТ 4: Переключение устройств с нормализацией")
    print("=" * 70)
    print("")
    print("⚠️  ВНИМАНИЕ: Этот тест требует ручного переключения устройств")
    print("   Пожалуйста, переключите OUTPUT устройство во время теста")
    print("")
    
    # Создаём плеер с мониторингом
    config = PlayerConfig(
        sample_rate=24000,
        channels=1,
        dtype='int16',
        buffer_size=512
    )
    
    player = TestPlayer(config, enable_realtime_monitoring=True)
    
    try:
        # Генерируем длинный тестовый сигнал (5 секунд)
        duration = 5.0
        internal_rate = 24000
        t = np.linspace(0, duration, int(internal_rate * duration))
        audio_data = (np.sin(2 * np.pi * 440 * t) * 0.3).astype(np.float32)
        audio_int16 = (audio_data * 32767).astype(np.int16)
        
        print(f"📊 Генерируем длинный сигнал: {len(audio_int16)} samples, {duration} секунд")
        print(f"▶️  Начинаем воспроизведение...")
        print(f"   Переключите OUTPUT устройство во время воспроизведения")
        print("")
        
        session_id = "test_session_switching"
        player.add_audio_data(audio_int16, metadata={'session_id': session_id})
        
        # Мониторим переключения
        initial_params = player._normalized_params
        if initial_params:
            print(f"📊 Начальные параметры:")
            print(f"   Sample Rate: {initial_params.sample_rate} Hz")
            print(f"   Channels: {initial_params.channels}")
            print("")
        
        # Ждём и проверяем переключения
        for i in range(10):
            time.sleep(0.5)
            if player._normalized_params and initial_params:
                current = player._normalized_params
                if (current.sample_rate != initial_params.sample_rate or 
                    current.channels != initial_params.channels):
                    print(f"🔄 Обнаружено переключение устройства!")
                    print(f"   Старые параметры: {initial_params.sample_rate} Hz, {initial_params.channels} ch")
                    print(f"   Новые параметры: {current.sample_rate} Hz, {current.channels} ch")
                    print("")
                    initial_params = current
        
        print("✅ Тест завершён")
        print("")
        
        return True
        
    except Exception as e:
        print(f"❌ Ошибка: {e}")
        import traceback
        traceback.print_exc()
        return False
    finally:
        player.stop()


def test_all_devices():
    """Тест нормализации всех доступных устройств"""
    print("=" * 70)
    print("ТЕСТ 5: Нормализация всех доступных устройств")
    print("=" * 70)
    print("")
    
    config = {
        'output_min_rate': 16000,
        'output_max_rate': 48000,
        'output_default_rate': 48000,
        'output_max_channels': 2,
    }
    
    normalizer = DeviceParamsNormalizer(config)
    
    devices = sd.query_devices()
    output_devices = []
    
    for i, dev in enumerate(devices):
        if dev.get('max_output_channels', 0) > 0:
            output_devices.append((i, dev))
    
    print(f"Найдено {len(output_devices)} OUTPUT устройств:")
    print("")
    
    all_ok = True
    
    for device_id, device_info in output_devices:
        device_name = device_info.get('name', 'Unknown')
        raw_rate = device_info.get('default_samplerate', 0)
        raw_channels = device_info.get('max_output_channels', 0)
        
        try:
            normalized = normalizer.select_output_params(device_info)
            
            # Проверяем что параметры корректны
            rate_ok = 16000 <= normalized.sample_rate <= 48000
            channels_ok = normalized.channels in (1, 2)
            
            status = "✅" if (rate_ok and channels_ok) else "❌"
            
            print(f"{status} \"{device_name}\" (ID={device_id})")
            print(f"   Исходные: {raw_rate} Hz, {raw_channels} ch")
            print(f"   Нормализовано: {normalized.sample_rate} Hz, {normalized.channels} ch")
            
            if not (rate_ok and channels_ok):
                all_ok = False
                print(f"   ⚠️  Параметры вне допустимого диапазона!")
            
            print("")
            
        except Exception as e:
            print(f"❌ Ошибка обработки \"{device_name}\": {e}")
            all_ok = False
            print("")
    
    return all_ok


def main():
    """Запуск всех тестов"""
    print("")
    print("=" * 70)
    print("КОМПЛЕКСНОЕ ТЕСТИРОВАНИЕ НОРМАЛИЗАЦИИ ПАРАМЕТРОВ УСТРОЙСТВ")
    print("=" * 70)
    print("")
    
    results = {}
    
    # Тест 1: Нормализация реальных устройств
    print("🔍 Запуск теста 1...")
    results['normalization'] = test_device_normalization_real()
    print("")
    time.sleep(1)
    
    # Тест 2: Конвертация аудио
    print("🔍 Запуск теста 2...")
    results['conversion'] = test_audio_conversion_real()
    print("")
    time.sleep(1)
    
    # Тест 3: Реальное воспроизведение
    print("🔍 Запуск теста 3...")
    print("   ⚠️  Будет воспроизведён звук (440 Hz, 1 секунда)")
    time.sleep(2)
    results['playback'] = test_playback_with_normalization()
    print("")
    time.sleep(1)
    
    # Тест 4: Переключение устройств (опционально)
    print("🔍 Запуск теста 4 (опционально)...")
    response = input("   Запустить тест переключения устройств? (y/n): ").strip().lower()
    if response == 'y':
        results['switching'] = test_device_switching_with_normalization()
    else:
        print("   ⏭️  Пропущен")
        results['switching'] = None
    print("")
    
    # Тест 5: Все устройства
    print("🔍 Запуск теста 5...")
    results['all_devices'] = test_all_devices()
    print("")
    
    # Итоги
    print("=" * 70)
    print("ИТОГИ ТЕСТИРОВАНИЯ")
    print("=" * 70)
    print("")
    
    for test_name, result in results.items():
        if result is None:
            status = "⏭️  ПРОПУЩЕН"
        elif result:
            status = "✅ ПРОЙДЕН"
        else:
            status = "❌ ПРОВАЛЕН"
        
        print(f"{status} - {test_name}")
    
    print("")
    
    # Общий результат
    passed = sum(1 for r in results.values() if r is True)
    failed = sum(1 for r in results.values() if r is False)
    skipped = sum(1 for r in results.values() if r is None)
    
    print(f"Пройдено: {passed}")
    print(f"Провалено: {failed}")
    print(f"Пропущено: {skipped}")
    print("")
    
    if failed == 0:
        print("=" * 70)
        print("✅ ВСЕ ТЕСТЫ ПРОЙДЕНЫ УСПЕШНО!")
        print("=" * 70)
        print("")
        print("💡 Нормализация параметров устройств работает корректно")
        print("   Готово к переносу в основной код")
        return 0
    else:
        print("=" * 70)
        print("❌ НЕКОТОРЫЕ ТЕСТЫ ПРОВАЛЕНЫ")
        print("=" * 70)
        return 1


if __name__ == '__main__':
    exit(main())

