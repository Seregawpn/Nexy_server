#!/usr/bin/env python3
"""
Скрипт для активации микрофона AirPods
"""

import subprocess
import time
import sounddevice as sd
import json

def check_airpods_status():
    """Проверяет текущий статус AirPods"""
    print("🔍 Проверяем статус AirPods...")
    
    # Проверяем устройства
    devices = sd.query_devices()
    airpods_devices = []
    
    for i, device in enumerate(devices):
        if 'AirPods' in device['name']:
            airpods_devices.append({
                'index': i,
                'name': device['name'],
                'input_channels': device['max_input_channels'],
                'output_channels': device['max_output_channels'],
                'sample_rate': device['default_samplerate']
            })
    
    print(f"📱 Найдено устройств AirPods: {len(airpods_devices)}")
    for device in airpods_devices:
        print(f"   Устройство {device['index']}: {device['name']}")
        print(f"   - Input: {device['input_channels']}, Output: {device['output_channels']}")
        print(f"   - Частота: {device['sample_rate']} Hz")
    
    return airpods_devices

def check_bluetooth_profile():
    """Проверяет Bluetooth профиль AirPods"""
    print("\n🔗 Проверяем Bluetooth профиль...")
    
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
                                print(f"   Устройство: {name}")
                                print(f"   - Тип: {info.get('device_minorType', 'Unknown')}")
                                print(f"   - Сервисы: {info.get('device_services', 'Unknown')}")
                                
                                # Проверяем HFP
                                services = str(info.get('device_services', ''))
                                hfp_active = 'HFP' in services
                                print(f"   - HFP активен: {'✅' if hfp_active else '❌'}")
                                
                                return hfp_active
    except Exception as e:
        print(f"   ❌ Ошибка: {e}")
    
    return False

def test_microphone(device_index):
    """Тестирует микрофон устройства"""
    print(f"\n🎤 Тестируем микрофон устройства {device_index}...")
    
    try:
        # Устанавливаем устройство
        sd.default.device = (device_index, sd.default.device[1])
        
        # Записываем 2 секунды
        print("   Говорите что-нибудь в течение 2 секунд...")
        import numpy as np
        audio_data = sd.rec(int(2 * 16000), samplerate=16000, channels=1, dtype='float32')
        sd.wait()
        
        # Анализируем
        rms = np.sqrt(np.mean(audio_data**2))
        peak = np.max(np.abs(audio_data))
        
        print(f"   📊 Результат: RMS={rms:.6f}, Peak={peak:.6f}")
        
        if rms > 0.001:
            print("   ✅ Микрофон работает!")
            return True
        else:
            print("   ❌ Микрофон не работает (тишина)")
            return False
            
    except Exception as e:
        print(f"   ❌ Ошибка тестирования: {e}")
        return False

def activate_hfp_profile():
    """Пытается активировать HFP профиль"""
    print("\n🔧 Попытка активации HFP профиля...")
    
    # Метод 1: Открыть настройки звука
    try:
        script = '''
        tell application "System Settings"
            activate
            set current pane to pane "com.apple.preference.sound"
        end tell
        '''
        result = subprocess.run(['osascript', '-e', script], capture_output=True, text=True, timeout=10)
        if result.returncode == 0:
            print("   ✅ Настройки звука открыты")
            print("   📋 В настройках:")
            print("   1. Перейдите на вкладку 'Вход'")
            print("   2. Выберите 'Sergiy's AirPods'")
            print("   3. Убедитесь, что микрофон активен")
            return True
        else:
            print("   ❌ Не удалось открыть настройки автоматически")
            print("   🔧 Откройте вручную: Системные настройки → Звук")
            return False
    except Exception as e:
        print(f"   ❌ Ошибка: {e}")
        return False

def main():
    """Основная функция"""
    print("🎧 АКТИВАЦИЯ МИКРОФОНА AIRPODS")
    print("=" * 50)
    
    # 1. Проверяем статус
    airpods_devices = check_airpods_status()
    if not airpods_devices:
        print("❌ AirPods не найдены!")
        return
    
    # 2. Проверяем Bluetooth профиль
    hfp_active = check_bluetooth_profile()
    
    # 3. Тестируем микрофон
    input_device = None
    for device in airpods_devices:
        if device['input_channels'] > 0:
            input_device = device
            break
    
    if input_device:
        mic_works = test_microphone(input_device['index'])
    else:
        print("❌ Не найдено устройство с микрофоном!")
        return
    
    # 4. Если микрофон не работает, пытаемся активировать HFP
    if not mic_works:
        print("\n🔧 Микрофон не работает, пытаемся активировать HFP...")
        activate_hfp_profile()
        
        print("\n⏳ Подождите 5 секунд и попробуйте снова...")
        time.sleep(5)
        
        # Повторный тест
        mic_works = test_microphone(input_device['index'])
    
    # 5. Результат
    print("\n" + "=" * 50)
    if mic_works:
        print("✅ AirPods микрофон работает!")
        print("🎧 Теперь можно использовать AirPods для записи")
    else:
        print("❌ AirPods микрофон не работает")
        print("💡 Рекомендации:")
        print("   1. Переподключите AirPods с выбором 'Использовать для микрофона'")
        print("   2. Используйте встроенный микрофон MacBook")
        print("   3. Проверьте разрешения на микрофон в настройках")

if __name__ == "__main__":
    main()
