"""
Smoke-тест для проверки, что память запрашивается только один раз

Проверяет:
1. Память запрашивается только в StreamingWorkflowIntegration (line 145)
2. В GrpcServiceIntegration нет дублирующего вызова памяти
"""

import pytest
import pytest_asyncio
import asyncio
from unittest.mock import Mock, AsyncMock, patch, MagicMock
from pathlib import Path
import sys

# Добавляем путь к корню проекта
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from integrations.workflow_integrations.streaming_workflow_integration import StreamingWorkflowIntegration
from integrations.service_integrations.grpc_service_integration import GrpcServiceIntegration


class TestMemorySingleCallSmoke:
    """Smoke-тест для проверки единого вызова памяти"""
    
    @pytest.fixture
    def mock_memory_workflow(self):
        """Мок MemoryWorkflowIntegration с отслеживанием вызовов"""
        memory_workflow = Mock()
        memory_workflow.is_initialized = True
        memory_workflow.get_memory_context_parallel = AsyncMock(return_value={'recent_context': 'test context'})
        memory_workflow.prefetch_memory = AsyncMock()
        memory_workflow.save_to_memory_background = AsyncMock()
        return memory_workflow
    
    @pytest.fixture
    def mock_text_module(self):
        """Мок текстового модуля"""
        module = Mock()
        module.is_initialized = True
        module.name = "text_processing"
        
        async def text_stream():
            yield "Тестовый ответ."
        
        async def process_mock(*args, **kwargs):
            return text_stream()
        
        module.process = AsyncMock(side_effect=process_mock)
        return module
    
    @pytest.fixture
    def mock_audio_module(self):
        """Мок аудио модуля"""
        module = Mock()
        module.is_initialized = True
        module.name = "audio_generation"
        
        async def generate_audio(*args, **kwargs):
            yield b"fake_audio_chunk"
        
        module.process = AsyncMock(return_value=generate_audio())
        return module
    
    @pytest_asyncio.fixture
    async def streaming_workflow(self, mock_text_module, mock_audio_module, mock_memory_workflow):
        """Инициализированный StreamingWorkflowIntegration"""
        workflow = StreamingWorkflowIntegration(
            text_processor=mock_text_module,
            audio_processor=mock_audio_module,
            memory_workflow=mock_memory_workflow
        )
        await workflow.initialize()
        return workflow, mock_memory_workflow
    
    @pytest_asyncio.fixture
    async def grpc_service(self, streaming_workflow, mock_memory_workflow):
        """Инициализированный GrpcServiceIntegration"""
        workflow, _ = streaming_workflow
        grpc_service = GrpcServiceIntegration(
            streaming_workflow=workflow,
            memory_workflow=mock_memory_workflow
        )
        await grpc_service.initialize()
        return grpc_service, mock_memory_workflow
    
    @pytest.mark.asyncio
    async def test_memory_called_once_in_streaming_workflow(self, streaming_workflow):
        """Проверка: память запрашивается только один раз в StreamingWorkflowIntegration"""
        workflow, mock_memory = streaming_workflow
        
        # Сбрасываем счётчик вызовов
        mock_memory.get_memory_context_parallel.reset_mock()
        
        request_data = {
            'text': 'Тестовый запрос',
            'session_id': 'test-session-1',
            'hardware_id': 'test-hardware-1'
        }
        
        # Обрабатываем запрос
        results = []
        async for result in workflow.process_request_streaming(request_data):
            results.append(result)
        
        # Проверяем, что get_memory_context_parallel вызван ровно один раз
        call_count = mock_memory.get_memory_context_parallel.call_count
        assert call_count == 1, (
            f"get_memory_context_parallel должен быть вызван ровно 1 раз, "
            f"но был вызван {call_count} раз(а)"
        )
        
        # Проверяем, что вызов был с правильным hardware_id
        mock_memory.get_memory_context_parallel.assert_called_once_with('test-hardware-1')
    
    @pytest.mark.asyncio
    async def test_memory_not_called_in_grpc_service(self, grpc_service):
        """Проверка: в GrpcServiceIntegration нет прямого вызова памяти"""
        grpc_service_obj, mock_memory = grpc_service
        
        # Сбрасываем счётчик вызовов
        mock_memory.get_memory_context_parallel.reset_mock()
        
        request_data = {
            'text': 'Тестовый запрос',
            'session_id': 'test-session-2',
            'hardware_id': 'test-hardware-2'
        }
        
        # Обрабатываем запрос через GrpcServiceIntegration
        results = []
        async for result in grpc_service_obj.process_request_complete(request_data):
            results.append(result)
        
        # Проверяем, что get_memory_context_parallel НЕ был вызван напрямую из GrpcServiceIntegration
        # (он должен вызываться только через StreamingWorkflowIntegration)
        # Но так как GrpcServiceIntegration вызывает StreamingWorkflowIntegration,
        # то вызов будет один раз через StreamingWorkflowIntegration
        
        # Проверяем, что вызов был только один раз (через StreamingWorkflowIntegration)
        call_count = mock_memory.get_memory_context_parallel.call_count
        assert call_count == 1, (
            f"get_memory_context_parallel должен быть вызван ровно 1 раз "
            f"(через StreamingWorkflowIntegration), но был вызван {call_count} раз(а). "
            f"Это означает, что есть дублирующий вызов в GrpcServiceIntegration!"
        )
        
        # Проверяем, что вызов был с правильным hardware_id
        mock_memory.get_memory_context_parallel.assert_called_once_with('test-hardware-2')
    
    @pytest.mark.asyncio
    async def test_no_duplicate_memory_calls_in_full_flow(self, grpc_service):
        """Проверка: при полном flow память запрашивается только один раз"""
        grpc_service_obj, mock_memory = grpc_service
        
        # Сбрасываем счётчик вызовов
        mock_memory.get_memory_context_parallel.reset_mock()
        
        request_data = {
            'text': 'Тестовый запрос для полного flow',
            'session_id': 'test-session-3',
            'hardware_id': 'test-hardware-3'
        }
        
        # Обрабатываем запрос через полный flow
        results = []
        async for result in grpc_service_obj.process_request_complete(request_data):
            results.append(result)
        
        # КРИТИЧЕСКАЯ ПРОВЕРКА: вызов должен быть ровно один раз
        call_count = mock_memory.get_memory_context_parallel.call_count
        assert call_count == 1, (
            f"❌ КРИТИЧЕСКАЯ ОШИБКА: get_memory_context_parallel вызван {call_count} раз(а) вместо 1! "
            f"Это означает дублирование вызовов памяти. "
            f"Ожидается: 1 вызов в StreamingWorkflowIntegration. "
            f"Найдено: {call_count} вызов(ов)"
        )
        
        # Проверяем, что результат обработки успешен
        final_results = [r for r in results if r.get('is_final')]
        assert len(final_results) > 0, "Должен быть финальный результат"
        assert final_results[0].get('success', False), "Обработка должна быть успешной"


if __name__ == "__main__":
    pytest.main([__file__, "-v", "-s"])
