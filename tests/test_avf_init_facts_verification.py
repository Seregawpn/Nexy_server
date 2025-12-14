"""
Изолированные тесты для проверки фактов из анализа логов
Цель: проверить гипотезы БЕЗ изменений кода
"""
import pytest
import pytest_asyncio
import asyncio
import sys
import logging
from pathlib import Path
from unittest.mock import Mock, patch, MagicMock
from io import StringIO

# Добавляем путь к проекту
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

logging.basicConfig(level=logging.INFO, format='%(levelname)s - %(name)s - %(message)s')

from integration.core.event_bus import EventBus
from integration.core.state_manager import ApplicationStateManager
from integration.core.error_handler import ErrorHandler
from integration.integrations.voice_recognition_integration import VoiceRecognitionIntegration


class TestAVFInitFactsVerification:
    """Тесты для проверки фактов из анализа логов"""
    
    @pytest_asyncio.fixture
    async def setup_integration(self):
        """Настройка интеграции для тестирования"""
        event_bus = EventBus()
        state_manager = ApplicationStateManager()
        error_handler = ErrorHandler(event_bus)
        
        if hasattr(state_manager, 'attach_event_bus'):
            state_manager.attach_event_bus(event_bus)
        elif hasattr(state_manager, 'set_event_bus'):
            state_manager.set_event_bus(event_bus)
        
        integration = VoiceRecognitionIntegration(
            event_bus=event_bus,
            state_manager=state_manager,
            error_handler=error_handler
        )
        
        yield integration
    
    @pytest.mark.asyncio
    async def test_fact_1_initialize_not_called(self, setup_integration):
        """Тест Факт 1: Проверка, вызывается ли initialize()"""
        integration = setup_integration
        
        print(f"\n{'='*80}")
        print(f"🔍 ТЕСТ 1: Проверка вызова initialize()")
        print(f"{'='*80}")
        
        # Проверяем состояние ДО initialize()
        use_avf_before = getattr(integration, '_use_avf', None)
        avf_engine_before = getattr(integration, '_avf_engine', None)
        initialized_before = getattr(integration, '_initialized', False)
        
        print(f"\n📊 Состояние ДО initialize():")
        print(f"   - _use_avf: {use_avf_before}")
        print(f"   - _avf_engine: {avf_engine_before is not None if avf_engine_before else False}")
        print(f"   - _initialized: {initialized_before}")
        
        # Перехватываем логи
        log_capture = StringIO()
        handler = logging.StreamHandler(log_capture)
        handler.setLevel(logging.INFO)
        logger = logging.getLogger('integration.integrations.voice_recognition_integration')
        logger.addHandler(handler)
        
        # Вызываем initialize()
        print(f"\n📋 Вызов initialize()...")
        result = await integration.initialize()
        
        # Получаем логи
        log_output = log_capture.getvalue()
        logger.removeHandler(handler)
        
        # Проверяем состояние ПОСЛЕ initialize()
        use_avf_after = getattr(integration, '_use_avf', None)
        avf_engine_after = getattr(integration, '_avf_engine', None)
        initialized_after = getattr(integration, '_initialized', False)
        
        print(f"\n📊 Состояние ПОСЛЕ initialize():")
        print(f"   - _use_avf: {use_avf_after}")
        print(f"   - _avf_engine: {avf_engine_after is not None if avf_engine_after else False}")
        print(f"   - _initialized: {initialized_after}")
        print(f"   - initialize() вернул: {result}")
        
        # Проверяем логи
        print(f"\n📋 Проверка логов:")
        has_init_log = "VoiceRecognitionIntegration.initialize() ВЫЗВАН" in log_output
        has_avf_start_log = "🔍 [AVF] Начало инициализации AVF..." in log_output
        has_avf_success_log = "✅ [AVF] AVFAudioEngine инициализирован" in log_output
        has_avf_error_log = "❌ [AVF] Ошибка создания AVFAudioEngine" in log_output
        has_avf_disabled_log = "ℹ️ [AVF] AVFoundation аудиосистема отключена" in log_output
        
        print(f"   - Лог 'initialize() ВЫЗВАН': {has_init_log}")
        print(f"   - Лог 'Начало инициализации AVF': {has_avf_start_log}")
        print(f"   - Лог 'AVFAudioEngine инициализирован': {has_avf_success_log}")
        print(f"   - Лог 'Ошибка создания AVFAudioEngine': {has_avf_error_log}")
        print(f"   - Лог 'AVFoundation аудиосистема отключена': {has_avf_disabled_log}")
        
        # Выводы
        print(f"\n📊 ВЫВОДЫ:")
        if not has_init_log:
            print(f"   ❌ initialize() НЕ вызывается или логирование не работает")
        elif not has_avf_start_log:
            print(f"   ❌ Код инициализации AVF НЕ выполняется (нет лога 'Начало инициализации AVF')")
        elif has_avf_success_log:
            print(f"   ✅ AVF инициализирован успешно")
            if avf_engine_after is None:
                print(f"   ⚠️ НО _avf_engine is None после инициализации - это проблема!")
        elif has_avf_error_log:
            print(f"   ❌ Ошибка при создании AVFAudioEngine")
        elif has_avf_disabled_log:
            print(f"   ⚠️ AVF отключен (причины в логе)")
        
        assert True  # Тест для диагностики
    
    @pytest.mark.asyncio
    async def test_fact_2_avf_engine_state(self, setup_integration):
        """Тест Факт 2: Проверка состояния _avf_engine после initialize()"""
        integration = setup_integration
        
        print(f"\n{'='*80}")
        print(f"🔍 ТЕСТ 2: Проверка состояния _avf_engine")
        print(f"{'='*80}")
        
        # Вызываем initialize()
        print(f"\n📋 Вызов initialize()...")
        await integration.initialize()
        
        # Проверяем состояние
        use_avf = getattr(integration, '_use_avf', None)
        avf_engine = getattr(integration, '_avf_engine', None)
        
        print(f"\n📊 Состояние после initialize():")
        print(f"   - _use_avf: {use_avf}")
        print(f"   - _avf_engine: {avf_engine is not None if avf_engine else False}")
        print(f"   - _avf_engine type: {type(avf_engine) if avf_engine else 'None'}")
        
        # Проверяем условие для новой логики
        condition_result = use_avf and avf_engine is not None
        print(f"\n📊 Условие для новой логики (строка 832):")
        print(f"   - _use_avf and _avf_engine is not None: {condition_result}")
        
        if condition_result:
            print(f"   ✅ Условие выполнено - новая логика AVF→Google будет использоваться")
        else:
            print(f"   ❌ Условие НЕ выполнено - будет использоваться LEGACY путь")
            if not use_avf:
                print(f"      - Причина: _use_avf=False")
            if avf_engine is None:
                print(f"      - Причина: _avf_engine=None")
        
        assert True  # Тест для диагностики
    
    @pytest.mark.asyncio
    async def test_fact_3_google_recognizer_creation(self, setup_integration):
        """Тест Факт 3: Проверка создания _google_recognizer при активации микрофона"""
        integration = setup_integration
        
        print(f"\n{'='*80}")
        print(f"🔍 ТЕСТ 3: Проверка создания _google_recognizer")
        print(f"{'='*80}")
        
        # Инициализируем
        await integration.initialize()
        
        # Проверяем состояние ДО активации
        use_avf = getattr(integration, '_use_avf', None)
        avf_engine = getattr(integration, '_avf_engine', None)
        google_recognizer_before = getattr(integration, '_google_recognizer', None)
        google_microphone_before = getattr(integration, '_google_microphone', None)
        
        print(f"\n📊 Состояние ДО активации микрофона:")
        print(f"   - _use_avf: {use_avf}")
        print(f"   - _avf_engine: {avf_engine is not None if avf_engine else False}")
        print(f"   - _google_recognizer: {google_recognizer_before is not None if google_recognizer_before else False}")
        print(f"   - _google_microphone: {google_microphone_before is not None if google_microphone_before else False}")
        
        # Проверяем условие для новой логики
        condition_result = use_avf and avf_engine is not None
        print(f"\n📊 Условие для новой логики:")
        print(f"   - _use_avf and _avf_engine is not None: {condition_result}")
        
        if not condition_result:
            print(f"\n   ❌ Условие НЕ выполнено - _google_recognizer НЕ будет создан")
            print(f"   ⚠️ Система будет использовать LEGACY путь")
        else:
            print(f"\n   ✅ Условие выполнено - _google_recognizer должен быть создан при активации")
            print(f"   ⚠️ Но нужно проверить реальную активацию микрофона")
        
        assert True  # Тест для диагностики
    
    @pytest.mark.asyncio
    async def test_fact_4_check_initialization_logs(self, setup_integration):
        """Тест Факт 4: Проверка логов инициализации"""
        integration = setup_integration
        
        print(f"\n{'='*80}")
        print(f"🔍 ТЕСТ 4: Проверка логов инициализации")
        print(f"{'='*80}")
        
        # Перехватываем логи
        log_capture = StringIO()
        handler = logging.StreamHandler(log_capture)
        handler.setLevel(logging.INFO)
        logger = logging.getLogger('integration.integrations.voice_recognition_integration')
        logger.addHandler(handler)
        
        # Вызываем initialize()
        await integration.initialize()
        
        # Получаем логи
        log_output = log_capture.getvalue()
        logger.removeHandler(handler)
        
        # Ищем ключевые логи
        expected_logs = [
            ("🔍 [AUDIO_DEBUG] VoiceRecognitionIntegration.initialize() ВЫЗВАН", "Вызов initialize()"),
            ("🔍 [AVF] Начало инициализации AVF...", "Начало инициализации AVF"),
            ("🔍 [AVF] UnifiedConfigLoader создан", "UnifiedConfigLoader создан"),
            ("🔍 [AVF] audio_config загружен", "audio_config загружен"),
            ("🔍 [AVF] avf_config загружен", "avf_config загружен"),
            ("🔍 [AVF] avf.enabled=", "avf.enabled проверка"),
            ("🔍 [AVF] _use_avf вычислен", "_use_avf вычислен"),
            ("✅ [AVF] AVFAudioEngine инициализирован", "AVFAudioEngine инициализирован (успех)"),
            ("❌ [AVF] Ошибка создания AVFAudioEngine", "AVFAudioEngine ошибка"),
            ("ℹ️ [AVF] AVFoundation аудиосистема отключена", "AVF отключен"),
        ]
        
        print(f"\n📋 Проверка ожидаемых логов:")
        found_logs = []
        missing_logs = []
        
        for log_pattern, description in expected_logs:
            found = log_pattern in log_output
            if found:
                found_logs.append(description)
                print(f"   ✅ {description}")
            else:
                missing_logs.append(description)
                print(f"   ❌ {description} - НЕ НАЙДЕН")
        
        print(f"\n📊 ИТОГИ:")
        print(f"   - Найдено логов: {len(found_logs)}/{len(expected_logs)}")
        print(f"   - Отсутствует логов: {len(missing_logs)}/{len(expected_logs)}")
        
        if missing_logs:
            print(f"\n   ⚠️ Отсутствующие логи:")
            for log in missing_logs:
                print(f"      - {log}")
        
        # Проверяем критичные логи
        if "🔍 [AVF] Начало инициализации AVF..." not in log_output:
            print(f"\n   ❌ КРИТИЧНО: Лог 'Начало инициализации AVF' отсутствует")
            print(f"      Это означает, что код инициализации AVF НЕ выполняется")
        
        if "✅ [AVF] AVFAudioEngine инициализирован" not in log_output and "❌ [AVF] Ошибка создания AVFAudioEngine" not in log_output and "ℹ️ [AVF] AVFoundation аудиосистема отключена" not in log_output:
            print(f"\n   ❌ КРИТИЧНО: Нет ни одного из финальных логов AVF")
            print(f"      Это означает, что код инициализации AVF не доходит до конца")
        
        assert True  # Тест для диагностики

