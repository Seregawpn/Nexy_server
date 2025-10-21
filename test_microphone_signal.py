#!/usr/bin/env python3
"""
Тест для проверки получения сигнала с микрофона
Проверяет, действительно ли микрофон получает сигнал или возвращает только нули
"""

import sys
import time
import numpy as np
from pathlib import Path

# Добавляем пути к модулям
CLIENT_ROOT = Path(__file__).parent
sys.path.insert(0, str(CLIENT_ROOT))
sys.path.insert(0, str(CLIENT_ROOT / "modules"))
sys.path.insert(0, str(CLIENT_ROOT / "integration"))

def test_microphone_signal():
    """Тестирует получение сигнала с микрофона"""
    try:
        import sounddevice as sd
        
        print("🔍 ТЕСТ: Получение сигнала с микрофона")
        print("=" * 50)
        
        # Получаем текущее default устройство
        default_setting = sd.default.device
        if hasattr(default_setting, '__getitem__'):
            device_id = default_setting[0]
        else:
            device_id = None
        
        if device_id is None:
            print("❌ Не удалось получить default устройство")
            return False
        
        # Получаем информацию об устройстве
        try:
            device_info = sd.query_devices(device_id, 'input')
            device_name = device_info.get('name', 'Unknown')
            print(f"🎤 Тестируем устройство: {device_name} (ID: {device_id})")
        except Exception as e:
            print(f"❌ Ошибка получения информации об устройстве: {e}")
            return False
        
        # Настройки записи
        sample_rate = 44100
        duration = 3.0  # 3 секунды
        channels = 1
        
        print(f"📊 Настройки: rate={sample_rate}Hz, duration={duration}s, channels={channels}")
        print("🎤 Начинаем запись... Говорите в микрофон!")
        
        # Записываем аудио
        try:
            audio_data = sd.rec(
                int(duration * sample_rate),
                samplerate=sample_rate,
                channels=channels,
                device=device_id,
                dtype='float32'
            )
            
            # Ждем завершения записи
            sd.wait()
            
            print("✅ Запись завершена")
            
            # Анализируем данные
            if audio_data.size > 0:
                # Вычисляем статистику
                peak = float(np.max(np.abs(audio_data)))
                rms = float(np.sqrt(np.mean(audio_data.astype(np.float64) ** 2)))
                rms_db = float(20 * np.log10(rms)) if rms > 0 else float("-inf")
                
                # Проверяем на тишину
                silence_threshold = 1e-5
                is_silent = peak < silence_threshold
                
                print(f"\n📈 АНАЛИЗ АУДИО:")
                print(f"  Peak: {peak:.6f}")
                print(f"  RMS: {rms:.6f}")
                print(f"  RMS (dB): {rms_db:.1f}")
                print(f"  Тишина: {'Да' if is_silent else 'Нет'}")
                
                if is_silent:
                    print("🚨 ПРОБЛЕМА: Микрофон возвращает только тишину!")
                    print("   Возможные причины:")
                    print("   1. Микрофон отключен в System Settings → Sound → Input")
                    print("   2. Input Level установлен в 0")
                    print("   3. Аппаратный mute на микрофоне")
                    print("   4. Нет разрешений на микрофон в Privacy & Security")
                    print("   5. Проблема с драйверами микрофона")
                    return False
                else:
                    print("✅ Микрофон получает сигнал")
                    return True
            else:
                print("❌ Нет аудио данных")
                return False
                
        except Exception as e:
            print(f"❌ Ошибка записи: {e}")
            return False
            
    except ImportError:
        print("❌ sounddevice не установлен")
        return False
    except Exception as e:
        print(f"❌ Ошибка: {e}")
        return False

def test_microphone_permissions():
    """Тестирует разрешения микрофона"""
    print("\n🔍 ТЕСТ: Разрешения микрофона")
    print("=" * 50)
    
    try:
        import sounddevice as sd
        
        # Пытаемся получить список устройств
        devices = sd.query_devices()
        print(f"📱 Найдено {len(devices)} аудио устройств")
        
        # Проверяем доступность каждого входного устройства
        input_devices = []
        for i, device in enumerate(devices):
            if device.get('max_input_channels', 0) > 0:
                device_name = device.get('name', 'Unknown')
                print(f"  {i}: {device_name}")
                
                # Проверяем доступность
                try:
                    sd.check_input_settings(
                        device=i,
                        samplerate=44100,
                        channels=1,
                        dtype='float32'
                    )
                    print(f"    ✅ Доступно")
                    input_devices.append((i, device_name))
                except Exception as e:
                    print(f"    ❌ Недоступно: {e}")
        
        if input_devices:
            print(f"\n✅ Найдено {len(input_devices)} доступных входных устройств")
            return True
        else:
            print("\n❌ Нет доступных входных устройств")
            print("   Проверьте разрешения в System Settings → Privacy & Security → Microphone")
            return False
            
    except Exception as e:
        print(f"❌ Ошибка проверки разрешений: {e}")
        return False

def test_system_audio_settings():
    """Тестирует системные настройки звука"""
    print("\n🔍 ТЕСТ: Системные настройки звука")
    print("=" * 50)
    
    try:
        import subprocess
        
        # Получаем текущее входное устройство через системную команду
        result = subprocess.run(
            ["osascript", "-e", "get volume settings"],
            capture_output=True,
            text=True,
            timeout=5
        )
        
        if result.returncode == 0:
            print(f"🔊 Системные настройки звука: {result.stdout.strip()}")
        else:
            print("⚠️ Не удалось получить системные настройки звука")
        
        # Проверяем, есть ли активные аудио процессы
        result = subprocess.run(
            ["ps", "aux"],
            capture_output=True,
            text=True,
            timeout=5
        )
        
        if result.returncode == 0:
            audio_processes = []
            for line in result.stdout.split('\n'):
                if any(keyword in line.lower() for keyword in ['coreaudiod', 'audio', 'sound']):
                    audio_processes.append(line.strip())
            
            if audio_processes:
                print(f"🔊 Найдено {len(audio_processes)} аудио процессов:")
                for process in audio_processes[:5]:  # Показываем первые 5
                    print(f"  {process}")
            else:
                print("⚠️ Аудио процессы не найдены")
        
        return True
        
    except Exception as e:
        print(f"❌ Ошибка проверки системных настроек: {e}")
        return False

def test_quicktime_comparison():
    """Тестирует сравнение с QuickTime"""
    print("\n🔍 ТЕСТ: Сравнение с QuickTime")
    print("=" * 50)
    
    print("📝 ИНСТРУКЦИЯ:")
    print("1. Откройте QuickTime Player")
    print("2. File → New Audio Recording")
    print("3. Запишите 3 секунды речи")
    print("4. Воспроизведите запись")
    print("5. Если в QuickTime есть звук, а в нашем тесте нет - проблема в коде")
    print("6. Если в QuickTime тоже тишина - проблема в системе")
    
    response = input("\nЕсть ли звук в QuickTime? (y/n): ").lower().strip()
    
    if response == 'y':
        print("✅ QuickTime получает звук - проблема в коде Nexy")
        return True
    elif response == 'n':
        print("❌ QuickTime тоже не получает звук - проблема в системе")
        return False
    else:
        print("⚠️ Неопределенный ответ")
        return None

def main():
    """Главная функция тестирования"""
    print("🚀 ТЕСТИРОВАНИЕ МИКРОФОНА")
    print("=" * 60)
    print("Проверяем, получает ли микрофон сигнал или возвращает только нули")
    print("=" * 60)
    
    results = {}
    
    # Запускаем все тесты
    results['signal'] = test_microphone_signal()
    results['permissions'] = test_microphone_permissions()
    results['system_settings'] = test_system_audio_settings()
    results['quicktime'] = test_quicktime_comparison()
    
    # Анализируем результаты
    print("\n📊 РЕЗУЛЬТАТЫ ТЕСТИРОВАНИЯ")
    print("=" * 60)
    
    for test_name, result in results.items():
        if result is True:
            status = "✅ ПРОЙДЕН"
        elif result is False:
            status = "❌ ПРОВАЛЕН"
        else:
            status = "⚠️ НЕОПРЕДЕЛЕН"
        print(f"{test_name}: {status}")
    
    # Выводим выводы
    print("\n💡 ВЫВОДЫ")
    print("=" * 60)
    
    if not results['signal']:
        print("🚨 ПРОБЛЕМА: Микрофон возвращает только нули")
        
        if results['permissions']:
            print("✅ Разрешения на микрофон есть")
        else:
            print("❌ Нет разрешений на микрофон")
        
        if results['quicktime'] is True:
            print("✅ QuickTime получает звук - проблема в коде Nexy")
            print("🔧 РЕКОМЕНДАЦИИ:")
            print("  1. Проверьте настройки аудио в Nexy")
            print("  2. Убедитесь, что используется правильное устройство")
            print("  3. Проверьте параметры записи (sample rate, channels)")
        elif results['quicktime'] is False:
            print("❌ QuickTime тоже не получает звук - проблема в системе")
            print("🔧 РЕКОМЕНДАЦИИ:")
            print("  1. Проверьте System Settings → Sound → Input")
            print("  2. Убедитесь, что Input Level не в нуле")
            print("  3. Проверьте аппаратный mute на микрофоне")
            print("  4. Перезапустите CoreAudio: sudo killall coreaudiod")
        else:
            print("⚠️ Не удалось определить причину")
    else:
        print("✅ Микрофон получает сигнал")
        print("🔧 РЕКОМЕНДАЦИИ:")
        print("  1. Проблема может быть в обработке аудио в Nexy")
        print("  2. Проверьте логи приложения")
        print("  3. Убедитесь, что аудио данные передаются корректно")

if __name__ == "__main__":
    main()
