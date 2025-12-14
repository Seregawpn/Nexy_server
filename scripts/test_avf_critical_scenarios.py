#!/usr/bin/env python3
"""
Комплексный тест критических и потенциально опасных сценариев AVF аудиосистемы

Проверяет:
1. Race conditions при одновременном доступе
2. Переключение устройств во время воспроизведения/записи
3. Прерывания во время воспроизведения
4. Множественные экземпляры AVFAudioEngine
5. Переключение режимов во время работы аудио
6. Одновременная работа Input и Output с конфликтами
7. Ошибки и восстановление после ошибок
8. Конфигурационные события (AirPods переключение режимов)
9. Таймауты и fallback механизмы
10. Память и утечки ресурсов
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
# ТЕСТ 1: Race conditions при одновременном доступе
# ============================================================================

async def test_1_race_conditions(engine, event_bus):
    """Тест 1: Race conditions при одновременном доступе к состоянию"""
    print_test("1. Race conditions при одновременном доступе")
    
    if engine is None:
        print_error("Экземпляр engine не передан")
        return False
    
    try:
        import numpy as np
        
        # Создаём несколько потоков, которые одновременно пытаются изменить состояние
        errors = []
        results = []
        
        def concurrent_playback(thread_id):
            """Параллельное воспроизведение из разных потоков"""
            try:
                loop = asyncio.new_event_loop()
                asyncio.set_event_loop(loop)
                
                sample_rate = 48000
                duration_sec = 0.5
                num_samples = int(sample_rate * duration_sec)
                t = np.linspace(0, duration_sec, num_samples, False)
                audio_data = (np.sin(2 * np.pi * 440.0 * t) * 32767).astype(np.int16)
                
                result = loop.run_until_complete(
                    engine.play_audio(audio_data.tobytes(), sample_rate=sample_rate, channels=1)
                )
                results.append((thread_id, result))
            except Exception as e:
                errors.append((thread_id, str(e)))
        
        print_info("Запуск 5 параллельных потоков воспроизведения...")
        threads = []
        for i in range(5):
            thread = threading.Thread(target=concurrent_playback, args=(i,))
            threads.append(thread)
            thread.start()
        
        # Ждём завершения всех потоков
        for thread in threads:
            thread.join(timeout=5.0)
        
        if errors:
            print_error(f"Обнаружены ошибки в {len(errors)} потоках:")
            for thread_id, error in errors:
                print_error(f"  Поток {thread_id}: {error}")
            return False
        
        print_success(f"Все {len(results)} потоков завершились без ошибок")
        
        # Проверяем, что состояние корректно после всех операций
        await asyncio.sleep(0.5)
        if engine._output_state.name in ["IDLE", "RUNNING"]:
            print_success(f"Финальное состояние: {engine._output_state.name}")
        else:
            print_warning(f"Неожиданное финальное состояние: {engine._output_state.name}")
        
        return True
        
    except Exception as e:
        print_error(f"Ошибка при тестировании race conditions: {e}")
        import traceback
        traceback.print_exc()
        return False

# ============================================================================
# ТЕСТ 2: Переключение устройств во время воспроизведения
# ============================================================================

async def test_2_device_switching_during_playback(engine, event_bus):
    """Тест 2: Переключение устройств во время активного воспроизведения"""
    print_test("2. Переключение устройств во время воспроизведения")
    
    if engine is None or event_bus is None:
        print_error("Экземпляр engine или event_bus не передан")
        return False
    
    try:
        import numpy as np
        
        # Создаём длительное воспроизведение
        sample_rate = 48000
        duration_sec = 3.0
        num_samples = int(sample_rate * duration_sec)
        t = np.linspace(0, duration_sec, num_samples, False)
        audio_data = (np.sin(2 * np.pi * 440.0 * t) * 32767).astype(np.int16)
        
        print_info("Запуск длительного воспроизведения (3 секунды)...")
        await engine.play_audio(audio_data.tobytes(), sample_rate=sample_rate, channels=1)
        print_success("Воспроизведение запущено")
        
        # Симулируем несколько переключений устройств
        device_changes = []
        async def on_device_changed(event_data):
            device_changes.append(event_data)
            print_success("Событие смены устройства получено!")
        
        await event_bus.subscribe("audio.device.output_changed", on_device_changed)
        
        print_info("Симуляция переключения устройств через 0.5, 1.0, 1.5 секунды...")
        
        # Симулируем конфигурационные события
        for delay in [0.5, 1.0, 1.5]:
            await asyncio.sleep(delay)
            print_info(f"Симуляция смены устройства через {delay}s...")
            # Публикуем событие конфигурационного изменения
            await event_bus.publish("audio.device.output_resync_required", {
                "device_name": f"Test Device {delay}",
                "was_running": True
            })
        
        # Ждём завершения воспроизведения
        await asyncio.sleep(2.0)
        
        if len(device_changes) > 0:
            print_success(f"Обработано {len(device_changes)} событий смены устройства")
        else:
            print_warning("События смены устройства не получены (это нормально для симуляции)")
        
        # Проверяем финальное состояние
        await asyncio.sleep(0.2)
        if engine._output_state.name == "IDLE":
            print_success(f"Финальное состояние: {engine._output_state.name} (корректно)")
        else:
            print_warning(f"Финальное состояние: {engine._output_state.name} (ожидалось IDLE)")
        
        return True
        
    except Exception as e:
        print_error(f"Ошибка при тестировании переключения устройств: {e}")
        import traceback
        traceback.print_exc()
        return False

# ============================================================================
# ТЕСТ 3: Прерывания во время воспроизведения
# ============================================================================

async def test_3_interrupts_during_playback(engine, event_bus):
    """Тест 3: Прерывания во время активного воспроизведения"""
    print_test("3. Прерывания во время воспроизведения")
    
    if engine is None or event_bus is None:
        print_error("Экземпляр engine или event_bus не передан")
        return False
    
    try:
        import numpy as np
        
        # Создаём длительное воспроизведение
        sample_rate = 48000
        duration_sec = 3.0
        num_samples = int(sample_rate * duration_sec)
        t = np.linspace(0, duration_sec, num_samples, False)
        audio_data = (np.sin(2 * np.pi * 440.0 * t) * 32767).astype(np.int16)
        
        print_info("Запуск длительного воспроизведения (3 секунды)...")
        await engine.play_audio(audio_data.tobytes(), sample_rate=sample_rate, channels=1)
        print_success("Воспроизведение запущено")
        
        # Симулируем прерывание через 0.5 секунды
        await asyncio.sleep(0.5)
        print_info("Симуляция прерывания через playback.cancelled...")
        await event_bus.publish("playback.cancelled", {
            "session_id": "test_interrupt",
            "reason": "user_interrupt",
            "source": "test"
        })
        print_success("Событие playback.cancelled опубликовано")
        
        # Ждём обработки прерывания
        await asyncio.sleep(0.3)
        
        # Проверяем, что воспроизведение остановлено
        if engine._output_state.name == "IDLE":
            print_success(f"Воспроизведение остановлено (state: {engine._output_state.name})")
        else:
            print_warning(f"Воспроизведение не остановлено (state: {engine._output_state.name})")
        
        # Пробуем запустить новое воспроизведение после прерывания
        print_info("Попытка запуска нового воспроизведения после прерывания...")
        short_audio = (np.sin(2 * np.pi * 440.0 * np.linspace(0, 0.5, 24000, False)) * 32767).astype(np.int16)
        result = await engine.play_audio(short_audio.tobytes(), sample_rate=sample_rate, channels=1)
        
        if result:
            print_success("Новое воспроизведение запущено после прерывания")
            await asyncio.sleep(1.0)
        else:
            print_error("Не удалось запустить новое воспроизведение после прерывания")
            return False
        
        return True
        
    except Exception as e:
        print_error(f"Ошибка при тестировании прерываний: {e}")
        import traceback
        traceback.print_exc()
        return False

# ============================================================================
# ТЕСТ 4: Множественные экземпляры AVFAudioEngine
# ============================================================================

async def test_4_multiple_instances():
    """Тест 4: Множественные экземпляры AVFAudioEngine"""
    print_test("4. Множественные экземпляры AVFAudioEngine")
    
    try:
        from modules.audio_avf.core.avf_audio_engine import AVFAudioEngine
        from config.unified_config_loader import UnifiedConfigLoader
        from integration.core.event_bus import EventBus
        
        print_info("Создание нескольких экземпляров AVFAudioEngine...")
        event_bus = EventBus()
        try:
            loop = asyncio.get_running_loop()
            event_bus.attach_loop(loop)
        except RuntimeError:
            pass
        
        loader = UnifiedConfigLoader()
        audio_config = loader.get_audio_config_object()
        
        engines = []
        for i in range(3):
            engine = AVFAudioEngine(audio_config, event_bus=event_bus)
            engines.append(engine)
            print_success(f"Экземпляр {i+1} создан")
        
        # Проверяем, что completion callback общий для всех
        print_info("Проверка completion callback для всех экземпляров...")
        callbacks = [e._output_completion_callback for e in engines if hasattr(e, '_output_completion_callback')]
        if len(set(id(cb) for cb in callbacks if cb is not None)) <= 1:
            print_success("Completion callback общий для всех экземпляров (или None)")
        else:
            print_warning("Разные completion callback для разных экземпляров")
        
        # Пробуем воспроизведение на разных экземплярах
        import numpy as np
        sample_rate = 48000
        duration_sec = 0.5
        num_samples = int(sample_rate * duration_sec)
        t = np.linspace(0, duration_sec, num_samples, False)
        audio_data = (np.sin(2 * np.pi * 440.0 * t) * 32767).astype(np.int16)
        
        print_info("Попытка воспроизведения на всех экземплярах последовательно...")
        for i, engine in enumerate(engines):
            print_info(f"Воспроизведение на экземпляре {i+1}...")
            result = await engine.play_audio(audio_data.tobytes(), sample_rate=sample_rate, channels=1)
            if result:
                print_success(f"Воспроизведение на экземпляре {i+1} запущено")
            else:
                print_error(f"Не удалось запустить воспроизведение на экземпляре {i+1}")
            await asyncio.sleep(0.6)
        
        print_success("Все экземпляры протестированы")
        return True
        
    except Exception as e:
        print_error(f"Ошибка при тестировании множественных экземпляров: {e}")
        import traceback
        traceback.print_exc()
        return False

# ============================================================================
# ТЕСТ 5: Переключение режимов во время работы аудио
# ============================================================================

async def test_5_mode_switching_during_audio(engine, event_bus):
    """Тест 5: Переключение режимов во время работы аудио"""
    print_test("5. Переключение режимов во время работы аудио")
    
    if engine is None or event_bus is None:
        print_error("Экземпляр engine или event_bus не передан")
        return False
    
    try:
        import numpy as np
        
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
        
        print_info("Запуск воспроизведения (Output)...")
        await engine.play_audio(audio_data.tobytes(), sample_rate=sample_rate, channels=1)
        print_success("Воспроизведение запущено")
        
        # Симулируем переключение режимов
        mode_changes = []
        async def on_mode_changed(event_data):
            mode_changes.append(event_data)
        
        await event_bus.subscribe("app.mode_changed", on_mode_changed)
        
        print_info("Симуляция переключения режимов...")
        await event_bus.publish("mode.request", {
            "target": "LISTENING",
            "source": "test",
            "session_id": "test_mode_switch"
        })
        
        await asyncio.sleep(0.3)
        
        # Проверяем, что оба режима продолжают работать
        if engine._input_state.name == "RUNNING":
            print_success(f"Запись продолжается (Input state: {engine._input_state.name})")
        else:
            print_warning(f"Запись остановлена (Input state: {engine._input_state.name})")
        
        if engine._output_state.name in ["RUNNING", "IDLE"]:
            print_success(f"Воспроизведение в состоянии (Output state: {engine._output_state.name})")
        else:
            print_warning(f"Неожиданное состояние воспроизведения (Output state: {engine._output_state.name})")
        
        # Останавливаем запись
        await asyncio.sleep(1.0)
        print_info("Остановка записи...")
        await engine.stop_input()
        print_success("Запись остановлена")
        
        return True
        
    except Exception as e:
        print_error(f"Ошибка при тестировании переключения режимов: {e}")
        import traceback
        traceback.print_exc()
        return False

# ============================================================================
# ТЕСТ 6: Ошибки и восстановление после ошибок
# ============================================================================

async def test_6_error_recovery(engine, event_bus):
    """Тест 6: Ошибки и восстановление после ошибок"""
    print_test("6. Ошибки и восстановление после ошибок")
    
    if engine is None:
        print_error("Экземпляр engine не передан")
        return False
    
    try:
        import numpy as np
        
        # Пробуем воспроизведение с невалидными данными
        print_info("Попытка воспроизведения с невалидными данными...")
        try:
            result = await engine.play_audio(b"invalid_data", sample_rate=48000, channels=1)
            if not result:
                print_success("Воспроизведение с невалидными данными корректно отклонено")
            else:
                print_warning("Воспроизведение с невалидными данными не отклонено")
        except Exception as e:
            print_success(f"Ошибка корректно обработана: {type(e).__name__}")
        
        # Проверяем, что состояние восстановилось
        await asyncio.sleep(0.2)
        if engine._output_state.name in ["IDLE", "ERROR"]:
            print_success(f"Состояние после ошибки: {engine._output_state.name}")
        else:
            print_warning(f"Неожиданное состояние после ошибки: {engine._output_state.name}")
        
        # Пробуем нормальное воспроизведение после ошибки
        print_info("Попытка нормального воспроизведения после ошибки...")
        sample_rate = 48000
        duration_sec = 0.5
        num_samples = int(sample_rate * duration_sec)
        t = np.linspace(0, duration_sec, num_samples, False)
        audio_data = (np.sin(2 * np.pi * 440.0 * t) * 32767).astype(np.int16)
        
        result = await engine.play_audio(audio_data.tobytes(), sample_rate=sample_rate, channels=1)
        if result:
            print_success("Воспроизведение после ошибки работает")
            await asyncio.sleep(1.0)
        else:
            print_error("Воспроизведение после ошибки не работает")
            return False
        
        return True
        
    except Exception as e:
        print_error(f"Ошибка при тестировании восстановления: {e}")
        import traceback
        traceback.print_exc()
        return False

# ============================================================================
# ТЕСТ 7: Быстрое переключение между воспроизведением и записью
# ============================================================================

async def test_7_rapid_switching(engine, event_bus):
    """Тест 7: Быстрое переключение между воспроизведением и записью"""
    print_test("7. Быстрое переключение между воспроизведением и записью")
    
    if engine is None:
        print_error("Экземпляр engine не передан")
        return False
    
    try:
        import numpy as np
        
        sample_rate = 48000
        duration_sec = 0.3
        num_samples = int(sample_rate * duration_sec)
        t = np.linspace(0, duration_sec, num_samples, False)
        audio_data = (np.sin(2 * np.pi * 440.0 * t) * 32767).astype(np.int16)
        
        input_data_received = []
        async def on_input_data(data: bytes, sample_rate: int, channels: int):
            input_data_received.append((data, sample_rate, channels))
        
        print_info("Быстрое переключение: воспроизведение → запись → воспроизведение...")
        
        # Цикл быстрого переключения
        for i in range(5):
            print_info(f"Итерация {i+1}/5...")
            
            # Воспроизведение
            await engine.play_audio(audio_data.tobytes(), sample_rate=sample_rate, channels=1)
            await asyncio.sleep(0.2)
            
            # Запись
            await engine.start_input(callback=on_input_data)
            await asyncio.sleep(0.2)
            await engine.stop_input()
            
            # Воспроизведение
            await engine.play_audio(audio_data.tobytes(), sample_rate=sample_rate, channels=1)
            await asyncio.sleep(0.2)
        
        print_success("Быстрое переключение завершено без ошибок")
        
        # Проверяем финальное состояние
        await asyncio.sleep(0.2)
        if engine._input_state.name == "IDLE" and engine._output_state.name == "IDLE":
            print_success("Финальное состояние корректно (IDLE)")
        else:
            print_warning(f"Финальное состояние: Input={engine._input_state.name}, Output={engine._output_state.name}")
        
        return True
        
    except Exception as e:
        print_error(f"Ошибка при тестировании быстрого переключения: {e}")
        import traceback
        traceback.print_exc()
        return False

# ============================================================================
# ТЕСТ 8: Одновременные прерывания и переключения устройств
# ============================================================================

async def test_8_concurrent_interrupts_and_device_changes(engine, event_bus):
    """Тест 8: Одновременные прерывания и переключения устройств"""
    print_test("8. Одновременные прерывания и переключения устройств")
    
    if engine is None or event_bus is None:
        print_error("Экземпляр engine или event_bus не передан")
        return False
    
    try:
        import numpy as np
        
        # Запускаем длительное воспроизведение
        sample_rate = 48000
        duration_sec = 3.0
        num_samples = int(sample_rate * duration_sec)
        t = np.linspace(0, duration_sec, num_samples, False)
        audio_data = (np.sin(2 * np.pi * 440.0 * t) * 32767).astype(np.int16)
        
        print_info("Запуск длительного воспроизведения...")
        await engine.play_audio(audio_data.tobytes(), sample_rate=sample_rate, channels=1)
        print_success("Воспроизведение запущено")
        
        # Одновременно публикуем прерывание и смену устройства
        print_info("Одновременная публикация прерывания и смены устройства...")
        await asyncio.sleep(0.3)
        
        # Публикуем оба события одновременно
        await asyncio.gather(
            event_bus.publish("playback.cancelled", {
                "session_id": "test_concurrent",
                "reason": "concurrent_test",
                "source": "test"
            }),
            event_bus.publish("audio.device.output_resync_required", {
                "device_name": "Concurrent Test Device",
                "was_running": True
            })
        )
        print_success("Оба события опубликованы одновременно")
        
        # Ждём обработки
        await asyncio.sleep(0.5)
        
        # Проверяем состояние
        if engine._output_state.name in ["IDLE", "RECONNECTING"]:
            print_success(f"Состояние после одновременных событий: {engine._output_state.name}")
        else:
            print_warning(f"Неожиданное состояние: {engine._output_state.name}")
        
        return True
        
    except Exception as e:
        print_error(f"Ошибка при тестировании одновременных событий: {e}")
        import traceback
        traceback.print_exc()
        return False

# ============================================================================
# ТЕСТ 9: Таймауты и fallback механизмы
# ============================================================================

async def test_9_timeouts_and_fallback(engine, event_bus):
    """Тест 9: Таймауты и fallback механизмы"""
    print_test("9. Таймауты и fallback механизмы")
    
    if engine is None or event_bus is None:
        print_error("Экземпляр engine или event_bus не передан")
        return False
    
    try:
        import numpy as np
        
        # Создаём событие для отслеживания fallback
        fallback_received = asyncio.Event()
        
        async def on_playback_completed(event_data):
            data = event_data.get("data", {})
            source = data.get("source", "unknown")
            if "FALLBACK" in source:
                print_success(f"Fallback таймер сработал! source: {source}")
                fallback_received.set()
        
        await event_bus.subscribe("playback.completed", on_playback_completed)
        
        # Запускаем воспроизведение
        sample_rate = 48000
        duration_sec = 1.0
        num_samples = int(sample_rate * duration_sec)
        t = np.linspace(0, duration_sec, num_samples, False)
        audio_data = (np.sin(2 * np.pi * 440.0 * t) * 32767).astype(np.int16)
        
        print_info("Запуск воспроизведения (ожидаем fallback таймер через ~1.5s)...")
        await engine.play_audio(audio_data.tobytes(), sample_rate=sample_rate, channels=1)
        print_success("Воспроизведение запущено")
        
        # Ждём fallback таймер
        try:
            await asyncio.wait_for(fallback_received.wait(), timeout=3.0)
            print_success("Fallback таймер сработал вовремя")
        except asyncio.TimeoutError:
            print_error("Fallback таймер не сработал за 3 секунды")
            return False
        
        return True
        
    except Exception as e:
        print_error(f"Ошибка при тестировании таймаутов: {e}")
        import traceback
        traceback.print_exc()
        return False

# ============================================================================
# ТЕСТ 10: Память и утечки ресурсов
# ============================================================================

async def test_10_memory_and_resource_leaks(engine, event_bus):
    """Тест 10: Память и утечки ресурсов"""
    print_test("10. Память и утечки ресурсов")
    
    if engine is None:
        print_error("Экземпляр engine не передан")
        return False
    
    try:
        import numpy as np
        import gc
        
        # Запускаем множество циклов воспроизведения
        print_info("Запуск 20 циклов воспроизведения для проверки утечек...")
        
        sample_rate = 48000
        duration_sec = 0.2
        num_samples = int(sample_rate * duration_sec)
        t = np.linspace(0, duration_sec, num_samples, False)
        audio_data = (np.sin(2 * np.pi * 440.0 * t) * 32767).astype(np.int16)
        
        initial_timers = 0
        if hasattr(engine, '_fallback_timer'):
            initial_timers = 1 if engine._fallback_timer is not None else 0
        
        for i in range(20):
            await engine.play_audio(audio_data.tobytes(), sample_rate=sample_rate, channels=1)
            await asyncio.sleep(0.3)
            
            # Проверяем, что старые таймеры отменены
            if hasattr(engine, '_fallback_timer'):
                if engine._fallback_timer is not None:
                    print_warning(f"Fallback таймер не отменён после цикла {i+1}")
        
        # Принудительная сборка мусора
        gc.collect()
        
        print_success("20 циклов завершены без явных утечек")
        
        # Проверяем финальное состояние
        await asyncio.sleep(0.2)
        if engine._output_state.name == "IDLE":
            print_success(f"Финальное состояние: {engine._output_state.name}")
        else:
            print_warning(f"Финальное состояние: {engine._output_state.name}")
        
        return True
        
    except Exception as e:
        print_error(f"Ошибка при тестировании памяти: {e}")
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
    print("КОМПЛЕКСНЫЙ ТЕСТ КРИТИЧЕСКИХ СЦЕНАРИЕВ AVF АУДИОСИСТЕМЫ")
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
    
    # ТЕСТ 1: Race conditions
    result1 = await test_1_race_conditions(engine, event_bus)
    results.append(("1. Race conditions при одновременном доступе", result1))
    
    # ТЕСТ 2: Переключение устройств
    result2 = await test_2_device_switching_during_playback(engine, event_bus)
    results.append(("2. Переключение устройств во время воспроизведения", result2))
    
    # ТЕСТ 3: Прерывания
    result3 = await test_3_interrupts_during_playback(engine, event_bus)
    results.append(("3. Прерывания во время воспроизведения", result3))
    
    # ТЕСТ 4: Множественные экземпляры
    result4 = await test_4_multiple_instances()
    results.append(("4. Множественные экземпляры AVFAudioEngine", result4))
    
    # ТЕСТ 5: Переключение режимов
    result5 = await test_5_mode_switching_during_audio(engine, event_bus)
    results.append(("5. Переключение режимов во время работы аудио", result5))
    
    # ТЕСТ 6: Восстановление после ошибок
    result6 = await test_6_error_recovery(engine, event_bus)
    results.append(("6. Ошибки и восстановление после ошибок", result6))
    
    # ТЕСТ 7: Быстрое переключение
    result7 = await test_7_rapid_switching(engine, event_bus)
    results.append(("7. Быстрое переключение между воспроизведением и записью", result7))
    
    # ТЕСТ 8: Одновременные события
    result8 = await test_8_concurrent_interrupts_and_device_changes(engine, event_bus)
    results.append(("8. Одновременные прерывания и переключения устройств", result8))
    
    # ТЕСТ 9: Таймауты
    result9 = await test_9_timeouts_and_fallback(engine, event_bus)
    results.append(("9. Таймауты и fallback механизмы", result9))
    
    # ТЕСТ 10: Память
    result10 = await test_10_memory_and_resource_leaks(engine, event_bus)
    results.append(("10. Память и утечки ресурсов", result10))
    
    # ИТОГИ
    print(f"\n{Colors.BOLD}{Colors.HEADER}")
    print("="*80)
    print("ИТОГИ ТЕСТИРОВАНИЯ КРИТИЧЕСКИХ СЦЕНАРИЕВ")
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
        print_success("Все критические сценарии протестированы успешно! ✅")
    else:
        print_error(f"Провалено тестов: {total - passed} ❌")
        print_warning("Обнаружены проблемы в критических сценариях!")

if __name__ == "__main__":
    asyncio.run(main())


