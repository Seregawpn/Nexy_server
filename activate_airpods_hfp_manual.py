#!/usr/bin/env python3
"""
Ручная активация HFP профиля для AirPods
"""

import subprocess
import time
import sounddevice as sd
import numpy as np

def test_airpods_microphone():
    """Тестирует микрофон AirPods"""
    print("🎧 Тестируем микрофон AirPods...")
    
    # Находим AirPods
    devices = sd.query_devices()
    airpods_idx = None
    
    for i, device in enumerate(devices):
        if "AirPods" in device['name'] and device['max_input_channels'] > 0:
            airpods_idx = i
            break
    
    if airpods_idx is None:
        print("❌ AirPods input не найдены")
        return False
    
    print(f"✅ AirPods найдены (index: {airpods_idx})")
    
    # Тестируем запись
    audio_buffer = []
    
    def callback(indata, frames, time, status):
        if status:
            print(f"⚠️  Status: {status}")
        audio_buffer.append(indata.copy())
    
    try:
        print("🗣️  ГОВОРИТЕ В МИКРОФОН AIRPODS СЕЙЧАС!")
        with sd.InputStream(device=airpods_idx, channels=1, samplerate=24000, 
                          dtype='int16', callback=callback, blocksize=1200):
            time.sleep(3)
        
        if audio_buffer:
            audio_data = np.concatenate(audio_buffer).astype(np.float32)
            rms = float(np.sqrt(np.mean(audio_data**2)))
            peak = float(np.max(np.abs(audio_data)))
            
            print(f"📊 Результат: RMS={rms:.6f}, Peak={peak:.6f}")
            
            if rms > 0.001:
                print("✅ AirPods микрофон работает!")
                return True
            else:
                print("❌ AirPods микрофон не работает (тишина)")
                return False
        else:
            print("❌ Нет аудио данных")
            return False
            
    except Exception as e:
        print(f"❌ Ошибка: {e}")
        return False

def method1_switchaudio_force():
    """Метод 1: Принудительное переключение через SwitchAudioSource"""
    print("\n🔧 МЕТОД 1: ПРИНУДИТЕЛЬНОЕ ПЕРЕКЛЮЧЕНИЕ")
    print("-" * 40)
    
    # Переключаем input
    print("🔄 Переключаем input на AirPods...")
    result = subprocess.run(['SwitchAudioSource', '-t', 'input', '-s', "Sergiy's AirPods"], 
                          capture_output=True, text=True)
    if result.returncode == 0:
        print("✅ Input переключен")
    else:
        print(f"❌ Ошибка input: {result.stderr}")
    
    time.sleep(0.5)
    
    # Переключаем output
    print("🔄 Переключаем output на AirPods...")
    result = subprocess.run(['SwitchAudioSource', '-t', 'output', '-s', "Sergiy's AirPods"], 
                          capture_output=True, text=True)
    if result.returncode == 0:
        print("✅ Output переключен")
    else:
        print(f"❌ Ошибка output: {result.stderr}")
    
    time.sleep(2)
    
    # Тестируем
    return test_airpods_microphone()

def method2_bluetooth_reset():
    """Метод 2: Сброс Bluetooth"""
    print("\n🔧 МЕТОД 2: СБРОС BLUETOOTH")
    print("-" * 40)
    
    print("🔄 Отключаем AirPods...")
    result = subprocess.run(['blueutil', '--disconnect', '1C:77:54:18:C8:A3'], 
                          capture_output=True, text=True)
    if result.returncode == 0:
        print("✅ AirPods отключены")
    else:
        print(f"❌ Ошибка отключения: {result.stderr}")
    
    time.sleep(3)
    
    print("🔄 Подключаем AirPods...")
    result = subprocess.run(['blueutil', '--connect', '1C:77:54:18:C8:A3'], 
                          capture_output=True, text=True)
    if result.returncode == 0:
        print("✅ AirPods подключены")
    else:
        print(f"❌ Ошибка подключения: {result.stderr}")
    
    time.sleep(5)
    
    # Переключаем на AirPods
    subprocess.run(['SwitchAudioSource', '-t', 'input', '-s', "Sergiy's AirPods"], 
                  capture_output=True, text=True)
    subprocess.run(['SwitchAudioSource', '-t', 'output', '-s', "Sergiy's AirPods"], 
                  capture_output=True, text=True)
    
    time.sleep(2)
    
    # Тестируем
    return test_airpods_microphone()

def method3_system_preferences():
    """Метод 3: Открытие системных настроек"""
    print("\n🔧 МЕТОД 3: СИСТЕМНЫЕ НАСТРОЙКИ")
    print("-" * 40)
    
    print("🔄 Открываем системные настройки звука...")
    
    applescript = '''
    tell application "System Settings" to activate
    delay 1
    tell application "System Events"
        tell process "System Settings"
            click menu item "Sound" of menu 1 of menu bar item "View" of menu bar 1
            delay 2
            click radio button "Input" of tab group 1 of group 1 of window 1
            delay 1
            try
                select (row 1 of table 1 of scroll area 1 of group 1 of window 1 whose value of text field 1 contains "Sergiy's AirPods")
            end try
        end tell
    end tell
    '''
    
    try:
        subprocess.run(['osascript', '-e', applescript], check=True)
        print("✅ Системные настройки открыты")
        print("👆 ВРУЧНУЮ выберите AirPods как input устройство")
        print("⏳ Ждем 10 секунд...")
        time.sleep(10)
        
        # Тестируем
        return test_airpods_microphone()
        
    except subprocess.CalledProcessError as e:
        print(f"❌ Ошибка AppleScript: {e}")
        return False

def main():
    """Основная функция"""
    print("🎯 РУЧНАЯ АКТИВАЦИЯ HFP ДЛЯ AIRPODS")
    print("=" * 50)
    
    # Проверяем текущее состояние
    print("📊 Текущее состояние:")
    result = subprocess.run(['SwitchAudioSource', '-c', '-t', 'input'], 
                          capture_output=True, text=True)
    print(f"   Input: {result.stdout.strip()}")
    
    result = subprocess.run(['SwitchAudioSource', '-c', '-t', 'output'], 
                          capture_output=True, text=True)
    print(f"   Output: {result.stdout.strip()}")
    
    # Тестируем текущее состояние
    print("\n🔍 ТЕСТ ТЕКУЩЕГО СОСТОЯНИЯ:")
    current_works = test_airpods_microphone()
    
    if current_works:
        print("🎉 AirPods уже работают!")
        return True
    
    # Пробуем методы активации
    methods = [
        ("Принудительное переключение", method1_switchaudio_force),
        ("Сброс Bluetooth", method2_bluetooth_reset),
        ("Системные настройки", method3_system_preferences)
    ]
    
    for name, method in methods:
        print(f"\n{'='*60}")
        print(f"ПРОБУЕМ: {name}")
        print('='*60)
        
        try:
            success = method()
            if success:
                print(f"🎉 УСПЕХ! {name} сработал!")
                print("✅ AirPods микрофон работает!")
                return True
            else:
                print(f"❌ {name} не сработал")
        except Exception as e:
            print(f"❌ Ошибка в {name}: {e}")
    
    print("\n❌ ВСЕ МЕТОДЫ НЕ СРАБОТАЛИ")
    print("💡 AirPods остались в A2DP режиме")
    print("🔧 Нужно активировать HFP вручную через системные настройки")
    
    return False

if __name__ == "__main__":
    main()

"""
Ручная активация HFP профиля для AirPods
"""

import subprocess
import time
import sounddevice as sd
import numpy as np

def test_airpods_microphone():
    """Тестирует микрофон AirPods"""
    print("🎧 Тестируем микрофон AirPods...")
    
    # Находим AirPods
    devices = sd.query_devices()
    airpods_idx = None
    
    for i, device in enumerate(devices):
        if "AirPods" in device['name'] and device['max_input_channels'] > 0:
            airpods_idx = i
            break
    
    if airpods_idx is None:
        print("❌ AirPods input не найдены")
        return False
    
    print(f"✅ AirPods найдены (index: {airpods_idx})")
    
    # Тестируем запись
    audio_buffer = []
    
    def callback(indata, frames, time, status):
        if status:
            print(f"⚠️  Status: {status}")
        audio_buffer.append(indata.copy())
    
    try:
        print("🗣️  ГОВОРИТЕ В МИКРОФОН AIRPODS СЕЙЧАС!")
        with sd.InputStream(device=airpods_idx, channels=1, samplerate=24000, 
                          dtype='int16', callback=callback, blocksize=1200):
            time.sleep(3)
        
        if audio_buffer:
            audio_data = np.concatenate(audio_buffer).astype(np.float32)
            rms = float(np.sqrt(np.mean(audio_data**2)))
            peak = float(np.max(np.abs(audio_data)))
            
            print(f"📊 Результат: RMS={rms:.6f}, Peak={peak:.6f}")
            
            if rms > 0.001:
                print("✅ AirPods микрофон работает!")
                return True
            else:
                print("❌ AirPods микрофон не работает (тишина)")
                return False
        else:
            print("❌ Нет аудио данных")
            return False
            
    except Exception as e:
        print(f"❌ Ошибка: {e}")
        return False

def method1_switchaudio_force():
    """Метод 1: Принудительное переключение через SwitchAudioSource"""
    print("\n🔧 МЕТОД 1: ПРИНУДИТЕЛЬНОЕ ПЕРЕКЛЮЧЕНИЕ")
    print("-" * 40)
    
    # Переключаем input
    print("🔄 Переключаем input на AirPods...")
    result = subprocess.run(['SwitchAudioSource', '-t', 'input', '-s', "Sergiy's AirPods"], 
                          capture_output=True, text=True)
    if result.returncode == 0:
        print("✅ Input переключен")
    else:
        print(f"❌ Ошибка input: {result.stderr}")
    
    time.sleep(0.5)
    
    # Переключаем output
    print("🔄 Переключаем output на AirPods...")
    result = subprocess.run(['SwitchAudioSource', '-t', 'output', '-s', "Sergiy's AirPods"], 
                          capture_output=True, text=True)
    if result.returncode == 0:
        print("✅ Output переключен")
    else:
        print(f"❌ Ошибка output: {result.stderr}")
    
    time.sleep(2)
    
    # Тестируем
    return test_airpods_microphone()

def method2_bluetooth_reset():
    """Метод 2: Сброс Bluetooth"""
    print("\n🔧 МЕТОД 2: СБРОС BLUETOOTH")
    print("-" * 40)
    
    print("🔄 Отключаем AirPods...")
    result = subprocess.run(['blueutil', '--disconnect', '1C:77:54:18:C8:A3'], 
                          capture_output=True, text=True)
    if result.returncode == 0:
        print("✅ AirPods отключены")
    else:
        print(f"❌ Ошибка отключения: {result.stderr}")
    
    time.sleep(3)
    
    print("🔄 Подключаем AirPods...")
    result = subprocess.run(['blueutil', '--connect', '1C:77:54:18:C8:A3'], 
                          capture_output=True, text=True)
    if result.returncode == 0:
        print("✅ AirPods подключены")
    else:
        print(f"❌ Ошибка подключения: {result.stderr}")
    
    time.sleep(5)
    
    # Переключаем на AirPods
    subprocess.run(['SwitchAudioSource', '-t', 'input', '-s', "Sergiy's AirPods"], 
                  capture_output=True, text=True)
    subprocess.run(['SwitchAudioSource', '-t', 'output', '-s', "Sergiy's AirPods"], 
                  capture_output=True, text=True)
    
    time.sleep(2)
    
    # Тестируем
    return test_airpods_microphone()

def method3_system_preferences():
    """Метод 3: Открытие системных настроек"""
    print("\n🔧 МЕТОД 3: СИСТЕМНЫЕ НАСТРОЙКИ")
    print("-" * 40)
    
    print("🔄 Открываем системные настройки звука...")
    
    applescript = '''
    tell application "System Settings" to activate
    delay 1
    tell application "System Events"
        tell process "System Settings"
            click menu item "Sound" of menu 1 of menu bar item "View" of menu bar 1
            delay 2
            click radio button "Input" of tab group 1 of group 1 of window 1
            delay 1
            try
                select (row 1 of table 1 of scroll area 1 of group 1 of window 1 whose value of text field 1 contains "Sergiy's AirPods")
            end try
        end tell
    end tell
    '''
    
    try:
        subprocess.run(['osascript', '-e', applescript], check=True)
        print("✅ Системные настройки открыты")
        print("👆 ВРУЧНУЮ выберите AirPods как input устройство")
        print("⏳ Ждем 10 секунд...")
        time.sleep(10)
        
        # Тестируем
        return test_airpods_microphone()
        
    except subprocess.CalledProcessError as e:
        print(f"❌ Ошибка AppleScript: {e}")
        return False

def main():
    """Основная функция"""
    print("🎯 РУЧНАЯ АКТИВАЦИЯ HFP ДЛЯ AIRPODS")
    print("=" * 50)
    
    # Проверяем текущее состояние
    print("📊 Текущее состояние:")
    result = subprocess.run(['SwitchAudioSource', '-c', '-t', 'input'], 
                          capture_output=True, text=True)
    print(f"   Input: {result.stdout.strip()}")
    
    result = subprocess.run(['SwitchAudioSource', '-c', '-t', 'output'], 
                          capture_output=True, text=True)
    print(f"   Output: {result.stdout.strip()}")
    
    # Тестируем текущее состояние
    print("\n🔍 ТЕСТ ТЕКУЩЕГО СОСТОЯНИЯ:")
    current_works = test_airpods_microphone()
    
    if current_works:
        print("🎉 AirPods уже работают!")
        return True
    
    # Пробуем методы активации
    methods = [
        ("Принудительное переключение", method1_switchaudio_force),
        ("Сброс Bluetooth", method2_bluetooth_reset),
        ("Системные настройки", method3_system_preferences)
    ]
    
    for name, method in methods:
        print(f"\n{'='*60}")
        print(f"ПРОБУЕМ: {name}")
        print('='*60)
        
        try:
            success = method()
            if success:
                print(f"🎉 УСПЕХ! {name} сработал!")
                print("✅ AirPods микрофон работает!")
                return True
            else:
                print(f"❌ {name} не сработал")
        except Exception as e:
            print(f"❌ Ошибка в {name}: {e}")
    
    print("\n❌ ВСЕ МЕТОДЫ НЕ СРАБОТАЛИ")
    print("💡 AirPods остались в A2DP режиме")
    print("🔧 Нужно активировать HFP вручную через системные настройки")
    
    return False

if __name__ == "__main__":
    main()
