#!/usr/bin/env python3
"""
Тест устойчивости клавиатурного монитора (Quartz Event Tap Watchdog & Stuck Modifier Recovery).
Проверяет механизмы самовосстановления при потере фокуса или залипании.
"""

import sys
import os
import time
import threading
import logging
from unittest.mock import MagicMock, patch
from pathlib import Path

# Добавляем пути к модулям
CLIENT_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(CLIENT_ROOT))

from modules.input_processing.keyboard.mac.quartz_monitor import QuartzKeyboardMonitor
from modules.input_processing.keyboard.types import KeyboardConfig, KeyEventType

# Настройка логирования
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger("KeyboardTest")

def test_config_values():
    """Проверка новых значений таймаутов в конфиге"""
    print("\n" + "="*80)
    print("ТЕСТ 1: Проверка конфигурации (120с / 60с)")
    print("="*80)
    
    config = KeyboardConfig(
        key_to_monitor="ctrl_n",
        short_press_threshold=0.1,
        long_press_threshold=0.6,
        event_cooldown=0.1,
        hold_check_interval=0.05,
        debounce_time=0.1
        # defaults should be 120 and 60 now
    )
    
    monitor = QuartzKeyboardMonitor(config)
    print(f"DEBUG: combo_timeout_sec = {monitor.combo_timeout_sec}")
    print(f"DEBUG: key_state_timeout_sec = {monitor.key_state_timeout_sec}")
    
    assert monitor.combo_timeout_sec == 120.0, f"Ожидалось 120.0, получено {monitor.combo_timeout_sec}"
    assert monitor.key_state_timeout_sec == 60.0, f"Ожидалось 60.0, получено {monitor.key_state_timeout_sec}"
    print("✅ ТЕСТ 1 ПРОЙДЕН: Таймауты увеличены корректно")

def test_watchdog_recovery():
    """Проверка Watchdog (восстановление отключенного тапа)"""
    print("\n" + "="*80)
    print("ТЕСТ 2: Проверка Watchdog (восстановление CGEventTap)")
    print("="*80)
    
    config = KeyboardConfig(
        key_to_monitor="ctrl_n",
        short_press_threshold=0.1,
        long_press_threshold=0.6,
        event_cooldown=0.1,
        hold_check_interval=0.05,
        debounce_time=0.1
    )
    
    # Мокаем Quartz функции
    with patch('Quartz.CGEventTapIsEnabled') as mock_enabled, \
         patch('Quartz.CGEventTapEnable') as mock_enable:
        
        monitor = QuartzKeyboardMonitor(config)
        monitor._tap = MagicMock() # Имитируем созданный тап
        monitor._last_tap_check_time = 0
        
        # Симулируем ситуацию: система отключила тап
        mock_enabled.return_value = False
        
        print("🔍 Симуляция: CGEventTap отключен системой...")
        monitor._check_and_recover_tap()
        
        # Проверяем, что watchdog вызвал включение
        mock_enable.assert_called_with(monitor._tap, True)
        assert monitor._tap_recovery_count == 1
        print(f"✅ Watchdog обнаружил отключение и вызвал восстановление (count={monitor._tap_recovery_count})")
        
        # Симулируем ситуацию: тап работает
        mock_enabled.return_value = True
        monitor._check_and_recover_tap()
        assert monitor._tap_recovery_count == 1 # Не должно увеличиться
        print("✅ Watchdog не вмешивается, если всё работает")

def test_stuck_modifier_recovery():
    """Проверка восстановления при расхождении состояния в коде и в системе"""
    print("\n" + "="*80)
    print("ТЕСТ 3: Проверка Stuck Modifier Recovery (CGEventSourceFlagsState)")
    print("="*80)
    
    config = KeyboardConfig(
        key_to_monitor="ctrl_n",
        short_press_threshold=0.1,
        long_press_threshold=0.6,
        event_cooldown=0.1,
        hold_check_interval=0.05,
        debounce_time=0.1
    )
    
    # Импортируем маску для мока
    from Quartz import kCGEventFlagMaskControl
    
    with patch('Quartz.CGEventSourceFlagsState') as mock_flags:
        monitor = QuartzKeyboardMonitor(config)
        
        # Ситуация: монитор думает что Control зажат, но в системе он ОТПУЩЕН
        monitor._control_pressed = True
        monitor._control_last_event_time = time.time()
        
        # Мокаем систему: Control не нажат (0)
        mock_flags.return_value = 0 
        
        print("🔍 Симуляция: Монитор думает Control нажат, но в Hardware он отпущен...")
        monitor._check_and_reset_stuck_state()
        
        assert monitor._control_pressed is False
        print("✅ Система обнаружила несоответствие и сбросила залипший Control")
        
        # Ситуация: монитор думает Control нажат, и в системе он НАЖАТ
        monitor._control_pressed = True
        mock_flags.return_value = kCGEventFlagMaskControl
        monitor._check_and_reset_stuck_state()
        
        assert monitor._control_pressed is True
        print("✅ Система подтвердила нажатие, сброс не потребовался")

if __name__ == "__main__":
    try:
        test_config_values()
        test_watchdog_recovery()
        test_stuck_modifier_recovery()
        print("\n" + "="*80)
        print("🎉 ВСЕ ТЕСТЫ УСПЕШНО ПРОЙДЕНЫ!")
        print("="*80)
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ ТЕСТ ПРОВАЛЕН: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
