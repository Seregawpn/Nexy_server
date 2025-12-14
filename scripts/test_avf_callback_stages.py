#!/usr/bin/env python3
"""
Пошаговый тест этапов создания Completion Callback в AVFAudioEngine

Проверяет каждый этап отдельно для выявления точного места ошибки или дублирования.
"""

import sys
import os
import logging
import asyncio
from pathlib import Path

# Добавляем путь к клиенту
client_path = Path(__file__).parent.parent
sys.path.insert(0, str(client_path))

# Настройка логирования
logging.basicConfig(
    level=logging.DEBUG,
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

def print_stage(stage_num: int, stage_name: str):
    """Вывести заголовок этапа"""
    print(f"\n{Colors.HEADER}{Colors.BOLD}{'='*80}{Colors.ENDC}")
    print(f"{Colors.HEADER}{Colors.BOLD}ЭТАП {stage_num}: {stage_name}{Colors.ENDC}")
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
# ЭТАП 1: Импорт AVAudioPlayerNode
# ============================================================================

def test_stage_1_import():
    """Тест этапа 1: Импорт AVAudioPlayerNode"""
    print_stage(1, "Импорт AVAudioPlayerNode из AVFoundation")
    
    try:
        print_info("Попытка импорта AVAudioPlayerNode...")
        from AVFoundation import AVAudioPlayerNode
        
        print_success("AVAudioPlayerNode успешно импортирован")
        print_info(f"Тип: {type(AVAudioPlayerNode)}")
        print_info(f"Модуль: {AVAudioPlayerNode.__module__}")
        
        # Проверяем наличие метода
        if hasattr(AVAudioPlayerNode, 'scheduleBuffer_atTime_options_completionHandler_'):
            print_success("Метод scheduleBuffer_atTime_options_completionHandler_ доступен")
        else:
            print_error("Метод scheduleBuffer_atTime_options_completionHandler_ НЕ доступен")
            return False
        
        # Проверяем, что это класс
        import inspect
        if inspect.isclass(AVAudioPlayerNode):
            print_success("AVAudioPlayerNode является классом")
        else:
            print_warning("AVAudioPlayerNode не является классом")
        
        return True
        
    except ImportError as e:
        print_error(f"ImportError при импорте AVAudioPlayerNode: {e}")
        print_error("Установите PyObjC: pip install pyobjc-framework-AVFoundation")
        return False
    except Exception as e:
        print_error(f"Неожиданная ошибка при импорте: {e}")
        import traceback
        traceback.print_exc()
        return False

# ============================================================================
# ЭТАП 2: Проверка глобальных переменных модуля
# ============================================================================

def test_stage_2_globals():
    """Тест этапа 2: Проверка глобальных переменных модуля"""
    print_stage(2, "Проверка глобальных переменных модуля avf_audio_engine")
    
    try:
        print_info("Импорт модуля avf_audio_engine...")
        from modules.audio_avf.core import avf_audio_engine
        
        # Проверяем глобальные переменные
        print_info("Проверка AVF_PLAYER_NODE_AVAILABLE...")
        if hasattr(avf_audio_engine, 'AVF_PLAYER_NODE_AVAILABLE'):
            avf_available = avf_audio_engine.AVF_PLAYER_NODE_AVAILABLE
            if avf_available:
                print_success(f"AVF_PLAYER_NODE_AVAILABLE = {avf_available}")
            else:
                print_error(f"AVF_PLAYER_NODE_AVAILABLE = {avf_available} (должно быть True)")
                return False
        else:
            print_error("AVF_PLAYER_NODE_AVAILABLE не найден в модуле")
            return False
        
        print_info("Проверка AVAudioPlayerNode...")
        if hasattr(avf_audio_engine, 'AVAudioPlayerNode'):
            avf_player_node = avf_audio_engine.AVAudioPlayerNode
            if avf_player_node is not None:
                print_success(f"AVAudioPlayerNode = {avf_player_node}")
                print_info(f"Тип: {type(avf_player_node)}")
            else:
                print_error("AVAudioPlayerNode = None (должно быть не None)")
                return False
        else:
            print_error("AVAudioPlayerNode не найден в модуле")
            return False
        
        print_info("Проверка _AVF_COMPLETION_CALLBACK...")
        if hasattr(avf_audio_engine, '_AVF_COMPLETION_CALLBACK'):
            callback = avf_audio_engine._AVF_COMPLETION_CALLBACK
            if callback is None:
                print_info("_AVF_COMPLETION_CALLBACK = None (ещё не создан, это нормально)")
            else:
                print_success(f"_AVF_COMPLETION_CALLBACK создан: {type(callback)}")
        else:
            print_error("_AVF_COMPLETION_CALLBACK не найден в модуле")
            return False
        
        return True
        
    except Exception as e:
        print_error(f"Ошибка при проверке глобальных переменных: {e}")
        import traceback
        traceback.print_exc()
        return False

# ============================================================================
# ЭТАП 3: Создание экземпляра AVFAudioEngine
# ============================================================================

def test_stage_3_create_engine():
    """Тест этапа 3: Создание экземпляра AVFAudioEngine"""
    print_stage(3, "Создание экземпляра AVFAudioEngine")
    
    try:
        print_info("Импорт AVFAudioEngine...")
        from modules.audio_avf.core.avf_audio_engine import AVFAudioEngine
        from config.unified_config_loader import UnifiedConfigLoader
        
        print_info("Загрузка конфигурации...")
        loader = UnifiedConfigLoader()
        audio_config = loader.get_audio_config_object()
        print_success("Конфигурация загружена")
        
        print_info("Создание экземпляра AVFAudioEngine...")
        # Создаём без event_bus для простоты теста
        engine = AVFAudioEngine(audio_config, event_bus=None)
        print_success("Экземпляр AVFAudioEngine создан")
        
        # Проверяем атрибуты
        print_info("Проверка атрибутов экземпляра...")
        
        if hasattr(engine, '_player_node'):
            if engine._player_node is not None:
                print_success(f"_player_node создан: {type(engine._player_node)}")
            else:
                print_error("_player_node = None (должно быть не None)")
                return False, None
        else:
            print_error("_player_node не найден в экземпляре")
            return False, None
        
        if hasattr(engine, '_output_completion_callback'):
            callback = engine._output_completion_callback
            if callback is not None:
                print_success(f"_output_completion_callback создан: {type(callback)}")
            else:
                print_warning("_output_completion_callback = None (может быть проблемой)")
        else:
            print_error("_output_completion_callback не найден в экземпляре")
            return False, None
        
        return True, engine
        
    except Exception as e:
        print_error(f"Ошибка при создании экземпляра: {e}")
        import traceback
        traceback.print_exc()
        return False, None

# ============================================================================
# ЭТАП 4: Проверка привязки player_node → engine
# ============================================================================

def test_stage_4_binding(engine):
    """Тест этапа 4: Проверка привязки player_node → engine"""
    print_stage(4, "Проверка привязки player_node → engine")
    
    if engine is None:
        print_error("Экземпляр engine не передан")
        return False
    
    try:
        from modules.audio_avf.core.avf_audio_engine import (
            _PLAYER_NODE_TO_ENGINE,
            _PLAYER_NODE_ID_MAP,
            _lookup_engine_by_player_node
        )
        
        print_info("Проверка привязки через _PLAYER_NODE_TO_ENGINE...")
        player_node = engine._player_node
        
        if player_node in _PLAYER_NODE_TO_ENGINE:
            bound_engine = _PLAYER_NODE_TO_ENGINE[player_node]
            if bound_engine is engine:
                print_success("Привязка найдена в _PLAYER_NODE_TO_ENGINE")
            else:
                print_warning(f"Привязка найдена, но указывает на другой экземпляр: {bound_engine is engine}")
        else:
            print_warning("Привязка НЕ найдена в _PLAYER_NODE_TO_ENGINE")
            print_info("Проверка через _PLAYER_NODE_ID_MAP...")
            player_id = id(player_node)
            if player_id in _PLAYER_NODE_ID_MAP:
                engine_ref = _PLAYER_NODE_ID_MAP[player_id]
                bound_engine = engine_ref()
                if bound_engine is engine:
                    print_success("Привязка найдена в _PLAYER_NODE_ID_MAP")
                else:
                    print_warning(f"Привязка найдена, но указывает на другой экземпляр")
            else:
                print_error("Привязка НЕ найдена ни в _PLAYER_NODE_TO_ENGINE, ни в _PLAYER_NODE_ID_MAP")
                return False
        
        print_info("Проверка через _lookup_engine_by_player_node...")
        found_engine = _lookup_engine_by_player_node(player_node)
        if found_engine is engine:
            print_success("_lookup_engine_by_player_node вернул правильный экземпляр")
        elif found_engine is None:
            print_error("_lookup_engine_by_player_node вернул None")
            return False
        else:
            print_warning(f"_lookup_engine_by_player_node вернул другой экземпляр: {found_engine is engine}")
            return False
        
        return True
        
    except Exception as e:
        print_error(f"Ошибка при проверке привязки: {e}")
        import traceback
        traceback.print_exc()
        return False

# ============================================================================
# ЭТАП 5: Проверка создания completion callback
# ============================================================================

def test_stage_5_callback_creation(engine):
    """Тест этапа 5: Проверка создания completion callback"""
    print_stage(5, "Проверка создания completion callback")
    
    if engine is None:
        print_error("Экземпляр engine не передан")
        return False
    
    try:
        from modules.audio_avf.core.avf_audio_engine import (
            _AVF_COMPLETION_CALLBACK,
            _create_avf_completion_callback
        )
        
        print_info("Проверка глобального _AVF_COMPLETION_CALLBACK...")
        if _AVF_COMPLETION_CALLBACK is not None:
            print_success(f"_AVF_COMPLETION_CALLBACK создан: {type(_AVF_COMPLETION_CALLBACK)}")
        else:
            print_warning("_AVF_COMPLETION_CALLBACK = None (будет создан при вызове)")
        
        print_info("Проверка engine._output_completion_callback...")
        if engine._output_completion_callback is not None:
            print_success(f"engine._output_completion_callback создан: {type(engine._output_completion_callback)}")
            
            # Проверяем, что это тот же объект, что и глобальный
            if engine._output_completion_callback is _AVF_COMPLETION_CALLBACK:
                print_success("engine._output_completion_callback совпадает с глобальным _AVF_COMPLETION_CALLBACK")
            else:
                print_warning("engine._output_completion_callback НЕ совпадает с глобальным _AVF_COMPLETION_CALLBACK")
        else:
            print_error("engine._output_completion_callback = None (должно быть не None)")
            return False
        
        # Проверяем, что callback можно вызвать (симуляция)
        print_info("Проверка типа callback...")
        callback = engine._output_completion_callback
        print_info(f"Тип callback: {type(callback)}")
        print_info(f"Callable: {callable(callback)}")
        
        return True
        
    except Exception as e:
        print_error(f"Ошибка при проверке callback: {e}")
        import traceback
        traceback.print_exc()
        return False

# ============================================================================
# ЭТАП 6: Проверка множественных экземпляров
# ============================================================================

def test_stage_6_multiple_instances():
    """Тест этапа 6: Проверка множественных экземпляров"""
    print_stage(6, "Проверка множественных экземпляров (дублирование)")
    
    try:
        from modules.audio_avf.core.avf_audio_engine import (
            AVFAudioEngine,
            _AVF_ENGINE_INSTANCES,
            _AVF_COMPLETION_CALLBACK
        )
        from config.unified_config_loader import UnifiedConfigLoader
        
        print_info("Создание первого экземпляра...")
        loader = UnifiedConfigLoader()
        audio_config = loader.get_audio_config_object()
        
        engine1 = AVFAudioEngine(audio_config, event_bus=None)
        print_success("Первый экземпляр создан")
        print_info(f"ID engine1: {id(engine1)}")
        print_info(f"ID engine1._player_node: {id(engine1._player_node) if engine1._player_node else None}")
        print_info(f"engine1._output_completion_callback: {engine1._output_completion_callback is not None}")
        
        callback1 = _AVF_COMPLETION_CALLBACK
        print_info(f"Глобальный _AVF_COMPLETION_CALLBACK после engine1: {callback1 is not None}")
        
        print_info("\nСоздание второго экземпляра...")
        engine2 = AVFAudioEngine(audio_config, event_bus=None)
        print_success("Второй экземпляр создан")
        print_info(f"ID engine2: {id(engine2)}")
        print_info(f"ID engine2._player_node: {id(engine2._player_node) if engine2._player_node else None}")
        print_info(f"engine2._output_completion_callback: {engine2._output_completion_callback is not None}")
        
        callback2 = _AVF_COMPLETION_CALLBACK
        print_info(f"Глобальный _AVF_COMPLETION_CALLBACK после engine2: {callback2 is not None}")
        
        # Проверяем, что callback один и тот же
        if callback1 is callback2:
            print_success("Глобальный callback одинаковый для обоих экземпляров (правильно)")
        else:
            print_error("Глобальный callback разный для разных экземпляров (проблема!)")
            return False
        
        if engine1._output_completion_callback is engine2._output_completion_callback:
            print_success("engine._output_completion_callback одинаковый для обоих экземпляров (правильно)")
        else:
            print_error("engine._output_completion_callback разный для разных экземпляров (проблема!)")
            return False
        
        # Проверяем _AVF_ENGINE_INSTANCES
        print_info(f"\nКоличество экземпляров в _AVF_ENGINE_INSTANCES: {len(_AVF_ENGINE_INSTANCES)}")
        if len(_AVF_ENGINE_INSTANCES) >= 2:
            print_success("Оба экземпляра зарегистрированы в _AVF_ENGINE_INSTANCES")
        else:
            print_warning(f"В _AVF_ENGINE_INSTANCES только {len(_AVF_ENGINE_INSTANCES)} экземпляр(ов)")
        
        return True
        
    except Exception as e:
        print_error(f"Ошибка при проверке множественных экземпляров: {e}")
        import traceback
        traceback.print_exc()
        return False

# ============================================================================
# ГЛАВНАЯ ФУНКЦИЯ
# ============================================================================

def main():
    """Главная функция для запуска всех тестов"""
    print(f"\n{Colors.BOLD}{Colors.HEADER}")
    print("="*80)
    print("ПОШАГОВЫЙ ТЕСТ ЭТАПОВ СОЗДАНИЯ COMPLETION CALLBACK")
    print("="*80)
    print(f"{Colors.ENDC}\n")
    
    results = []
    
    # ЭТАП 1: Импорт
    result1 = test_stage_1_import()
    results.append(("Этап 1: Импорт AVAudioPlayerNode", result1))
    if not result1:
        print_error("\n❌ ЭТАП 1 ПРОВАЛЕН. Остановка тестирования.")
        return
    
    # ЭТАП 2: Глобальные переменные
    result2 = test_stage_2_globals()
    results.append(("Этап 2: Глобальные переменные", result2))
    if not result2:
        print_error("\n❌ ЭТАП 2 ПРОВАЛЕН. Остановка тестирования.")
        return
    
    # ЭТАП 3: Создание экземпляра
    result3, engine = test_stage_3_create_engine()
    results.append(("Этап 3: Создание экземпляра", result3))
    if not result3:
        print_error("\n❌ ЭТАП 3 ПРОВАЛЕН. Остановка тестирования.")
        return
    
    # ЭТАП 4: Привязка
    result4 = test_stage_4_binding(engine)
    results.append(("Этап 4: Привязка player_node → engine", result4))
    
    # ЭТАП 5: Callback
    result5 = test_stage_5_callback_creation(engine)
    results.append(("Этап 5: Создание completion callback", result5))
    
    # ЭТАП 6: Множественные экземпляры
    result6 = test_stage_6_multiple_instances()
    results.append(("Этап 6: Множественные экземпляры", result6))
    
    # ИТОГИ
    print(f"\n{Colors.BOLD}{Colors.HEADER}")
    print("="*80)
    print("ИТОГИ ТЕСТИРОВАНИЯ")
    print("="*80)
    print(f"{Colors.ENDC}\n")
    
    for stage_name, result in results:
        if result:
            print(f"{Colors.OKGREEN}✅ {stage_name}: ПРОЙДЕН{Colors.ENDC}")
        else:
            print(f"{Colors.FAIL}❌ {stage_name}: ПРОВАЛЕН{Colors.ENDC}")
    
    passed = sum(1 for _, result in results if result)
    total = len(results)
    
    print(f"\n{Colors.BOLD}Результат: {passed}/{total} этапов пройдено{Colors.ENDC}\n")
    
    if passed == total:
        print_success("Все этапы пройдены успешно! ✅")
    else:
        print_error(f"Провалено этапов: {total - passed} ❌")

if __name__ == "__main__":
    main()


