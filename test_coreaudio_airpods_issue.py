#!/usr/bin/env python3
"""
Тестовый скрипт для проверки гипотезы о "залипании" AirPods в CoreAudio/PortAudio
Проверяет, действительно ли macOS продолжает сообщать через CoreAudio/PortAudio,
что default-микрофон — это AirPods, даже если они уже не отображаются в настройках звука.
"""

import sys
import time
import json
import subprocess
from pathlib import Path

# Добавляем пути к модулям
CLIENT_ROOT = Path(__file__).parent
sys.path.insert(0, str(CLIENT_ROOT))
sys.path.insert(0, str(CLIENT_ROOT / "modules"))
sys.path.insert(0, str(CLIENT_ROOT / "integration"))

def test_1_portaudio_default_device():
    """Тест 1: Проверяем что возвращает PortAudio как default устройство"""
    print("🔍 ТЕСТ 1: PortAudio default устройство")
    print("=" * 50)
    
    try:
        import sounddevice as sd
        
        # Получаем default устройство
        default_setting = sd.default.device
        print(f"sd.default.device: {default_setting}")
        
        if hasattr(default_setting, '__getitem__'):
            default_input = default_setting[0]
            if default_input is not None:
                try:
                    input_info = sd.query_devices(default_input, 'input')
                    device_name = input_info.get('name', 'Unknown')
                    print(f"Default INPUT: {default_input} - {device_name}")
                    
                    # Проверяем, содержит ли имя AirPods
                    if 'airpods' in device_name.lower():
                        print("🚨 ПРОБЛЕМА: PortAudio считает AirPods default устройством!")
                        return False
                    else:
                        print("✅ PortAudio показывает корректное default устройство")
                        return True
                except Exception as e:
                    print(f"❌ Ошибка получения информации об устройстве: {e}")
                    return False
        else:
            print("❌ Не удалось получить default устройство")
            return False
            
    except ImportError:
        print("❌ sounddevice не установлен")
        return False
    except Exception as e:
        print(f"❌ Ошибка: {e}")
        return False

def test_2_system_audio_settings():
    """Тест 2: Проверяем системные настройки звука через system_profiler"""
    print("\n🔍 ТЕСТ 2: Системные настройки звука")
    print("=" * 50)
    
    try:
        # Получаем системную информацию об аудио
        result = subprocess.run(
            ["system_profiler", "SPAudioDataType", "-json"],
            capture_output=True,
            text=True,
            timeout=10
        )
        
        if result.returncode == 0:
            data = json.loads(result.stdout)
            
            print("Системные аудио устройства:")
            airpods_found = False
            default_device = None
            
            for item in data.get('SPAudioDataType', []):
                name = item.get('_name', 'Unknown')
                print(f"  - {name}")
                
                # Проверяем, является ли это устройство по умолчанию
                if item.get('coreaudio_default_audio_system_device'):
                    default_device = name
                    print(f"    ⭐ СИСТЕМНОЕ УСТРОЙСТВО ПО УМОЛЧАНИЮ")
                
                # Проверяем наличие AirPods
                if 'airpods' in name.lower():
                    airpods_found = True
                    print(f"    🔵 BLUETOOTH устройство (AirPods)")
            
            print(f"\nРезультат:")
            print(f"  AirPods найдены в системе: {'Да' if airpods_found else 'Нет'}")
            print(f"  Системное default устройство: {default_device or 'Не определено'}")
            
            if airpods_found and default_device and 'airpods' in default_device.lower():
                print("🚨 ПРОБЛЕМА: Система считает AirPods default устройством!")
                return False
            else:
                print("✅ Системные настройки корректны")
                return True
        else:
            print(f"❌ Не удалось получить системную информацию: {result.stderr}")
            return False
            
    except subprocess.TimeoutExpired:
        print("❌ Таймаут при получении системной информации")
        return False
    except Exception as e:
        print(f"❌ Ошибка: {e}")
        return False

def test_3_portaudio_cache_reset():
    """Тест 3: Проверяем, помогает ли сброс кеша PortAudio"""
    print("\n🔍 ТЕСТ 3: Сброс кеша PortAudio")
    print("=" * 50)
    
    try:
        import sounddevice as sd
        
        # Запоминаем исходное состояние
        original_default = sd.default.device
        print(f"Исходное sd.default.device: {original_default}")
        
        # Сбрасываем кеш
        print("Сбрасываем кеш PortAudio...")
        sd.default.device = (None, None)
        
        # Проверяем новое состояние
        new_default = sd.default.device
        print(f"Новое sd.default.device: {new_default}")
        
        # Восстанавливаем исходное состояние
        sd.default.device = original_default
        print(f"Восстановлено sd.default.device: {sd.default.device}")
        
        # Проверяем, изменилось ли что-то
        if new_default != original_default:
            print("✅ Сброс кеша изменил default устройство")
            return True
        else:
            print("⚠️ Сброс кеша не изменил default устройство")
            return False
            
    except Exception as e:
        print(f"❌ Ошибка: {e}")
        return False

def test_4_coreaudio_restart():
    """Тест 4: Проверяем, помогает ли перезапуск CoreAudio"""
    print("\n🔍 ТЕСТ 4: Перезапуск CoreAudio")
    print("=" * 50)
    
    try:
        import sounddevice as sd
        
        # Запоминаем состояние до перезапуска
        before_restart = sd.default.device
        print(f"До перезапуска CoreAudio: {before_restart}")
        
        # Перезапускаем CoreAudio
        print("Перезапускаем CoreAudio...")
        result = subprocess.run(
            ["sudo", "killall", "coreaudiod"],
            capture_output=True,
            text=True,
            timeout=10
        )
        
        if result.returncode == 0:
            print("✅ CoreAudio перезапущен успешно")
            
            # Ждем стабилизации
            print("Ждем стабилизации (3 секунды)...")
            time.sleep(3.0)
            
            # Проверяем состояние после перезапуска
            after_restart = sd.default.device
            print(f"После перезапуска CoreAudio: {after_restart}")
            
            # Проверяем, изменилось ли что-то
            if after_restart != before_restart:
                print("✅ Перезапуск CoreAudio изменил default устройство")
                return True
            else:
                print("⚠️ Перезапуск CoreAudio не изменил default устройство")
                return False
        else:
            print(f"❌ Не удалось перезапустить CoreAudio: {result.stderr}")
            return False
            
    except subprocess.TimeoutExpired:
        print("❌ Таймаут при перезапуске CoreAudio")
        return False
    except Exception as e:
        print(f"❌ Ошибка: {e}")
        return False

def test_5_device_availability():
    """Тест 5: Проверяем доступность устройств"""
    print("\n🔍 ТЕСТ 5: Доступность устройств")
    print("=" * 50)
    
    try:
        import sounddevice as sd
        
        # Получаем список всех устройств
        devices = sd.query_devices()
        print(f"Найдено {len(devices)} аудио устройств:")
        
        available_inputs = []
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
                    print(f"    ✅ Доступно для записи")
                    available_inputs.append((i, device_name))
                except Exception as e:
                    print(f"    ❌ Недоступно: {e}")
        
        print(f"\nДоступно {len(available_inputs)} входных устройств:")
        for device_id, device_name in available_inputs:
            print(f"  - {device_name} (ID: {device_id})")
        
        return len(available_inputs) > 0
        
    except Exception as e:
        print(f"❌ Ошибка: {e}")
        return False

def main():
    """Главная функция тестирования"""
    print("🚀 ТЕСТИРОВАНИЕ ГИПОТЕЗЫ О 'ЗАЛИПАНИИ' AIRPODS")
    print("=" * 60)
    print("Проверяем, действительно ли macOS продолжает сообщать через")
    print("CoreAudio/PortAudio, что default-микрофон — это AirPods,")
    print("даже если они уже не отображаются в настройках звука.")
    print("=" * 60)
    
    results = {}
    
    # Запускаем все тесты
    results['portaudio_default'] = test_1_portaudio_default_device()
    results['system_settings'] = test_2_system_audio_settings()
    results['cache_reset'] = test_3_portaudio_cache_reset()
    results['coreaudio_restart'] = test_4_coreaudio_restart()
    results['device_availability'] = test_5_device_availability()
    
    # Анализируем результаты
    print("\n📊 РЕЗУЛЬТАТЫ ТЕСТИРОВАНИЯ")
    print("=" * 60)
    
    for test_name, result in results.items():
        status = "✅ ПРОЙДЕН" if result else "❌ ПРОВАЛЕН"
        print(f"{test_name}: {status}")
    
    # Выводим выводы
    print("\n💡 ВЫВОДЫ")
    print("=" * 60)
    
    if not results['portaudio_default']:
        print("🚨 ПОДТВЕРЖДЕНА ГИПОТЕЗА: PortAudio показывает AirPods как default устройство")
        print("   даже если они не отображаются в системных настройках")
    else:
        print("✅ PortAudio показывает корректное default устройство")
    
    if not results['system_settings']:
        print("🚨 ПОДТВЕРЖДЕНА ГИПОТЕЗА: Система считает AirPods default устройством")
    else:
        print("✅ Системные настройки корректны")
    
    if results['cache_reset']:
        print("✅ Сброс кеша PortAudio помогает обновить default устройство")
    else:
        print("⚠️ Сброс кеша PortAudio не помогает")
    
    if results['coreaudio_restart']:
        print("✅ Перезапуск CoreAudio помогает обновить default устройство")
    else:
        print("⚠️ Перезапуск CoreAudio не помогает")
    
    if results['device_availability']:
        print("✅ Есть доступные альтернативные устройства")
    else:
        print("❌ Нет доступных альтернативных устройств")
    
    # Рекомендации
    print("\n🔧 РЕКОМЕНДАЦИИ")
    print("=" * 60)
    
    if not results['portaudio_default'] or not results['system_settings']:
        print("1. Выполните: sudo killall coreaudiod")
        print("2. Подождите 3-5 секунд для стабилизации")
        print("3. Проверьте настройки звука в System Preferences")
        print("4. Убедитесь, что Continuity-микрофон отключен")
        print("5. Перезапустите Nexy")
    else:
        print("✅ Проблема с 'залипанием' AirPods не обнаружена")
        print("   Возможно, проблема в другом месте")

if __name__ == "__main__":
    main()
