"""
Audio Utils - Утилиты для обработки аудио

ОСНОВНЫЕ ФУНКЦИИ:
1. Resampling - пересчет частоты дискретизации
2. Channel conversion - конвертация каналов
3. Audio normalization - нормализация аудио
4. Format conversion - конвертация форматов
5. Crossfade - плавные переходы между чанками
"""

import logging
import numpy as np
from typing import Union, Optional
from scipy import signal

logger = logging.getLogger(__name__)

def resample_audio(audio_data: np.ndarray, target_sample_rate: int, original_sample_rate: int = 24000) -> np.ndarray:
    """
    Пересчет частоты дискретизации аудио
    
    Args:
        audio_data: Аудио данные
        target_sample_rate: Целевая частота дискретизации
        original_sample_rate: Исходная частота дискретизации (по умолчанию 24 kHz согласно спецификации gRPC)
        
    Returns:
        Пересчитанные аудио данные
    """
    try:
        if original_sample_rate == target_sample_rate:
            return audio_data
        
        # Вычисляем коэффициент пересчета
        ratio = target_sample_rate / original_sample_rate
        
        # Пересчитываем используя scipy.signal.resample для качественного ресемплинга
        resampled_data = signal.resample(audio_data, int(len(audio_data) * ratio))
        
        # Приводим к правильному типу
        if audio_data.dtype == np.int16:
            resampled_data = resampled_data.astype(np.int16)
        elif audio_data.dtype == np.float32:
            resampled_data = resampled_data.astype(np.float32)
        
        logger.debug(f"🔄 Resampling: {original_sample_rate}Hz → {target_sample_rate}Hz (ratio: {ratio:.3f})")
        
        return resampled_data
        
    except Exception as e:
        logger.error(f"❌ Ошибка resampling: {e}")
        return audio_data

def convert_channels(audio_data: np.ndarray, target_channels: int) -> np.ndarray:
    """
    Конвертирует количество каналов аудио
    
    Args:
        audio_data: Аудио данные
        target_channels: Целевое количество каналов
        
    Returns:
        Аудио данные с целевым количеством каналов
    """
    try:
        if len(audio_data.shape) == 1:
            # Моно в стерео
            if target_channels == 2:
                return np.column_stack((audio_data, audio_data))
            else:
                return audio_data
        elif len(audio_data.shape) == 2:
            current_channels = audio_data.shape[1]
            if current_channels == target_channels:
                return audio_data
            elif current_channels == 1 and target_channels == 2:
                return np.column_stack((audio_data[:, 0], audio_data[:, 0]))
            elif current_channels == 2 and target_channels == 1:
                return np.mean(audio_data, axis=1)
            else:
                return audio_data
        else:
            return audio_data
            
    except Exception as e:
        logger.error(f"❌ Ошибка конвертации каналов: {e}")
        return audio_data

def apply_crossfade(prev_chunk: np.ndarray, next_chunk: np.ndarray, fade_samples: int = 512) -> np.ndarray:
    """
    Применяет crossfade между двумя чанками для устранения щелчков
    
    Args:
        prev_chunk: Предыдущий чанк (последние fade_samples сэмплов)
        next_chunk: Следующий чанк (первые fade_samples сэмплов)
        fade_samples: Количество сэмплов для crossfade (по умолчанию 512 = ~10ms @ 48kHz)
        
    Returns:
        Объединенный чанк с плавным переходом
    """
    try:
        # Сохраняем исходный dtype
        original_dtype = prev_chunk.dtype
        
        # Конвертируем в float32 для плавного crossfade
        if prev_chunk.dtype == np.int16:
            prev_float = prev_chunk.astype(np.float32) / 32768.0
            next_float = next_chunk.astype(np.float32) / 32768.0
        elif prev_chunk.dtype == np.int32:
            prev_float = prev_chunk.astype(np.float32) / 2147483648.0
            next_float = next_chunk.astype(np.float32) / 2147483648.0
        else:
            prev_float = prev_chunk.astype(np.float32)
            next_float = next_chunk.astype(np.float32)
        
        # Нормализуем форму: приводим к 2D если нужно
        prev_2d = prev_float.reshape(-1, 1) if prev_float.ndim == 1 else prev_float
        next_2d = next_float.reshape(-1, 1) if next_float.ndim == 1 else next_float
        
        # Проверяем размеры
        if len(prev_2d) < fade_samples or len(next_2d) < fade_samples:
            # Если чанки слишком маленькие, просто конкатенируем
            if prev_chunk.ndim == 1 and next_chunk.ndim == 1:
                return np.concatenate([prev_chunk, next_chunk])
            else:
                return np.vstack([prev_chunk.reshape(-1, 1) if prev_chunk.ndim == 1 else prev_chunk,
                                 next_chunk.reshape(-1, 1) if next_chunk.ndim == 1 else next_chunk])
        
        # Берем последние fade_samples предыдущего чанка
        prev_tail = prev_2d[-fade_samples:]
        # Берем первые fade_samples следующего чанка
        next_head = next_2d[:fade_samples]
        
        # Создаем fade-out для предыдущего чанка (от 1.0 до 0.0)
        fade_out = np.linspace(1.0, 0.0, fade_samples)
        # Создаем fade-in для следующего чанка (от 0.0 до 1.0)
        fade_in = np.linspace(0.0, 1.0, fade_samples)
        
        # Применяем fade к каждому каналу
        if prev_tail.ndim == 2:
            # 2D (стерео или больше каналов)
            fade_out_2d = fade_out[:, np.newaxis]
            fade_in_2d = fade_in[:, np.newaxis]
            prev_faded = prev_tail * fade_out_2d
            next_faded = next_head * fade_in_2d
            crossfade_region = prev_faded + next_faded
        else:
            # 1D (моно)
            prev_faded = prev_tail * fade_out
            next_faded = next_head * fade_in
            crossfade_region = prev_faded + next_faded
        
        # Объединяем: предыдущий чанк (без последних fade_samples) + crossfade + следующий чанк (без первых fade_samples)
        prev_body = prev_2d[:-fade_samples]
        next_body = next_2d[fade_samples:]
        
        # Конкатенируем все части
        if len(prev_body) > 0 and len(next_body) > 0:
            result_float = np.vstack([prev_body, crossfade_region, next_body])
        elif len(prev_body) > 0:
            result_float = np.vstack([prev_body, crossfade_region])
        elif len(next_body) > 0:
            result_float = np.vstack([crossfade_region, next_body])
        else:
            result_float = crossfade_region
        
        # Конвертируем обратно в исходный dtype
        if original_dtype == np.int16:
            result = np.clip(result_float * 32768.0, -32768, 32767).astype(np.int16)
        elif original_dtype == np.int32:
            result = np.clip(result_float * 2147483648.0, -2147483648, 2147483647).astype(np.int32)
        else:
            result = result_float.astype(original_dtype)
        
        # Возвращаем в исходной форме
        if prev_chunk.ndim == 1 and next_chunk.ndim == 1:
            return result.flatten()
        else:
            return result
        
    except Exception as e:
        logger.error(f"❌ Ошибка crossfade: {e}")
        # В случае ошибки просто конкатенируем
        if prev_chunk.ndim == 1 and next_chunk.ndim == 1:
            return np.concatenate([prev_chunk, next_chunk])
        else:
            return np.vstack([prev_chunk.reshape(-1, 1) if prev_chunk.ndim == 1 else prev_chunk,
                             next_chunk.reshape(-1, 1) if next_chunk.ndim == 1 else next_chunk])
