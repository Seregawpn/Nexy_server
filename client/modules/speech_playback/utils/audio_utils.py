"""
Утилиты для работы с аудио
"""

import numpy as np


def resample_audio(audio_data: np.ndarray, source_rate: int, target_rate: int) -> np.ndarray:
    """Ресемплинг аудио данных"""
    if source_rate == target_rate:
        return audio_data
    return audio_data


def convert_channels(
    audio_data: np.ndarray, source_channels: int, target_channels: int
) -> np.ndarray:
    """Конвертация количества каналов"""
    if source_channels == target_channels:
        return audio_data
    return audio_data
