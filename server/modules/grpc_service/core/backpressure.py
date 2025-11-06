"""
Backpressure для gRPC стримов (PR-7)
Лимиты на одновременно открытые стримы и защита от "молчаливых" клиентов
"""

import asyncio
import time
import logging
import sys
import os
from typing import Dict, Optional
from collections import defaultdict
from dataclasses import dataclass, field
from pathlib import Path

# Добавляем путь к корню проекта
project_root = Path(__file__).parent.parent.parent.parent
sys.path.insert(0, str(project_root))

from config.unified_config import get_config

logger = logging.getLogger(__name__)


@dataclass
class StreamLimits:
    """Лимиты для стримов (используется конфиг из unified_config)"""
    max_concurrent_streams: int = 50
    idle_timeout_seconds: int = 300
    max_message_rate_per_second: int = 10
    grace_period_seconds: int = 30
    
    @classmethod
    def from_config(cls) -> 'StreamLimits':
        """Загрузка лимитов из unified_config"""
        try:
            config = get_config()
            if hasattr(config, 'backpressure'):
                bp_config = config.backpressure
                return cls(
                    max_concurrent_streams=bp_config.max_concurrent_streams,
                    idle_timeout_seconds=bp_config.idle_timeout_seconds,
                    max_message_rate_per_second=bp_config.max_message_rate_per_second,
                    grace_period_seconds=bp_config.grace_period_seconds
                )
        except Exception as e:
            logger.warning(f"Не удалось загрузить backpressure конфиг, используем дефолты: {e}")
        
        # Дефолтные значения
        return cls()


@dataclass
class StreamInfo:
    """Информация о стриме"""
    stream_id: str
    hardware_id: str
    start_time: float = field(default_factory=time.time)
    last_message_time: float = field(default_factory=time.time)
    message_count: int = 0
    message_timestamps: list[float] = field(default_factory=list)


class BackpressureManager:
    """
    Менеджер backpressure для gRPC стримов
    
    Обеспечивает:
    - Лимит на одновременно открытые стримы
    - Защиту от "молчаливых" клиентов (idle timeout)
    - Защиту от чрезмерного количества сообщений (rate limiting)
    """
    
    def __init__(self, limits: Optional[StreamLimits] = None):
        """
        Инициализация менеджера backpressure
        
        Args:
            limits: Лимиты для стримов (по умолчанию загружаются из unified_config)
        """
        self.limits = limits or StreamLimits.from_config()
        self.active_streams: Dict[str, StreamInfo] = {}
        self.lock = asyncio.Lock()
        
        # Запускаем фоновую задачу для проверки idle таймаутов
        self._cleanup_task: Optional[asyncio.Task] = None
    
    async def start(self):
        """Запуск фоновой задачи очистки"""
        self._cleanup_task = asyncio.create_task(self._cleanup_idle_streams())
    
    async def stop(self):
        """Остановка фоновой задачи"""
        if self._cleanup_task:
            self._cleanup_task.cancel()
            try:
                await self._cleanup_task
            except asyncio.CancelledError:
                pass
    
    async def acquire_stream(self, stream_id: str, hardware_id: str) -> tuple[bool, Optional[str]]:
        """
        Попытка получить разрешение на открытие стрима
        
        Args:
            stream_id: Идентификатор стрима
            hardware_id: Идентификатор оборудования
        
        Returns:
            (success, error_message)
        """
        async with self.lock:
            # Проверяем лимит на одновременно открытые стримы
            if len(self.active_streams) >= self.limits.max_concurrent_streams:
                # Отдельный код ошибки для лимита стримов (PR-7)
                return (False, f"STREAM_LIMIT_EXCEEDED: Maximum concurrent streams limit reached ({self.limits.max_concurrent_streams})")
            
            # Регистрируем стрим
            stream_info = StreamInfo(
                stream_id=stream_id,
                hardware_id=hardware_id
            )
            self.active_streams[stream_id] = stream_info
            
            logger.info(
                f"Stream acquired: {stream_id} (active: {len(self.active_streams)}/{self.limits.max_concurrent_streams})",
                extra={
                    'scope': 'grpc',
                    'method': 'StreamAudio',
                    'decision': 'stream_acquired',
                    'ctx': {
                        'stream_id': stream_id,
                        'hardware_id': hardware_id,
                        'active_streams': len(self.active_streams),
                        'max_streams': self.limits.max_concurrent_streams
                    }
                }
            )
            
            return (True, None)
    
    async def release_stream(self, stream_id: str):
        """
        Освобождение стрима
        
        Args:
            stream_id: Идентификатор стрима
        """
        async with self.lock:
            if stream_id in self.active_streams:
                stream_info = self.active_streams.pop(stream_id)
                duration = time.time() - stream_info.start_time
                
                logger.info(
                    f"Stream released: {stream_id} (duration: {duration:.2f}s, messages: {stream_info.message_count})",
                    extra={
                        'scope': 'grpc',
                        'method': 'StreamAudio',
                        'decision': 'stream_released',
                        'ctx': {
                            'stream_id': stream_id,
                            'duration_seconds': duration,
                            'message_count': stream_info.message_count,
                            'active_streams': len(self.active_streams)
                        }
                    }
                )
    
    async def check_message_rate(self, stream_id: str) -> tuple[bool, Optional[str]]:
        """
        Проверка rate limit для сообщений
        
        Args:
            stream_id: Идентификатор стрима
        
        Returns:
            (allowed, error_message)
        """
        async with self.lock:
            if stream_id not in self.active_streams:
                return (False, "Stream not found")
            
            stream_info = self.active_streams[stream_id]
            current_time = time.time()
            
            # Обновляем время последнего сообщения
            stream_info.last_message_time = current_time
            stream_info.message_count += 1
            
            # Очищаем старые временные метки (старше 1 секунды)
            stream_info.message_timestamps = [
                ts for ts in stream_info.message_timestamps
                if current_time - ts < 1.0
            ]
            
            # Проверяем rate limit
            if len(stream_info.message_timestamps) >= self.limits.max_message_rate_per_second:
                return (False, f"Message rate limit exceeded ({self.limits.max_message_rate_per_second} messages/second)")
            
            # Добавляем текущую временную метку
            stream_info.message_timestamps.append(current_time)
            
            return (True, None)
    
    async def _cleanup_idle_streams(self):
        """Фоновая задача для очистки неактивных стримов"""
        while True:
            try:
                await asyncio.sleep(30)  # Проверяем каждые 30 секунд
                
                current_time = time.time()
                idle_streams = []
                
                async with self.lock:
                    for stream_id, stream_info in list(self.active_streams.items()):
                        idle_time = current_time - stream_info.last_message_time
                        
                        if idle_time > self.limits.idle_timeout_seconds:
                            idle_streams.append((stream_id, stream_info))
                    
                    # Удаляем неактивные стримы
                    for stream_id, stream_info in idle_streams:
                        del self.active_streams[stream_id]
                        
                        logger.warning(
                            f"Stream closed due to idle timeout: {stream_id} (idle: {idle_time:.2f}s)",
                            extra={
                                'scope': 'grpc',
                                'method': 'StreamAudio',
                                'decision': 'stream_idle_timeout',
                                'ctx': {
                                    'stream_id': stream_id,
                                    'hardware_id': stream_info.hardware_id,
                                    'idle_time_seconds': idle_time,
                                    'active_streams': len(self.active_streams)
                                }
                            }
                        )
                
            except asyncio.CancelledError:
                break
            except Exception as e:
                logger.error(f"Error in cleanup_idle_streams: {e}", extra={
                    'scope': 'backpressure',
                    'decision': 'error',
                    'ctx': {'error': str(e)}
                })
    
    def get_stats(self) -> Dict:
        """Получение статистики"""
        return {
            'active_streams': len(self.active_streams),
            'max_concurrent_streams': self.limits.max_concurrent_streams,
            'idle_timeout_seconds': self.limits.idle_timeout_seconds,
            'max_message_rate_per_second': self.limits.max_message_rate_per_second
        }


# Глобальный экземпляр менеджера backpressure
_global_backpressure: Optional[BackpressureManager] = None


def get_backpressure_manager() -> BackpressureManager:
    """
    Получение глобального экземпляра менеджера backpressure
    
    Returns:
        Экземпляр BackpressureManager
    """
    global _global_backpressure
    if _global_backpressure is None:
        _global_backpressure = BackpressureManager()
    return _global_backpressure

