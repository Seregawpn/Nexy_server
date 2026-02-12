"""
ChunkBuffer - Буфер для хранения аудио чанков
"""

import logging
from typing import Any
import uuid

import numpy as np

logger = logging.getLogger(__name__)


class ChunkInfo:
    """Информация о чанке"""

    def __init__(self, chunk_id: str, data: np.ndarray, metadata: dict[str, Any]):
        self.chunk_id = chunk_id
        self.data = data
        self.metadata = metadata


class ChunkBuffer:
    """Буфер для хранения аудио чанков"""

    def __init__(self, sample_rate: int, channels: int, dtype: str):
        """Инициализация буфера"""
        self.sample_rate = sample_rate
        self.channels = channels
        self.dtype = dtype
        self._chunks: dict[str, ChunkInfo] = {}

    def add_chunk(self, audio_data: np.ndarray, metadata: dict[str, Any]) -> str:
        """Добавление чанка в буфер"""
        chunk_id = str(uuid.uuid4())
        chunk = ChunkInfo(chunk_id, audio_data, metadata)
        self._chunks[chunk_id] = chunk
        logger.debug(f"Чанк добавлен: {chunk_id}")
        return chunk_id

    def get_chunk(self, chunk_id: str) -> ChunkInfo | None:
        """Получение чанка по ID"""
        return self._chunks.get(chunk_id)

    def remove_chunk(self, chunk_id: str) -> bool:
        """Удаление чанка из буфера"""
        if chunk_id in self._chunks:
            del self._chunks[chunk_id]
            logger.debug(f"Чанк удален: {chunk_id}")
            return True
        return False

    def clear(self):
        """Очистка буфера"""
        self._chunks.clear()
        logger.debug("Буфер очищен")

    def clear_all(self):
        """Очистка буфера (алиас для clear)"""
        self.clear()

    def size(self) -> int:
        """Размер буфера (количество чанков)"""
        return len(self._chunks)

    @property
    def is_empty(self) -> bool:
        """Проверка, пуст ли буфер"""
        return len(self._chunks) == 0

    @property
    def queue_size(self) -> int:
        """Размер очереди (алиас для size)"""
        return self.size()

    @property
    def buffer_size(self) -> int:
        """Размер буфера в байтах (упрощенная версия - возвращаем 0)"""
        return 0

    @property
    def has_data(self) -> bool:
        """Проверка, есть ли данные в буфере"""
        return not self.is_empty

    def get_playback_data(self, frames: int) -> np.ndarray:
        """Получение данных для воспроизведения (упрощенная версия)"""
        if self.is_empty:
            return np.array([], dtype=np.int16)

        # Берем первый чанк из буфера
        chunk_info = next(iter(self._chunks.values()))
        if chunk_info is None:
            return np.array([], dtype=np.int16)

        # Возвращаем данные чанка (первые frames сэмплов)
        data = chunk_info.data
        if len(data) <= frames:
            # Весь чанк - удаляем его
            self.remove_chunk(chunk_info.chunk_id)
            return data
        else:
            # Часть чанка - обрезаем и обновляем
            result = data[:frames]
            chunk_info.data = data[frames:]
            return result
