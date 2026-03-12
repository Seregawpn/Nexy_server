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
from integrations.workflow_integrations.interrupt_workflow_integration import InterruptException
from modules.grpc_service.core.grpc_server import NewStreamingServicer
from modules.grpc_service import streaming_pb2


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

    @pytest.mark.asyncio
    async def test_memory_save_prefers_prepared_route_over_final_stream_route(self):
        """Prepared route должен оставаться Source of Truth для memory update."""
        workflow = Mock(spec=StreamingWorkflowIntegration)
        workflow.is_initialized = True

        async def process_streaming(_request_data):
            yield {
                'success': True,
                'text_response': 'Yes, I can. Who should I send the message to?',
                'route': 'messages',
            }
            yield {
                'success': True,
                'text_full_response': 'Yes, I can. Who should I send the message to?',
                'route': 'messages',
                'is_final': True,
            }

        workflow.process_request_streaming = Mock(side_effect=lambda *args, **kwargs: process_streaming(*args, **kwargs))

        memory_workflow = Mock()
        memory_workflow.is_initialized = True
        memory_workflow.initialize = AsyncMock(return_value=True)
        memory_workflow.save_to_memory_background = AsyncMock(return_value=True)

        grpc_integration = GrpcServiceIntegration(
            streaming_workflow=workflow,
            memory_workflow=memory_workflow,
        )
        await grpc_integration.initialize()

        request_data = {
            'text': 'Can you send messages for me?',
            'session_id': 'test-session-capability-route',
            'hardware_id': 'test-hardware',
            '_assistant_runtime_v2_signals': {
                'route': 'capability',
            }
        }

        results = []
        async for result in grpc_integration.process_request_complete(request_data):
            results.append(result)

        assert results, "Должен быть хотя бы один streamed result"
        memory_workflow.save_to_memory_background.assert_awaited_once()
        save_data = memory_workflow.save_to_memory_background.await_args.args[0]
        assert save_data['route'] == 'capability'

    @pytest.mark.asyncio
    async def test_interrupt_exception_does_not_fallback_to_direct_processing(self, mock_streaming_workflow):
        interrupt_workflow = Mock()
        interrupt_workflow.is_initialized = True

        async def process_with_interrupts(_workflow_func, _hardware_id, _session_id):
            raise InterruptException("Global interrupt active for test-hardware")
            yield  # pragma: no cover

        interrupt_workflow.process_with_interrupts = process_with_interrupts

        grpc_integration = GrpcServiceIntegration(
            streaming_workflow=mock_streaming_workflow,
            interrupt_workflow=interrupt_workflow,
        )
        await grpc_integration.initialize()

        request_data = {
            'text': 'Open Telegram',
            'session_id': 'test-session-interrupt',
            'hardware_id': 'test-hardware',
        }

        results = []
        async for result in grpc_integration.process_request_complete(request_data):
            results.append(result)

        assert len(results) == 1
        assert results[0]['success'] is False
        assert results[0]['error_code'] == 'CANCELLED'
        assert results[0]['error_type'] == 'interrupted'
        mock_streaming_workflow.process_request_streaming.assert_not_called()

    @pytest.mark.asyncio
    async def test_interrupt_wrapper_error_after_partial_yield_does_not_restart_workflow(
        self,
        mock_streaming_workflow,
    ):
        interrupt_workflow = Mock()
        interrupt_workflow.is_initialized = True

        async def process_with_interrupts(workflow_func, _hardware_id, _session_id):
            async for item in workflow_func():
                yield item
                break
            raise RuntimeError("wrapper crashed after partial yield")

        interrupt_workflow.process_with_interrupts = process_with_interrupts

        grpc_integration = GrpcServiceIntegration(
            streaming_workflow=mock_streaming_workflow,
            interrupt_workflow=interrupt_workflow,
        )
        await grpc_integration.initialize()

        request_data = {
            'text': 'Open Telegram',
            'session_id': 'test-session-wrapper',
            'hardware_id': 'test-hardware',
        }

        results = []
        async for result in grpc_integration.process_request_complete(request_data):
            results.append(result)

        assert any(result.get('text_response') == 'Открываю Telegram' for result in results)
        assert results[-1]['success'] is False
        assert results[-1]['error_type'] == 'interrupt_wrapper_error'
        assert mock_streaming_workflow.process_request_streaming.call_count == 1

    @pytest.mark.asyncio
    async def test_action_message_order_after_text_audio(self):
        """Тест 5: ActionMessage отправляется после text/audio в рамках одного item"""
        servicer = NewStreamingServicer()
        mock_manager = Mock()
        mock_manager.initialize = AsyncMock(return_value=True)
        mock_manager.streaming_workflow = None
        mock_manager.interrupt_workflow = Mock()
        mock_manager.interrupt_workflow.check_interrupts = AsyncMock(return_value=False)

        async def process_stream(request_data):
            yield {
                'success': True,
                'text_response': 'Hello',
                'audio_chunk': b'1234',
                'command_payload': {
                    'event': 'mcp.command_request',
                    'payload': {'session_id': request_data['session_id'], 'command': 'open_app', 'args': {'app_name': 'Safari'}}
                }
            }

        mock_manager.process = process_stream
        servicer.grpc_service_manager = mock_manager

        request = streaming_pb2.StreamRequest(
            prompt="test",
            hardware_id="valid_hardware_id",
            session_id="123e4567-e89b-42d3-a456-426614174000"
        )
        context = Mock()

        kinds = []
        with patch('modules.grpc_service.core.grpc_server.get_metrics', return_value={'active_connections': 0}), \
             patch('modules.grpc_service.core.grpc_server.set_active_connections'), \
             patch('modules.grpc_service.core.grpc_server.record_request'):
            async for response in servicer.StreamAudio(request, context):
                if response.text_chunk:
                    kinds.append("text")
                elif response.audio_chunk and response.audio_chunk.audio_data:
                    kinds.append("audio")
                elif response.action_message and response.action_message.action_json:
                    kinds.append("action")
                elif response.end_message:
                    kinds.append("end")

        # ожидаем порядок: text -> audio -> action -> end
        assert "text" in kinds and "audio" in kinds and "action" in kinds
        assert kinds.index("text") < kinds.index("audio") < kinds.index("action")


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
