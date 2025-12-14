#!/usr/bin/env python3
"""
Изолированный тест инициализации и передачи данных в AVF аудиосистеме

Проверяет полный цикл:
1. Инициализация AudioSystemIntegration → создание AVFAudioEngine
2. Передача AVFAudioEngine в SpeechPlaybackIntegration через initialize()
3. Передача данных: playback.raw_audio → SpeechPlaybackIntegration → AVFAudioEngine.play_audio()
4. Получение события: audio.playback.completed → playback.completed

Это изолирует проблему, которая постоянно возникает - инициализация и передача данных.
"""

import sys
import os
import logging
import asyncio
import time
from pathlib import Path
from typing import Optional, Dict, Any

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
# ТЕСТ 1: Инициализация AudioSystemIntegration → создание AVFAudioEngine
# ============================================================================

async def test_1_audio_system_initialization():
    """Тест 1: Инициализация AudioSystemIntegration → создание AVFAudioEngine"""
    print_test("1. Инициализация AudioSystemIntegration → создание AVFAudioEngine")
    
    try:
        from integration.integrations.audio_system_integration import AudioSystemIntegration
        from integration.core.event_bus import EventBus
        from integration.core.state_manager import ApplicationStateManager
        from integration.core.error_handler import ErrorHandler
        
        print_info("Создание EventBus, StateManager, ErrorHandler...")
        event_bus = EventBus()
        state_manager = ApplicationStateManager()
        state_manager.attach_event_bus(event_bus)
        error_handler = ErrorHandler(event_bus)
        
        # Прикрепляем event loop
        try:
            loop = asyncio.get_running_loop()
            event_bus.attach_loop(loop)
        except RuntimeError:
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            event_bus.attach_loop(loop)
        
        print_success("EventBus, StateManager, ErrorHandler созданы")
        
        print_info("Создание AudioSystemIntegration...")
        audio_system = AudioSystemIntegration(
            event_bus=event_bus,
            state_manager=state_manager,
            error_handler=error_handler
        )
        print_success("AudioSystemIntegration создан")
        
        print_info("Инициализация AudioSystemIntegration...")
        init_result = await audio_system.initialize()
        if init_result:
            print_success("AudioSystemIntegration инициализирован")
        else:
            print_error("AudioSystemIntegration не инициализирован")
            return None, None, None
        
        print_info("Запуск AudioSystemIntegration...")
        start_result = await audio_system.start()
        if start_result:
            print_success("AudioSystemIntegration запущен")
        else:
            print_error("AudioSystemIntegration не запущен")
            return None, None, None
        
        print_info("Проверка наличия AVFAudioEngine...")
        avf_engine = audio_system.get_avf_engine()
        if avf_engine is not None:
            print_success(f"AVFAudioEngine получен: {type(avf_engine).__name__}")
            
            # Проверяем критичные атрибуты
            print_info("Проверка критичных атрибутов AVFAudioEngine...")
            
            # 1. Completion callback
            if hasattr(avf_engine, '_output_completion_callback'):
                if avf_engine._output_completion_callback is not None:
                    print_success("Completion callback инициализирован")
                else:
                    print_error("Completion callback НЕ инициализирован (критично!)")
            else:
                print_warning("Атрибут _output_completion_callback не найден")
            
            # 2. Player node
            if hasattr(avf_engine, '_player_node'):
                if avf_engine._player_node is not None:
                    print_success("Player node создан")
                else:
                    print_error("Player node НЕ создан (критично!)")
            else:
                print_warning("Атрибут _player_node не найден")
            
            # 3. Event bus
            if hasattr(avf_engine, '_event_bus'):
                if avf_engine._event_bus is not None:
                    print_success("Event bus прикреплён")
                else:
                    print_warning("Event bus НЕ прикреплён")
            else:
                print_warning("Атрибут _event_bus не найден")
            
            return audio_system, avf_engine, event_bus
        else:
            print_error("AVFAudioEngine НЕ получен (критично!)")
            return None, None, None
        
    except Exception as e:
        print_error(f"Ошибка при инициализации AudioSystemIntegration: {e}")
        import traceback
        traceback.print_exc()
        return None, None, None

# ============================================================================
# ТЕСТ 2: Передача AVFAudioEngine в SpeechPlaybackIntegration
# ============================================================================

async def test_2_speech_playback_initialization(avf_engine, event_bus):
    """Тест 2: Передача AVFAudioEngine в SpeechPlaybackIntegration"""
    print_test("2. Передача AVFAudioEngine в SpeechPlaybackIntegration")
    
    if avf_engine is None or event_bus is None:
        print_error("AVFAudioEngine или EventBus не передан")
        return None
    
    try:
        from integration.integrations.speech_playback_integration import SpeechPlaybackIntegration
        from integration.core.state_manager import ApplicationStateManager
        from integration.core.error_handler import ErrorHandler
        
        print_info("Создание StateManager, ErrorHandler...")
        state_manager = ApplicationStateManager()
        state_manager.attach_event_bus(event_bus)
        error_handler = ErrorHandler(event_bus)
        print_success("StateManager, ErrorHandler созданы")
        
        print_info("Создание SpeechPlaybackIntegration...")
        speech_playback = SpeechPlaybackIntegration(
            event_bus=event_bus,
            state_manager=state_manager,
            error_handler=error_handler
        )
        print_success("SpeechPlaybackIntegration создан")
        
        print_info("Инициализация SpeechPlaybackIntegration с AVFAudioEngine...")
        init_result = await speech_playback.initialize(avf_engine=avf_engine)
        if init_result:
            print_success("SpeechPlaybackIntegration инициализирован")
        else:
            print_error("SpeechPlaybackIntegration не инициализирован")
            return None
        
        print_info("Проверка наличия AVFAudioEngine в SpeechPlaybackIntegration...")
        if hasattr(speech_playback, '_avf_engine'):
            if speech_playback._avf_engine is not None:
                print_success("AVFAudioEngine присутствует в SpeechPlaybackIntegration")
                
                # Проверяем, что это тот же экземпляр
                if speech_playback._avf_engine is avf_engine:
                    print_success("Это тот же экземпляр AVFAudioEngine (правильная передача)")
                else:
                    print_warning("Это другой экземпляр AVFAudioEngine (возможна проблема)")
                
                # Проверяем _use_avf
                if hasattr(speech_playback, '_use_avf'):
                    if speech_playback._use_avf:
                        print_success("_use_avf = True (AVF будет использован)")
                    else:
                        print_error("_use_avf = False (AVF НЕ будет использован!)")
                else:
                    print_warning("Атрибут _use_avf не найден")
            else:
                print_error("AVFAudioEngine НЕ присутствует в SpeechPlaybackIntegration (критично!)")
                return None
        else:
            print_error("Атрибут _avf_engine не найден в SpeechPlaybackIntegration (критично!)")
            return None
        
        print_info("Запуск SpeechPlaybackIntegration...")
        start_result = await speech_playback.start()
        if start_result:
            print_success("SpeechPlaybackIntegration запущен")
        else:
            print_error("SpeechPlaybackIntegration не запущен")
            return None
        
        return speech_playback
        
    except Exception as e:
        print_error(f"Ошибка при инициализации SpeechPlaybackIntegration: {e}")
        import traceback
        traceback.print_exc()
        return None

# ============================================================================
# ТЕСТ 3: Передача данных playback.raw_audio → AVFAudioEngine
# ============================================================================

async def test_3_data_flow(speech_playback, event_bus):
    """Тест 3: Передача данных playback.raw_audio → AVFAudioEngine"""
    print_test("3. Передача данных playback.raw_audio → AVFAudioEngine")
    
    if speech_playback is None or event_bus is None:
        print_error("SpeechPlaybackIntegration или EventBus не передан")
        return False
    
    try:
        import numpy as np
        
        # Создаём тестовые аудио данные
        sample_rate = 48000
        duration_sec = 1.0
        num_samples = int(sample_rate * duration_sec)
        t = np.linspace(0, duration_sec, num_samples, False)
        audio_data = (np.sin(2 * np.pi * 440.0 * t) * 32767).astype(np.int16)
        
        print_info(f"Созданы тестовые аудио данные: {len(audio_data)} samples, {sample_rate}Hz, 1ch")
        print_success("Тестовые аудио данные созданы")
        
        # Создаём события для отслеживания
        raw_audio_received = asyncio.Event()
        playback_started = asyncio.Event()
        playback_completed = asyncio.Event()
        
        async def on_playback_started(event_data):
            print_success("Событие playback.started получено!")
            playback_started.set()
        
        async def on_playback_completed(event_data):
            print_success("Событие playback.completed получено!")
            data = event_data.get("data", {})
            source = data.get("source", "unknown")
            finished = data.get("finished", False)
            print_info(f"  source: {source}, finished: {finished}")
            playback_completed.set()
        
        await event_bus.subscribe("playback.started", on_playback_started)
        await event_bus.subscribe("playback.completed", on_playback_completed)
        
        print_info("Подписки на события созданы")
        
        # ✅ КРИТИЧНО: Проверяем, что SpeechPlaybackIntegration подписан на событие
        print_info("Проверка подписки на playback.raw_audio...")
        if hasattr(event_bus, 'subscribers') and "playback.raw_audio" in event_bus.subscribers:
            subscribers_count = len(event_bus.subscribers["playback.raw_audio"])
            print_success(f"Найдено {subscribers_count} подписчика(ов) на playback.raw_audio")
        else:
            print_error("Нет подписчиков на playback.raw_audio!")
            return False
        
        # Небольшая задержка для завершения подписки
        await asyncio.sleep(0.1)
        
        # Публикуем событие playback.raw_audio
        # ✅ КРИТИЧНО: EventBus оборачивает данные в {'type': 'event', 'data': {...}, 'timestamp': ...}
        # Поэтому передаём данные напрямую, без дополнительной обёртки в "data"
        print_info("Публикация события playback.raw_audio...")
        await event_bus.publish("playback.raw_audio", {
            "audio_data": audio_data,  # numpy array, не bytes!
            "sample_rate": sample_rate,
            "channels": 1,
            "pattern": "test_initialization",
            "priority": 5
        })
        print_success("Событие playback.raw_audio опубликовано")
        
        # Даём время на обработку события
        await asyncio.sleep(0.2)
        
        # Ждём обработки события
        await asyncio.sleep(0.1)
        
        # Проверяем, что событие обработано
        if playback_started.is_set():
            print_success("Событие playback.started получено (данные переданы в AVFAudioEngine)")
        else:
            print_warning("Событие playback.started не получено (возможно, обработка ещё идёт)")
        
        # Ждём завершения воспроизведения (увеличиваем таймаут для fallback таймера)
        # Fallback таймер срабатывает через duration + 0.5 секунды, поэтому ждём дольше
        print_info("Ожидание завершения воспроизведения (до 5 секунд для fallback таймера)...")
        try:
            await asyncio.wait_for(playback_completed.wait(), timeout=5.0)
            print_success("Событие playback.completed получено (воспроизведение завершено)")
            return True
        except asyncio.TimeoutError:
            print_error("Событие playback.completed НЕ получено за 5 секунд (критично!)")
            print_error("Это означает, что completion callback не работает и fallback таймер тоже не сработал")
            return False
        
    except Exception as e:
        print_error(f"Ошибка при тестировании передачи данных: {e}")
        import traceback
        traceback.print_exc()
        return False

# ============================================================================
# ТЕСТ 4: Полный цикл от инициализации до получения события
# ============================================================================

async def test_4_full_cycle():
    """Тест 4: Полный цикл от инициализации до получения события"""
    print_test("4. Полный цикл от инициализации до получения события")
    
    try:
        # Шаг 1: Инициализация AudioSystemIntegration
        print_info("Шаг 1: Инициализация AudioSystemIntegration...")
        audio_system, avf_engine, event_bus = await test_1_audio_system_initialization()
        if audio_system is None or avf_engine is None or event_bus is None:
            print_error("Шаг 1 провален: AudioSystemIntegration не инициализирован")
            return False
        print_success("Шаг 1 завершён: AudioSystemIntegration инициализирован")
        
        # Шаг 2: Передача AVFAudioEngine в SpeechPlaybackIntegration
        print_info("\nШаг 2: Передача AVFAudioEngine в SpeechPlaybackIntegration...")
        speech_playback = await test_2_speech_playback_initialization(avf_engine, event_bus)
        if speech_playback is None:
            print_error("Шаг 2 провален: SpeechPlaybackIntegration не инициализирован")
            return False
        print_success("Шаг 2 завершён: SpeechPlaybackIntegration инициализирован")
        
        # Шаг 3: Передача данных
        print_info("\nШаг 3: Передача данных playback.raw_audio → AVFAudioEngine...")
        data_flow_result = await test_3_data_flow(speech_playback, event_bus)
        if not data_flow_result:
            print_error("Шаг 3 провален: Передача данных не работает")
            return False
        print_success("Шаг 3 завершён: Данные переданы и событие playback.completed получено")
        
        print_success("\n✅ Полный цикл работает корректно!")
        return True
        
    except Exception as e:
        print_error(f"Ошибка при тестировании полного цикла: {e}")
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
    print("ИЗОЛИРОВАННЫЙ ТЕСТ ИНИЦИАЛИЗАЦИИ И ПЕРЕДАЧИ ДАННЫХ")
    print("="*80)
    print(f"{Colors.ENDC}\n")
    
    results = []
    
    # ТЕСТ 1: Инициализация AudioSystemIntegration
    print_info("Запуск теста 1: Инициализация AudioSystemIntegration...")
    audio_system, avf_engine, event_bus = await test_1_audio_system_initialization()
    result1 = audio_system is not None and avf_engine is not None and event_bus is not None
    results.append(("1. Инициализация AudioSystemIntegration", result1))
    
    if not result1:
        print_error("Тест 1 провален, остальные тесты пропущены")
    else:
        # ТЕСТ 2: Передача AVFAudioEngine в SpeechPlaybackIntegration
        print_info("\nЗапуск теста 2: Передача AVFAudioEngine в SpeechPlaybackIntegration...")
        speech_playback = await test_2_speech_playback_initialization(avf_engine, event_bus)
        result2 = speech_playback is not None
        results.append(("2. Передача AVFAudioEngine в SpeechPlaybackIntegration", result2))
        
        if not result2:
            print_error("Тест 2 провален, остальные тесты пропущены")
        else:
            # ТЕСТ 3: Передача данных
            print_info("\nЗапуск теста 3: Передача данных playback.raw_audio → AVFAudioEngine...")
            result3 = await test_3_data_flow(speech_playback, event_bus)
            results.append(("3. Передача данных playback.raw_audio → AVFAudioEngine", result3))
            
            # ТЕСТ 4: Полный цикл
            print_info("\nЗапуск теста 4: Полный цикл от инициализации до получения события...")
            result4 = await test_4_full_cycle()
            results.append(("4. Полный цикл от инициализации до получения события", result4))
    
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
        print_success("Инициализация и передача данных работают корректно!")
    else:
        print_error(f"Провалено тестов: {total - passed} ❌")
        print_error("Проблема с инициализацией или передачей данных обнаружена!")

if __name__ == "__main__":
    asyncio.run(main())


