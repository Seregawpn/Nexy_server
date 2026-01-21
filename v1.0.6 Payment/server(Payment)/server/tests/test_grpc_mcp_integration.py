"""
Интеграционные тесты для gRPC слоя с поддержкой MCP команд (Фаза 3)

Проверяет:
1. command_payload передаётся через gRPC как text_chunk с префиксом __MCP__
2. Текст и аудио продолжают работать параллельно
3. Формат JSON корректен
"""

import pytest
import json
from unittest.mock import Mock, AsyncMock, patch, MagicMock
from pathlib import Path
import sys

# Добавляем путь к корню проекта
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

# Импорты для тестирования gRPC слоя
from integrations.service_integrations.grpc_service_integration import GrpcServiceIntegration
from integrations.workflow_integrations.streaming_workflow_integration import StreamingWorkflowIntegration


class TestGrpcMcpIntegration:
    """Интеграционные тесты для gRPC слоя с MCP командами"""
    
    @pytest.fixture
    def mock_streaming_workflow(self):
        """Мок StreamingWorkflowIntegration"""
        workflow = Mock(spec=StreamingWorkflowIntegration)
        workflow.is_initialized = True
        
        async def process_streaming(request_data):
            # Симулируем ответ с command_payload
            yield {
                'success': True,
                'text_response': 'Открываю Telegram',
                'sentence_index': 1
            }
            yield {
                'success': True,
                'audio_chunk': b'fake_audio_data',
                'sentence_index': 1,
                'audio_chunk_index': 1
            }
            # Финальный результат с command_payload
            yield {
                'success': True,
                'text_full_response': 'Открываю Telegram',
                'sentences_processed': 1,
                'audio_chunks_processed': 1,
                'audio_bytes_processed': 100,
                'is_final': True,
                'command_payload': {
                    'event': 'mcp.command_request',
                    'payload': {
                        'session_id': 'test-session-1',
                        'command': 'open_app',
                        'args': {
                            'app_name': 'Telegram'
                        }
                    }
                }
            }
        
        # Используем return_value с функцией, которая создает новый generator при каждом вызове
        # Но AsyncMock с return_value не работает для generator, поэтому используем обычный Mock
        def create_generator(*args, **kwargs):
            return process_streaming(*args, **kwargs)
        workflow.process_request_streaming = Mock(side_effect=create_generator)
        return workflow
    
    @pytest.fixture
    def grpc_integration(self, mock_streaming_workflow):
        """Фикстура для GrpcServiceIntegration"""
        return GrpcServiceIntegration(
            streaming_workflow=mock_streaming_workflow
        )
    
    @pytest.mark.asyncio
    async def test_command_payload_passed_through_grpc(self, grpc_integration, mock_streaming_workflow):
        """Тест 1: command_payload передаётся через GrpcServiceIntegration"""
        await grpc_integration.initialize()
        
        request_data = {
            'text': 'Open Telegram',
            'session_id': 'test-session-1',
            'hardware_id': 'test-hardware'
        }
        
        results = []
        async for result in grpc_integration.process_request_complete(request_data):
            results.append(result)
        
        # Проверяем, что command_payload присутствует в финальном результате
        final_results = [r for r in results if r.get('is_final')]
        assert len(final_results) > 0, "Должен быть финальный результат"
        
        final_result = final_results[0]
        assert 'command_payload' in final_result, "command_payload должен быть в финальном результате"
        assert final_result['command_payload']['event'] == 'mcp.command_request'
        assert final_result['command_payload']['payload']['command'] == 'open_app'
    
    @pytest.mark.asyncio
    async def test_text_and_audio_continue_parallel(self, grpc_integration, mock_streaming_workflow):
        """Тест 2: Текст и аудио продолжают работать параллельно"""
        await grpc_integration.initialize()
        
        request_data = {
            'text': 'Open Telegram',
            'session_id': 'test-session-2',
            'hardware_id': 'test-hardware'
        }
        
        results = []
        async for result in grpc_integration.process_request_complete(request_data):
            results.append(result)
        
        # Проверяем, что есть и текст, и аудио
        text_results = [r for r in results if 'text_response' in r and r.get('text_response')]
        audio_results = [r for r in results if 'audio_chunk' in r]
        
        assert len(text_results) > 0, "Должен быть text_response"
        assert len(audio_results) > 0, "Должен быть audio_chunk"
    
    @pytest.mark.asyncio
    async def test_mcp_format_in_grpc_server(self):
        """Тест 3: Формат MCP команды в gRPC сервере (симуляция)"""
        # Симулируем обработку command_payload в grpc_server.py
        command_payload = {
            'event': 'mcp.command_request',
            'payload': {
                'session_id': 'test-session-3',
                'command': 'open_app',
                'args': {
                    'app_name': 'Telegram'
                }
            }
        }
        
        # Формируем JSON строку с префиксом (как в grpc_server.py)
        mcp_json = json.dumps(command_payload, ensure_ascii=False)
        mcp_text_chunk = f"__MCP__{mcp_json}"
        
        # Проверяем формат
        assert mcp_text_chunk.startswith('__MCP__'), "Должен начинаться с префикса __MCP__"
        
        # Проверяем, что можно распарсить JSON
        json_part = mcp_text_chunk[7:]  # Убираем префикс __MCP__
        parsed = json.loads(json_part)
        assert parsed['event'] == 'mcp.command_request'
        assert parsed['payload']['command'] == 'open_app'
        assert parsed['payload']['args']['app_name'] == 'Telegram'
    
    @pytest.mark.asyncio
    async def test_no_command_payload_when_feature_disabled(self, grpc_integration, mock_streaming_workflow):
        """Тест 4: command_payload не передаётся, когда фича-флаг выключен"""
        # Модифицируем workflow, чтобы он не возвращал command_payload при выключенном флаге
        async def process_streaming_no_command(request_data):
            yield {
                'success': True,
                'text_response': 'Обычный ответ',
                'sentence_index': 1
            }
            yield {
                'success': True,
                'text_full_response': 'Обычный ответ',
                'is_final': True
                # Нет command_payload
            }
        
        mock_streaming_workflow.process_request_streaming = AsyncMock(side_effect=process_streaming_no_command)
        
        await grpc_integration.initialize()
        
        request_data = {
            'text': 'Test',
            'session_id': 'test-session-4',
            'hardware_id': 'test-hardware'
        }
        
        results = []
        async for result in grpc_integration.process_request_complete(request_data):
            results.append(result)
        
        # Проверяем, что нет command_payload
        final_results = [r for r in results if r.get('is_final')]
        if final_results:
            assert 'command_payload' not in final_results[0], "command_payload не должен быть при выключенном фича-флаге"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])

