#!/usr/bin/env python3
"""
Тест для проверки функциональности комбинации Control+N

Проверяет:
1. Инициализацию монитора с ctrl_n
2. Обработку событий PRESS, SHORT_PRESS, LONG_PRESS, RELEASE
3. Правильность стейт-машины для комбинации
"""

import asyncio
import logging
from pathlib import Path
import sys
import time

# Добавляем корень проекта в PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from modules.input_processing.keyboard.keyboard_monitor import KeyboardMonitor
from modules.input_processing.keyboard.mac.quartz_monitor import QuartzKeyboardMonitor
from modules.input_processing.keyboard.types import KeyboardConfig, KeyEventType

# Настройка логирования
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class TestCtrlNCombo:
    """Тест комбинации Control+N"""
    
    def __init__(self):
        self.events_received = []
        self.event_times = {}
        
    def on_press(self, event):
        """Обработчик PRESS"""
        logger.info(f"✅ PRESS получен: {event.key}, timestamp={event.timestamp}")
        self.events_received.append(("PRESS", event.timestamp))
        self.event_times["press"] = time.time()
        
    def on_short_press(self, event):
        """Обработчик SHORT_PRESS"""
        logger.info(f"✅ SHORT_PRESS получен: {event.key}, duration={event.duration:.3f}s")
        self.events_received.append(("SHORT_PRESS", event.timestamp, event.duration))
        self.event_times["short_press"] = time.time()
        
    def on_long_press(self, event):
        """Обработчик LONG_PRESS"""
        logger.info(f"✅ LONG_PRESS получен: {event.key}, duration={event.duration:.3f}s")
        self.events_received.append(("LONG_PRESS", event.timestamp, event.duration))
        self.event_times["long_press"] = time.time()
        
    def on_release(self, event):
        """Обработчик RELEASE"""
        logger.info(f"✅ RELEASE получен: {event.key}, duration={event.duration:.3f}s")
        self.events_received.append(("RELEASE", event.timestamp, event.duration))
        self.event_times["release"] = time.time()
    
    async def test_quartz_monitor(self):
        """Тестирует QuartzKeyboardMonitor с комбинацией Control+N"""
        print("=" * 70)
        print("🧪 ТЕСТ: QuartzKeyboardMonitor с Control+N")
        print("=" * 70)
        print()
        
        # Создаем конфигурацию
        config = KeyboardConfig(
            key_to_monitor="ctrl_n",
            short_press_threshold=0.1,
            long_press_threshold=0.6,
            event_cooldown=0.1,
            hold_check_interval=0.05,
            debounce_time=0.1,
        )
        
        # Создаем монитор
        monitor = QuartzKeyboardMonitor(config)
        
        if not monitor.keyboard_available:
            print("❌ Quartz недоступен - пропускаем тест")
            return False
        
        # Регистрируем обработчики
        loop = asyncio.get_event_loop()
        monitor.set_loop(loop)
        monitor.register_callback(KeyEventType.PRESS, self.on_press)
        monitor.register_callback(KeyEventType.SHORT_PRESS, self.on_short_press)
        monitor.register_callback(KeyEventType.LONG_PRESS, self.on_long_press)
        monitor.register_callback(KeyEventType.RELEASE, self.on_release)
        
        # Запускаем мониторинг
        print("🔧 Запускаем мониторинг...")
        if not monitor.start_monitoring():
            print("❌ Не удалось запустить мониторинг")
            return False
        
        print("✅ Мониторинг запущен")
        print()
        print("📋 ИНСТРУКЦИИ ДЛЯ ТЕСТИРОВАНИЯ:")
        print("1. Нажмите Control+N быстро (tap) - должен сработать SHORT_PRESS")
        print("2. Нажмите Control+N и удерживайте >= 0.6s - должен сработать LONG_PRESS")
        print("3. Попробуйте нажать только Control или только N - событий быть не должно")
        print("4. Попробуйте отпустить Control раньше N (и наоборот)")
        print()
        print("⏱️  Тест будет работать 30 секунд...")
        print("Нажмите Ctrl+C для досрочной остановки")
        print("=" * 70)
        print()
        
        try:
            # Ждем 30 секунд
            await asyncio.sleep(30)
        except KeyboardInterrupt:
            print("\n⚠️ Тест прерван пользователем")
        
        # Останавливаем мониторинг
        monitor.stop_monitoring()
        
        # Выводим результаты
        print()
        print("=" * 70)
        print("📊 РЕЗУЛЬТАТЫ ТЕСТА")
        print("=" * 70)
        print(f"Всего событий получено: {len(self.events_received)}")
        print()
        
        if self.events_received:
            print("Полученные события:")
            for i, event in enumerate(self.events_received, 1):
                print(f"  {i}. {event}")
        else:
            print("⚠️ События не получены - проверьте разрешения Accessibility/Input Monitoring")
        
        print()
        print("Статус монитора:")
        status = monitor.get_status()
        for key, value in status.items():
            print(f"  {key}: {value}")
        
        return len(self.events_received) > 0
    
    async def test_keyboard_monitor(self):
        """Тестирует KeyboardMonitor (fallback) с комбинацией Control+N"""
        print("=" * 70)
        print("🧪 ТЕСТ: KeyboardMonitor (fallback) с Control+N")
        print("=" * 70)
        print()
        
        # Создаем конфигурацию
        config = KeyboardConfig(
            key_to_monitor="ctrl_n",
            short_press_threshold=0.1,
            long_press_threshold=0.6,
            event_cooldown=0.1,
            hold_check_interval=0.05,
            debounce_time=0.1,
        )
        
        # Создаем монитор
        monitor = KeyboardMonitor(config)
        
        if not monitor.keyboard_available:
            print("❌ Клавиатура недоступна - пропускаем тест")
            return False
        
        # Регистрируем обработчики
        loop = asyncio.get_event_loop()
        monitor.set_loop(loop)
        monitor.register_callback(KeyEventType.PRESS, self.on_press)
        monitor.register_callback(KeyEventType.SHORT_PRESS, self.on_short_press)
        monitor.register_callback(KeyEventType.LONG_PRESS, self.on_long_press)
        monitor.register_callback(KeyEventType.RELEASE, self.on_release)
        
        # Запускаем мониторинг
        print("🔧 Запускаем мониторинг...")
        if not monitor.start_monitoring():
            print("❌ Не удалось запустить мониторинг")
            return False
        
        print("✅ Мониторинг запущен")
        print()
        print("📋 ИНСТРУКЦИИ ДЛЯ ТЕСТИРОВАНИЯ:")
        print("1. Нажмите Control+N быстро (tap) - должен сработать SHORT_PRESS")
        print("2. Нажмите Control+N и удерживайте >= 0.6s - должен сработать LONG_PRESS")
        print("3. Попробуйте нажать только Control или только N - событий быть не должно")
        print()
        print("⏱️  Тест будет работать 30 секунд...")
        print("Нажмите Ctrl+C для досрочной остановки")
        print("=" * 70)
        print()
        
        try:
            # Ждем 30 секунд
            await asyncio.sleep(30)
        except KeyboardInterrupt:
            print("\n⚠️ Тест прерван пользователем")
        
        # Останавливаем мониторинг
        monitor.stop_monitoring()
        
        # Выводим результаты
        print()
        print("=" * 70)
        print("📊 РЕЗУЛЬТАТЫ ТЕСТА")
        print("=" * 70)
        print(f"Всего событий получено: {len(self.events_received)}")
        print()
        
        if self.events_received:
            print("Полученные события:")
            for i, event in enumerate(self.events_received, 1):
                print(f"  {i}. {event}")
        else:
            print("⚠️ События не получены")
        
        print()
        print("Статус монитора:")
        status = monitor.get_status()
        for key, value in status.items():
            print(f"  {key}: {value}")
        
        return len(self.events_received) > 0


async def main():
    """Главная функция теста"""
    print("=" * 70)
    print("🧪 ТЕСТИРОВАНИЕ КОМБИНАЦИИ CONTROL+N")
    print("=" * 70)
    print()
    
    tester = TestCtrlNCombo()
    
    # Тестируем Quartz монитор
    print("Выберите тест:")
    print("1. QuartzKeyboardMonitor (macOS нативный)")
    print("2. KeyboardMonitor (fallback/pynput)")
    print("3. Оба")
    print()
    
    choice = input("Ваш выбор (1/2/3): ").strip()
    
    results = {}
    
    if choice in ("1", "3"):
        print()
        tester.events_received = []  # Сбрасываем события
        results["quartz"] = await tester.test_quartz_monitor()
    
    if choice in ("2", "3"):
        print()
        tester.events_received = []  # Сбрасываем события
        results["keyboard"] = await tester.test_keyboard_monitor()
    
    # Итоговый отчет
    print()
    print("=" * 70)
    print("📋 ИТОГОВЫЙ ОТЧЕТ")
    print("=" * 70)
    for test_name, result in results.items():
        status = "✅ ПРОЙДЕН" if result else "❌ ПРОВАЛЕН"
        print(f"{test_name}: {status}")
    print("=" * 70)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n\n⚠️ Тест прерван пользователем")
        sys.exit(0)


