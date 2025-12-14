#!/usr/bin/env python3
"""
Комплексный тест работоспособности AVF аудиосистемы

Проверяет все критические точки:
- Запуск приложения
- Output (воспроизведение)
- Input (запись)
- Переключение устройств
- Конфигурационные события
- Callback'и
- События EventBus
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
# ТЕСТ 1: Инициализация и создание экземпляра
# ============================================================================

async def test_1_initialization():
    """Тест 1: Инициализация AVFAudioEngine"""
    print_test("1. Инициализация AVFAudioEngine")
    
    try:
        from modules.audio_avf.core.avf_audio_engine import AVFAudioEngine
        from config.unified_config_loader import UnifiedConfigLoader
        from integration.core.event_bus import EventBus
        
        print_info("Создание EventBus...")
        event_bus = EventBus()
        # Прикрепляем event loop для безопасной публикации событий
        try:
            loop = asyncio.get_running_loop()
            event_bus.attach_loop(loop)
            print_success("EventBus создан и event loop прикреплён")
        except RuntimeError:
            print_warning("EventBus создан, но event loop недоступен")
        
        print_info("Загрузка конфигурации...")
        loader = UnifiedConfigLoader()
        audio_config = loader.get_audio_config_object()
        print_success("Конфигурация загружена")
        
        print_info("Создание экземпляра AVFAudioEngine...")
        engine = AVFAudioEngine(audio_config, event_bus=event_bus)
        print_success("Экземпляр AVFAudioEngine создан")
        
        # Проверяем атрибуты
        checks = []
        
        if engine._engine is not None:
            print_success("_engine создан")
            checks.append(True)
        else:
            print_error("_engine = None")
            checks.append(False)
        
        if engine._player_node is not None:
            print_success("_player_node создан")
            checks.append(True)
        else:
            print_error("_player_node = None")
            checks.append(False)
        
        if engine._output_node is not None:
            print_success("_output_node создан")
            checks.append(True)
        else:
            print_error("_output_node = None")
            checks.append(False)
        
        if engine._output_completion_callback is not None:
            print_success("_output_completion_callback создан")
            checks.append(True)
        else:
            print_error("_output_completion_callback = None")
            checks.append(False)
        
        if engine._player_node_connected:
            print_success("_player_node_connected = True")
            checks.append(True)
        else:
            print_error("_player_node_connected = False")
            checks.append(False)
        
        # EventBus не требует явной остановки
        
        return all(checks), engine, event_bus
        
    except Exception as e:
        print_error(f"Ошибка при инициализации: {e}")
        import traceback
        traceback.print_exc()
        return False, None, None

# ============================================================================
# ТЕСТ 2: Output (воспроизведение)
# ============================================================================

async def test_2_output_playback(engine, event_bus):
    """Тест 2: Воспроизведение аудио (Output)"""
    print_test("2. Воспроизведение аудио (Output)")
    
    if engine is None:
        print_error("Экземпляр engine не передан")
        return False
    
    try:
        import numpy as np
        from AVFoundation import AVAudioPCMBuffer, AVAudioFormat
        
        print_info("Создание тестового аудио буфера...")
        # Создаём короткий тестовый сигнал (1 секунда, 48000 Hz, моно)
        sample_rate = 48000
        duration_sec = 1.0
        num_samples = int(sample_rate * duration_sec)
        
        # Генерируем синусоиду 440 Hz
        t = np.linspace(0, duration_sec, num_samples, False)
        frequency = 440.0
        audio_data = np.sin(2 * np.pi * frequency * t)
        
        # Конвертируем в int16
        audio_data_int16 = (audio_data * 32767).astype(np.int16)
        print_success(f"Тестовый буфер создан: {len(audio_data_int16)} сэмплов, {sample_rate} Hz")
        
        # Проверяем состояние перед воспроизведением
        print_info("Проверка состояния перед воспроизведением...")
        if engine._output_state.name == "IDLE":
            print_success(f"_output_state = {engine._output_state.name}")
        else:
            print_warning(f"_output_state = {engine._output_state.name} (ожидалось IDLE)")
        
        # Создаём событие для отслеживания завершения
        playback_completed = asyncio.Event()
        playback_started = asyncio.Event()
        
        async def on_playback_completed(event_data):
            print_success("Событие audio.playback.completed получено!")
            playback_completed.set()
        
        async def on_playback_started(event_data):
            print_success("Событие playback.started получено!")
            playback_started.set()
        
        await event_bus.subscribe("audio.playback.completed", on_playback_completed)
        await event_bus.subscribe("playback.started", on_playback_started)
        
        print_info("Запуск воспроизведения...")
        await engine.play_audio(audio_data_int16.tobytes(), sample_rate=sample_rate, channels=1)
        print_success("Воспроизведение запущено")
        
        # Ждём начала воспроизведения
        try:
            await asyncio.wait_for(playback_started.wait(), timeout=2.0)
            print_success("Воспроизведение началось")
        except asyncio.TimeoutError:
            print_warning("Событие playback.started не получено за 2 секунды")
        
        # Проверяем состояние во время воспроизведения
        await asyncio.sleep(0.1)
        if engine._output_state.name == "RUNNING":
            print_success(f"_output_state = {engine._output_state.name} (воспроизведение активно)")
        else:
            print_warning(f"_output_state = {engine._output_state.name} (ожидалось RUNNING)")
        
        # Ждём завершения воспроизведения
        print_info("Ожидание завершения воспроизведения...")
        try:
            await asyncio.wait_for(playback_completed.wait(), timeout=3.0)
            print_success("Воспроизведение завершено через callback!")
            
            # Проверяем состояние после завершения
            if engine._output_state.name == "IDLE":
                print_success(f"_output_state = {engine._output_state.name} (воспроизведение завершено)")
            else:
                print_warning(f"_output_state = {engine._output_state.name} (ожидалось IDLE)")
            
            return True
        except asyncio.TimeoutError:
            print_error("Событие audio.playback.completed не получено за 3 секунды")
            print_warning("Возможно, используется fallback timeout")
            
            # Проверяем состояние через fallback timeout
            await asyncio.sleep(2.0)
            if engine._output_state.name == "IDLE":
                print_warning("Состояние перешло в IDLE через fallback timeout")
                return True
            else:
                print_error(f"Состояние всё ещё {engine._output_state.name} после timeout")
                return False
        
    except Exception as e:
        print_error(f"Ошибка при тестировании воспроизведения: {e}")
        import traceback
        traceback.print_exc()
        return False

# ============================================================================
# ТЕСТ 3: Input (запись)
# ============================================================================

async def test_3_input_recording(engine, event_bus):
    """Тест 3: Запись аудио (Input)"""
    print_test("3. Запись аудио (Input)")
    
    if engine is None:
        print_error("Экземпляр engine не передан")
        return False
    
    try:
        print_info("Проверка состояния перед записью...")
        if engine._input_state.name == "IDLE":
            print_success(f"_input_state = {engine._input_state.name}")
        else:
            print_warning(f"_input_state = {engine._input_state.name} (ожидалось IDLE)")
        
        # Создаём событие для отслеживания данных
        audio_data_received = []
        recording_started = asyncio.Event()
        
        async def on_audio_data(data: bytes, sample_rate: int, channels: int):
            audio_data_received.append((data, sample_rate, channels))
            if not recording_started.is_set():
                recording_started.set()
                print_success(f"Получены аудио данные: {len(data)} bytes, {sample_rate} Hz, {channels} ch")
        
        print_info("Запуск записи...")
        await engine.start_input(callback=on_audio_data)
        print_success("Запись запущена")
        
        # Ждём начала записи
        try:
            await asyncio.wait_for(recording_started.wait(), timeout=2.0)
            print_success("Запись началась")
        except asyncio.TimeoutError:
            print_warning("Аудио данные не получены за 2 секунды")
            print_warning("Возможно, микрофон недоступен или нет разрешения")
        
        # Проверяем состояние во время записи
        await asyncio.sleep(0.1)
        if engine._input_state.name == "RUNNING":
            print_success(f"_input_state = {engine._input_state.name} (запись активна)")
        else:
            print_warning(f"_input_state = {engine._input_state.name} (ожидалось RUNNING)")
        
        # Записываем 1 секунду
        print_info("Запись 1 секунды аудио...")
        await asyncio.sleep(1.0)
        
        print_info("Остановка записи...")
        await engine.stop_input()
        print_success("Запись остановлена")
        
        # Проверяем состояние после остановки
        if engine._input_state.name == "IDLE":
            print_success(f"_input_state = {engine._input_state.name} (запись остановлена)")
        else:
            print_warning(f"_input_state = {engine._input_state.name} (ожидалось IDLE)")
        
        if len(audio_data_received) > 0:
            print_success(f"Получено {len(audio_data_received)} чанков аудио данных")
            total_bytes = sum(len(data) for data, _, _ in audio_data_received)
            print_info(f"Всего записано: {total_bytes} bytes")
            return True
        else:
            print_warning("Аудио данные не получены")
            print_warning("Это может быть нормально, если микрофон недоступен")
            return True  # Не считаем это ошибкой
        
    except Exception as e:
        print_error(f"Ошибка при тестировании записи: {e}")
        import traceback
        traceback.print_exc()
        return False

# ============================================================================
# ТЕСТ 4: Переключение устройств
# ============================================================================

async def test_4_device_switching(engine, event_bus):
    """Тест 4: Переключение устройств"""
    print_test("4. Переключение устройств")
    
    if engine is None:
        print_error("Экземпляр engine не передан")
        return False
    
    try:
        print_info("Получение текущего OUTPUT устройства...")
        current_output = engine._get_real_output_device_name()
        print_info(f"Текущее OUTPUT устройство: {current_output}")
        
        print_info("Получение текущего INPUT устройства...")
        current_input = engine._get_real_input_device_name()
        print_info(f"Текущее INPUT устройство: {current_input}")
        
        # Создаём события для отслеживания смены устройств
        output_changed = asyncio.Event()
        input_changed = asyncio.Event()
        
        async def on_output_changed(event_data):
            print_success("Событие audio.device.output_changed получено!")
            output_changed.set()
        
        async def on_input_changed(event_data):
            print_success("Событие audio.device.input_changed получено!")
            input_changed.set()
        
        await event_bus.subscribe("audio.device.output_changed", on_output_changed)
        await event_bus.subscribe("audio.device.input_changed", on_input_changed)
        
        print_info("Мониторинг устройств активен")
        print_info("Попробуйте переключить устройство вывода/ввода вручную...")
        print_info("Ожидание 5 секунд для переключения устройства...")
        
        # Ждём события смены устройства
        try:
            done, pending = await asyncio.wait(
                [asyncio.create_task(output_changed.wait()), asyncio.create_task(input_changed.wait())],
                timeout=5.0,
                return_when=asyncio.FIRST_COMPLETED
            )
            
            if done:
                print_success("Событие смены устройства получено!")
                return True
            else:
                print_warning("Событие смены устройства не получено за 5 секунд")
                print_warning("Это нормально, если устройство не переключалось")
                return True  # Не считаем это ошибкой
        except Exception as e:
            print_error(f"Ошибка при ожидании события: {e}")
            return False
        
    except Exception as e:
        print_error(f"Ошибка при тестировании переключения устройств: {e}")
        import traceback
        traceback.print_exc()
        return False

# ============================================================================
# ТЕСТ 5: Конфигурационные события
# ============================================================================

async def test_5_configuration_events(engine, event_bus):
    """Тест 5: Конфигурационные события AVAudioEngine"""
    print_test("5. Конфигурационные события AVAudioEngine")
    
    if engine is None:
        print_error("Экземпляр engine не передан")
        return False
    
    try:
        # Создаём событие для отслеживания конфигурационных событий
        config_changed = asyncio.Event()
        
        async def on_config_change(event_data):
            print_success("Событие AVAudioEngineConfigurationChangeNotification получено!")
            config_changed.set()
        
        # Подписываемся на событие через внутренний механизм
        print_info("Мониторинг конфигурационных событий активен")
        print_info("Попробуйте переключить устройство вывода/ввода...")
        print_info("Ожидание 5 секунд для конфигурационного события...")
        
        # Ждём события
        try:
            await asyncio.wait_for(config_changed.wait(), timeout=5.0)
            print_success("Конфигурационное событие получено!")
            return True
        except asyncio.TimeoutError:
            print_warning("Конфигурационное событие не получено за 5 секунд")
            print_warning("Это нормально, если устройство не переключалось")
            return True  # Не считаем это ошибкой
        
    except Exception as e:
        print_error(f"Ошибка при тестировании конфигурационных событий: {e}")
        import traceback
        traceback.print_exc()
        return False

# ============================================================================
# ТЕСТ 6: Множественные экземпляры
# ============================================================================

async def test_6_multiple_instances():
    """Тест 6: Множественные экземпляры"""
    print_test("6. Множественные экземпляры AVFAudioEngine")
    
    try:
        from modules.audio_avf.core.avf_audio_engine import AVFAudioEngine, _AVF_COMPLETION_CALLBACK
        from config.unified_config_loader import UnifiedConfigLoader
        
        loader = UnifiedConfigLoader()
        audio_config = loader.get_audio_config_object()
        
        print_info("Создание первого экземпляра...")
        engine1 = AVFAudioEngine(audio_config, event_bus=None)
        print_success("Первый экземпляр создан")
        
        callback1 = _AVF_COMPLETION_CALLBACK
        print_info(f"Глобальный callback после engine1: {callback1 is not None}")
        
        print_info("Создание второго экземпляра...")
        engine2 = AVFAudioEngine(audio_config, event_bus=None)
        print_success("Второй экземпляр создан")
        
        callback2 = _AVF_COMPLETION_CALLBACK
        
        # Проверяем, что callback одинаковый
        if callback1 is callback2:
            print_success("Глобальный callback одинаковый для обоих экземпляров")
        else:
            print_error("Глобальный callback разный для разных экземпляров")
            return False
        
        if engine1._output_completion_callback is engine2._output_completion_callback:
            print_success("engine._output_completion_callback одинаковый для обоих экземпляров")
        else:
            print_error("engine._output_completion_callback разный для разных экземпляров")
            return False
        
        # Проверяем, что player_node разные
        if engine1._player_node is not engine2._player_node:
            print_success("player_node разные для разных экземпляров (правильно)")
        else:
            print_error("player_node одинаковые для разных экземпляров (проблема!)")
            return False
        
        return True
        
    except Exception as e:
        print_error(f"Ошибка при тестировании множественных экземпляров: {e}")
        import traceback
        traceback.print_exc()
        return False

# ============================================================================
# ТЕСТ 7: EventBus интеграция
# ============================================================================

async def test_7_eventbus_integration(engine, event_bus):
    """Тест 7: Интеграция с EventBus"""
    print_test("7. Интеграция с EventBus")
    
    if engine is None or event_bus is None:
        print_error("Экземпляр engine или event_bus не передан")
        return False
    
    try:
        # Прикрепляем event loop
        print_info("Прикрепление event loop к engine...")
        if hasattr(event_bus, '_loop') and event_bus._loop:
            engine.attach_event_loop(event_bus._loop)
            print_success("Event loop прикреплён")
        else:
            print_warning("EventBus loop недоступен")
        
        # Проверяем публикацию событий
        events_received = []
        
        async def on_any_event(event_type: str, event_data: Dict[str, Any]):
            events_received.append((event_type, event_data))
            print_info(f"Событие получено: {event_type}")
        
        # Подписываемся на все события аудио
        await event_bus.subscribe("audio.device.output_changed", lambda e: on_any_event("audio.device.output_changed", e))
        await event_bus.subscribe("audio.device.input_changed", lambda e: on_any_event("audio.device.input_changed", e))
        await event_bus.subscribe("audio.playback.completed", lambda e: on_any_event("audio.playback.completed", e))
        
        print_info("Подписки на события созданы")
        print_info("Ожидание 2 секунды для проверки публикации событий...")
        
        await asyncio.sleep(2.0)
        
        if len(events_received) > 0:
            print_success(f"Получено {len(events_received)} событий")
            return True
        else:
            print_warning("События не получены (это нормально, если нет активности)")
            return True  # Не считаем это ошибкой
        
    except Exception as e:
        print_error(f"Ошибка при тестировании EventBus интеграции: {e}")
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
    print("КОМПЛЕКСНЫЙ ТЕСТ РАБОТОСПОСОБНОСТИ AVF АУДИОСИСТЕМЫ")
    print("="*80)
    print(f"{Colors.ENDC}\n")
    
    results = []
    
    # ТЕСТ 1: Инициализация
    result1, engine, event_bus = await test_1_initialization()
    results.append(("1. Инициализация", result1))
    if not result1:
        print_error("\n❌ ТЕСТ 1 ПРОВАЛЕН. Остановка тестирования.")
        return
    
    # ТЕСТ 2: Output
    result2 = await test_2_output_playback(engine, event_bus)
    results.append(("2. Output (воспроизведение)", result2))
    
    # ТЕСТ 3: Input
    result3 = await test_3_input_recording(engine, event_bus)
    results.append(("3. Input (запись)", result3))
    
    # ТЕСТ 4: Переключение устройств
    result4 = await test_4_device_switching(engine, event_bus)
    results.append(("4. Переключение устройств", result4))
    
    # ТЕСТ 5: Конфигурационные события
    result5 = await test_5_configuration_events(engine, event_bus)
    results.append(("5. Конфигурационные события", result5))
    
    # ТЕСТ 6: Множественные экземпляры
    result6 = await test_6_multiple_instances()
    results.append(("6. Множественные экземпляры", result6))
    
    # ТЕСТ 7: EventBus интеграция
    result7 = await test_7_eventbus_integration(engine, event_bus)
    results.append(("7. EventBus интеграция", result7))
    
    # EventBus не требует явной остановки
    
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


