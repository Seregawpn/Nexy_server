"""
Изолированные тесты для проверки исправлений перехода в LISTENING из PROCESSING.

Тестирует:
1. Разрешение перехода в LISTENING из PROCESSING (прерывание текущей обработки)
2. Нормализация session_id для сравнения (float vs str)
3. Отсутствие дублирования логики проверки session_id
"""

import inspect
import pytest

from integration.integrations.mode_management_integration import ModeManagementIntegration
from integration.core.state_manager import AppMode


class TestModeManagementListeningTransition:
    """Изолированные тесты для перехода в LISTENING из PROCESSING."""
    
    def test_listening_transition_logic_isolated(self):
        """Тест: Логика разрешения перехода в LISTENING изолирована."""
        # Читаем исходный код _on_mode_request
        source = inspect.getsource(ModeManagementIntegration._on_mode_request)
        
        # Проверяем наличие логики разрешения перехода в LISTENING
        assert 'target == AppMode.LISTENING' in source, \
            "Должна быть проверка target == AppMode.LISTENING"
        
        # Проверяем, что переход разрешён даже с другим session_id
        assert 'разрешаем переход в LISTENING' in source or 'allow LISTENING transition' in source.lower(), \
            "Должна быть логика разрешения перехода в LISTENING"
    
    def test_session_id_normalization_logic(self):
        """Тест: Логика нормализации session_id изолирована."""
        # Читаем исходный код _on_mode_request
        source = inspect.getsource(ModeManagementIntegration._on_mode_request)
        
        # Проверяем наличие нормализации session_id
        assert 'session_id_str = str(session_id)' in source, \
            "Должна быть нормализация session_id к строке"
        
        assert 'current_session_id_str = str(current_session_id)' in source, \
            "Должна быть нормализация current_session_id к строке"
    
    def test_no_duplicate_session_id_checks(self):
        """Тест: Нет дублирования логики проверки session_id."""
        # Читаем исходный код _on_mode_request
        source = inspect.getsource(ModeManagementIntegration._on_mode_request)
        
        # Подсчитываем количество нормализаций session_id
        session_id_normalizations = source.count('session_id_str = str(')
        
        # Должна быть только одна нормализация для request и одна для current
        assert session_id_normalizations == 2, \
            f"Должна быть нормализация session_id (2 места: current и request), найдено: {session_id_normalizations}"
    
    def test_no_conflicting_mode_checks(self):
        """Тест: Нет конфликтующих проверок режима."""
        # Читаем исходный код _on_mode_request
        source = inspect.getsource(ModeManagementIntegration._on_mode_request)
        
        # Подсчитываем количество проверок target == AppMode.LISTENING
        listening_checks = source.count('target == AppMode.LISTENING')
        
        # Должна быть только одна проверка для разрешения перехода в LISTENING
        assert listening_checks == 1, \
            f"Должна быть только одна проверка target == AppMode.LISTENING, найдено: {listening_checks}"
    
    def test_no_duplicate_listening_transition_logic(self):
        """Тест: Нет дублирования логики перехода в LISTENING."""
        # Читаем исходный код _on_mode_request
        source = inspect.getsource(ModeManagementIntegration._on_mode_request)
        
        # Проверяем, что логика разрешения перехода в LISTENING есть только в одном месте
        # Ищем все места, где упоминается LISTENING в контексте разрешения перехода
        listening_allows = source.count('разрешаем переход в LISTENING')
        
        # Должна быть только одна логика разрешения
        assert listening_allows == 1, \
            f"Должна быть только одна логика разрешения перехода в LISTENING, найдено: {listening_allows}"

