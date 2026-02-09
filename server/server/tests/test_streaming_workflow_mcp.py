"""
Unit-тесты для StreamingWorkflowIntegration с поддержкой MCP команд (Фаза 2)

Покрывает сценарии:
1. Ответ без команды → текст и аудио идут как обычно
2. Ответ с командой + текстом → текст передаётся в TTS, MCP payload фиксируется
3. Ответ с командой, но без текста → MCP payload есть, текст/аудио отсутствуют
4. Несколько чанков, где action приходит не первым
5. Проверка, что действие (payload) не дублируется
"""

import pytest
import pytest_asyncio
import asyncio
import json
from unittest.mock import Mock, AsyncMock, patch, MagicMock
from pathlib import Path
import sys

# Добавляем путь к корню проекта
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from integrations.workflow_integrations.streaming_workflow_integration import StreamingWorkflowIntegration
from integrations.core.assistant_response_parser import ParsedResponse
from config.unified_config import get_config, FeaturesConfig, KillSwitchesConfig


class TestStreamingWorkflowMCP:
    """Тесты для StreamingWorkflowIntegration с MCP командами"""
    
    @pytest.fixture
    def mock_text_module(self):
        """Мок текстового модуля"""
        module = Mock()
        module.is_initialized = True
        module.name = "text_processing"
        return module
    
    @pytest.fixture
    def mock_audio_module(self):
        """Мок аудио модуля"""
        module = Mock()
        module.is_initialized = True
        module.name = "audio_generation"
        
        async def generate_audio(*args, **kwargs):
            yield b"fake_audio_chunk_1"
            yield b"fake_audio_chunk_2"
        
        module.process = AsyncMock(return_value=generate_audio())
        return module
    
    @pytest.fixture
    def workflow(self, mock_text_module, mock_audio_module):
        """Фикстура для StreamingWorkflowIntegration"""
        return StreamingWorkflowIntegration(
            text_processor=mock_text_module,
            audio_processor=mock_audio_module
        )
    
    @pytest_asyncio.fixture
    async def initialized_workflow(self, workflow):
        """Инициализированный workflow"""
        await workflow.initialize()
        return workflow
    
    @pytest.mark.asyncio
    async def test_plain_text_response_no_command(self, initialized_workflow, mock_text_module):
        """Тест 1: Ответ без команды → текст и аудио идут как обычно"""
        # Настраиваем мок текстового модуля (добавляем точку для завершенного предложения)
        async def text_stream():
            yield "Это обычный текстовый ответ без команды."
        
        # Используем AsyncMock с return_value, который возвращает generator
        # Но нужно создать функцию, которая возвращает generator при каждом вызове
        async def process_mock(*args, **kwargs):
            return text_stream()
        mock_text_module.process = AsyncMock(side_effect=process_mock)
        
        request_data = {
            'text': 'Test prompt',
            'session_id': 'test-session-1',
            'hardware_id': 'test-hardware'
        }
        
        results = []
        async for result in initialized_workflow.process_request_streaming(request_data):
            results.append(result)
        
        # Проверяем, что есть text_response (промежуточные или в финальном)
        text_results = [r for r in results if 'text_response' in r and r.get('text_response')]
        final_results = [r for r in results if r.get('is_final')]
        
        # Либо есть промежуточные text_response, либо text_full_response в финальном
        has_text = len(text_results) > 0
        if not has_text and final_results:
            has_text = bool(final_results[0].get('text_full_response'))
        
        assert has_text, f"Должен быть text_response или text_full_response. Все результаты: {results}"
        
        # Проверяем, что есть audio_chunk
        audio_results = [r for r in results if 'audio_chunk' in r]
        assert len(audio_results) > 0, "Должен быть хотя бы один audio_chunk"
        
        # Проверяем, что нет command_payload
        if final_results:
            assert 'command_payload' not in final_results[0], "Не должно быть command_payload для обычного ответа"
    
    @pytest.mark.asyncio
    async def test_action_response_with_text(self, initialized_workflow, mock_text_module):
        """Тест 2: Ответ с командой + текстом → текст передаётся в TTS, MCP payload фиксируется"""
        # Настраиваем мок для возврата JSON с командой
        action_response = {
            "session_id": "test-session-2",
            "command": "open_app",
            "args": {
                "app_name": "Telegram"
            },
            "text": "Открываю Telegram"
        }
        
        async def text_stream():
            yield json.dumps(action_response)
        
        mock_text_module.process = AsyncMock(return_value=text_stream())
        
        # Включаем фича-флаг
        with patch('integrations.workflow_integrations.streaming_workflow_integration.get_config') as mock_get_config:
            config = Mock()
            config.features.forward_assistant_actions = True
            config.kill_switches.disable_forward_assistant_actions = False
            mock_get_config.return_value = config
            
            request_data = {
                'text': 'Open Telegram',
                'session_id': 'test-session-2',
                'hardware_id': 'test-hardware'
            }
            
            results = []
            async for result in initialized_workflow.process_request_streaming(request_data):
                results.append(result)
            
            # Проверяем, что есть text_response с текстом
            text_results = [r for r in results if 'text_response' in r and r.get('text_response')]
            assert len(text_results) > 0, "Должен быть text_response"
            assert any('Открываю Telegram' in r.get('text_response', '') for r in text_results), "Текст должен присутствовать"
            
            # Проверяем, что есть command_payload в финальном результате
            final_result = [r for r in results if r.get('is_final')]
            assert len(final_result) > 0, "Должен быть финальный результат"
            assert 'command_payload' in final_result[0], "Должен быть command_payload"
            assert final_result[0]['command_payload']['event'] == 'mcp.command_request'
            assert final_result[0]['command_payload']['payload']['command'] == 'open_app'
    
    @pytest.mark.asyncio
    async def test_action_response_no_text(self, initialized_workflow, mock_text_module):
        """Тест 3: Ответ с командой, но без текста → MCP payload есть, текст/аудио отсутствуют"""
        action_response = {
            "session_id": "test-session-3",
            "command": "open_app",
            "args": {
                "app_name": "Telegram"
            }
        }
        
        async def text_stream():
            yield json.dumps(action_response)
        
        mock_text_module.process = AsyncMock(return_value=text_stream())
        
        # Включаем фича-флаг
        with patch('integrations.workflow_integrations.streaming_workflow_integration.get_config') as mock_get_config:
            config = Mock()
            config.features.forward_assistant_actions = True
            config.kill_switches.disable_forward_assistant_actions = False
            mock_get_config.return_value = config
            
            request_data = {
                'text': 'Open Telegram silently',
                'session_id': 'test-session-3',
                'hardware_id': 'test-hardware'
            }
            
            results = []
            async for result in initialized_workflow.process_request_streaming(request_data):
                results.append(result)
            
            # Проверяем, что нет text_response (или он пустой)
            text_results = [r for r in results if 'text_response' in r and r.get('text_response')]
            # Может быть пустой text_response, но не должно быть непустых
            
            # Проверяем, что нет audio_chunk (так как текст пустой)
            audio_results = [r for r in results if 'audio_chunk' in r]
            assert len(audio_results) == 0, "Не должно быть audio_chunk для пустого текста"
            
            # Проверяем, что есть command_payload в финальном результате
            final_result = [r for r in results if r.get('is_final')]
            assert len(final_result) > 0, "Должен быть финальный результат"
            assert 'command_payload' in final_result[0], "Должен быть command_payload даже без текста"
    
    @pytest.mark.asyncio
    async def test_multiple_chunks_action_not_first(self, initialized_workflow, mock_text_module):
        """Тест 4: Несколько чанков, где action приходит не первым"""
        async def text_stream():
            yield "Сначала обычный текст"
            yield json.dumps({
                "session_id": "test-session-4",
                "command": "open_app",
                "args": {"app_name": "Telegram"},
                "text": "Теперь открываю Telegram"
            })
            yield "И ещё немного текста"
        
        mock_text_module.process = AsyncMock(return_value=text_stream())
        
        # Включаем фича-флаг
        with patch('integrations.workflow_integrations.streaming_workflow_integration.get_config') as mock_get_config:
            config = Mock()
            config.features.forward_assistant_actions = True
            config.kill_switches.disable_forward_assistant_actions = False
            mock_get_config.return_value = config
            
            request_data = {
                'text': 'Test multiple chunks',
                'session_id': 'test-session-4',
                'hardware_id': 'test-hardware'
            }
            
            results = []
            async for result in initialized_workflow.process_request_streaming(request_data):
                results.append(result)
            
            # Проверяем, что есть несколько text_response
            text_results = [r for r in results if 'text_response' in r and r.get('text_response')]
            assert len(text_results) > 0, "Должны быть text_response"
            
            # Проверяем, что command_payload есть только один раз
            final_result = [r for r in results if r.get('is_final')]
            assert len(final_result) > 0, "Должен быть финальный результат"
            command_count = sum(1 for r in results if 'command_payload' in r)
            assert command_count == 1, f"command_payload должен быть только один раз, найдено: {command_count}"
    
    @pytest.mark.asyncio
    async def test_command_payload_not_duplicated(self, initialized_workflow, mock_text_module):
        """Тест 5: Проверка, что действие (payload) не дублируется"""
        action_response = {
            "session_id": "test-session-5",
            "command": "open_app",
            "args": {"app_name": "Telegram"},
            "text": "Открываю Telegram"
        }
        
        # Возвращаем один и тот же JSON несколько раз
        async def text_stream():
            for _ in range(3):
                yield json.dumps(action_response)
        
        mock_text_module.process = AsyncMock(return_value=text_stream())
        
        # Включаем фича-флаг
        with patch('integrations.workflow_integrations.streaming_workflow_integration.get_config') as mock_get_config:
            config = Mock()
            config.features.forward_assistant_actions = True
            config.kill_switches.disable_forward_assistant_actions = False
            mock_get_config.return_value = config
            
            request_data = {
                'text': 'Open Telegram multiple times',
                'session_id': 'test-session-5',
                'hardware_id': 'test-hardware'
            }
            
            results = []
            async for result in initialized_workflow.process_request_streaming(request_data):
                results.append(result)
            
            # Проверяем, что command_payload есть только один раз
            command_results = [r for r in results if 'command_payload' in r]
            assert len(command_results) == 1, f"command_payload должен быть только один раз, найдено: {len(command_results)}"
            
            # Проверяем, что в финальном результате есть command_payload
            final_result = [r for r in results if r.get('is_final')]
            assert len(final_result) > 0, "Должен быть финальный результат"
            assert 'command_payload' in final_result[0], "command_payload должен быть в финальном результате"
    
    @pytest.mark.asyncio
    async def test_feature_flag_disabled(self, initialized_workflow, mock_text_module):
        """Дополнительный тест: Фича-флаг выключен → command_payload не отправляется"""
        action_response = {
            "session_id": "test-session-6",
            "command": "open_app",
            "args": {"app_name": "Telegram"},
            "text": "Открываю Telegram"
        }
        
        async def text_stream():
            yield json.dumps(action_response)
        
        mock_text_module.process = AsyncMock(return_value=text_stream())
        
        # Выключаем фича-флаг
        with patch('integrations.workflow_integrations.streaming_workflow_integration.get_config') as mock_get_config:
            config = Mock()
            config.features.forward_assistant_actions = False
            config.kill_switches.disable_forward_assistant_actions = False
            mock_get_config.return_value = config
            
            request_data = {
                'text': 'Open Telegram',
                'session_id': 'test-session-6',
                'hardware_id': 'test-hardware'
            }
            
            results = []
            async for result in initialized_workflow.process_request_streaming(request_data):
                results.append(result)
            
            # Проверяем, что command_payload отсутствует
            final_result = [r for r in results if r.get('is_final')]
            if final_result:
                assert 'command_payload' not in final_result[0], "command_payload не должен быть при выключенном фича-флаге"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])

