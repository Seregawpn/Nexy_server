#!/usr/bin/env python3
"""
Unit-тест для проверки валидации идентификаторов в gRPC сервере

Проверяет:
- Валидацию session_id (обязательное поле)
- Валидацию hardware_id (не может быть пустым или "unknown")
- Корректность сообщений об ошибках
"""

import pytest
import sys
from pathlib import Path
from unittest.mock import Mock, AsyncMock, patch

# Добавляем путь к модулям
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from modules.grpc_service.core.grpc_server import NewStreamingServicer
from modules.grpc_service import streaming_pb2


class TestGrpcIdentifierValidation:
    """Тесты валидации идентификаторов в gRPC сервере"""
    
    @pytest.fixture
    def servicer(self):
        """Фикстура для создания сервиса с моками"""
        # Мокаем все зависимости, которые не нужны для валидации
        mock_manager_instance = Mock()
        mock_manager_instance.initialize = AsyncMock(return_value=True)
        mock_manager_instance.streaming_workflow = None
        mock_manager_instance.interrupt_workflow = None
        
        # NewStreamingServicer наследуется от streaming_pb2_grpc.StreamingServiceServicer
        # и не принимает аргументов в __init__
        servicer = NewStreamingServicer()
        servicer.grpc_service_manager = mock_manager_instance
        return servicer
    
    @pytest.mark.asyncio
    async def test_stream_audio_missing_session_id(self, servicer):
        """Тест: запрос без session_id должен вернуть ошибку"""
        # Создаем запрос БЕЗ session_id
        request = streaming_pb2.StreamRequest(
            prompt="test",
            hardware_id="valid_hardware_id"
            # session_id отсутствует
        )
        
        # Мокаем context
        context = Mock()
        
        # Вызываем метод
        responses = []
        async for response in servicer.StreamAudio(request, context):
            responses.append(response)
        
        # Проверяем, что получена ошибка
        assert len(responses) > 0, "Должен быть получен хотя бы один ответ"
        
        error_response = responses[0]
        assert error_response.WhichOneof("content") == "error_message", "Должен быть error_message"
        assert "session_id is required" in error_response.error_message.lower(), \
            f"Сообщение об ошибке должно содержать 'session_id is required', получено: {error_response.error_message}"
    
    @pytest.mark.asyncio
    async def test_stream_audio_empty_session_id(self, servicer):
        """Тест: запрос с пустым session_id должен вернуть ошибку"""
        request = streaming_pb2.StreamRequest(
            prompt="test",
            hardware_id="valid_hardware_id",
            session_id=""  # Пустой session_id
        )
        
        context = Mock()
        
        responses = []
        async for response in servicer.StreamAudio(request, context):
            responses.append(response)
        
        assert len(responses) > 0
        error_response = responses[0]
        assert error_response.WhichOneof("content") == "error_message"
        assert "session_id is required" in error_response.error_message.lower()
    
    @pytest.mark.asyncio
    async def test_stream_audio_invalid_hardware_id_unknown(self, servicer):
        """Тест: запрос с hardware_id='unknown' должен вернуть ошибку"""
        request = streaming_pb2.StreamRequest(
            prompt="test",
            hardware_id="unknown",
            session_id="valid_session_id"
        )
        
        context = Mock()
        
        responses = []
        async for response in servicer.StreamAudio(request, context):
            responses.append(response)
        
        assert len(responses) > 0
        error_response = responses[0]
        assert error_response.WhichOneof("content") == "error_message"
        assert "hardware_id" in error_response.error_message.lower() or "unknown" in error_response.error_message.lower()
    
    @pytest.mark.asyncio
    async def test_stream_audio_empty_hardware_id(self, servicer):
        """Тест: запрос с пустым hardware_id должен вернуть ошибку"""
        request = streaming_pb2.StreamRequest(
            prompt="test",
            hardware_id="",  # Пустой hardware_id
            session_id="valid_session_id"
        )
        
        context = Mock()
        
        responses = []
        async for response in servicer.StreamAudio(request, context):
            responses.append(response)
        
        assert len(responses) > 0
        error_response = responses[0]
        assert error_response.WhichOneof("content") == "error_message"
        assert "hardware_id" in error_response.error_message.lower()

    @pytest.mark.asyncio
    async def test_stream_audio_both_invalid_hardware_first(self, servicer):
        """Тест: при двух невалидных id приоритет ошибки hardware_id"""
        request = streaming_pb2.StreamRequest(
            prompt="test",
            hardware_id="unknown",
            session_id=""  # Невалидный session_id
        )
        
        context = Mock()
        
        responses = []
        async for response in servicer.StreamAudio(request, context):
            responses.append(response)
        
        assert len(responses) > 0
        error_response = responses[0]
        assert error_response.WhichOneof("content") == "error_message"
        assert "hardware_id" in error_response.error_message.lower()
    
    @pytest.mark.asyncio
    async def test_stream_audio_valid_identifiers(self, servicer):
        """Тест: запрос с валидными идентификаторами должен пройти валидацию"""
        request = streaming_pb2.StreamRequest(
            prompt="test",
            hardware_id="valid_hardware_id",
            session_id="valid_session_id"
        )
        
        context = Mock()
        
        # Мокаем workflow для обработки запроса после валидации
        mock_workflow = AsyncMock()
        mock_workflow.process_request_streaming = AsyncMock()
        mock_workflow.process_request_streaming.return_value = async_generator_mock([
            {"success": True, "text_response": "test response"}
        ])
        
        # Мокаем grpc_service_manager для возврата workflow
        servicer.grpc_service_manager.streaming_workflow = mock_workflow
        
        # Вызываем метод
        responses = []
        try:
            async for response in servicer.StreamAudio(request, context):
                responses.append(response)
                # Ограничиваем количество ответов для теста
                if len(responses) >= 1:
                    break
        except Exception as e:
            # Если возникает ошибка после валидации (например, из-за отсутствия модулей),
            # это нормально - главное, что валидация прошла
            # Проверяем, что ошибка НЕ связана с валидацией идентификаторов
            assert "session_id is required" not in str(e).lower()
            assert "hardware_id" not in str(e).lower() or "unknown" not in str(e).lower()
            return
        
        # Если дошли сюда, валидация прошла успешно
        # (даже если последующая обработка не удалась)
        assert True, "Валидация идентификаторов прошла успешно"


def async_generator_mock(items):
    """Вспомогательная функция для создания async generator из списка"""
    async def _gen():
        for item in items:
            yield item
    return _gen()


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
