#!/usr/bin/env python3
"""
Глубокая диагностика проблемы с AirPods микрофоном
"""

import sounddevice as sd
import numpy as np
import subprocess
import json
import time
from datetime import datetime

def check_system_audio_info():
    """Проверяет системную информацию об аудио"""
    print("🔍 1. СИСТЕМНАЯ ИНФОРМАЦИЯ ОБ АУДИО")
    print("=" * 50)
    
    try:
        # system_profiler для аудио
        result = subprocess.run(['system_profiler', 'SPAudioDataType'], 
                              capture_output=True, text=True, timeout=10)
        if result.returncode == 0:
            print("✅ system_profiler SPAudioDataType:")
            lines = result.stdout.split('\n')
            for line in lines:
                if 'AirPods' in line or 'Microphone' in line or 'Input' in line:
                    print(f"   {line.strip()}")
        else:
            print("❌ Ошибка system_profiler")
    except Exception as e:
        print(f"❌ Ошибка: {e}")

def check_bluetooth_detailed():
    """Детальная проверка Bluetooth"""
    print("\n🔗 2. ДЕТАЛЬНАЯ BLUETOOTH ИНФОРМАЦИЯ")
    print("=" * 50)
    
    try:
        result = subprocess.run(['system_profiler', 'SPBluetoothDataType', '-json'], 
                              capture_output=True, text=True, timeout=10)
        if result.returncode == 0:
            data = json.loads(result.stdout)
            
            for device in data.get('SPBluetoothDataType', []):
                if 'device_connected' in device:
                    for connected in device['device_connected']:
                        for name, info in connected.items():
                            if 'AirPods' in name:
                                print(f"📱 Устройство: {name}")
                                print(f"   - Адрес: {info.get('device_address', 'Unknown')}")
                                print(f"   - Тип: {info.get('device_minorType', 'Unknown')}")
                                print(f"   - Сервисы: {info.get('device_services', 'Unknown')}")
                                print(f"   - Версия: {info.get('device_firmwareVersion', 'Unknown')}")
                                print(f"   - Батарея: {info.get('device_batteryLevelLeft', 'Unknown')}% / {info.get('device_batteryLevelRight', 'Unknown')}%")
                                
                                # Анализ сервисов
                                services = str(info.get('device_services', ''))
                                print(f"   - HFP: {'✅' if 'HFP' in services else '❌'}")
                                print(f"   - A2DP: {'✅' if 'A2DP' in services else '❌'}")
                                print(f"   - AVRCP: {'✅' if 'AVRCP' in services else '❌'}")
                                
                                # Проверяем тип устройства
                                device_type = info.get('device_minorType', '')
                                if device_type == 'Headphones':
                                    print("   ⚠️  ПРОБЛЕМА: Устройство в режиме 'Headphones' (только A2DP)")
                                    print("   💡 Нужен режим 'Headset' для микрофона")
                                elif device_type == 'Headset':
                                    print("   ✅ Устройство в режиме 'Headset' (HFP активен)")
                                
                                return info
    except Exception as e:
        print(f"❌ Ошибка: {e}")
    
    return None

def check_audio_devices_detailed():
    """Детальная проверка аудио устройств"""
    print("\n🎧 3. ДЕТАЛЬНАЯ ИНФОРМАЦИЯ ОБ АУДИО УСТРОЙСТВАХ")
    print("=" * 50)
    
    devices = sd.query_devices()
    airpods_devices = []
    
    for i, device in enumerate(devices):
        if 'AirPods' in device['name']:
            airpods_devices.append((i, device))
            print(f"📱 Устройство {i}: {device['name']}")
            print(f"   - Input каналы: {device['max_input_channels']}")
            print(f"   - Output каналы: {device['max_output_channels']}")
            print(f"   - Частота: {device['default_samplerate']} Hz")
            print(f"   - Латентность: {device.get('default_low_input_latency', 'Unknown')}")
            print(f"   - Высокая латентность: {device.get('default_high_input_latency', 'Unknown')}")
            print()
    
    return airpods_devices

def test_airpods_stream():
    """Тестирует поток AirPods"""
    print("\n🎤 4. ТЕСТИРОВАНИЕ ПОТОКА AIRPODS")
    print("=" * 50)
    
    airpods_input = None
    devices = sd.query_devices()
    
    # Находим AirPods input устройство
    for i, device in enumerate(devices):
        if 'AirPods' in device['name'] and device['max_input_channels'] > 0:
            airpods_input = i
            break
    
    if airpods_input is None:
        print("❌ AirPods input устройство не найдено")
        return False
    
    print(f"📱 Тестируем AirPods input (устройство {airpods_input})")
    
    try:
        # Тест 1: Проверка возможности открытия потока
        print("🔍 Тест 1: Открытие потока...")
        
        def audio_callback(indata, frames, time, status):
            if status:
                print(f"   ⚠️  Статус потока: {status}")
        
        # Пытаемся открыть поток
        with sd.InputStream(device=airpods_input, 
                          channels=1, 
                          samplerate=16000, 
                          callback=audio_callback,
                          blocksize=1024) as stream:
            print("   ✅ Поток успешно открыт")
            
            # Тест 2: Запись данных
            print("🔍 Тест 2: Запись данных...")
            print("   Говорите что-нибудь в течение 2 секунд...")
            
            data = stream.read(32000)[0]  # 2 секунды при 16kHz
            
            # Анализ данных
            rms = np.sqrt(np.mean(data**2))
            peak = np.max(np.abs(data))
            
            print(f"   📊 RMS: {rms:.6f}")
            print(f"   📊 Peak: {peak:.6f}")
            
            if rms > 0.001:
                print("   ✅ Данные записываются")
                return True
            else:
                print("   ❌ Данные не записываются (тишина)")
                return False
                
    except Exception as e:
        print(f"   ❌ Ошибка потока: {e}")
        return False

def check_permissions():
    """Проверяет разрешения на микрофон"""
    print("\n🔐 5. ПРОВЕРКА РАЗРЕШЕНИЙ НА МИКРОФОН")
    print("=" * 50)
    
    try:
        # Проверяем через tccutil
        result = subprocess.run(['tccutil', 'reset', 'Microphone'], 
                              capture_output=True, text=True, timeout=5)
        print(f"tccutil reset result: {result.returncode}")
        
        # Проверяем активные процессы с доступом к микрофону
        result = subprocess.run(['lsof', '/dev/audio*'], 
                              capture_output=True, text=True, timeout=5)
        if result.returncode == 0:
            print("✅ Процессы с доступом к аудио:")
            for line in result.stdout.split('\n')[:5]:  # Первые 5 строк
                if line.strip():
                    print(f"   {line}")
        else:
            print("❌ Нет процессов с доступом к аудио")
            
    except Exception as e:
        print(f"❌ Ошибка проверки разрешений: {e}")

def test_different_sample_rates():
    """Тестирует разные частоты дискретизации"""
    print("\n📊 6. ТЕСТИРОВАНИЕ РАЗНЫХ ЧАСТОТ")
    print("=" * 50)
    
    airpods_input = None
    devices = sd.query_devices()
    
    for i, device in enumerate(devices):
        if 'AirPods' in device['name'] and device['max_input_channels'] > 0:
            airpods_input = i
            break
    
    if airpods_input is None:
        print("❌ AirPods input устройство не найдено")
        return
    
    frequencies = [8000, 16000, 22050, 24000, 32000, 44100, 48000]
    
    for freq in frequencies:
        try:
            print(f"🔍 Тест {freq} Hz...", end=" ")
            
            # Быстрый тест записи
            audio_data = sd.rec(int(1 * freq), 
                              samplerate=freq, 
                              channels=1, 
                              device=airpods_input,
                              dtype='float32')
            sd.wait()
            
            rms = np.sqrt(np.mean(audio_data**2))
            peak = np.max(np.abs(audio_data))
            
            if rms > 0.001:
                print(f"✅ RMS={rms:.6f}")
            else:
                print(f"❌ RMS={rms:.6f}")
                
        except Exception as e:
            print(f"❌ Ошибка: {e}")

def check_audio_hardware():
    """Проверяет аудио оборудование"""
    print("\n🔧 7. ПРОВЕРКА АУДИО ОБОРУДОВАНИЯ")
    print("=" * 50)
    
    try:
        # Проверяем Core Audio
        result = subprocess.run(['system_profiler', 'SPAudioDataType'], 
                              capture_output=True, text=True, timeout=10)
        if result.returncode == 0:
            print("✅ Core Audio информация:")
            lines = result.stdout.split('\n')
            for line in lines:
                if 'Core Audio' in line or 'Audio' in line:
                    print(f"   {line.strip()}")
        
        # Проверяем активные аудио устройства
        result = subprocess.run(['sw_vers'], capture_output=True, text=True, timeout=5)
        if result.returncode == 0:
            print("\n📱 Версия macOS:")
            for line in result.stdout.split('\n'):
                if line.strip():
                    print(f"   {line}")
                    
    except Exception as e:
        print(f"❌ Ошибка: {e}")

def generate_diagnosis_report():
    """Генерирует отчет диагностики"""
    print("\n" + "=" * 70)
    print("📋 ОТЧЕТ ДИАГНОСТИКИ")
    print("=" * 70)
    
    # Собираем данные
    bluetooth_info = check_bluetooth_detailed()
    airpods_devices = check_audio_devices_detailed()
    stream_works = test_airpods_stream()
    
    print("\n🎯 ВЫВОДЫ:")
    print("-" * 30)
    
    if bluetooth_info:
        device_type = bluetooth_info.get('device_minorType', '')
        services = str(bluetooth_info.get('device_services', ''))
        
        if device_type == 'Headphones':
            print("❌ ПРОБЛЕМА: AirPods в режиме 'Headphones'")
            print("   💡 Решение: Переподключить с активацией микрофона")
            print("   🔧 Это активирует HFP профиль")
        elif device_type == 'Headset':
            print("✅ AirPods в режиме 'Headset'")
            if not stream_works:
                print("   ⚠️  Но микрофон все равно не работает")
                print("   💡 Возможные причины:")
                print("      - Проблемы с разрешениями")
                print("      - Конфликт драйверов")
                print("      - Аппаратная проблема")
        else:
            print(f"⚠️  Неизвестный тип устройства: {device_type}")
    
    if not stream_works:
        print("\n❌ Микрофон AirPods не записывает данные")
        print("💡 Рекомендации:")
        print("   1. Переподключите AirPods с выбором 'Использовать для микрофона'")
        print("   2. Проверьте настройки звука в Системных настройках")
        print("   3. Используйте встроенный микрофон MacBook")
        print("   4. Проверьте разрешения на микрофон")
    else:
        print("\n✅ Микрофон AirPods работает!")

def main():
    """Основная функция диагностики"""
    print("🔍 ГЛУБОКАЯ ДИАГНОСТИКА AIRPODS МИКРОФОНА")
    print("=" * 70)
    print(f"🕐 Время: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    # Выполняем все проверки
    check_system_audio_info()
    check_bluetooth_detailed()
    check_audio_devices_detailed()
    test_airpods_stream()
    check_permissions()
    test_different_sample_rates()
    check_audio_hardware()
    
    # Генерируем отчет
    generate_diagnosis_report()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⏹️  Диагностика прервана")
    except Exception as e:
        print(f"\n❌ Ошибка: {e}")
        import traceback
        traceback.print_exc()
