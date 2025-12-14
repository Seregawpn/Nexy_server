"""
Простой тест для проверки состояния AVF БЕЗ вызова initialize()
Цель: проверить факты из анализа логов
"""
import pytest
import sys
from pathlib import Path

# Добавляем путь к проекту
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from integration.core.event_bus import EventBus
from integration.core.state_manager import ApplicationStateManager
from integration.core.error_handler import ErrorHandler
from integration.integrations.voice_recognition_integration import VoiceRecognitionIntegration


class TestAVFStateSimple:
    """Простой тест для проверки состояния AVF"""
    
    def test_fact_1_initial_state(self):
        """Тест Факт 1: Проверка начального состояния после __init__()"""
        print(f"\n{'='*80}")
        print(f"🔍 ТЕСТ 1: Проверка начального состояния после __init__()")
        print(f"{'='*80}")
        
        event_bus = EventBus()
        state_manager = ApplicationStateManager()
        error_handler = ErrorHandler(event_bus)
        
        integration = VoiceRecognitionIntegration(
            event_bus=event_bus,
            state_manager=state_manager,
            error_handler=error_handler
        )
        
        # Проверяем состояние
        use_avf = getattr(integration, '_use_avf', None)
        avf_engine = getattr(integration, '_avf_engine', None)
        initialized = getattr(integration, '_initialized', False)
        
        print(f"\n📊 Состояние после __init__() (БЕЗ initialize()):")
        print(f"   - _use_avf: {use_avf}")
        print(f"   - _avf_engine: {avf_engine is not None if avf_engine else False}")
        print(f"   - _initialized: {initialized}")
        
        # Выводы
        print(f"\n📊 ВЫВОДЫ:")
        if use_avf is False:
            print(f"   ✅ ОЖИДАЕМО: _use_avf=False после __init__() (инициализация в initialize())")
        elif use_avf is None:
            print(f"   ⚠️ НЕОЖИДАННО: _use_avf=None после __init__()")
        else:
            print(f"   ⚠️ НЕОЖИДАННО: _use_avf={use_avf} после __init__() (ожидалось False)")
        
        if avf_engine is None:
            print(f"   ✅ ОЖИДАЕМО: _avf_engine=None после __init__() (создается в initialize())")
        else:
            print(f"   ⚠️ НЕОЖИДАННО: _avf_engine создан после __init__()")
        
        if not initialized:
            print(f"   ✅ ОЖИДАЕМО: _initialized=False после __init__() (устанавливается в initialize())")
        else:
            print(f"   ⚠️ НЕОЖИДАННО: _initialized=True после __init__()")
        
        assert True  # Тест для диагностики
    
    def test_fact_2_condition_check(self):
        """Тест Факт 2: Проверка условия для новой логики"""
        print(f"\n{'='*80}")
        print(f"🔍 ТЕСТ 2: Проверка условия для новой логики")
        print(f"{'='*80}")
        
        event_bus = EventBus()
        state_manager = ApplicationStateManager()
        error_handler = ErrorHandler(event_bus)
        
        integration = VoiceRecognitionIntegration(
            event_bus=event_bus,
            state_manager=state_manager,
            error_handler=error_handler
        )
        
        # Проверяем состояние
        use_avf = getattr(integration, '_use_avf', None)
        avf_engine = getattr(integration, '_avf_engine', None)
        
        # Условие из строки 832
        condition_result = use_avf and avf_engine is not None
        
        print(f"\n📊 Условие для новой логики (строка 832):")
        print(f"   if self._use_avf and self._avf_engine is not None:")
        print(f"   - _use_avf: {use_avf}")
        print(f"   - _avf_engine is not None: {avf_engine is not None}")
        print(f"   - Результат условия: {condition_result}")
        
        print(f"\n📊 ВЫВОДЫ:")
        if not condition_result:
            print(f"   ✅ ОЖИДАЕМО: Условие НЕ выполнено после __init__()")
            print(f"      - Новая логика AVF→Google НЕ будет использоваться")
            print(f"      - Система будет использовать LEGACY путь")
            if not use_avf:
                print(f"      - Причина: _use_avf={use_avf}")
            if avf_engine is None:
                print(f"      - Причина: _avf_engine=None")
        else:
            print(f"   ⚠️ НЕОЖИДАННО: Условие выполнено после __init__()")
            print(f"      - Это означает, что AVF инициализирован в __init__()")
        
        assert True  # Тест для диагностики
    
    def test_fact_3_code_location(self):
        """Тест Факт 3: Проверка расположения кода инициализации AVF"""
        print(f"\n{'='*80}")
        print(f"🔍 ТЕСТ 3: Проверка расположения кода инициализации AVF")
        print(f"{'='*80}")
        
        import inspect
        from integration.integrations.voice_recognition_integration import VoiceRecognitionIntegration
        
        # Получаем исходный код метода initialize
        initialize_method = VoiceRecognitionIntegration.initialize
        source_lines = inspect.getsourcelines(initialize_method)
        
        print(f"\n📊 Информация о методе initialize():")
        print(f"   - Файл: {inspect.getfile(initialize_method)}")
        print(f"   - Строка начала: {source_lines[1]}")
        print(f"   - Количество строк: {len(source_lines[0])}")
        
        # Ищем код инициализации AVF
        source_code = ''.join(source_lines[0])
        
        has_avf_init = "🔍 [AVF] Начало инициализации AVF" in source_code
        has_avf_engine_create = "self._avf_engine = AVFAudioEngine" in source_code
        has_avf_success_log = "✅ [AVF] AVFAudioEngine инициализирован" in source_code
        
        print(f"\n📊 Проверка наличия кода инициализации AVF:")
        print(f"   - Код 'Начало инициализации AVF': {has_avf_init}")
        print(f"   - Код 'self._avf_engine = AVFAudioEngine': {has_avf_engine_create}")
        print(f"   - Код 'AVFAudioEngine инициализирован': {has_avf_success_log}")
        
        print(f"\n📊 ВЫВОДЫ:")
        if has_avf_init and has_avf_engine_create:
            print(f"   ✅ Код инициализации AVF находится в методе initialize()")
            print(f"      - Это означает, что для создания _avf_engine нужно вызвать initialize()")
        else:
            print(f"   ❌ Код инициализации AVF НЕ найден в методе initialize()")
            print(f"      - Это означает, что инициализация происходит в другом месте")
        
        assert True  # Тест для диагностики

