"""
Audio Utils - Утилиты для обработки аудио данных
"""

import logging
from typing import Any

import numpy as np

logger = logging.getLogger(__name__)

def normalize_audio(audio_data: np.ndarray, target_dtype: Any = np.int16) -> np.ndarray:
    """Нормализует аудио данные"""
    logger.debug(f"🔍 [AUDIO_DEBUG] Нормализация аудио: shape={audio_data.shape}, dtype={audio_data.dtype} -> {target_dtype}")
    try:
        if audio_data.dtype != target_dtype:
            # Конвертируем в float32 для нормализации
            if audio_data.dtype == np.int16:
                audio_float = audio_data.astype(np.float32) / 32767.0
            elif audio_data.dtype == np.int32:
                audio_float = audio_data.astype(np.float32) / 2147483647.0
            else:
                audio_float = audio_data.astype(np.float32)
            
            # Нормализуем
            max_val = np.max(np.abs(audio_float))
            if max_val > 0:
                audio_float = audio_float / max_val
            
            # Конвертируем в целевой тип
            if target_dtype == np.int16:
                return (audio_float * 32767).astype(np.int16)
            elif target_dtype == np.int32:
                return (audio_float * 2147483647).astype(np.int32)
            else:
                return audio_float.astype(target_dtype)
        else:
            logger.debug(f"🔍 [AUDIO_DEBUG] Аудио уже в нужном формате: {target_dtype}")
            return audio_data
            
    except Exception as e:
        logger.error(f"❌ [AUDIO_ERROR] Ошибка нормализации аудио: {e}")
        return audio_data

def resample_audio(audio_data: np.ndarray, original_rate: int, target_rate: int) -> np.ndarray:
    """
    Изменяет частоту дискретизации аудио (линейная интерполяция).
    
    🔧 PRODUCTION: Использует round() для избежания систематического дрейфа длины.
    🔧 PRODUCTION: Dtype guard - приводит к float32 если необходимо.
    """
    logger.debug(f"🔍 [AUDIO_DEBUG] Изменение частоты дискретизации: {original_rate}Hz -> {target_rate}Hz")
    try:
        if original_rate == target_rate:
            logger.debug(f"🔍 [AUDIO_DEBUG] Частота дискретизации не изменилась: {original_rate}Hz")
            return audio_data
        
        # 🔧 PRODUCTION ФИКС #3: Dtype guard - приводим к float32 если необходимо
        if audio_data.dtype not in [np.float32, np.float64]:
            logger.warning(f"⚠️ [RESAMPLE] Неожиданный dtype: {audio_data.dtype}, приводим к float32")
            # Если int16 - нормализуем
            if audio_data.dtype == np.int16:
                audio_data = audio_data.astype(np.float32) / 32768.0
            else:
                audio_data = audio_data.astype(np.float32)
        
        # Простое изменение частоты дискретизации
        ratio = target_rate / original_rate
        
        # 🔧 PRODUCTION ФИКС #2: Используем round() вместо int() для избежания систематического дрейфа
        new_length = int(round(len(audio_data) * ratio))
        
        if new_length == 0:
            logger.warning(f"⚠️ [RESAMPLE] new_length=0, возвращаем пустой массив")
            return np.array([], dtype=audio_data.dtype)
        
        # Линейная интерполяция
        # 🔧 PRODUCTION ФИКС #1: Оптимизация - используем linspace для indices
        # xp (точки данных) можно кэшировать на уровне player'а, но здесь оставляем как есть
        indices = np.linspace(0, len(audio_data) - 1, new_length, dtype=np.float32)
        xp = np.arange(len(audio_data), dtype=np.float32)
        result = np.interp(indices, xp, audio_data)
        
        # Сохраняем исходный dtype (если был float32/float64)
        result = result.astype(audio_data.dtype)
        
        logger.debug(f"🔍 [AUDIO_DEBUG] Частота дискретизации изменена: {len(audio_data)} -> {len(result)} сэмплов")
        return result
        
    except Exception as e:
        logger.error(f"❌ [AUDIO_ERROR] Ошибка изменения частоты дискретизации: {e}")
        return audio_data

def convert_channels(audio_data: np.ndarray, target_channels: int) -> np.ndarray:
    """Конвертирует количество каналов аудио"""
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

def detect_silence(audio_data: np.ndarray, threshold: float = 0.01) -> list[tuple[int, int]]:
    """Обнаруживает тишину в аудио"""
    try:
        # Вычисляем энергию сигнала
        if len(audio_data.shape) == 2:
            energy = np.sqrt(np.mean(audio_data ** 2, axis=1))
        else:
            energy = np.abs(audio_data)
            
        # Находим участки тишины
        silence_mask = energy < threshold
        silence_regions = []
        
        in_silence = False
        start = 0
        
        for i, is_silent in enumerate(silence_mask):
            if is_silent and not in_silence:
                start = i
                in_silence = True
            elif not is_silent and in_silence:
                silence_regions.append((start, i))
                in_silence = False
                
        if in_silence:
            silence_regions.append((start, len(silence_mask)))
            
        return silence_regions
        
    except Exception as e:
        logger.error(f"❌ Ошибка обнаружения тишины: {e}")
        return []

def trim_silence(audio_data: np.ndarray, threshold: float = 0.01) -> np.ndarray:
    """Удаляет тишину с начала и конца аудио"""
    try:
        silence_regions = detect_silence(audio_data, threshold)
        
        if not silence_regions:
            return audio_data
            
        # Удаляем тишину с начала
        start_idx = 0
        for start, end in silence_regions:
            if start == 0:
                start_idx = end
            else:
                break
                
        # Удаляем тишину с конца
        end_idx = len(audio_data)
        for start, end in reversed(silence_regions):
            if end == len(audio_data):
                end_idx = start
            else:
                break
                
        return audio_data[start_idx:end_idx]
        
    except Exception as e:
        logger.error(f"❌ Ошибка удаления тишины: {e}")
        return audio_data

def get_audio_info(audio_data: np.ndarray, sample_rate: int) -> dict[str, Any]:
    """Возвращает информацию об аудио"""
    try:
        duration = len(audio_data) / sample_rate
        channels = 1 if len(audio_data.shape) == 1 else audio_data.shape[1]
        
        return {
            "duration": duration,
            "sample_rate": sample_rate,
            "channels": channels,
            "samples": len(audio_data),
            "dtype": str(audio_data.dtype),
            "shape": audio_data.shape
        }
        
    except Exception as e:
        logger.error(f"❌ Ошибка получения информации об аудио: {e}")
        return {}
