"""
Изолированный тест для проверки полного прерывания диалога.

Проблема: При прерывании воспроизводится только один чанк, но не происходит
полное прерывание всего диалога. Нужно, чтобы при прерывании все чанки
отменялись, а не только текущий.
"""

import pytest
import pytest_asyncio
import asyncio
from unittest.mock import MagicMock, AsyncMock, patch
from integration.integrations.speech_playback_integration import SpeechPlaybackIntegration
from integration.core.event_bus import EventBus
from integration.core.state_manager import ApplicationStateManager
from integration.core.error_handler import ErrorHandler


@pytest.fixture
def mock_event_bus():
    """Мок EventBus"""
    bus = MagicMock(spec=EventBus)
    bus.publish = AsyncMock()
    bus.subscribe = AsyncMock()
    bus.unsubscribe = AsyncMock()
    return bus


@pytest.fixture
def mock_state_manager():
    """Мок ApplicationStateManager"""
    manager = MagicMock(spec=ApplicationStateManager)
    manager.get_current_session_id = MagicMock(return_value="test_session_123")
    manager.update_session_id = MagicMock()
    return manager


@pytest.fixture
def mock_error_handler():
    """Мок ErrorHandler"""
    return MagicMock(spec=ErrorHandler)


@pytest.fixture
def mock_avf_engine():
    """Мок AVFAudioEngine"""
    engine = MagicMock()
    engine.is_output_active = False
    engine.stop_output = AsyncMock(return_value=True)
    engine.play_audio = AsyncMock(return_value=True)
    return engine


@pytest_asyncio.fixture
async def speech_playback_integration(mock_event_bus, mock_state_manager, mock_error_handler, mock_avf_engine):
    """Создаем SpeechPlaybackIntegration с моками"""
    integration = SpeechPlaybackIntegration(
        event_bus=mock_event_bus,
        state_manager=mock_state_manager,
        error_handler=mock_error_handler
    )
    
    # Мокируем AVF engine
    integration._avf_engine = mock_avf_engine
    integration._use_avf = True
    
    # Инициализируем
    await integration.initialize()
    
    return integration


@pytest.mark.asyncio
async def test_interrupt_cancels_all_chunks(speech_playback_integration, mock_avf_engine, mock_state_manager):
    """Тест: При прерывании отменяются все чанки, а не только текущий"""
    session_id = "test_session_123"
    mock_state_manager.get_current_session_id.return_value = session_id
    
    # Шаг 1: Добавляем несколько чанков в буфер
    chunk1 = {
        "data": b"chunk1_data" * 1000,
        "sample_rate": 48000,
        "channels": 1
    }
    chunk2 = {
        "data": b"chunk2_data" * 1000,
        "sample_rate": 48000,
        "channels": 1
    }
    
    # Добавляем чанки в буфер
    speech_playback_integration._avf_chunk_buffer[session_id] = [
        {"data": chunk1["data"], "sample_rate": chunk1["sample_rate"], "channels": chunk1["channels"]},
        {"data": chunk2["data"], "sample_rate": chunk2["sample_rate"], "channels": chunk2["channels"]}
    ]
    speech_playback_integration._avf_is_playing[session_id] = True
    
    # Шаг 2: Публикуем прерывание
    interrupt_event = {
        "type": "playback.cancelled",
        "data": {
            "session_id": session_id,
            "source": "keyboard",
            "reason": "user_interrupt"
        }
    }
    
    await speech_playback_integration._on_unified_interrupt(interrupt_event)
    
    # Шаг 3: Проверяем, что все чанки отменены
    assert session_id in speech_playback_integration._cancelled_sessions or str(session_id) in speech_playback_integration._cancelled_sessions, \
        "Сессия должна быть помечена как отменённая"
    
    assert session_id not in speech_playback_integration._avf_chunk_buffer, \
        "Буфер чанков должен быть очищен для отменённой сессии"
    
    assert session_id not in speech_playback_integration._avf_is_playing, \
        "Флаг воспроизведения должен быть очищен для отменённой сессии"
    
    # Шаг 4: Проверяем, что фоновый процесс отменён
    assert speech_playback_integration._avf_playback_task is None or speech_playback_integration._avf_playback_task.done(), \
        "Фоновый процесс воспроизведения должен быть отменён"
    
    # Шаг 5: Проверяем, что AVF engine остановлен
    mock_avf_engine.stop_output.assert_called_once()


@pytest.mark.asyncio
async def test_new_chunks_ignored_after_interrupt(speech_playback_integration, mock_state_manager):
    """Тест: Новые чанки игнорируются после прерывания"""
    session_id = "test_session_123"
    mock_state_manager.get_current_session_id.return_value = session_id
    
    # Шаг 1: Публикуем прерывание
    interrupt_event = {
        "type": "playback.cancelled",
        "data": {
            "session_id": session_id,
            "source": "keyboard",
            "reason": "user_interrupt"
        }
    }
    
    await speech_playback_integration._on_unified_interrupt(interrupt_event)
    
    # Шаг 2: Пытаемся добавить новый чанк после прерывания
    new_chunk_event = {
        "type": "grpc.response.audio",
        "data": {
            "session_id": session_id,
            "bytes": b"new_chunk_data" * 1000,
            "dtype": "int16",
            "sample_rate": 48000,
            "channels": 1
        }
    }
    
    # Мокируем методы для проверки, что чанк не обрабатывается
    original_add_chunk = speech_playback_integration._avf_chunk_buffer.get
    
    await speech_playback_integration._on_audio_chunk(new_chunk_event)
    
    # Шаг 3: Проверяем, что чанк не добавлен в буфер
    assert session_id not in speech_playback_integration._avf_chunk_buffer or \
           len(speech_playback_integration._avf_chunk_buffer.get(session_id, [])) == 0, \
        "Новый чанк не должен быть добавлен в буфер после прерывания"


@pytest.mark.asyncio
async def test_interrupt_with_normalized_session_id(speech_playback_integration, mock_state_manager):
    """Тест: Прерывание работает с нормализованным session_id (float -> str)"""
    session_id_float = 1234567890.123456
    session_id_str = str(session_id_float)
    mock_state_manager.get_current_session_id.return_value = session_id_float
    
    # Шаг 1: Добавляем чанк в буфер
    speech_playback_integration._avf_chunk_buffer[session_id_float] = [
        {"data": b"chunk_data" * 1000, "sample_rate": 48000, "channels": 1}
    ]
    speech_playback_integration._avf_is_playing[session_id_float] = True
    
    # Шаг 2: Публикуем прерывание с float session_id
    interrupt_event = {
        "type": "playback.cancelled",
        "data": {
            "session_id": session_id_float,
            "source": "keyboard",
            "reason": "user_interrupt"
        }
    }
    
    await speech_playback_integration._on_unified_interrupt(interrupt_event)
    
    # Шаг 3: Проверяем, что сессия отменена (как float, так и str)
    assert session_id_float in speech_playback_integration._cancelled_sessions or \
           session_id_str in speech_playback_integration._cancelled_sessions, \
        "Сессия должна быть помечена как отменённая (float или str)"
    
    # Шаг 4: Пытаемся добавить новый чанк с float session_id
    new_chunk_event = {
        "type": "grpc.response.audio",
        "data": {
            "session_id": session_id_float,
            "bytes": b"new_chunk_data" * 1000,
            "dtype": "int16",
            "sample_rate": 48000,
            "channels": 1
        }
    }
    
    await speech_playback_integration._on_audio_chunk(new_chunk_event)
    
    # Шаг 5: Проверяем, что чанк не добавлен
    assert session_id_float not in speech_playback_integration._avf_chunk_buffer or \
           len(speech_playback_integration._avf_chunk_buffer.get(session_id_float, [])) == 0, \
        "Новый чанк не должен быть добавлен после прерывания (нормализация session_id работает)"

