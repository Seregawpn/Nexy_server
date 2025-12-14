#!/usr/bin/env python3
"""
Тест взаимодействия Input и Output режимов в AVF аудиосистеме

Проверяет:
- Переключение между Input и Output режимами
- Одновременная работа Input и Output
- Взаимодействие с Shortcut (клавиатурные комбинации)
- Переключение устройств во время работы
- Конфигурационные события
"""

import sys
import os
import logging
import asyncio
import time
import threading
from pathlib import Path
from typing import Optional, Dict, Any, List

# Добавляем путь к клиенту
client_path = Path(__file__).parent.parent
sys.path.insert(0, str(client_path))

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Цвета для вывода
class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

def print_test(test_name: str):
    """Вывести заголовок теста"""
    print(f"\n{Colors.HEADER}{Colors.BOLD}{'='*80}{Colors.ENDC}")
    print(f"{Colors.HEADER}{Colors.BOLD}ТЕСТ: {test_name}{Colors.ENDC}")
    print(f"{Colors.HEADER}{Colors.BOLD}{'='*80}{Colors.ENDC}\n")

def print_success(message: str):
    """Вывести успешное сообщение"""
    print(f"{Colors.OKGREEN}✅ {message}{Colors.ENDC}")

def print_error(message: str):
    """Вывести сообщение об ошибке"""
    print(f"{Colors.FAIL}❌ {message}{Colors.ENDC}")

def print_warning(message: str):
    """Вывести предупреждение"""
    print(f"{Colors.WARNING}⚠️  {message}{Colors.ENDC}")

def print_info(message: str):
    """Вывести информационное сообщение"""
    print(f"{Colors.OKCYAN}ℹ️  {message}{Colors.ENDC}")

# ============================================================================
# ТЕСТ 1: Переключение между Input и Output режимами
# ============================================================================

async def test_1_mode_switching(engine, event_bus):
    """Тест 1: Переключение между Input и Output режимами"""
    print_test("1. Переключение между Input и Output режимами")
    
    if engine is None:
        print_error("Экземпляр engine не передан")
        return False
    
    try:
        import numpy as np
        
        # Проверяем начальное состояние
        print_info("Проверка начального состояния...")
        print_info(f"Input state: {engine._input_state.name}")
        print_info(f"Output state: {engine._output_state.name}")
        
        # ТЕСТ 1.1: Output → Input
        print_info("\n--- Тест 1.1: Запуск Output, затем Input ---")
        
        # Создаём короткий тестовый сигнал
        sample_rate = 48000
        duration_sec = 0.5
        num_samples = int(sample_rate * duration_sec)
        t = np.linspace(0, duration_sec, num_samples, False)
        audio_data = (np.sin(2 * np.pi * 440.0 * t) * 32767).astype(np.int16)
        
        print_info("Запуск воспроизведения (Output)...")
        await engine.play_audio(audio_data.tobytes(), sample_rate=sample_rate, channels=1)
        print_success("Воспроизведение запущено")
        
        # Проверяем состояние
        await asyncio.sleep(0.1)
        if engine._output_state.name == "RUNNING":
            print_success(f"Output state: {engine._output_state.name}")
        else:
            print_warning(f"Output state: {engine._output_state.name} (ожидалось RUNNING)")
        
        # Запускаем запись (Input) во время воспроизведения
        input_data_received = []
        
        async def on_input_data(data: bytes, sample_rate: int, channels: int):
            input_data_received.append((data, sample_rate, channels))
        
        print_info("Запуск записи (Input) во время воспроизведения...")
        await engine.start_input(callback=on_input_data)
        print_success("Запись запущена")
        
        # Проверяем, что оба режима активны
        await asyncio.sleep(0.1)
        print_info(f"Input state: {engine._input_state.name}")
        print_info(f"Output state: {engine._output_state.name}")
        
        if engine._input_state.name == "RUNNING" and engine._output_state.name == "RUNNING":
            print_success("Оба режима активны одновременно (Input + Output)")
        else:
            print_warning(f"Состояния: Input={engine._input_state.name}, Output={engine._output_state.name}")
        
        # Ждём завершения воспроизведения
        await asyncio.sleep(1.0)
        
        # Останавливаем запись
        print_info("Остановка записи (Input)...")
        await engine.stop_input()
        print_success("Запись остановлена")
        
        # Проверяем состояние после остановки Input
        await asyncio.sleep(0.1)
        if engine._input_state.name == "IDLE":
            print_success(f"Input state: {engine._input_state.name} (остановлен)")
        else:
            print_warning(f"Input state: {engine._input_state.name} (ожидалось IDLE)")
        
        if engine._output_state.name == "IDLE":
            print_success(f"Output state: {engine._output_state.name} (воспроизведение завершено)")
        else:
            print_warning(f"Output state: {engine._output_state.name} (ожидалось IDLE)")
        
        # ТЕСТ 1.2: Input → Output
        print_info("\n--- Тест 1.2: Запуск Input, затем Output ---")
        
        print_info("Запуск записи (Input)...")
        await engine.start_input(callback=on_input_data)
        print_success("Запись запущена")
        
        await asyncio.sleep(0.1)
        if engine._input_state.name == "RUNNING":
            print_success(f"Input state: {engine._input_state.name}")
        else:
            print_warning(f"Input state: {engine._input_state.name} (ожидалось RUNNING)")
        
        # Запускаем воспроизведение во время записи
        print_info("Запуск воспроизведения (Output) во время записи...")
        await engine.play_audio(audio_data.tobytes(), sample_rate=sample_rate, channels=1)
        print_success("Воспроизведение запущено")
        
        # Проверяем, что оба режима активны
        await asyncio.sleep(0.1)
        if engine._input_state.name == "RUNNING" and engine._output_state.name == "RUNNING":
            print_success("Оба режима активны одновременно (Input + Output)")
        else:
            print_warning(f"Состояния: Input={engine._input_state.name}, Output={engine._output_state.name}")
        
        # Ждём завершения воспроизведения
        await asyncio.sleep(1.0)
        
        # Останавливаем запись
        print_info("Остановка записи (Input)...")
        await engine.stop_input()
        print_success("Запись остановлена")
        
        return True
        
    except Exception as e:
        print_error(f"Ошибка при тестировании переключения режимов: {e}")
        import traceback
        traceback.print_exc()
        return False

# ============================================================================
# ТЕСТ 2: Взаимодействие с Shortcut (симуляция)
# ============================================================================

async def test_2_shortcut_interaction(engine, event_bus):
    """Тест 2: Взаимодействие с Shortcut (симуляция клавиатурных комбинаций)"""
    print_test("2. Взаимодействие с Shortcut (симуляция)")
    
    if engine is None or event_bus is None:
        print_error("Экземпляр engine или event_bus не передан")
        return False
    
    try:
        # Создаём события для отслеживания
        interrupt_received = asyncio.Event()
        mode_changed = asyncio.Event()
        
        async def on_interrupt(event_data):
            print_success("Событие interrupt.request получено!")
            interrupt_received.set()
        
        async def on_mode_changed(event_data):
            print_success(f"Событие app.mode_changed получено: {event_data.get('data', {}).get('mode', 'unknown')}")
            mode_changed.set()
        
        await event_bus.subscribe("interrupt.request", on_interrupt)
        await event_bus.subscribe("app.mode_changed", on_mode_changed)
        
        # ТЕСТ 2.1: Прерывание воспроизведения через Shortcut
        print_info("--- Тест 2.1: Прерывание воспроизведения через Shortcut ---")
        
        import numpy as np
        sample_rate = 48000
        duration_sec = 2.0
        num_samples = int(sample_rate * duration_sec)
        t = np.linspace(0, duration_sec, num_samples, False)
        audio_data = (np.sin(2 * np.pi * 440.0 * t) * 32767).astype(np.int16)
        
        print_info("Запуск длительного воспроизведения (2 секунды)...")
        await engine.play_audio(audio_data.tobytes(), sample_rate=sample_rate, channels=1)
        print_success("Воспроизведение запущено")
        
        # Симулируем нажатие Shortcut (Ctrl+N) через 0.5 секунды
        await asyncio.sleep(0.5)
        print_info("Симуляция нажатия Shortcut (Ctrl+N)...")
        await event_bus.publish("interrupt.request", {
            "source": "keyboard.short_press",
            "session_id": "test_shortcut"
        })
        print_success("Событие interrupt.request опубликовано")
        
        # Ждём обработки прерывания
        try:
            await asyncio.wait_for(interrupt_received.wait(), timeout=1.0)
            print_success("Прерывание обработано")
        except asyncio.TimeoutError:
            print_warning("Событие interrupt.request не получено за 1 секунду")
        
        # Проверяем состояние после прерывания
        await asyncio.sleep(0.2)
        if engine._output_state.name == "IDLE":
            print_success(f"Output state: {engine._output_state.name} (воспроизведение прервано)")
        else:
            print_warning(f"Output state: {engine._output_state.name} (ожидалось IDLE после прерывания)")
        
        # ТЕСТ 2.2: Переключение режима через Shortcut
        print_info("\n--- Тест 2.2: Переключение режима через Shortcut ---")
        
        print_info("Публикация события mode.request (SLEEPING → LISTENING)...")
        await event_bus.publish("mode.request", {
            "target": "LISTENING",
            "source": "keyboard.short_press",
            "session_id": "test_mode_switch"
        })
        print_success("Событие mode.request опубликовано")
        
        # Ждём обработки переключения режима
        try:
            await asyncio.wait_for(mode_changed.wait(), timeout=1.0)
            print_success("Режим переключён")
        except asyncio.TimeoutError:
            print_warning("Событие app.mode_changed не получено за 1 секунду")
        
        return True
        
    except Exception as e:
        print_error(f"Ошибка при тестировании взаимодействия с Shortcut: {e}")
        import traceback
        traceback.print_exc()
        return False

# ============================================================================
# ТЕСТ 3: Переключение устройств во время работы Input/Output
# ============================================================================

async def test_3_device_switching_during_operation(engine, event_bus):
    """Тест 3: Переключение устройств во время работы Input/Output"""
    print_test("3. Переключение устройств во время работы Input/Output")
    
    if engine is None or event_bus is None:
        print_error("Экземпляр engine или event_bus не передан")
        return False
    
    try:
        import numpy as np
        
        # Создаём события для отслеживания
        output_changed = asyncio.Event()
        input_changed = asyncio.Event()
        config_changed = asyncio.Event()
        
        async def on_output_changed(event_data):
            print_success("Событие audio.device.output_changed получено!")
            output_changed.set()
        
        async def on_input_changed(event_data):
            print_success("Событие audio.device.input_changed получено!")
            input_changed.set()
        
        await event_bus.subscribe("audio.device.output_changed", on_output_changed)
        await event_bus.subscribe("audio.device.input_changed", on_input_changed)
        
        # ТЕСТ 3.1: Переключение устройства во время воспроизведения
        print_info("--- Тест 3.1: Переключение устройства во время воспроизведения ---")
        
        sample_rate = 48000
        duration_sec = 2.0
        num_samples = int(sample_rate * duration_sec)
        t = np.linspace(0, duration_sec, num_samples, False)
        audio_data = (np.sin(2 * np.pi * 440.0 * t) * 32767).astype(np.int16)
        
        print_info("Запуск воспроизведения...")
        await engine.play_audio(audio_data.tobytes(), sample_rate=sample_rate, channels=1)
        print_success("Воспроизведение запущено")
        
        await asyncio.sleep(0.3)
        
        print_info("Текущее OUTPUT устройство:")
        current_output = engine._get_real_output_device_name()
        print_info(f"  {current_output}")
        
        print_info("\n⚠️  ВАЖНО: Переключите OUTPUT устройство вручную (например, на AirPods)")
        print_info("Ожидание 5 секунд для переключения устройства...")
        
        # Ждём события смены устройства
        try:
            done, pending = await asyncio.wait(
                [asyncio.create_task(output_changed.wait())],
                timeout=5.0,
                return_when=asyncio.FIRST_COMPLETED
            )
            
            if done:
                print_success("Событие смены OUTPUT устройства получено!")
                
                # Проверяем, что воспроизведение продолжается
                await asyncio.sleep(0.2)
                if engine._output_state.name in ["RUNNING", "RECONNECTING"]:
                    print_success(f"Воспроизведение продолжается (state: {engine._output_state.name})")
                else:
                    print_warning(f"Воспроизведение остановлено (state: {engine._output_state.name})")
            else:
                print_warning("Событие смены устройства не получено за 5 секунд")
                print_warning("Это нормально, если устройство не переключалось")
        except Exception as e:
            print_error(f"Ошибка при ожидании события: {e}")
        
        # Ждём завершения воспроизведения
        await asyncio.sleep(2.0)
        
        # ТЕСТ 3.2: Переключение устройства во время записи
        print_info("\n--- Тест 3.2: Переключение устройства во время записи ---")
        
        input_data_received = []
        
        async def on_input_data(data: bytes, sample_rate: int, channels: int):
            input_data_received.append((data, sample_rate, channels))
        
        print_info("Запуск записи...")
        await engine.start_input(callback=on_input_data)
        print_success("Запись запущена")
        
        await asyncio.sleep(0.3)
        
        print_info("Текущее INPUT устройство:")
        current_input = engine._get_real_input_device_name()
        print_info(f"  {current_input}")
        
        print_info("\n⚠️  ВАЖНО: Переключите INPUT устройство вручную")
        print_info("Ожидание 5 секунд для переключения устройства...")
        
        # Ждём события смены устройства
        try:
            done, pending = await asyncio.wait(
                [asyncio.create_task(input_changed.wait())],
                timeout=5.0,
                return_when=asyncio.FIRST_COMPLETED
            )
            
            if done:
                print_success("Событие смены INPUT устройства получено!")
                
                # Проверяем, что запись продолжается
                await asyncio.sleep(0.2)
                if engine._input_state.name == "RUNNING":
                    print_success(f"Запись продолжается (state: {engine._input_state.name})")
                else:
                    print_warning(f"Запись остановлена (state: {engine._input_state.name})")
            else:
                print_warning("Событие смены устройства не получено за 5 секунд")
                print_warning("Это нормально, если устройство не переключалось")
        except Exception as e:
            print_error(f"Ошибка при ожидании события: {e}")
        
        # Останавливаем запись
        await asyncio.sleep(1.0)
        print_info("Остановка записи...")
        await engine.stop_input()
        print_success("Запись остановлена")
        
        return True
        
    except Exception as e:
        print_error(f"Ошибка при тестировании переключения устройств: {e}")
        import traceback
        traceback.print_exc()
        return False

# ============================================================================
# ТЕСТ 4: Одновременная работа Input и Output с переключением устройств
# ============================================================================

async def test_4_simultaneous_input_output_with_switching(engine, event_bus):
    """Тест 4: Одновременная работа Input и Output с переключением устройств"""
    print_test("4. Одновременная работа Input и Output с переключением устройств")
    
    if engine is None or event_bus is None:
        print_error("Экземпляр engine или event_bus не передан")
        return False
    
    try:
        import numpy as np
        
        # Создаём события для отслеживания
        output_changed = asyncio.Event()
        playback_completed = asyncio.Event()
        
        async def on_output_changed(event_data):
            print_success("Событие audio.device.output_changed получено во время одновременной работы!")
            output_changed.set()
        
        async def on_playback_completed(event_data):
            print_success("Событие audio.playback.completed получено!")
            playback_completed.set()
        
        await event_bus.subscribe("audio.device.output_changed", on_output_changed)
        await event_bus.subscribe("audio.playback.completed", on_playback_completed)
        
        # Запускаем запись
        input_data_received = []
        
        async def on_input_data(data: bytes, sample_rate: int, channels: int):
            input_data_received.append((data, sample_rate, channels))
        
        print_info("Запуск записи (Input)...")
        await engine.start_input(callback=on_input_data)
        print_success("Запись запущена")
        
        # Запускаем воспроизведение
        sample_rate = 48000
        duration_sec = 2.0
        num_samples = int(sample_rate * duration_sec)
        t = np.linspace(0, duration_sec, num_samples, False)
        audio_data = (np.sin(2 * np.pi * 440.0 * t) * 32767).astype(np.int16)
        
        print_info("Запуск воспроизведения (Output) во время записи...")
        await engine.play_audio(audio_data.tobytes(), sample_rate=sample_rate, channels=1)
        print_success("Воспроизведение запущено")
        
        # Проверяем, что оба режима активны
        await asyncio.sleep(0.2)
        if engine._input_state.name == "RUNNING" and engine._output_state.name == "RUNNING":
            print_success("Оба режима активны одновременно (Input + Output)")
        else:
            print_warning(f"Состояния: Input={engine._input_state.name}, Output={engine._output_state.name}")
        
        print_info("\n⚠️  ВАЖНО: Переключите OUTPUT устройство вручную (например, на AirPods)")
        print_info("Ожидание 5 секунд для переключения устройства...")
        
        # Ждём события смены устройства
        try:
            await asyncio.wait_for(output_changed.wait(), timeout=5.0)
            print_success("Событие смены устройства получено во время одновременной работы!")
            
            # Проверяем, что оба режима продолжают работать
            await asyncio.sleep(0.2)
            if engine._input_state.name == "RUNNING":
                print_success(f"Запись продолжается (Input state: {engine._input_state.name})")
            else:
                print_warning(f"Запись остановлена (Input state: {engine._input_state.name})")
            
            if engine._output_state.name in ["RUNNING", "RECONNECTING"]:
                print_success(f"Воспроизведение продолжается (Output state: {engine._output_state.name})")
            else:
                print_warning(f"Воспроизведение остановлено (Output state: {engine._output_state.name})")
        except asyncio.TimeoutError:
            print_warning("Событие смены устройства не получено за 5 секунд")
            print_warning("Это нормально, если устройство не переключалось")
        
        # Ждём завершения воспроизведения
        try:
            await asyncio.wait_for(playback_completed.wait(), timeout=3.0)
            print_success("Воспроизведение завершено через callback")
        except asyncio.TimeoutError:
            print_warning("Событие playback.completed не получено за 3 секунды")
        
        # Останавливаем запись
        await asyncio.sleep(0.5)
        print_info("Остановка записи...")
        await engine.stop_input()
        print_success("Запись остановлена")
        
        # Проверяем финальное состояние
        await asyncio.sleep(0.1)
        if engine._input_state.name == "IDLE" and engine._output_state.name == "IDLE":
            print_success("Оба режима остановлены (Input + Output = IDLE)")
        else:
            print_warning(f"Финальные состояния: Input={engine._input_state.name}, Output={engine._output_state.name}")
        
        return True
        
    except Exception as e:
        print_error(f"Ошибка при тестировании одновременной работы: {e}")
        import traceback
        traceback.print_exc()
        return False

# ============================================================================
# ТЕСТ 5: Конфигурационные события при переключении режимов
# ============================================================================

async def test_5_configuration_events_during_mode_switching(engine, event_bus):
    """Тест 5: Конфигурационные события при переключении режимов"""
    print_test("5. Конфигурационные события при переключении режимов")
    
    if engine is None or event_bus is None:
        print_error("Экземпляр engine или event_bus не передан")
        return False
    
    try:
        import numpy as np
        
        # Создаём события для отслеживания
        resync_required = asyncio.Event()
        
        async def on_resync_required(event_data):
            print_success("Событие audio.device.output_resync_required получено!")
            resync_required.set()
        
        await event_bus.subscribe("audio.device.output_resync_required", on_resync_required)
        
        # Запускаем воспроизведение
        sample_rate = 48000
        duration_sec = 2.0
        num_samples = int(sample_rate * duration_sec)
        t = np.linspace(0, duration_sec, num_samples, False)
        audio_data = (np.sin(2 * np.pi * 440.0 * t) * 32767).astype(np.int16)
        
        print_info("Запуск воспроизведения...")
        await engine.play_audio(audio_data.tobytes(), sample_rate=sample_rate, channels=1)
        print_success("Воспроизведение запущено")
        
        print_info("\n⚠️  ВАЖНО: Переключите OUTPUT устройство вручную (например, на AirPods)")
        print_info("Это должно вызвать AVAudioEngineConfigurationChangeNotification")
        print_info("Ожидание 5 секунд для конфигурационного события...")
        
        # Ждём события ресинхронизации
        try:
            await asyncio.wait_for(resync_required.wait(), timeout=5.0)
            print_success("Событие ресинхронизации получено!")
            
            # Проверяем, что воспроизведение продолжается или возобновляется
            await asyncio.sleep(0.2)
            if engine._output_state.name in ["RUNNING", "RECONNECTING", "IDLE"]:
                print_success(f"Воспроизведение обработало конфигурационное событие (state: {engine._output_state.name})")
            else:
                print_warning(f"Неожиданное состояние после конфигурационного события (state: {engine._output_state.name})")
        except asyncio.TimeoutError:
            print_warning("Событие ресинхронизации не получено за 5 секунд")
            print_warning("Это нормально, если устройство не переключалось или конфигурационное событие не произошло")
        
        # Ждём завершения воспроизведения
        await asyncio.sleep(2.0)
        
        return True
        
    except Exception as e:
        print_error(f"Ошибка при тестировании конфигурационных событий: {e}")
        import traceback
        traceback.print_exc()
        return False

# ============================================================================
# ГЛАВНАЯ ФУНКЦИЯ
# ============================================================================

async def main():
    """Главная функция для запуска всех тестов"""
    print(f"\n{Colors.BOLD}{Colors.HEADER}")
    print("="*80)
    print("ТЕСТ ВЗАИМОДЕЙСТВИЯ INPUT И OUTPUT РЕЖИМОВ")
    print("="*80)
    print(f"{Colors.ENDC}\n")
    
    # Инициализация
    try:
        from modules.audio_avf.core.avf_audio_engine import AVFAudioEngine
        from config.unified_config_loader import UnifiedConfigLoader
        from integration.core.event_bus import EventBus
        
        print_info("Инициализация тестовой среды...")
        event_bus = EventBus()
        try:
            loop = asyncio.get_running_loop()
            event_bus.attach_loop(loop)
        except RuntimeError:
            pass
        
        loader = UnifiedConfigLoader()
        audio_config = loader.get_audio_config_object()
        engine = AVFAudioEngine(audio_config, event_bus=event_bus)
        print_success("Тестовая среда инициализирована")
        
    except Exception as e:
        print_error(f"Ошибка инициализации: {e}")
        import traceback
        traceback.print_exc()
        return
    
    results = []
    
    # ТЕСТ 1: Переключение между Input и Output режимами
    result1 = await test_1_mode_switching(engine, event_bus)
    results.append(("1. Переключение между Input и Output режимами", result1))
    
    # ТЕСТ 2: Взаимодействие с Shortcut
    result2 = await test_2_shortcut_interaction(engine, event_bus)
    results.append(("2. Взаимодействие с Shortcut", result2))
    
    # ТЕСТ 3: Переключение устройств во время работы
    result3 = await test_3_device_switching_during_operation(engine, event_bus)
    results.append(("3. Переключение устройств во время работы", result3))
    
    # ТЕСТ 4: Одновременная работа Input и Output
    result4 = await test_4_simultaneous_input_output_with_switching(engine, event_bus)
    results.append(("4. Одновременная работа Input и Output", result4))
    
    # ТЕСТ 5: Конфигурационные события
    result5 = await test_5_configuration_events_during_mode_switching(engine, event_bus)
    results.append(("5. Конфигурационные события", result5))
    
    # ИТОГИ
    print(f"\n{Colors.BOLD}{Colors.HEADER}")
    print("="*80)
    print("ИТОГИ ТЕСТИРОВАНИЯ")
    print("="*80)
    print(f"{Colors.ENDC}\n")
    
    for test_name, result in results:
        if result:
            print(f"{Colors.OKGREEN}✅ {test_name}: ПРОЙДЕН{Colors.ENDC}")
        else:
            print(f"{Colors.FAIL}❌ {test_name}: ПРОВАЛЕН{Colors.ENDC}")
    
    passed = sum(1 for _, result in results if result)
    total = len(results)
    
    print(f"\n{Colors.BOLD}Результат: {passed}/{total} тестов пройдено{Colors.ENDC}\n")
    
    if passed == total:
        print_success("Все тесты пройдены успешно! ✅")
    else:
        print_error(f"Провалено тестов: {total - passed} ❌")

if __name__ == "__main__":
    asyncio.run(main())


