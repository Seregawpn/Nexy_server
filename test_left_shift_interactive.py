#!/usr/bin/env python3
"""
Интерактивный тест для проверки left_shift активатора
Проверяет, что мониторы правильно реагируют на нажатия клавиш
"""

import sys
import time
from pathlib import Path

try:
    from Quartz import (
        CFRunLoopRun, CFRunLoopStop, CFRunLoopGetCurrent, CFRunLoopGetMain,
        CFRunLoopRunInMode, kCFRunLoopDefaultMode
    )
    QUARTZ_AVAILABLE = True
except ImportError:
    QUARTZ_AVAILABLE = False

# Добавляем пути к модулям
CLIENT_ROOT = Path(__file__).parent
sys.path.insert(0, str(CLIENT_ROOT))
sys.path.insert(0, str(CLIENT_ROOT / "modules"))
sys.path.insert(0, str(CLIENT_ROOT / "integration"))

from modules.input_processing.keyboard.mac.quartz_monitor import QuartzKeyboardMonitor
from modules.input_processing.keyboard.keyboard_monitor import KeyboardMonitor
from modules.input_processing.keyboard.types import KeyboardConfig, KeyEventType

# Счетчики событий
event_counts = {
    'press': 0,
    'short_press': 0,
    'long_press': 0,
    'release': 0
}

def on_press(event):
    """Обработчик нажатия клавиши"""
    global event_counts
    event_counts['press'] += 1
    print(f"🎤 PRESS: timestamp={event.timestamp}, key={event.key}")

def on_short_press(event):
    """Обработчик короткого нажатия"""
    global event_counts
    event_counts['short_press'] += 1
    print(f"🛑 SHORT_PRESS: duration={event.duration:.3f}s, key={event.key}")

def on_long_press(event):
    """Обработчик длинного нажатия"""
    global event_counts
    event_counts['long_press'] += 1
    print(f"🎤 LONG_PRESS: duration={event.duration:.3f}s, key={event.key}")

def on_release(event):
    """Обработчик отпускания клавиши"""
    global event_counts
    event_counts['release'] += 1
    print(f"🛑 RELEASE: duration={event.duration:.3f}s, key={event.key}")

def test_quartz_monitor():
    """Тест QuartzKeyboardMonitor"""
    print("=" * 60)
    print("ИНТЕРАКТИВНЫЙ ТЕСТ: QuartzKeyboardMonitor")
    print("=" * 60)
    print("\n📝 Инструкции:")
    print("   1. Нажмите и удерживайте Левый Shift (≥0.6s) для LONG_PRESS")
    print("   2. Быстро нажмите и отпустите Левый Shift (<0.1s) для SHORT_PRESS")
    print("   3. Нажмите Ctrl+C для остановки теста\n")
    
    config = KeyboardConfig(
        key_to_monitor='left_shift',
        short_press_threshold=0.1,
        long_press_threshold=0.6,
        event_cooldown=0.1,
        hold_check_interval=0.05,
        debounce_time=0.1
    )
    
    try:
        monitor = QuartzKeyboardMonitor(config)
        
        # Регистрируем обработчики
        monitor.register_callback(KeyEventType.PRESS, on_press)
        monitor.register_callback(KeyEventType.SHORT_PRESS, on_short_press)
        monitor.register_callback(KeyEventType.LONG_PRESS, on_long_press)
        monitor.register_callback(KeyEventType.RELEASE, on_release)
        
        print("✅ Монитор инициализирован")
        print(f"✅ key_to_monitor: {monitor.key_to_monitor}")
        print(f"✅ target_keycode: {monitor._target_keycode}")
        print("\n🔄 Запуск мониторинга...")
        print("   (Нажмите Ctrl+C для остановки)\n")
        
        monitoring_result = monitor.start_monitoring()
        print(f"🔍 Результат start_monitoring(): {monitoring_result}")  # Для отладки
        
        if monitoring_result:
            print("✅ Мониторинг запущен успешно\n")
            
            # Ждем события - запускаем run loop для обработки событий
            try:
                print(f"🔍 QUARTZ_AVAILABLE: {QUARTZ_AVAILABLE}")  # Для отладки
                if QUARTZ_AVAILABLE:
                    print("🔄 Запуск CFRunLoop для обработки событий...")
                    print("   (Нажмите Ctrl+C для остановки)\n")
                    
                    # ВАЖНО: Запускаем run loop в главном потоке, а не в отдельном
                    # События добавляются в главный run loop, поэтому он должен быть активен
                    print("⏳ Ожидание событий клавиатуры (нажмите любую клавишу)...\n")
                    print("💡 Подсказка: Нажмите ЛЕВЫЙ Shift (слева на клавиатуре, не Правый!)")
                    print("   Левый Shift имеет keycode=56, Правый Shift имеет keycode=60\n")
                    
                    # Запускаем run loop в главном потоке с таймаутом для возможности прерывания
                    try:
                        while True:
                            # Обрабатываем события run loop с таймаутом 0.1 секунды
                            # Это позволяет прервать цикл через KeyboardInterrupt
                            current_loop = CFRunLoopGetCurrent()
                            result = CFRunLoopRunInMode(kCFRunLoopDefaultMode, 0.1, False)
                            
                            # Если run loop остановлен, выходим
                            if result == 2:  # kCFRunLoopRunFinished
                                break
                            
                            # Небольшая задержка для снижения нагрузки на CPU
                            time.sleep(0.01)
                    except KeyboardInterrupt:
                        pass
                else:
                    # Fallback: просто ждем
                    print("⏳ Ожидание событий клавиатуры (нажмите любую клавишу)...\n")
                    while True:
                        time.sleep(1)
            except KeyboardInterrupt:
                print("\n\n🛑 Остановка мониторинга...")
                monitor.stop_monitoring()
                print("✅ Мониторинг остановлен")
        else:
            print("❌ Не удалось запустить мониторинг (возможно, нет разрешений)")
            print("   Попробуйте запустить с правами администратора или предоставьте разрешения")
            return False
            
    except Exception as e:
        print(f"❌ ОШИБКА: {e}")
        import traceback
        traceback.print_exc()
        return False
    
    # Выводим статистику
    print("\n" + "=" * 60)
    print("СТАТИСТИКА СОБЫТИЙ:")
    print("=" * 60)
    print(f"   PRESS: {event_counts['press']}")
    print(f"   SHORT_PRESS: {event_counts['short_press']}")
    print(f"   LONG_PRESS: {event_counts['long_press']}")
    print(f"   RELEASE: {event_counts['release']}")
    print("=" * 60)
    
    return True

def test_keyboard_monitor():
    """Тест KeyboardMonitor (pynput)"""
    print("=" * 60)
    print("ИНТЕРАКТИВНЫЙ ТЕСТ: KeyboardMonitor (pynput)")
    print("=" * 60)
    print("\n📝 Инструкции:")
    print("   1. Нажмите и удерживайте Левый Shift (≥0.6s) для LONG_PRESS")
    print("   2. Быстро нажмите и отпустите Левый Shift (<0.1s) для SHORT_PRESS")
    print("   3. Нажмите Ctrl+C для остановки теста\n")
    
    config = KeyboardConfig(
        key_to_monitor='left_shift',
        short_press_threshold=0.1,
        long_press_threshold=0.6,
        event_cooldown=0.1,
        hold_check_interval=0.05,
        debounce_time=0.1
    )
    
    try:
        monitor = KeyboardMonitor(config)
        
        # Регистрируем обработчики
        monitor.register_callback(KeyEventType.PRESS, on_press)
        monitor.register_callback(KeyEventType.SHORT_PRESS, on_short_press)
        monitor.register_callback(KeyEventType.LONG_PRESS, on_long_press)
        monitor.register_callback(KeyEventType.RELEASE, on_release)
        
        print("✅ Монитор инициализирован")
        print(f"✅ key_to_monitor: {monitor.key_to_monitor}")
        print("\n🔄 Запуск мониторинга...")
        print("   (Нажмите Ctrl+C для остановки)\n")
        
        monitor.start_monitoring()
        print("✅ Мониторинг запущен успешно\n")
        print("⏳ Ожидание событий клавиатуры...\n")
        
        # Ждем события
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            print("\n\n🛑 Остановка мониторинга...")
            monitor.stop_monitoring()
            print("✅ Мониторинг остановлен")
            
    except Exception as e:
        print(f"❌ ОШИБКА: {e}")
        import traceback
        traceback.print_exc()
        return False
    
    # Выводим статистику
    print("\n" + "=" * 60)
    print("СТАТИСТИКА СОБЫТИЙ:")
    print("=" * 60)
    print(f"   PRESS: {event_counts['press']}")
    print(f"   SHORT_PRESS: {event_counts['short_press']}")
    print(f"   LONG_PRESS: {event_counts['long_press']}")
    print(f"   RELEASE: {event_counts['release']}")
    print("=" * 60)
    
    return True

def main():
    """Главная функция"""
    print("\n" + "=" * 60)
    print("ИНТЕРАКТИВНОЕ ТЕСТИРОВАНИЕ: left_shift активатор")
    print("=" * 60 + "\n")
    
    print("Выберите тест:")
    print("   1. QuartzKeyboardMonitor (macOS нативный)")
    print("   2. KeyboardMonitor (pynput fallback)")
    print("   3. Выход")
    
    choice = input("\nВаш выбор (1-3): ").strip()
    
    if choice == "1":
        test_quartz_monitor()
    elif choice == "2":
        test_keyboard_monitor()
    elif choice == "3":
        print("Выход...")
        return 0
    else:
        print("❌ Неверный выбор")
        return 1
    
    return 0

if __name__ == "__main__":
    sys.exit(main())

      