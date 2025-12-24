"""
ChunkBuffer - Буфер для хранения и управления аудио чанками

ОСНОВНЫЕ ПРИНЦИПЫ:
1. Очередь чанков для последовательного воспроизведения
2. Буфер воспроизведения для непрерывного потока
3. Thread-safety - безопасная работа в многопоточной среде
4. Управление памятью - контроль максимального размера
"""

import logging
import threading
import time
import uuid
from collections import deque
from typing import Optional, Dict, Any
from dataclasses import dataclass

import numpy as np

from .state import ChunkInfo, ChunkState

logger = logging.getLogger(__name__)


class ChunkBuffer:
    """Буфер для хранения и управления аудио чанками"""
    
    def __init__(self, max_memory_mb: int = 50, channels: int = 1, dtype=np.int16):
        """
        Инициализация буфера
        
        Args:
            max_memory_mb: Максимальный размер буфера в мегабайтах
            channels: Количество каналов
            dtype: Тип данных (np.int16 по умолчанию)
        """
        self.max_memory_bytes = max_memory_mb * 1024 * 1024
        self.channels = channels
        self.dtype = dtype
        
        # Очередь чанков (FIFO)
        self._queue: deque = deque()
        self._queue_lock = threading.RLock()
        
        # Буфер воспроизведения (непрерывный поток данных)
        self._playback_buffer: list = []
        self._playback_lock = threading.RLock()
        
        # Текущий воспроизводимый чанк
        self._current_chunk_data: Optional[np.ndarray] = None
        self._current_chunk_offset: int = 0
        
        # Статистика
        self._total_bytes_added = 0
        self._total_bytes_played = 0
        
        logger.debug(f"🔧 ChunkBuffer инициализирован: max_memory={max_memory_mb}MB, channels={channels}, dtype={dtype}")
    
    @property
    def queue_size(self) -> int:
        """Размер очереди чанков"""
        with self._queue_lock:
            return len(self._queue)
    
    @property
    def buffer_size(self) -> int:
        """Размер буфера воспроизведения (в сэмплах)"""
        with self._playback_lock:
            total = 0
            for chunk_data in self._playback_buffer:
                if chunk_data is not None and len(chunk_data) > 0:
                    total += len(chunk_data)
            if self._current_chunk_data is not None:
                remaining = len(self._current_chunk_data) - self._current_chunk_offset
                total += max(0, remaining)
            return total
    
    @property
    def has_data(self) -> bool:
        """Есть ли данные для воспроизведения"""
        with self._playback_lock:
            return (self._current_chunk_data is not None and 
                   self._current_chunk_offset < len(self._current_chunk_data)) or \
                   len(self._playback_buffer) > 0 or \
                   self.queue_size > 0
    
    @property
    def is_empty(self) -> bool:
        """Проверка, пуст ли буфер (для совместимости)"""
        return not self.has_data
    
    def set_channels(self, new_channels: int):
        """Обновить количество каналов"""
        with self._playback_lock:
            self.channels = new_channels
            logger.debug(f"🔧 ChunkBuffer: channels обновлено до {new_channels}")
    
    def add_chunk(self, audio_data: np.ndarray, priority: int = 0, metadata: Optional[Dict[str, Any]] = None) -> str:
        """
        Добавить чанк в очередь
        
        Args:
            audio_data: Аудио данные (numpy array)
            priority: Приоритет чанка (не используется, для совместимости)
            metadata: Метаданные чанка
            
        Returns:
            chunk_id: ID чанка
        """
        # Генерируем уникальный ID
        chunk_id = f"chunk_{int(time.time() * 1000)}_{uuid.uuid4().hex[:8]}"
        
        # Создаем ChunkInfo
        chunk_info = ChunkInfo(
            chunk_id=chunk_id,
            data=b"",  # Данные хранятся в numpy array, не в bytes
            timestamp=time.time(),
            state=ChunkState.QUEUED
        )
        
        # Проверяем размер памяти
        chunk_bytes = audio_data.nbytes if hasattr(audio_data, 'nbytes') else len(audio_data) * audio_data.dtype.itemsize
        self._total_bytes_added += chunk_bytes
        
        # Проверка лимита памяти (упрощенная - просто логируем)
        if self._total_bytes_added > self.max_memory_bytes:
            logger.warning(f"⚠️ ChunkBuffer: превышен лимит памяти ({self._total_bytes_added / 1024 / 1024:.1f}MB > {self.max_memory_bytes / 1024 / 1024:.1f}MB)")
        
        # Добавляем в очередь
        with self._queue_lock:
            self._queue.append((chunk_info, audio_data, metadata))
            logger.debug(f"✅ Чанк добавлен: {chunk_id} (size: {len(audio_data)}, queue: {len(self._queue)})")
        
        return chunk_id
    
    def get_next_chunk(self, timeout: float = 0.1) -> Optional[ChunkInfo]:
        """
        Получить следующий чанк из очереди
        
        Args:
            timeout: Таймаут ожидания (не используется, для совместимости)
            
        Returns:
            ChunkInfo или None
        """
        with self._queue_lock:
            if not self._queue:
                return None
            
            chunk_info, audio_data, metadata = self._queue.popleft()
            chunk_info.state = ChunkState.BUFFERED
            
            # Сохраняем данные для воспроизведения
            with self._playback_lock:
                self._playback_buffer.append(audio_data)
            
            logger.debug(f"🔍 Получен чанк: {chunk_info.chunk_id}")
            return chunk_info
    
    def add_to_playback_buffer(self, chunk_info: ChunkInfo) -> bool:
        """
        Добавить чанк в буфер воспроизведения (для совместимости)
        
        Args:
            chunk_info: Информация о чанке
            
        Returns:
            True если успешно
        """
        # Данные уже добавлены в get_next_chunk
        return True
    
    def mark_chunk_completed(self, chunk_info: ChunkInfo):
        """
        Отметить чанк как завершенный
        
        Args:
            chunk_info: Информация о чанке
        """
        chunk_info.state = ChunkState.COMPLETED
        logger.debug(f"✅ Чанк завершен: {chunk_info.chunk_id}")
    
    def get_playback_data(self, frames: int) -> np.ndarray:
        """
        Получить данные для воспроизведения
        
        Args:
            frames: Количество фреймов для воспроизведения
            
        Returns:
            numpy array с аудио данными (2D: frames x channels)
        """
        with self._playback_lock:
            if not self._playback_buffer and self._current_chunk_data is None:
                # Нет данных - возвращаем пустой массив
                return np.zeros((frames, self.channels), dtype=self.dtype)
            
            # Собираем данные из буфера
            collected_frames = []
            remaining_frames = frames
            
            # Обрабатываем текущий чанк
            if self._current_chunk_data is not None:
                remaining_in_chunk = len(self._current_chunk_data) - self._current_chunk_offset
                if remaining_in_chunk > 0:
                    take_frames = min(remaining_frames, remaining_in_chunk)
                    chunk_slice = self._current_chunk_data[self._current_chunk_offset:self._current_chunk_offset + take_frames]
                    
                    # Преобразуем в 2D и нормализуем каналы
                    if chunk_slice.ndim == 1:
                        chunk_slice = chunk_slice.reshape(-1, 1)
                    # Нормализуем до нужного количества каналов
                    if chunk_slice.shape[1] != self.channels:
                        if chunk_slice.shape[1] == 1 and self.channels > 1:
                            # Моно → стерео: дублируем канал
                            chunk_slice = np.repeat(chunk_slice, self.channels, axis=1)
                        elif chunk_slice.shape[1] > 1 and self.channels == 1:
                            # Стерео → моно: берем первый канал
                            chunk_slice = chunk_slice[:, :1]
                    
                    collected_frames.append(chunk_slice)
                    self._current_chunk_offset += take_frames
                    remaining_frames -= take_frames
                    
                    # Если чанк закончился, очищаем
                    if self._current_chunk_offset >= len(self._current_chunk_data):
                        self._current_chunk_data = None
                        self._current_chunk_offset = 0
            
            # Обрабатываем очередь буфера
            while remaining_frames > 0 and self._playback_buffer:
                chunk_data = self._playback_buffer.pop(0)
                
                # Преобразуем в 2D и нормализуем каналы
                if chunk_data.ndim == 1:
                    chunk_data = chunk_data.reshape(-1, 1)
                # Нормализуем до нужного количества каналов
                if chunk_data.shape[1] != self.channels:
                    if chunk_data.shape[1] == 1 and self.channels > 1:
                        # Моно → стерео: дублируем канал
                        chunk_data = np.repeat(chunk_data, self.channels, axis=1)
                    elif chunk_data.shape[1] > 1 and self.channels == 1:
                        # Стерео → моно: берем первый канал
                        chunk_data = chunk_data[:, :1]
                
                if len(chunk_data) <= remaining_frames:
                    # Весь чанк помещается
                    collected_frames.append(chunk_data)
                    remaining_frames -= len(chunk_data)
                else:
                    # Берем часть чанка
                    collected_frames.append(chunk_data[:remaining_frames])
                    # Сохраняем остаток как текущий чанк
                    self._current_chunk_data = chunk_data[remaining_frames:]
                    self._current_chunk_offset = 0
                    remaining_frames = 0
            
            # Объединяем все фреймы (теперь все имеют одинаковое количество каналов)
            if collected_frames:
                # Проверяем, что все массивы имеют одинаковое количество каналов
                for i, frame in enumerate(collected_frames):
                    if frame.shape[1] != self.channels:
                        # Нормализуем если нужно
                        if frame.shape[1] == 1 and self.channels > 1:
                            collected_frames[i] = np.repeat(frame, self.channels, axis=1)
                        elif frame.shape[1] > 1 and self.channels == 1:
                            collected_frames[i] = frame[:, :1]
                
                result = np.concatenate(collected_frames, axis=0)
                self._total_bytes_played += result.nbytes
            else:
                result = np.zeros((frames, self.channels), dtype=self.dtype)
            
            # Дополняем до нужного размера если не хватает
            if len(result) < frames:
                padding = np.zeros((frames - len(result), self.channels), dtype=self.dtype)
                result = np.concatenate([result, padding], axis=0)
            
            return result
    
    def clear_all(self):
        """Очистить все буферы"""
        with self._queue_lock:
            self._queue.clear()
        
        with self._playback_lock:
            self._playback_buffer.clear()
            self._current_chunk_data = None
            self._current_chunk_offset = 0
        
        logger.debug("🧹 ChunkBuffer очищен")
    
    def wait_for_completion(self, timeout: Optional[float] = None) -> bool:
        """
        Ждать завершения воспроизведения всех чанков
        
        Args:
            timeout: Таймаут ожидания (None = бесконечно)
            
        Returns:
            True если все чанки воспроизведены
        """
        start_time = time.time()
        
        while True:
            if not self.has_data:
                return True
            
            if timeout is not None and (time.time() - start_time) > timeout:
                return False
            
            time.sleep(0.01)
    
    def get_stats(self) -> Dict[str, Any]:
        """Получить статистику буфера"""
        with self._queue_lock, self._playback_lock:
            return {
                'queue_size': len(self._queue),
                'buffer_size': self.buffer_size,
                'has_data': self.has_data,
                'total_bytes_added': self._total_bytes_added,
                'total_bytes_played': self._total_bytes_played,
                'channels': self.channels,
                'dtype': str(self.dtype)
            }


# Экспорт ChunkInfo из state для совместимости
from .state import ChunkInfo

__all__ = ['ChunkBuffer', 'ChunkInfo']
