#!/usr/bin/env python3
"""
Тестовый скрипт для проверки функциональности left_shift активатора
"""

import sys
import time
from pathlib import Path

# Добавляем пути к модулям
CLIENT_ROOT = Path(__file__).parent
sys.path.insert(0, str(CLIENT_ROOT))
sys.path.insert(0, str(CLIENT_ROOT / "modules"))
sys.path.insert(0, str(CLIENT_ROOT / "integration"))

from config.unified_config_loader import UnifiedConfigLoader
from modules.input_processing.keyboard.mac.quartz_monitor import QuartzKeyboardMonitor
from modules.input_processing.keyboard.keyboard_monitor import KeyboardMonitor
from modules.input_processing.keyboard.types import KeyboardConfig, KeyEventType

def test_configuration():
    """Тест 1: Проверка конфигурации"""
    print("=" * 60)
    print("ТЕСТ 1: Проверка конфигурации")
    print("=" * 60)
    
    loader = UnifiedConfigLoader()
    config = loader._load_config()
    keyboard_config = config.get('integrations', {}).get('keyboard', {})
    
    assert keyboard_config.get('key_to_monitor') == 'left_shift', \
        f"ОШИБКА: key_to_monitor должен быть 'left_shift', получено: {keyboard_config.get('key_to_monitor')}"
    
    print(f"✅ key_to_monitor: {keyboard_config.get('key_to_monitor')}")
    print(f"✅ short_press_threshold: {keyboard_config.get('short_press_threshold')}")
    print(f"✅ long_press_threshold: {keyboard_config.get('long_press_threshold')}")
    print("✅ Конфигурация корректна\n")
    return keyboard_config

def test_quartz_monitor(keyboard_config):
    """Тест 2: Проверка QuartzKeyboardMonitor"""
    print("=" * 60)
    print("ТЕСТ 2: Проверка QuartzKeyboardMonitor")
    print("=" * 60)
    
    config = KeyboardConfig(
        key_to_monitor=keyboard_config.get('key_to_monitor'),
        short_press_threshold=keyboard_config.get('short_press_threshold', 0.1),
        long_press_threshold=keyboard_config.get('long_press_threshold', 0.6),
        event_cooldown=keyboard_config.get('event_cooldown', 0.1),
        hold_check_interval=keyboard_config.get('hold_check_interval', 0.05),
        debounce_time=keyboard_config.get('debounce_time', 0.1)
    )
    
    monitor = QuartzKeyboardMonitor(config)
    
    assert monitor.key_to_monitor == 'left_shift', \
        f"ОШИБКА: key_to_monitor должен быть 'left_shift', получено: {monitor.key_to_monitor}"
    assert monitor._target_keycode == 56, \
        f"ОШИБКА: target_keycode должен быть 56, получено: {monitor._target_keycode}"
    assert 'left_shift' in monitor.KEYCODES, \
        "ОШИБКА: KEYCODES должен содержать 'left_shift'"
    assert 'space' not in monitor.KEYCODES, \
        "ОШИБКА: KEYCODES не должен содержать 'space'"
    
    print(f"✅ key_to_monitor: {monitor.key_to_monitor}")
    print(f"✅ target_keycode: {monitor._target_keycode}")
    print(f"✅ KEYCODES содержит left_shift: {'left_shift' in monitor.KEYCODES}")
    print(f"✅ KEYCODES не содержит space: {'space' not in monitor.KEYCODES}")
    print("✅ QuartzKeyboardMonitor работает корректно\n")
    return monitor

def test_keyboard_monitor(keyboard_config):
    """Тест 3: Проверка KeyboardMonitor (pynput)"""
    print("=" * 60)
    print("ТЕСТ 3: Проверка KeyboardMonitor (pynput)")
    print("=" * 60)
    
    config = KeyboardConfig(
        key_to_monitor=keyboard_config.get('key_to_monitor'),
        short_press_threshold=keyboard_config.get('short_press_threshold', 0.1),
        long_press_threshold=keyboard_config.get('long_press_threshold', 0.6),
        event_cooldown=keyboard_config.get('event_cooldown', 0.1),
        hold_check_interval=keyboard_config.get('hold_check_interval', 0.05),
        debounce_time=keyboard_config.get('debounce_time', 0.1)
    )
    
    monitor = KeyboardMonitor(config)
    
    assert monitor.key_to_monitor == 'left_shift', \
        f"ОШИБКА: key_to_monitor должен быть 'left_shift', получено: {monitor.key_to_monitor}"
    
    print(f"✅ key_to_monitor: {monitor.key_to_monitor}")
    print(f"✅ keyboard_available: {monitor.keyboard_available}")
    print("✅ KeyboardMonitor работает корректно\n")
    return monitor

def test_logs_and_comments():
    """Тест 4: Проверка логов и комментариев"""
    print("=" * 60)
    print("ТЕСТ 4: Проверка логов и комментариев")
    print("=" * 60)
    
    import re
    
    file_path = CLIENT_ROOT / "integration" / "integrations" / "input_processing_integration.py"
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    left_shift_count = len(re.findall(r'left_shift', content))
    space_count = len(re.findall(r'\bspace\b', content))
    probel_count = len(re.findall(r'пробел|ПРОБЕЛ', content))
    
    assert left_shift_count >= 3, \
        f"ОШИБКА: должно быть минимум 3 упоминания left_shift, найдено: {left_shift_count}"
    assert space_count == 0, \
        f"ОШИБКА: не должно быть упоминаний space, найдено: {space_count}"
    assert probel_count == 0, \
        f"ОШИБКА: не должно быть упоминаний пробел/ПРОБЕЛ, найдено: {probel_count}"
    
    print(f"✅ Упоминаний left_shift: {left_shift_count}")
    print(f"✅ Упоминаний space: {space_count}")
    print(f"✅ Упоминаний пробел/ПРОБЕЛ: {probel_count}")
    print("✅ Логи и комментарии обновлены корректно\n")

def test_integration_import():
    """Тест 5: Проверка импорта InputProcessingIntegration"""
    print("=" * 60)
    print("ТЕСТ 5: Проверка импорта InputProcessingIntegration")
    print("=" * 60)
    
    try:
        from integration.integrations.input_processing_integration import InputProcessingIntegration
        print("✅ InputProcessingIntegration импортирован успешно\n")
    except Exception as e:
        print(f"❌ ОШИБКА импорта: {e}\n")
        raise

def main():
    """Главная функция тестирования"""
    print("\n" + "=" * 60)
    print("ТЕСТИРОВАНИЕ: Изменение активатора с space на left_shift")
    print("=" * 60 + "\n")
    
    try:
        # Тест 1: Конфигурация
        keyboard_config = test_configuration()
        
        # Тест 2: QuartzKeyboardMonitor
        quartz_monitor = test_quartz_monitor(keyboard_config)
        
        # Тест 3: KeyboardMonitor (pynput)
        keyboard_monitor = test_keyboard_monitor(keyboard_config)
        
        # Тест 4: Логи и комментарии
        test_logs_and_comments()
        
        # Тест 5: Импорт интеграции
        test_integration_import()
        
        print("=" * 60)
        print("✅ ВСЕ ТЕСТЫ ПРОЙДЕНЫ УСПЕШНО!")
        print("=" * 60)
        print("\n📝 Следующие шаги:")
        print("   1. Запустите приложение: python main.py")
        print("   2. Нажмите и удерживайте Левый Shift (≥0.6s) для активации микрофона")
        print("   3. Отпустите Левый Shift для остановки записи")
        print("   4. Проверьте логи: должны содержать 'left_shift' (не 'space')\n")
        
        return 0
        
    except AssertionError as e:
        print(f"\n❌ ТЕСТ ПРОВАЛЕН: {e}\n")
        return 1
    except Exception as e:
        print(f"\n❌ ОШИБКА: {e}\n")
        import traceback
        traceback.print_exc()
        return 1

if __name__ == "__main__":
    sys.exit(main())

